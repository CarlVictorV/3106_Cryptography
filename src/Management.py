from RSA_modified import RSA_Create, RSA_Decrypt
from Caesar_modified import Caesar
from TranspositionCipher import TranspositionCipher
from Vernam_modified import Vernam_modified
from Vigenere_modified import Vigenere_modified
from in_out import in_out_cipher, in_out_plain


class management_plain_to_cipher:
    def __init__(self, in_out):
        self.in_out = in_out
        self.file_data = self.in_out.file_data

    def encrypt(self):
        # Initialize the ciphers
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month, self.in_out.year)
        rsa = RSA_Create(self.in_out.month, self.in_out.day)
        transposition = TranspositionCipher(
            self.in_out.day + self.in_out.month)
        verna = Vernam_modified(self.in_out.md5 + self.in_out.sha256)

        # Encrypt the file data
        self.file_data = rsa.encrypt(self.file_data)
        self.file_data = "-".join(map(str, self.file_data))
        self.file_data = rsa.encrypt(self.file_data)
        self.file_data = "-".join(map(str, self.file_data))
        self.file_data = caesar.encrypt(self.file_data)
        self.file_data = vigenere.encrypt(self.file_data)
        self.file_data = transposition.encrypt(self.file_data)
        self.file_data = verna.encrypt(self.file_data)
        self.file_data = vigenere.encrypt(self.file_data)

        # Write the encrypted data to the output file
        self.in_out.output(rsa.get_private_key()[
                           0], rsa.get_private_key()[1], self.file_data)

    def test(self):
        # Initialize the ciphers
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month, self.in_out.year)
        rsa = RSA_Create(self.in_out.month, self.in_out.day)
        transposition = TranspositionCipher(
            self.in_out.day + self.in_out.month)
        verna = Vernam_modified(self.in_out.md5 + self.in_out.sha256)

        # Encrypt the file data
        print("Original File Data: " + self.file_data)
        self.file_data = rsa.encrypt(self.file_data)
        self.file_data = "-".join(map(str, self.file_data))
        self.file_data = rsa.encrypt(self.file_data)
        self.file_data = "-".join(map(str, self.file_data))
        print("RSA Encrypted File Data: " + self.file_data)
        self.file_data = caesar.encrypt(self.file_data)
        print("Caesar Encrypted File Data: " + self.file_data)
        self.file_data = vigenere.encrypt(self.file_data)
        print("Vigenere Encrypted File Data: " + self.file_data)
        self.file_data = transposition.encrypt(self.file_data)
        print("Transposition Encrypted File Data: " + self.file_data)
        self.file_data = verna.encrypt(self.file_data)
        print("Vernam Encrypted File Data: " + self.file_data)
        self.file_data = vigenere.encrypt(self.file_data)
        print("Vigenere Encrypted File Data: " + self.file_data)

        # Decrypt the file data
        rsa_decrypted = RSA_Decrypt(
            rsa.get_private_key()[0], rsa.get_private_key()[1])
        
        self.file_data = vigenere.decrypt(self.file_data)
        print("Vigenere Decrypted File Data: " + self.file_data)
        self.file_data = verna.decrypt(self.file_data)
        print("Vernam Decrypted File Data: " + self.file_data)
        self.file_data = transposition.decrypt(self.file_data)
        print("Transposition Decrypted File Data: " + self.file_data)
        self.file_data = vigenere.decrypt(self.file_data)
        print("Vigenere Decrypted File Data: " + self.file_data)
        self.file_data = caesar.decrypt(self.file_data)
        print("Caesar Decrypted File Data: " + self.file_data)
        self.file_data = rsa_decrypted.decrypt(self.file_data)
        self.file_data = rsa_decrypted.decrypt(self.file_data)
        print("RSA Decrypted File Data: " + self.file_data)


class management_cipher_to_plain:
    def __init__(self, in_out):
        self.in_out = in_out
        self.file_data = self.in_out.encrypted_data

    def decrypt(self):
        # Initialize the ciphers
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month, self.in_out.year)
        rsa = RSA_Decrypt(self.in_out.private_key, self.in_out.modulus)
        transposition = TranspositionCipher(
            self.in_out.day + self.in_out.month)
        verna = Vernam_modified(self.in_out.md5 + self.in_out.sha256)

        # Decrypt the file data
        self.file_data = vigenere.decrypt(self.file_data)
        self.file_data = verna.decrypt(self.file_data)
        self.file_data = transposition.decrypt(self.file_data)
        self.file_data = vigenere.decrypt(self.file_data)
        self.file_data = caesar.decrypt(self.file_data)
        self.file_data = rsa.decrypt(self.file_data)
        self.file_data = rsa.decrypt(self.file_data)

        # Write the decrypted data to the output file
        self.in_out.file_data = self.file_data
        self.in_out.output()

    def test(self):
        # Initialize the ciphers
        caesar = Caesar(self.in_out.day)
        vigenere = Vigenere_modified(self.in_out.month, self.in_out.year)
        rsa = RSA_Decrypt(self.in_out.private_key, self.in_out.modulus)
        transposition = TranspositionCipher(
            self.in_out.day + self.in_out.month)
        verna = Vernam_modified(self.in_out.md5 + self.in_out.sha256)

        # Decrypt the file data
        print("Original File Data: " + self.file_data)
        self.file_data = verna.decrypt(self.file_data)
        print("Vernam Decrypted File Data: " + self.file_data)
        self.file_data = transposition.decrypt(self.file_data)
        print("Transposition Decrypted File Data: " + self.file_data)
        self.file_data = vigenere.decrypt(self.file_data)
        print("Vigenere Decrypted File Data: " + self.file_data)
        self.file_data = caesar.decrypt(self.file_data)
        print("Caesar Decrypted File Data: " + self.file_data)
        self.file_data = rsa.decrypt(self.file_data)
        print("RSA Decrypted File Data: " + self.file_data)


if __name__ == "__main__":
    # Plain to cipher
    # inputt = in_out_plain("input_plain.txt", 10, 3, 2021)
    # management = management_plain_to_cipher(inputt)
    # management.encrypt()

    # Cipher to plain
    inputt = in_out_cipher("rrr")
    management = management_cipher_to_plain(inputt)
    management.decrypt()

    # Test
    # inputt = in_out_plain("input_plain.txt", 10, 3, 2021)
    # management = management_plain_to_cipher(inputt)
    # management.test()
