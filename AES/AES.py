import numpy as np
import math
S_BOX = [
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
]

rcon = np.array(['01000000', '02000000', '04000000', '08000000', '10000000', '20000000', '40000000', '80000000', '1b000000', '36000000'])

def is_binary_str(variable):
    return set(variable).issubset({'0', '1'}) and isinstance(variable, str)

def zero_pad(object, target_len):
    while len(object) < target_len:
        object = '0' + object
    return object

def is_hex_str(variable):
    hex_digits = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
    return set(variable).issubset(hex_digits) and isinstance(variable, str)

def hex_str_2_bi_str(variable, number_of_digits = None):
    if number_of_digits == None:
        number_of_digits = 4 * len(variable)
    assert is_hex_str(variable)
    variable = int(variable, 16)
    variable = bin(variable)[2:]
    variable = zero_pad(variable, number_of_digits)
    return variable

def XOR_binary_str(str1, str2):
    assert is_binary_str(str1)
    assert is_binary_str(str2)
    assert len(str1) == len(str2)
    num1 = int(str1, 2)
    num2 = int(str2, 2)
    out = num1 ^ num2
    out = bin(out)[2:]
    out = zero_pad(out, len(str1))
    assert len(out) == len(str1)
    return out

def sub_bytes_element(element):
        assert is_hex_str(element)
        assert len(element) == 2
        x = int(element[0], 16 )
        y = int(element[1], 16 )
        return S_BOX[x][y]
    
def rot_word(word):
    assert is_hex_str(word)
    assert len(str(word)) == 8
    return word[2:] + word[:2]

def sub_word(word):
    assert is_hex_str(word)
    assert len(word) == 8
    word = [word[2*i:2*i+2] for i in range(4)]
    return ''.join(np.vectorize(sub_bytes_element)(word))

def bi_str_2_hex_str(variable, number_of_digits = None):
    if number_of_digits == None:
        number_of_digits = math.ceil(len(variable) / 4)
    assert is_hex_str(variable)
    variable = int(variable, 2)
    variable = hex(variable)[2:]
    variable = zero_pad(variable, number_of_digits)
    return variable
    
def XOR_hex_str(str1, str2):
    str1_bi = hex_str_2_bi_str(str1)
    str2_bi = hex_str_2_bi_str(str2)
    out_bi = XOR_binary_str(str1_bi, str2_bi)
    out = bi_str_2_hex_str(out_bi)
    return out
    
class State():
    mix_columns_matrix = (('02', '03', '01', '01'),
                          ('01', '02', '03', '01'),
                          ('01', '01', '02', '03'),
                          ('03', '01', '01', '02'))
    def __init__(self, plaintext, key):
        assert is_hex_str(plaintext)
        assert len(plaintext) == 32
        assert is_hex_str(key)
        assert len(key) in {32, 48, 64}
        self.plaintext = plaintext
        self.key = key
        self.key_size = len(key)
        self.state = self.plaintext_to_state(plaintext)
        self.generate_round_keys()

    def plaintext_to_state(self, plaintext):
        assert is_hex_str(plaintext)
        assert len(plaintext) == 32
        plaintext = [plaintext[2*i:2*i+2] for i in range(16)]
        return np.array(list(plaintext)).reshape((4,4)).transpose()

    def generate_round_keys(self):
        N = int(len(self.key) / 2 / 4)              #length of key in 32 bit (4 bytes) words
        K = [self.key[8*i:8*i+8] for i in range(N)] #initial key broken into 32 bit (4 bytes) words
        R = int(len(self.key) / 8 + 7)              #number of rounds required
        # W = np.empty(4 * R, dtype=str)
        W = [''] * (4 * R)
        for i in range(4 * R):
            if i < N:
                assert isinstance(rot_word(K[i]), str)
                W[i] = K[i]
                assert isinstance(rot_word(W[i]), str)
                
            elif (i % N) == 0:
                W[i] = XOR_hex_str(rcon[int(i / N - 1)], XOR_hex_str(W[i-N], sub_word(rot_word(W[i-1]))))
            elif N > 6 and (i % N) == 4:
                W[i] = XOR_hex_str(W[i - N], sub_word(W[i - 1]))
            else:
                W[i] = XOR_hex_str(W[i - N], W[i - 1])
        self.round_keys = np.array([[W[i][0:2], W[i][2:4], W[i][4:6], W[i][6:8]] for i in range(4 * R)]).reshape((R,4,4)).transpose((0,2,1))

    def sub_bytes(self):
        self.state = np.vectorize(sub_bytes_element)(self.state)
    
    def shift_rows(self):
        self.state[0] = np.roll(self.state[0], -0)
        self.state[1] = np.roll(self.state[1], -1)
        self.state[2] = np.roll(self.state[2], -2)
        self.state[3] = np.roll(self.state[3], -3)

    def mix_columns_mul(self, coe, hex_bite):
        assert coe in ('01', '02', '03')
        bi_bite = hex_str_2_bi_str(hex_bite)
        assert len(hex_bite) == 2
        assert len(bi_bite) == 8
        if coe == '01':
            return hex_bite
        elif coe == '02':
            last_bit = bi_bite[0]
            bi_bite = bi_bite[1:] + '0'
            hex_bite = bi_str_2_hex_str(bi_bite)
            if(last_bit == '1'):
                hex_bite = XOR_hex_str(hex_bite, '1b')
            return hex_bite
        elif coe == '03':
            return XOR_hex_str(hex_bite, self.mix_columns_mul('02', hex_bite))        
    def mix_columns(self):
        new_state = np.array([['00'] * 4] * 4)
        for column in range(4):
            for row in range(4):
                for i in range(4):
                    partial_new_state = self.mix_columns_mul(self.mix_columns_matrix[row][i], self.state[i][column])
                    new_state[row][column] = XOR_hex_str(new_state[row][column], partial_new_state)
        self.state = new_state
    
    def add_round_key(self, subkey):
        for i in range(4):
            for j in range(4):
                self.state[i][j] = XOR_hex_str(self.state[i][j], subkey[i][j])
    def encrypt(self):
        R = int(len(self.key) / 8 + 7)
        self.add_round_key(self.round_keys[0])
        for i in range(R - 2):
            round_index = i + 1
            self.sub_bytes()
            self.shift_rows()
            self.mix_columns()
            self.add_round_key(self.round_keys[round_index])
        self.sub_bytes()
        self.shift_rows()
        self.add_round_key(self.round_keys[R - 1])
        
        self.last_ciphertext = ''.join(self.state.transpose().flatten())
        assert is_hex_str(self.last_ciphertext)
        assert len(self.last_ciphertext) == 32
        return self.last_ciphertext