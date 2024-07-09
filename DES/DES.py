S_BOX = [
    # This table lists the eight S-boxes used in DES.
    # Each S-box replaces a 6-bit input with a 4-bit output.
    # Given a 6-bit input, the 4-bit output is found by selecting the row using the outer two bits,
    # and the column using the inner four bits.
    [
        ["1110", "0100", "1101", "0001", "0010", "1111", "1011", "1000", "0011", "1010", "0110", "1100", "0101", "1001", "0000", "0111"],
        ["0000", "1111", "0111", "0100", "1110", "0010", "1101", "0001", "1010", "0110", "1100", "1011", "1001", "0101", "0011", "1000"],
        ["0100", "0001", "1110", "1000", "1101", "0110", "0010", "1011", "1111", "1100", "1001", "0111", "0011", "1010", "0101", "0000"],
        ["1111", "1100", "1000", "0010", "0100", "1001", "0001", "0111", "0101", "1011", "0011", "1110", "1010", "0000", "0110", "1101"],
        ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    ],
    [
        ["1111", "0001", "1000", "1110", "0110", "1011", "0011", "0100", "1001", "0111", "0010", "1101", "1100", "0000", "0101", "1010"],
        ["0011", "1101", "0100", "0111", "1111", "0010", "1000", "1110", "1100", "0000", "0001", "1010", "0110", "1001", "1011", "0101"],
        ["0000", "1110", "0111", "1011", "1010", "0100", "1101", "0001", "0101", "1000", "1100", "0110", "1001", "0011", "0010", "1111"],
        ["1101", "1000", "1010", "0001", "0011", "1111", "0100", "0010", "1011", "0110", "0111", "1100", "0000", "0101", "1110", "1001"],
        ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    ],
    [
        ["1010", "0000", "1001", "1110", "0110", "0011", "1111", "0101", "0001", "1101", "1100", "0111", "1011", "0100", "0010", "1000"],
        ["1101", "0111", "0000", "1001", "0011", "0100", "0110", "1010", "0010", "1000", "0101", "1110", "1100", "1011", "1111", "0001"],
        ["1101", "0110", "0100", "1001", "1000", "1111", "0011", "0000", "1011", "0001", "0010", "1100", "0101", "1010", "1110", "0111"],
        ["0001", "1010", "1101", "0000", "0110", "1001", "1000", "0111", "0100", "1111", "1110", "0011", "1011", "0101", "0010", "1100"],
        ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    ],
    [
        ["0111", "1101", "1110", "0011", "0000", "0110", "1001", "1010", "0001", "0010", "1000", "0101", "1011", "1100", "0100", "1111"],
        ["1101", "1000", "1011", "0101", "0110", "1111", "0000", "0011", "0100", "0111", "0010", "1100", "0001", "1010", "1110", "1001"],
        ["1010", "0110", "1001", "0000", "1100", "1011", "0111", "1101", "1111", "0001", "0011", "1110", "0101", "0010", "1000", "0100"],
        ["0011", "1111", "0000", "0110", "1010", "0001", "1101", "1000", "1001", "0100", "0101", "1011", "1100", "0111", "0010", "1110"],
        ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    ],
    [
        ["0010", "1100", "0100", "0001", "0111", "1010", "1011", "0110", "1000", "0101", "0011", "1111", "1101", "0000", "1110", "1001"],
        ["1110", "1011", "0010", "1100", "0100", "0111", "1101", "0001", "0101", "0000", "1111", "1010", "0011", "1001", "1000", "0110"],
        ["0100", "0010", "0001", "1011", "1010", "1101", "0111", "1000", "1111", "1001", "1100", "0101", "0110", "0011", "0000", "1110"],
        ["1011", "1000", "1100", "0111", "0001", "1110", "0010", "1101", "0110", "1111", "0000", "1001", "1010", "0100", "0101", "0011"],
        ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    ],
    [
        ["1100", "0001", "1010", "1111", "1001", "0010", "0110", "1000", "0000", "1101", "0011", "0100", "1110", "0111", "0101", "1011"],
        ["1010", "1111", "0100", "0010", "0111", "1100", "1001", "0101", "0110", "0001", "1101", "1110", "0000", "1011", "0011", "1000"],
        ["1001", "1110", "1111", "0101", "0010", "1000", "1100", "0011", "0111", "0000", "0100", "1010", "0001", "1101", "1011", "0110"],
        ["0100", "0011", "0010", "1100", "1001", "0101", "1111", "1010", "1011", "1110", "0001", "0111", "0110", "0000", "1000", "1101"],
        ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    ],
    [
        ["0100", "1011", "0010", "1110", "1111", "0000", "1000", "1101", "0011", "1100", "1001", "0111", "0101", "1010", "0110", "0001"],
        ["1101", "0000", "1011", "0111", "0100", "1001", "0001", "1010", "1110", "0011", "0101", "1100", "0010", "1111", "1000", "0110"],
        ["0001", "0100", "1011", "1101", "1100", "0011", "0111", "1110", "1010", "1111", "0110", "1000", "0000", "0101", "1001", "0010"],
        ["0110", "1011", "1101", "1000", "0001", "0100", "1010", "0111", "1001", "0101", "0000", "1111", "1110", "0010", "0011", "1100"],
        ["0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    ],
    [
        ["1101", "0010", "1000", "0100", "0110", "1111", "1011", "0001", "1010", "1001", "0011", "1110", "0101", "0000", "1100", "0111"],
        ["0001", "1111", "1101", "1000", "1010", "0011", "0111", "0100", "1100", "0101", "0110", "1011", "0000", "1110", "1001", "0010"],
        ["0111", "1011", "0100", "0001", "1001", "1100", "1110", "0010", "0000", "0110", "1010", "1101", "1111", "0011", "0101", "1000"],
        ["0010", "0001", "1110", "0111", "0100", "1010", "1000", "1101", "1111", "1100", "1001", "0000", "0011", "0101", "0110", "1011"]
    ]
]
# these table are take from wikipedia and their indices start from 1 not 0
# https://en.wikipedia.org/wiki/DES_supplementary_material
expantion_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

permutation_table = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

initial_permutation_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

final_permutation_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9,49 ,17 ,57 ,25
]

permuted_choice_1_left_table = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36
]

