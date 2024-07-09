import unittest
import DES

class TestTECBinvperm_encrypt(unittest.TestCase):

    def test_0(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '95f8a5e5dd31d900'
        CIPHERTEXT = '8000000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_1(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'dd7f121ca5015619'
        CIPHERTEXT = '4000000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_2(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '2e8653104f3834ea'
        CIPHERTEXT = '2000000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_3(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '4bd388ff6cd81d4f'
        CIPHERTEXT = '1000000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_4(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '20b9e767b2fb1456'
        CIPHERTEXT = '0800000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_5(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '55579380d77138ef'
        CIPHERTEXT = '0400000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_6(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '6cc5defaaf04512f'
        CIPHERTEXT = '0200000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_7(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0d9f279ba5d87260'
        CIPHERTEXT = '0100000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_8(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'd9031b0271bd5a0a'
        CIPHERTEXT = '0080000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_9(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '424250b37c3dd951'
        CIPHERTEXT = '0040000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_10(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'b8061b7ecd9a21e5'
        CIPHERTEXT = '0020000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_11(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'f15d0f286b65bd28'
        CIPHERTEXT = '0010000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_12(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'add0cc8d6e5deba1'
        CIPHERTEXT = '0008000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_13(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e6d5f82752ad63d1'
        CIPHERTEXT = '0004000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_14(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'ecbfe3bd3f591a5e'
        CIPHERTEXT = '0002000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_15(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'f356834379d165cd'
        CIPHERTEXT = '0001000000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_16(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '2b9f982f20037fa9'
        CIPHERTEXT = '0000800000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_17(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '889de068a16f0be6'
        CIPHERTEXT = '0000400000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_18(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e19e275d846a1298'
        CIPHERTEXT = '0000200000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_19(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '329a8ed523d71aec'
        CIPHERTEXT = '0000100000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_20(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e7fce22557d23c97'
        CIPHERTEXT = '0000080000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_21(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '12a9f5817ff2d65d'
        CIPHERTEXT = '0000040000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_22(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'a484c3ad38dc9c19'
        CIPHERTEXT = '0000020000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_23(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'fbe00a8a1ef8ad72'
        CIPHERTEXT = '0000010000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_24(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '750d079407521363'
        CIPHERTEXT = '0000008000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_25(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '64feed9c724c2faf'
        CIPHERTEXT = '0000004000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_26(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'f02b263b328e2b60'
        CIPHERTEXT = '0000002000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_27(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '9d64555a9a10b852'
        CIPHERTEXT = '0000001000000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_28(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'd106ff0bed5255d7'
        CIPHERTEXT = '0000000800000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_29(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e1652c6b138c64a5'
        CIPHERTEXT = '0000000400000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_30(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e428581186ec8f46'
        CIPHERTEXT = '0000000200000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_31(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'aeb5f5ede22d1a36'
        CIPHERTEXT = '0000000100000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_32(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e943d7568aec0c5c'
        CIPHERTEXT = '0000000080000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_33(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'df98c8276f54b04b'
        CIPHERTEXT = '0000000040000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_34(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'b160e4680f6c696f'
        CIPHERTEXT = '0000000020000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_35(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'fa0752b07d9c4ab8'
        CIPHERTEXT = '0000000010000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_36(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'ca3a2b036dbc8502'
        CIPHERTEXT = '0000000008000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_37(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '5e0905517bb59bcf'
        CIPHERTEXT = '0000000004000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_38(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '814eeb3b91d90726'
        CIPHERTEXT = '0000000002000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_39(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '4d49db1532919c9f'
        CIPHERTEXT = '0000000001000000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_40(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '25eb5fc3f8cf0621'
        CIPHERTEXT = '0000000000800000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_41(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'ab6a20c0620d1c6f'
        CIPHERTEXT = '0000000000400000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_42(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '79e90dbc98f92cca'
        CIPHERTEXT = '0000000000200000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_43(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '866ecedd8072bb0e'
        CIPHERTEXT = '0000000000100000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_44(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '8b54536f2f3e64a8'
        CIPHERTEXT = '0000000000080000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_45(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'ea51d3975595b86b'
        CIPHERTEXT = '0000000000040000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_46(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'caffc6ac4542de31'
        CIPHERTEXT = '0000000000020000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_47(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '8dd45a2ddf90796c'
        CIPHERTEXT = '0000000000010000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_48(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '1029d55e880ec2d0'
        CIPHERTEXT = '0000000000008000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_49(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '5d86cb23639dbea9'
        CIPHERTEXT = '0000000000004000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_50(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '1d1ca853ae7c0c5f'
        CIPHERTEXT = '0000000000002000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_51(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'ce332329248f3228'
        CIPHERTEXT = '0000000000001000'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_52(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '8405d1abe24fb942'
        CIPHERTEXT = '0000000000000800'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_53(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e643d78090ca4207'
        CIPHERTEXT = '0000000000000400'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_54(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '48221b9937748a23'
        CIPHERTEXT = '0000000000000200'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_55(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'dd7c0bbd61fafd54'
        CIPHERTEXT = '0000000000000100'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_56(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '2fbc291a570db5c4'
        CIPHERTEXT = '0000000000000080'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_57(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'e07c30d7e4e26e12'
        CIPHERTEXT = '0000000000000040'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_58(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0953e2258e8e90a1'
        CIPHERTEXT = '0000000000000020'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_59(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '5b711bc4ceebf2ee'
        CIPHERTEXT = '0000000000000010'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_60(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'cc083f1e6d9e85f6'
        CIPHERTEXT = '0000000000000008'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_61(self):
        KEYs = '0101010101010101'
        PLAINTEXT = 'd2fd8867d50d2dfe'
        CIPHERTEXT = '0000000000000004'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_62(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '06e7ea22ce92708f'
        CIPHERTEXT = '0000000000000002'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_63(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '166b40b44aba4bd6'
        CIPHERTEXT = '0000000000000001'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

class TestTECBinvperm_decrypt(unittest.TestCase):

    def test_0(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '8000000000000000'
        PLAINTEXT = '95f8a5e5dd31d900'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_1(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '4000000000000000'
        PLAINTEXT = 'dd7f121ca5015619'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_2(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '2000000000000000'
        PLAINTEXT = '2e8653104f3834ea'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_3(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '1000000000000000'
        PLAINTEXT = '4bd388ff6cd81d4f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_4(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0800000000000000'
        PLAINTEXT = '20b9e767b2fb1456'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_5(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0400000000000000'
        PLAINTEXT = '55579380d77138ef'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_6(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0200000000000000'
        PLAINTEXT = '6cc5defaaf04512f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_7(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0100000000000000'
        PLAINTEXT = '0d9f279ba5d87260'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_8(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0080000000000000'
        PLAINTEXT = 'd9031b0271bd5a0a'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_9(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0040000000000000'
        PLAINTEXT = '424250b37c3dd951'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_10(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0020000000000000'
        PLAINTEXT = 'b8061b7ecd9a21e5'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_11(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0010000000000000'
        PLAINTEXT = 'f15d0f286b65bd28'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_12(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0008000000000000'
        PLAINTEXT = 'add0cc8d6e5deba1'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_13(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0004000000000000'
        PLAINTEXT = 'e6d5f82752ad63d1'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_14(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0002000000000000'
        PLAINTEXT = 'ecbfe3bd3f591a5e'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_15(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0001000000000000'
        PLAINTEXT = 'f356834379d165cd'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_16(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000800000000000'
        PLAINTEXT = '2b9f982f20037fa9'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_17(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000400000000000'
        PLAINTEXT = '889de068a16f0be6'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_18(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000200000000000'
        PLAINTEXT = 'e19e275d846a1298'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_19(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000100000000000'
        PLAINTEXT = '329a8ed523d71aec'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_20(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000080000000000'
        PLAINTEXT = 'e7fce22557d23c97'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_21(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000040000000000'
        PLAINTEXT = '12a9f5817ff2d65d'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_22(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000020000000000'
        PLAINTEXT = 'a484c3ad38dc9c19'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_23(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000010000000000'
        PLAINTEXT = 'fbe00a8a1ef8ad72'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_24(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000008000000000'
        PLAINTEXT = '750d079407521363'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_25(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000004000000000'
        PLAINTEXT = '64feed9c724c2faf'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_26(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000002000000000'
        PLAINTEXT = 'f02b263b328e2b60'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_27(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000001000000000'
        PLAINTEXT = '9d64555a9a10b852'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_28(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000800000000'
        PLAINTEXT = 'd106ff0bed5255d7'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_29(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000400000000'
        PLAINTEXT = 'e1652c6b138c64a5'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_30(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000200000000'
        PLAINTEXT = 'e428581186ec8f46'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_31(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000100000000'
        PLAINTEXT = 'aeb5f5ede22d1a36'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_32(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000080000000'
        PLAINTEXT = 'e943d7568aec0c5c'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_33(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000040000000'
        PLAINTEXT = 'df98c8276f54b04b'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_34(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000020000000'
        PLAINTEXT = 'b160e4680f6c696f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_35(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000010000000'
        PLAINTEXT = 'fa0752b07d9c4ab8'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_36(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000008000000'
        PLAINTEXT = 'ca3a2b036dbc8502'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_37(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000004000000'
        PLAINTEXT = '5e0905517bb59bcf'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_38(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000002000000'
        PLAINTEXT = '814eeb3b91d90726'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_39(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000001000000'
        PLAINTEXT = '4d49db1532919c9f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_40(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000800000'
        PLAINTEXT = '25eb5fc3f8cf0621'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_41(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000400000'
        PLAINTEXT = 'ab6a20c0620d1c6f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_42(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000200000'
        PLAINTEXT = '79e90dbc98f92cca'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_43(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000100000'
        PLAINTEXT = '866ecedd8072bb0e'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_44(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000080000'
        PLAINTEXT = '8b54536f2f3e64a8'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_45(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000040000'
        PLAINTEXT = 'ea51d3975595b86b'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_46(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000020000'
        PLAINTEXT = 'caffc6ac4542de31'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_47(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000010000'
        PLAINTEXT = '8dd45a2ddf90796c'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_48(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000008000'
        PLAINTEXT = '1029d55e880ec2d0'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_49(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000004000'
        PLAINTEXT = '5d86cb23639dbea9'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_50(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000002000'
        PLAINTEXT = '1d1ca853ae7c0c5f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_51(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000001000'
        PLAINTEXT = 'ce332329248f3228'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_52(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000800'
        PLAINTEXT = '8405d1abe24fb942'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_53(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000400'
        PLAINTEXT = 'e643d78090ca4207'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_54(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000200'
        PLAINTEXT = '48221b9937748a23'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_55(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000100'
        PLAINTEXT = 'dd7c0bbd61fafd54'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_56(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000080'
        PLAINTEXT = '2fbc291a570db5c4'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_57(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000040'
        PLAINTEXT = 'e07c30d7e4e26e12'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_58(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000020'
        PLAINTEXT = '0953e2258e8e90a1'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_59(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000010'
        PLAINTEXT = '5b711bc4ceebf2ee'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_60(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000008'
        PLAINTEXT = 'cc083f1e6d9e85f6'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_61(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000004'
        PLAINTEXT = 'd2fd8867d50d2dfe'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_62(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000002'
        PLAINTEXT = '06e7ea22ce92708f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_63(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0000000000000001'
        PLAINTEXT = '166b40b44aba4bd6'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

class TestTECBpermop_encrypt(unittest.TestCase):

    def test_0(self):
        KEYs = '1046913489980131'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '88d55e54f54c97b4'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_1(self):
        KEYs = '1007103489988020'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '0c0cc00c83ea48fd'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_2(self):
        KEYs = '10071034c8980120'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '83bc8ef3a6570183'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_3(self):
        KEYs = '1046103489988020'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'df725dcad94ea2e9'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_4(self):
        KEYs = '1086911519190101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'e652b53b550be8b0'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_5(self):
        KEYs = '1086911519580101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'af527120c485cbb0'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_6(self):
        KEYs = '5107b01519580101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '0f04ce393db926d5'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_7(self):
        KEYs = '1007b01519190101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'c9f00ffc74079067'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_8(self):
        KEYs = '3107915498080101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '7cfd82a593252b4e'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_9(self):
        KEYs = '3107919498080101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'cb49a2f9e91363e3'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_10(self):
        KEYs = '10079115b9080140'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '00b588be70d23f56'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_11(self):
        KEYs = '3107911598080140'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '406a9a6ab43399ae'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_12(self):
        KEYs = '1007d01589980101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '6cb773611dca9ada'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_13(self):
        KEYs = '9107911589980101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '67fd21c17dbb5d70'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_14(self):
        KEYs = '9107d01589190101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '9592cb4110430787'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_15(self):
        KEYs = '1007d01598980120'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'a6b7ff68a318ddd3'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_16(self):
        KEYs = '1007940498190101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '4d102196c914ca16'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_17(self):
        KEYs = '0107910491190401'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '2dfa9f4573594965'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_18(self):
        KEYs = '0107910491190101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'b46604816c0e0774'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_19(self):
        KEYs = '0107940491190401'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '6e7e6221a4f34e87'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_20(self):
        KEYs = '19079210981a0101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'aa85e74643233199'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_21(self):
        KEYs = '1007911998190801'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '2e5a19db4d1962d6'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_22(self):
        KEYs = '10079119981a0801'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '23a866a809d30894'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_23(self):
        KEYs = '1007921098190101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'd812d961f017d320'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_24(self):
        KEYs = '100791159819010b'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '055605816e58608f'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_25(self):
        KEYs = '1004801598190101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'abd88e8b1b7716f1'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_26(self):
        KEYs = '1004801598190102'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '537ac95be69da1e1'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_27(self):
        KEYs = '1004801598190108'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'aed0f6ae3c25cdd8'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_28(self):
        KEYs = '1002911598100104'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'b3e35a5ee53e7b8d'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_29(self):
        KEYs = '1002911598190104'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '61c79c71921a2ef8'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_30(self):
        KEYs = '1002911598100201'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'e2f5728f0995013c'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_31(self):
        KEYs = '1002911698100101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '1aeac39a61f0a464'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

class TestTECBpermop_decrypt(unittest.TestCase):

    def test_0(self):
        KEYs = '1046913489980131'
        CIPHERTEXT = '88d55e54f54c97b4'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_1(self):
        KEYs = '1007103489988020'
        CIPHERTEXT = '0c0cc00c83ea48fd'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_2(self):
        KEYs = '10071034c8980120'
        CIPHERTEXT = '83bc8ef3a6570183'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_3(self):
        KEYs = '1046103489988020'
        CIPHERTEXT = 'df725dcad94ea2e9'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_4(self):
        KEYs = '1086911519190101'
        CIPHERTEXT = 'e652b53b550be8b0'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_5(self):
        KEYs = '1086911519580101'
        CIPHERTEXT = 'af527120c485cbb0'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_6(self):
        KEYs = '5107b01519580101'
        CIPHERTEXT = '0f04ce393db926d5'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_7(self):
        KEYs = '1007b01519190101'
        CIPHERTEXT = 'c9f00ffc74079067'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_8(self):
        KEYs = '3107915498080101'
        CIPHERTEXT = '7cfd82a593252b4e'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_9(self):
        KEYs = '3107919498080101'
        CIPHERTEXT = 'cb49a2f9e91363e3'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_10(self):
        KEYs = '10079115b9080140'
        CIPHERTEXT = '00b588be70d23f56'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_11(self):
        KEYs = '3107911598080140'
        CIPHERTEXT = '406a9a6ab43399ae'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_12(self):
        KEYs = '1007d01589980101'
        CIPHERTEXT = '6cb773611dca9ada'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_13(self):
        KEYs = '9107911589980101'
        CIPHERTEXT = '67fd21c17dbb5d70'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_14(self):
        KEYs = '9107d01589190101'
        CIPHERTEXT = '9592cb4110430787'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_15(self):
        KEYs = '1007d01598980120'
        CIPHERTEXT = 'a6b7ff68a318ddd3'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_16(self):
        KEYs = '1007940498190101'
        CIPHERTEXT = '4d102196c914ca16'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_17(self):
        KEYs = '0107910491190401'
        CIPHERTEXT = '2dfa9f4573594965'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_18(self):
        KEYs = '0107910491190101'
        CIPHERTEXT = 'b46604816c0e0774'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_19(self):
        KEYs = '0107940491190401'
        CIPHERTEXT = '6e7e6221a4f34e87'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_20(self):
        KEYs = '19079210981a0101'
        CIPHERTEXT = 'aa85e74643233199'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_21(self):
        KEYs = '1007911998190801'
        CIPHERTEXT = '2e5a19db4d1962d6'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_22(self):
        KEYs = '10079119981a0801'
        CIPHERTEXT = '23a866a809d30894'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_23(self):
        KEYs = '1007921098190101'
        CIPHERTEXT = 'd812d961f017d320'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_24(self):
        KEYs = '100791159819010b'
        CIPHERTEXT = '055605816e58608f'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_25(self):
        KEYs = '1004801598190101'
        CIPHERTEXT = 'abd88e8b1b7716f1'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_26(self):
        KEYs = '1004801598190102'
        CIPHERTEXT = '537ac95be69da1e1'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_27(self):
        KEYs = '1004801598190108'
        CIPHERTEXT = 'aed0f6ae3c25cdd8'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_28(self):
        KEYs = '1002911598100104'
        CIPHERTEXT = 'b3e35a5ee53e7b8d'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_29(self):
        KEYs = '1002911598190104'
        CIPHERTEXT = '61c79c71921a2ef8'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_30(self):
        KEYs = '1002911598100201'
        CIPHERTEXT = 'e2f5728f0995013c'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_31(self):
        KEYs = '1002911698100101'
        CIPHERTEXT = '1aeac39a61f0a464'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

class TestTECBsubtab_encrypt(unittest.TestCase):
    def test_0(self):
        KEYs = '7ca110454a1a6e57'
        PLAINTEXT = '01a1d6d039776742'
        CIPHERTEXT = '690f5b0d9a26939b'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_1(self):
        KEYs = '0131d9619dc1376e'
        PLAINTEXT = '5cd54ca83def57da'
        CIPHERTEXT = '7a389d10354bd271'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_2(self):
        KEYs = '07a1133e4a0b2686'
        PLAINTEXT = '0248d43806f67172'
        CIPHERTEXT = '868ebb51cab4599a'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_3(self):
        KEYs = '3849674c2602319e'
        PLAINTEXT = '51454b582ddf440a'
        CIPHERTEXT = '7178876e01f19b2a'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_4(self):
        KEYs = '04b915ba43feb5b6'
        PLAINTEXT = '42fd443059577fa2'
        CIPHERTEXT = 'af37fb421f8c4095'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_5(self):
        KEYs = '0113b970fd34f2ce'
        PLAINTEXT = '059b5e0851cf143a'
        CIPHERTEXT = '86a560f10ec6d85b'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_6(self):
        KEYs = '0170f175468fb5e6'
        PLAINTEXT = '0756d8e0774761d2'
        CIPHERTEXT = '0cd3da020021dc09'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_7(self):
        KEYs = '43297fad38e373fe'
        PLAINTEXT = '762514b829bf486a'
        CIPHERTEXT = 'ea676b2cb7db2b7a'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_8(self):
        KEYs = '07a7137045da2a16'
        PLAINTEXT = '3bdd119049372802'
        CIPHERTEXT = 'dfd64a815caf1a0f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_9(self):
        KEYs = '04689104c2fd3b2f'
        PLAINTEXT = '26955f6835af609a'
        CIPHERTEXT = '5c513c9c4886c088'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_10(self):
        KEYs = '37d06bb516cb7546'
        PLAINTEXT = '164d5e404f275232'
        CIPHERTEXT = '0a2aeeae3ff4ab77'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_11(self):
        KEYs = '1f08260d1ac2465e'
        PLAINTEXT = '6b056e18759f5cca'
        CIPHERTEXT = 'ef1bf03e5dfa575a'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_12(self):
        KEYs = '584023641aba6176'
        PLAINTEXT = '004bd6ef09176062'
        CIPHERTEXT = '88bf0db6d70dee56'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_13(self):
        KEYs = '025816164629b007'
        PLAINTEXT = '480d39006ee762f2'
        CIPHERTEXT = 'a1f9915541020b56'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_14(self):
        KEYs = '49793ebc79b3258f'
        PLAINTEXT = '437540c8698f3cfa'
        CIPHERTEXT = '6fbf1cafcffd0556'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_15(self):
        KEYs = '4fb05e1515ab73a7'
        PLAINTEXT = '072d43a077075292'
        CIPHERTEXT = '2f22e49bab7ca1ac'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_16(self):
        KEYs = '49e95d6d4ca229bf'
        PLAINTEXT = '02fe55778117f12a'
        CIPHERTEXT = '5a6b612cc26cce4a'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_17(self):
        KEYs = '018310dc409b26d6'
        PLAINTEXT = '1d9d5c5018f728c2'
        CIPHERTEXT = '5f4c038ed12b2e41'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_18(self):
        KEYs = '1c587f1c13924fef'
        PLAINTEXT = '305532286d6f295a'
        CIPHERTEXT = '63fac0d034d9f793'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

class TestTECBsubtab_decrypt(unittest.TestCase):
    def test_0(self):
        KEYs = '7ca110454a1a6e57'
        CIPHERTEXT = '690f5b0d9a26939b'
        PLAINTEXT = '01a1d6d039776742'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_1(self):
        KEYs = '0131d9619dc1376e'
        CIPHERTEXT = '7a389d10354bd271'
        PLAINTEXT = '5cd54ca83def57da'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_2(self):
        KEYs = '07a1133e4a0b2686'
        CIPHERTEXT = '868ebb51cab4599a'
        PLAINTEXT = '0248d43806f67172'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_3(self):
        KEYs = '3849674c2602319e'
        CIPHERTEXT = '7178876e01f19b2a'
        PLAINTEXT = '51454b582ddf440a'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_4(self):
        KEYs = '04b915ba43feb5b6'
        CIPHERTEXT = 'af37fb421f8c4095'
        PLAINTEXT = '42fd443059577fa2'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_5(self):
        KEYs = '0113b970fd34f2ce'
        CIPHERTEXT = '86a560f10ec6d85b'
        PLAINTEXT = '059b5e0851cf143a'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_6(self):
        KEYs = '0170f175468fb5e6'
        CIPHERTEXT = '0cd3da020021dc09'
        PLAINTEXT = '0756d8e0774761d2'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_7(self):
        KEYs = '43297fad38e373fe'
        CIPHERTEXT = 'ea676b2cb7db2b7a'
        PLAINTEXT = '762514b829bf486a'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_8(self):
        KEYs = '07a7137045da2a16'
        CIPHERTEXT = 'dfd64a815caf1a0f'
        PLAINTEXT = '3bdd119049372802'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_9(self):
        KEYs = '04689104c2fd3b2f'
        CIPHERTEXT = '5c513c9c4886c088'
        PLAINTEXT = '26955f6835af609a'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_10(self):
        KEYs = '37d06bb516cb7546'
        CIPHERTEXT = '0a2aeeae3ff4ab77'
        PLAINTEXT = '164d5e404f275232'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_11(self):
        KEYs = '1f08260d1ac2465e'
        CIPHERTEXT = 'ef1bf03e5dfa575a'
        PLAINTEXT = '6b056e18759f5cca'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_12(self):
        KEYs = '584023641aba6176'
        CIPHERTEXT = '88bf0db6d70dee56'
        PLAINTEXT = '004bd6ef09176062'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_13(self):
        KEYs = '025816164629b007'
        CIPHERTEXT = 'a1f9915541020b56'
        PLAINTEXT = '480d39006ee762f2'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_14(self):
        KEYs = '49793ebc79b3258f'
        CIPHERTEXT = '6fbf1cafcffd0556'
        PLAINTEXT = '437540c8698f3cfa'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_15(self):
        KEYs = '4fb05e1515ab73a7'
        CIPHERTEXT = '2f22e49bab7ca1ac'
        PLAINTEXT = '072d43a077075292'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_16(self):
        KEYs = '49e95d6d4ca229bf'
        CIPHERTEXT = '5a6b612cc26cce4a'
        PLAINTEXT = '02fe55778117f12a'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_17(self):
        KEYs = '018310dc409b26d6'
        CIPHERTEXT = '5f4c038ed12b2e41'
        PLAINTEXT = '1d9d5c5018f728c2'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_18(self):
        KEYs = '1c587f1c13924fef'
        CIPHERTEXT = '63fac0d034d9f793'
        PLAINTEXT = '305532286d6f295a'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

class TestTECBvarkey_encrypt(unittest.TestCase):
    def test_0(self):
        KEYs = '8001010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '95a8d72813daa94d'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_1(self):
        KEYs = '4001010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '0eec1487dd8c26d5'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_2(self):
        KEYs = '2001010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '7ad16ffb79c45926'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_3(self):
        KEYs = '1001010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'd3746294ca6a6cf3'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_4(self):
        KEYs = '0801010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '809f5f873c1fd761'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_5(self):
        KEYs = '0401010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'c02faffec989d1fc'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_6(self):
        KEYs = '0201010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '4615aa1d33e72f10'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_7(self):
        KEYs = '0180010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '2055123350c00858'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_8(self):
        KEYs = '0140010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'df3b99d6577397c8'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_9(self):
        KEYs = '0120010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '31fe17369b5288c9'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_10(self):
        KEYs = '0110010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'dfdd3cc64dae1642'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_11(self):
        KEYs = '0108010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '178c83ce2b399d94'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_12(self):
        KEYs = '0104010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '50f636324a9b7f80'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_13(self):
        KEYs = '0102010101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'a8468ee3bc18f06d'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_14(self):
        KEYs = '0101800101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'a2dc9e92fd3cde92'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_15(self):
        KEYs = '0101400101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'cac09f797d031287'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_16(self):
        KEYs = '0101200101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '90ba680b22aeb525'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_17(self):
        KEYs = '0101100101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'ce7a24f350e280b6'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_18(self):
        KEYs = '0101080101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '882bff0aa01a0b87'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_19(self):
        KEYs = '0101040101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '25610288924511c2'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_20(self):
        KEYs = '0101020101010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'c71516c29c75d170'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_21(self):
        KEYs = '0101018001010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '5199c29a52c9f059'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_22(self):
        KEYs = '0101014001010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'c22f0a294a71f29f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_23(self):
        KEYs = '0101012001010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'ee371483714c02ea'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_24(self):
        KEYs = '0101011001010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'a81fbd448f9e522f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_25(self):
        KEYs = '0101010801010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '4f644c92e192dfed'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_26(self):
        KEYs = '0101010401010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '1afa9a66a6df92ae'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_27(self):
        KEYs = '0101010201010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'b3c1cc715cb879d8'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_28(self):
        KEYs = '0101010180010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '19d032e64ab0bd8b'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_29(self):
        KEYs = '0101010140010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '3cfaa7a7dc8720dc'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_30(self):
        KEYs = '0101010120010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'b7265f7f447ac6f3'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_31(self):
        KEYs = '0101010110010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '9db73b3c0d163f54'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_32(self):
        KEYs = '0101010108010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '8181b65babf4a975'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_33(self):
        KEYs = '0101010104010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '93c9b64042eaa240'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_34(self):
        KEYs = '0101010102010101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '5570530829705592'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_35(self):
        KEYs = '0101010101800101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '8638809e878787a0'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_36(self):
        KEYs = '0101010101400101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '41b9a79af79ac208'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_37(self):
        KEYs = '0101010101200101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '7a9be42f2009a892'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_38(self):
        KEYs = '0101010101100101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '29038d56ba6d2745'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_39(self):
        KEYs = '0101010101080101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '5495c6abf1e5df51'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_40(self):
        KEYs = '0101010101040101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'ae13dbd561488933'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_41(self):
        KEYs = '0101010101020101'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '024d1ffa8904e389'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_42(self):
        KEYs = '0101010101018001'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'd1399712f99bf02e'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_43(self):
        KEYs = '0101010101014001'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '14c1d7c1cffec79e'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_44(self):
        KEYs = '0101010101012001'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '1de5279dae3bed6f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_45(self):
        KEYs = '0101010101011001'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'e941a33f85501303'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_46(self):
        KEYs = '0101010101010801'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'da99dbbc9a03f379'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_47(self):
        KEYs = '0101010101010401'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'b7fc92f91d8e92e9'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_48(self):
        KEYs = '0101010101010201'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'ae8e5caa3ca04e85'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_49(self):
        KEYs = '0101010101010180'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '9cc62df43b6eed74'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_50(self):
        KEYs = '0101010101010140'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'd863dbb5c59a91a0'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_51(self):
        KEYs = '0101010101010120'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'a1ab2190545b91d7'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_52(self):
        KEYs = '0101010101010110'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '0875041e64c570f7'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_53(self):
        KEYs = '0101010101010108'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '5a594528bebef1cc'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_54(self):
        KEYs = '0101010101010104'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = 'fcdb3291de21f0c0'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_55(self):
        KEYs = '0101010101010102'
        PLAINTEXT = '0000000000000000'
        CIPHERTEXT = '869efd7f9f265a09'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

class TestTECBvarkey_decrypt(unittest.TestCase):
    def test_0(self):
        KEYs = '8001010101010101'
        CIPHERTEXT = '95a8d72813daa94d'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_1(self):
        KEYs = '4001010101010101'
        CIPHERTEXT = '0eec1487dd8c26d5'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_2(self):
        KEYs = '2001010101010101'
        CIPHERTEXT = '7ad16ffb79c45926'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_3(self):
        KEYs = '1001010101010101'
        CIPHERTEXT = 'd3746294ca6a6cf3'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_4(self):
        KEYs = '0801010101010101'
        CIPHERTEXT = '809f5f873c1fd761'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_5(self):
        KEYs = '0401010101010101'
        CIPHERTEXT = 'c02faffec989d1fc'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_6(self):
        KEYs = '0201010101010101'
        CIPHERTEXT = '4615aa1d33e72f10'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_7(self):
        KEYs = '0180010101010101'
        CIPHERTEXT = '2055123350c00858'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_8(self):
        KEYs = '0140010101010101'
        CIPHERTEXT = 'df3b99d6577397c8'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_9(self):
        KEYs = '0120010101010101'
        CIPHERTEXT = '31fe17369b5288c9'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_10(self):
        KEYs = '0110010101010101'
        CIPHERTEXT = 'dfdd3cc64dae1642'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_11(self):
        KEYs = '0108010101010101'
        CIPHERTEXT = '178c83ce2b399d94'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_12(self):
        KEYs = '0104010101010101'
        CIPHERTEXT = '50f636324a9b7f80'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_13(self):
        KEYs = '0102010101010101'
        CIPHERTEXT = 'a8468ee3bc18f06d'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_14(self):
        KEYs = '0101800101010101'
        CIPHERTEXT = 'a2dc9e92fd3cde92'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_15(self):
        KEYs = '0101400101010101'
        CIPHERTEXT = 'cac09f797d031287'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_16(self):
        KEYs = '0101200101010101'
        CIPHERTEXT = '90ba680b22aeb525'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_17(self):
        KEYs = '0101100101010101'
        CIPHERTEXT = 'ce7a24f350e280b6'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_18(self):
        KEYs = '0101080101010101'
        CIPHERTEXT = '882bff0aa01a0b87'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_19(self):
        KEYs = '0101040101010101'
        CIPHERTEXT = '25610288924511c2'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_20(self):
        KEYs = '0101020101010101'
        CIPHERTEXT = 'c71516c29c75d170'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_21(self):
        KEYs = '0101018001010101'
        CIPHERTEXT = '5199c29a52c9f059'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_22(self):
        KEYs = '0101014001010101'
        CIPHERTEXT = 'c22f0a294a71f29f'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_23(self):
        KEYs = '0101012001010101'
        CIPHERTEXT = 'ee371483714c02ea'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_24(self):
        KEYs = '0101011001010101'
        CIPHERTEXT = 'a81fbd448f9e522f'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_25(self):
        KEYs = '0101010801010101'
        CIPHERTEXT = '4f644c92e192dfed'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_26(self):
        KEYs = '0101010401010101'
        CIPHERTEXT = '1afa9a66a6df92ae'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_27(self):
        KEYs = '0101010201010101'
        CIPHERTEXT = 'b3c1cc715cb879d8'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_28(self):
        KEYs = '0101010180010101'
        CIPHERTEXT = '19d032e64ab0bd8b'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_29(self):
        KEYs = '0101010140010101'
        CIPHERTEXT = '3cfaa7a7dc8720dc'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_30(self):
        KEYs = '0101010120010101'
        CIPHERTEXT = 'b7265f7f447ac6f3'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_31(self):
        KEYs = '0101010110010101'
        CIPHERTEXT = '9db73b3c0d163f54'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_32(self):
        KEYs = '0101010108010101'
        CIPHERTEXT = '8181b65babf4a975'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_33(self):
        KEYs = '0101010104010101'
        CIPHERTEXT = '93c9b64042eaa240'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_34(self):
        KEYs = '0101010102010101'
        CIPHERTEXT = '5570530829705592'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_35(self):
        KEYs = '0101010101800101'
        CIPHERTEXT = '8638809e878787a0'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_36(self):
        KEYs = '0101010101400101'
        CIPHERTEXT = '41b9a79af79ac208'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_37(self):
        KEYs = '0101010101200101'
        CIPHERTEXT = '7a9be42f2009a892'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_38(self):
        KEYs = '0101010101100101'
        CIPHERTEXT = '29038d56ba6d2745'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_39(self):
        KEYs = '0101010101080101'
        CIPHERTEXT = '5495c6abf1e5df51'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_40(self):
        KEYs = '0101010101040101'
        CIPHERTEXT = 'ae13dbd561488933'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_41(self):
        KEYs = '0101010101020101'
        CIPHERTEXT = '024d1ffa8904e389'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_42(self):
        KEYs = '0101010101018001'
        CIPHERTEXT = 'd1399712f99bf02e'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_43(self):
        KEYs = '0101010101014001'
        CIPHERTEXT = '14c1d7c1cffec79e'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_44(self):
        KEYs = '0101010101012001'
        CIPHERTEXT = '1de5279dae3bed6f'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_45(self):
        KEYs = '0101010101011001'
        CIPHERTEXT = 'e941a33f85501303'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_46(self):
        KEYs = '0101010101010801'
        CIPHERTEXT = 'da99dbbc9a03f379'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_47(self):
        KEYs = '0101010101010401'
        CIPHERTEXT = 'b7fc92f91d8e92e9'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_48(self):
        KEYs = '0101010101010201'
        CIPHERTEXT = 'ae8e5caa3ca04e85'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_49(self):
        KEYs = '0101010101010180'
        CIPHERTEXT = '9cc62df43b6eed74'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_50(self):
        KEYs = '0101010101010140'
        CIPHERTEXT = 'd863dbb5c59a91a0'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_51(self):
        KEYs = '0101010101010120'
        CIPHERTEXT = 'a1ab2190545b91d7'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_52(self):
        KEYs = '0101010101010110'
        CIPHERTEXT = '0875041e64c570f7'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_53(self):
        KEYs = '0101010101010108'
        CIPHERTEXT = '5a594528bebef1cc'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_54(self):
        KEYs = '0101010101010104'
        CIPHERTEXT = 'fcdb3291de21f0c0'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_55(self):
        KEYs = '0101010101010102'
        CIPHERTEXT = '869efd7f9f265a09'
        PLAINTEXT = '0000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

class TestTECBvartext_encrypt(unittest.TestCase):
    def test_0(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '8000000000000000'
        CIPHERTEXT = '95f8a5e5dd31d900'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_1(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '4000000000000000'
        CIPHERTEXT = 'dd7f121ca5015619'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_2(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '2000000000000000'
        CIPHERTEXT = '2e8653104f3834ea'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_3(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '1000000000000000'
        CIPHERTEXT = '4bd388ff6cd81d4f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_4(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0800000000000000'
        CIPHERTEXT = '20b9e767b2fb1456'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_5(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0400000000000000'
        CIPHERTEXT = '55579380d77138ef'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_6(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0200000000000000'
        CIPHERTEXT = '6cc5defaaf04512f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_7(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0100000000000000'
        CIPHERTEXT = '0d9f279ba5d87260'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_8(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0080000000000000'
        CIPHERTEXT = 'd9031b0271bd5a0a'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_9(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0040000000000000'
        CIPHERTEXT = '424250b37c3dd951'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_10(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0020000000000000'
        CIPHERTEXT = 'b8061b7ecd9a21e5'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_11(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0010000000000000'
        CIPHERTEXT = 'f15d0f286b65bd28'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_12(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0008000000000000'
        CIPHERTEXT = 'add0cc8d6e5deba1'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_13(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0004000000000000'
        CIPHERTEXT = 'e6d5f82752ad63d1'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_14(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0002000000000000'
        CIPHERTEXT = 'ecbfe3bd3f591a5e'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_15(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0001000000000000'
        CIPHERTEXT = 'f356834379d165cd'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_16(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000800000000000'
        CIPHERTEXT = '2b9f982f20037fa9'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_17(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000400000000000'
        CIPHERTEXT = '889de068a16f0be6'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_18(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000200000000000'
        CIPHERTEXT = 'e19e275d846a1298'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_19(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000100000000000'
        CIPHERTEXT = '329a8ed523d71aec'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_20(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000080000000000'
        CIPHERTEXT = 'e7fce22557d23c97'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_21(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000040000000000'
        CIPHERTEXT = '12a9f5817ff2d65d'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_22(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000020000000000'
        CIPHERTEXT = 'a484c3ad38dc9c19'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_23(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000010000000000'
        CIPHERTEXT = 'fbe00a8a1ef8ad72'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_24(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000008000000000'
        CIPHERTEXT = '750d079407521363'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_25(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000004000000000'
        CIPHERTEXT = '64feed9c724c2faf'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_26(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000002000000000'
        CIPHERTEXT = 'f02b263b328e2b60'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_27(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000001000000000'
        CIPHERTEXT = '9d64555a9a10b852'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_28(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000800000000'
        CIPHERTEXT = 'd106ff0bed5255d7'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_29(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000400000000'
        CIPHERTEXT = 'e1652c6b138c64a5'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_30(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000200000000'
        CIPHERTEXT = 'e428581186ec8f46'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_31(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000100000000'
        CIPHERTEXT = 'aeb5f5ede22d1a36'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_32(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000080000000'
        CIPHERTEXT = 'e943d7568aec0c5c'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_33(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000040000000'
        CIPHERTEXT = 'df98c8276f54b04b'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_34(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000020000000'
        CIPHERTEXT = 'b160e4680f6c696f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_35(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000010000000'
        CIPHERTEXT = 'fa0752b07d9c4ab8'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_36(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000008000000'
        CIPHERTEXT = 'ca3a2b036dbc8502'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_37(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000004000000'
        CIPHERTEXT = '5e0905517bb59bcf'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_38(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000002000000'
        CIPHERTEXT = '814eeb3b91d90726'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_39(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000001000000'
        CIPHERTEXT = '4d49db1532919c9f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_40(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000800000'
        CIPHERTEXT = '25eb5fc3f8cf0621'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_41(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000400000'
        CIPHERTEXT = 'ab6a20c0620d1c6f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_42(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000200000'
        CIPHERTEXT = '79e90dbc98f92cca'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_43(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000100000'
        CIPHERTEXT = '866ecedd8072bb0e'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_44(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000080000'
        CIPHERTEXT = '8b54536f2f3e64a8'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_45(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000040000'
        CIPHERTEXT = 'ea51d3975595b86b'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_46(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000020000'
        CIPHERTEXT = 'caffc6ac4542de31'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_47(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000010000'
        CIPHERTEXT = '8dd45a2ddf90796c'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_48(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000008000'
        CIPHERTEXT = '1029d55e880ec2d0'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_49(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000004000'
        CIPHERTEXT = '5d86cb23639dbea9'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_50(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000002000'
        CIPHERTEXT = '1d1ca853ae7c0c5f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_51(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000001000'
        CIPHERTEXT = 'ce332329248f3228'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_52(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000800'
        CIPHERTEXT = '8405d1abe24fb942'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_53(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000400'
        CIPHERTEXT = 'e643d78090ca4207'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_54(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000200'
        CIPHERTEXT = '48221b9937748a23'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_55(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000100'
        CIPHERTEXT = 'dd7c0bbd61fafd54'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_56(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000080'
        CIPHERTEXT = '2fbc291a570db5c4'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_57(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000040'
        CIPHERTEXT = 'e07c30d7e4e26e12'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_58(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000020'
        CIPHERTEXT = '0953e2258e8e90a1'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_59(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000010'
        CIPHERTEXT = '5b711bc4ceebf2ee'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_60(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000008'
        CIPHERTEXT = 'cc083f1e6d9e85f6'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_61(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000004'
        CIPHERTEXT = 'd2fd8867d50d2dfe'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_62(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000002'
        CIPHERTEXT = '06e7ea22ce92708f'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

    def test_63(self):
        KEYs = '0101010101010101'
        PLAINTEXT = '0000000000000001'
        CIPHERTEXT = '166b40b44aba4bd6'
        self.assertEqual(DES.des_hex(PLAINTEXT, KEYs), CIPHERTEXT)

class TestTECBvartext_decrypt(unittest.TestCase):
    def test_0(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '95f8a5e5dd31d900'
        PLAINTEXT = '8000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_1(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'dd7f121ca5015619'
        PLAINTEXT = '4000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_2(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '2e8653104f3834ea'
        PLAINTEXT = '2000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_3(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '4bd388ff6cd81d4f'
        PLAINTEXT = '1000000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_4(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '20b9e767b2fb1456'
        PLAINTEXT = '0800000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_5(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '55579380d77138ef'
        PLAINTEXT = '0400000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_6(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '6cc5defaaf04512f'
        PLAINTEXT = '0200000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_7(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0d9f279ba5d87260'
        PLAINTEXT = '0100000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_8(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'd9031b0271bd5a0a'
        PLAINTEXT = '0080000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_9(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '424250b37c3dd951'
        PLAINTEXT = '0040000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_10(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'b8061b7ecd9a21e5'
        PLAINTEXT = '0020000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_11(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'f15d0f286b65bd28'
        PLAINTEXT = '0010000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_12(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'add0cc8d6e5deba1'
        PLAINTEXT = '0008000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_13(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e6d5f82752ad63d1'
        PLAINTEXT = '0004000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_14(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'ecbfe3bd3f591a5e'
        PLAINTEXT = '0002000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_15(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'f356834379d165cd'
        PLAINTEXT = '0001000000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_16(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '2b9f982f20037fa9'
        PLAINTEXT = '0000800000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_17(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '889de068a16f0be6'
        PLAINTEXT = '0000400000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_18(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e19e275d846a1298'
        PLAINTEXT = '0000200000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_19(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '329a8ed523d71aec'
        PLAINTEXT = '0000100000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_20(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e7fce22557d23c97'
        PLAINTEXT = '0000080000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_21(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '12a9f5817ff2d65d'
        PLAINTEXT = '0000040000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_22(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'a484c3ad38dc9c19'
        PLAINTEXT = '0000020000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_23(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'fbe00a8a1ef8ad72'
        PLAINTEXT = '0000010000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_24(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '750d079407521363'
        PLAINTEXT = '0000008000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_25(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '64feed9c724c2faf'
        PLAINTEXT = '0000004000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_26(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'f02b263b328e2b60'
        PLAINTEXT = '0000002000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_27(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '9d64555a9a10b852'
        PLAINTEXT = '0000001000000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_28(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'd106ff0bed5255d7'
        PLAINTEXT = '0000000800000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_29(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e1652c6b138c64a5'
        PLAINTEXT = '0000000400000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_30(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e428581186ec8f46'
        PLAINTEXT = '0000000200000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_31(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'aeb5f5ede22d1a36'
        PLAINTEXT = '0000000100000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_32(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e943d7568aec0c5c'
        PLAINTEXT = '0000000080000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_33(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'df98c8276f54b04b'
        PLAINTEXT = '0000000040000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_34(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'b160e4680f6c696f'
        PLAINTEXT = '0000000020000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_35(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'fa0752b07d9c4ab8'
        PLAINTEXT = '0000000010000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_36(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'ca3a2b036dbc8502'
        PLAINTEXT = '0000000008000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_37(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '5e0905517bb59bcf'
        PLAINTEXT = '0000000004000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_38(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '814eeb3b91d90726'
        PLAINTEXT = '0000000002000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_39(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '4d49db1532919c9f'
        PLAINTEXT = '0000000001000000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_40(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '25eb5fc3f8cf0621'
        PLAINTEXT = '0000000000800000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_41(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'ab6a20c0620d1c6f'
        PLAINTEXT = '0000000000400000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_42(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '79e90dbc98f92cca'
        PLAINTEXT = '0000000000200000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_43(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '866ecedd8072bb0e'
        PLAINTEXT = '0000000000100000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_44(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '8b54536f2f3e64a8'
        PLAINTEXT = '0000000000080000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_45(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'ea51d3975595b86b'
        PLAINTEXT = '0000000000040000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_46(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'caffc6ac4542de31'
        PLAINTEXT = '0000000000020000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_47(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '8dd45a2ddf90796c'
        PLAINTEXT = '0000000000010000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_48(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '1029d55e880ec2d0'
        PLAINTEXT = '0000000000008000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_49(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '5d86cb23639dbea9'
        PLAINTEXT = '0000000000004000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_50(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '1d1ca853ae7c0c5f'
        PLAINTEXT = '0000000000002000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_51(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'ce332329248f3228'
        PLAINTEXT = '0000000000001000'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_52(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '8405d1abe24fb942'
        PLAINTEXT = '0000000000000800'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_53(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e643d78090ca4207'
        PLAINTEXT = '0000000000000400'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_54(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '48221b9937748a23'
        PLAINTEXT = '0000000000000200'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_55(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'dd7c0bbd61fafd54'
        PLAINTEXT = '0000000000000100'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_56(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '2fbc291a570db5c4'
        PLAINTEXT = '0000000000000080'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_57(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'e07c30d7e4e26e12'
        PLAINTEXT = '0000000000000040'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_58(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '0953e2258e8e90a1'
        PLAINTEXT = '0000000000000020'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_59(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '5b711bc4ceebf2ee'
        PLAINTEXT = '0000000000000010'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_60(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'cc083f1e6d9e85f6'
        PLAINTEXT = '0000000000000008'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_61(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = 'd2fd8867d50d2dfe'
        PLAINTEXT = '0000000000000004'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_62(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '06e7ea22ce92708f'
        PLAINTEXT = '0000000000000002'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

    def test_63(self):
        KEYs = '0101010101010101'
        CIPHERTEXT = '166b40b44aba4bd6'
        PLAINTEXT = '0000000000000001'
        self.assertEqual(DES.des_hex(CIPHERTEXT, KEYs, decrypt=True), PLAINTEXT)

if __name__ == '__main__':
    unittest.main()