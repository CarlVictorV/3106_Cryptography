from inputs import Input, Output
from RSA_modified import RSA_Decrypt, RSA_Create


class Godfrey():
    def __init__(self, input):
        self.input = input
        self.output = Output(self.input.type)

    def encrypt(self):
        tempdata = self.input.file_data
        rsa = RSA_Create(self.input.month, self.input.day)
        tempdata = rsa.encrypt(tempdata)
        print(tempdata)
        self.output.store("-".join(map(str, tempdata)))

    def decrypt(self):
        tempdata = self.input.file_data
        rsa = RSA_Decrypt(self.input.month, self.input.day)
        
        tempdata = rsa.decrypt2(tempdata)
        print(tempdata)
        self.output.store(tempdata)


def test_encrypt():
    input = Input("input_plain.txt", 1, 1, 2020, "plaintext")
    godfrey = Godfrey(input)
    godfrey.encrypt()


def test_decrypt():
    input = Input("input_cipher.txt", 1, 1, 2020, "ciphertext")
    godfrey = Godfrey(input)
    godfrey.decrypt()


if __name__ == "__main__":
    test_encrypt()
    test_decrypt()