permuted_choice_1_right_table = [
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

permuted_choice_2_table = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

number_of_rotations_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def is_binary_str(variable):
    return set(variable).issubset({'0', '1'}) and isinstance(variable, str)

def zero_pad(object, target_len):
    while len(object) < target_len:
        object = '0' + object
    return object

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

def initial_permutation(in_64):
    assert is_binary_str(in_64)
    assert len(in_64) == 64
    out_64 = ""
    for pos in initial_permutation_table:
        out_64 += in_64[pos - 1]
    return out_64

def final_permutation(in_64):
    assert is_binary_str(in_64)
    assert len(in_64) == 64
    out_64 = ""
    for pos in final_permutation_table:
        out_64 += in_64[pos - 1]
    return out_64

def expantion(in_32):
    assert is_binary_str(in_32)
    assert len(in_32) == 32
    out_48 = ""
    for pos in expantion_table:
        out_48 += in_32[pos - 1]
    return out_48

def s_box(s_box_id, in_6):
    assert is_binary_str(in_6)
    assert len(in_6) == 6
    row_id = int(in_6[0] + in_6[-1], 2)
    column_id = int(in_6[1:-1], 2)
    return S_BOX[s_box_id][row_id][column_id]

def substitution(in_48):
    assert is_binary_str(in_48)
    assert len(in_48) == 48
    out_32 = ''
    for s_box_id in range(8):
        out_32 += s_box(s_box_id, in_48[s_box_id * 6 : (s_box_id + 1) * 6])
    assert len(out_32) == 32
    return out_32

def permutation(in_32):
    assert is_binary_str(in_32)
    assert len(in_32) == 32
    out_32 = ""
    for pos in permutation_table:
        out_32 += in_32[pos - 1]
    return out_32

def f_function(half_block_32, subkey_48):
    assert is_binary_str(half_block_32)
    assert is_binary_str(subkey_48)
    assert len(half_block_32) == 32
    assert len(subkey_48) == 48
    expantion_out_48 = expantion(half_block_32)
    substitution_in_48 = XOR_binary_str(expantion_out_48, subkey_48)
    substitution_out_32 = substitution(substitution_in_48)
    out_32 = permutation(substitution_out_32)
    assert len(out_32) == 32
    return out_32

def des_round(in_64, subkey_48):
    assert is_binary_str(in_64)
    assert len(in_64) == 64
    assert is_binary_str(subkey_48)
    assert len(subkey_48) == 48
    left_half_in_32 = in_64[0:32]
    right_half_in_32 = in_64[32:64]
    left_half_out_32 = right_half_in_32
    right_half_out_32 = XOR_binary_str(f_function(right_half_in_32, subkey_48), left_half_in_32)
    out_64 = left_half_out_32 + right_half_out_32
    assert len(out_64) == 64
    return out_64

def rotate(in_n, number_of_rotation):
    return in_n[number_of_rotation : ] + in_n[0 : number_of_rotation]

def pc_2(key_56):
    assert is_binary_str(key_56)
    assert len(key_56) == 56
    out_48 = ""
    for pos in permuted_choice_2_table:
        out_48 += key_56[pos - 1]
    assert len(out_48) == 48
    return out_48

def key_schedule(key_64):
    assert is_binary_str(key_64)
    assert len(key_64) == 64
    left_half = ""
    for pos in permuted_choice_1_left_table:
        left_half += key_64[pos - 1]
    right_half = ""
    for pos in permuted_choice_1_right_table:
        right_half += key_64[pos - 1]
    out = list()
    for i in range(16):
        right_half = rotate(right_half, number_of_rotations_table[i])
        left_half = rotate(left_half, number_of_rotations_table[i])
        out.append(pc_2(left_half + right_half))
    return out

def des(plaintext_64, key_64, decrypt=False):
    assert is_binary_str(plaintext_64)
    assert is_binary_str(key_64)
    assert len(plaintext_64) == 64
    assert len(key_64) == 64
    ciphertext_64 = initial_permutation(plaintext_64)
    subkeys = key_schedule(key_64)
    if decrypt:
        subkeys.reverse()
    for subkey in subkeys:
        ciphertext_64 = des_round(ciphertext_64, subkey)
    ciphertext_64 = ciphertext_64[32:64] + ciphertext_64[0:32]
    ciphertext_64 = final_permutation(ciphertext_64)
    return ciphertext_64

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

def des_hex(plaintext_16, key_16, decrypt=False):
    plaintext_64 = hex_str_2_bi_str(plaintext_16)
    key_64 = hex_str_2_bi_str(key_16)
    out_64 =  des(plaintext_64, key_64, decrypt)
    out_16 = hex(int(out_64, 2))[2:]
    out_16 = zero_pad(out_16, 16)
    return out_16

if __name__ == "__main__":
    pass