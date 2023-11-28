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
        print("To be continued")

    def decrypt(self):
        print("To be continued")

    def checking(self):
        rsa = RSA_Create(self.in_out.month, self.in_out.day)
        rsa_decrypt = RSA_Decrypt(rsa.get_private_key()[
                                  0], rsa.get_private_key()[1])
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month)
        print("Printing Pre-Encryption")
        temp = self.file_data
        print(temp)
        temp = rsa.encrypt(temp)
        print(temp)
        temp = "-".join(map(str, temp))
        temp1 = caesar.encrypt("".join(map(str, temp)))
        print(temp1)
        # Storing in file
        self.in_out.file_data = temp1
        self.in_out.output()
        md = self.in_out.md5

        # TO BE CONTINUED

        # DECRYPTING
        print("Printing Post-Decryption")
        temp1 = Caesar.decrypt(caesar, temp1)
        print(temp1)
        temp1 = rsa_decrypt.decrypt(temp1)
        print(temp1)

        

if __name__ == "__main__":
    inputt = in_out_plain("input_plain.txt", 10, 3, 2021)
    management = management(inputt)
    management.checking()
