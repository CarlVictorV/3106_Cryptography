from RSA_modified import RSA_Create, RSA_Decrypt
from Caesar_modified import Caesar
from Vigenere_modified import Vigenere_modified
from in_out import in_out_plain


class management:
    def __init__(self, in_out):
        self.in_out = in_out
        self.file_data = self.in_out.file_data

    def encrypt(self):
        rsa = RSA_Create(self.in_out.month, self.in_out.day)
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month)
        temp = self.file_data
        temp = rsa.encrypt(temp)
        temp = "-".join(map(str, temp))
        temp1 = caesar.encrypt("".join(map(str, temp)))
        temp2 = vigenere.encrypt(temp1)
        self.file_data = temp2
        print(self.file_data)

    def decrypt(self):
        rsa = RSA_Create(self.in_out.month, self.in_out.day)
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month)
        self.file_data = Vigenere_modified.decrypt(vigenere, self.file_data)
        self.file_data = Caesar.decrypt(caesar, self.file_data)
        self.file_data = RSA_Create.decrypt(rsa, self.file_data)
        self.in_out.output(self.file_data)

    def checking(self):
        rsa = RSA_Create(self.in_out.month, self.in_out.day)
        caesar = Caesar(self.in_out.day)
        temp = self.file_data
        temp = rsa.encrypt(temp)
        print(temp)
        temp = "-".join(map(str, temp))
        print(temp)
        temp1 = caesar.encrypt("".join(map(str, temp)))
        # temp2 = vigenere.encrypt(temp1)
        self.file_data = temp1
        print(self.file_data)
        # self.file_data = Vigenere_modified.decrypt(vigenere, self.file_data)
        # print(self.file_data)
        temp1 = caesar.decrypt(self.file_data)
        print(temp1)
        rsa_decrypt = RSA_Decrypt(
            rsa.get_private_key(), rsa.get_public_key()[1])
        # convert temp1 to list
        temp1 = temp1.split("-")
        temp1 = list(map(int, temp1))
        temp2 = rsa_decrypt.decrypt2(temp1)
        print(temp2)
        self.file_data = temp2
        print(self.file_data)


if __name__ == "__main__":
    inputt = in_out_plain("input_plain.txt", 1, 1, 2021)
    management = management(inputt)
    management.checking()
