from RSA_modified import RSA_Create, RSA_Decrypt
from Caesar_modified import Caesar
from Vigenere_modified import Vigenere_modified
from in_out import in_out_plain
import random



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
        rsa_decrypt = RSA_Decrypt(rsa.get_private_key()[0], rsa.get_private_key()[1])
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month)

        temp = self.file_data
        print("temp: ", temp)
        temp = rsa.encrypt(temp)
        print("rsa: ", temp)
        temp = "-".join(map(str, temp))
        print("rsa: ", temp)
        temp1 = caesar.encrypt("".join(map(str, temp)))
        print("caesar: ", temp1)

        # Decrypt
        temp1 = Caesar.decrypt(caesar, temp1)
        print("caesar der: ", temp1)
        temp1 = temp1.split("-")
        print("caesar der: ", temp1)
        temp1 = list(map(int, temp1))
        print("caesar der: ", temp1)
        temp1 = rsa_decrypt.decrypt23(temp1)
        print(temp1)

        # temp = self.file_data
        # print(temp)
        # temp = rsa.encrypt(temp)
        # print(temp)
        # temp = "-".join(map(str, temp))


        # # Decrypt
        # # REvert string to list
        # temp = temp.split("-")
        # # Convert string to int
        # temp = list(map(int, temp))
        
        # # Decrypt
        # temp = rsa_decrypt.decrypt23(temp)
        # print(temp)
        
       


if __name__ == "__main__":
    inputt = in_out_plain("input_plain.txt", 10, 24, 2021)
    management = management(inputt)
    management.checking()
