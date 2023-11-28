class Vigenere_modified:
    def __init__(self, key):
        self.string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;'\"/\\<>(){}[]-=_+?!@#$%^&*~`"
        self.key = key
        self.key_index = 0

    def encrypt(self, plaintext):
        # Inputs a plaintext string and outputs an encrypted string
        # Format of plaintext is a string of any characters in self.string
        # 448-43C9-A5A-A46-967-9A3-CA4-CA5-6BB-94C-4468-A34-98A-BC6-587-B43-499-B85-4B-435C-4363-799-67A-4AB-5AC-4348
        ciphertext = ""
        for i, c in enumerate(plaintext):
            index = (self.string.find(
                c) + self.string.find(self.key[i % len(self.key)])) % len(self.string)
            ciphertext += self.string[index]
        return ciphertext

    def decrypt(self, ciphertext):
        # Inputs a ciphertext string and outputs a decrypted string
        # Format of ciphertext is a string of any characters in self.string
        # Zin2s?=aq8pwI
        plaintext = ""
        for i, c in enumerate(ciphertext):
            index = (self.string.find(
                c) - self.string.find(self.key[i % len(self.key)])) % len(self.string)
            plaintext += self.string[index]
        return plaintext


def main():
    # Example usage:
    vigenere = Vigenere_modified("December2022")
    plaintext = "448-43C9-A5A-A46-967-9A3-CA4-CA5-6BB-94C-4468-A34-98A-BC6-587-B43-499-B85-4B-435C-4363-799-67A-4AB-5AC-4348"
    encrypted_text = vigenere.encrypt(plaintext)
    print("Encrypted:", encrypted_text)
    decrypted_text = vigenere.decrypt(encrypted_text)
    print("Decrypted:", decrypted_text)


if __name__ == "__main__":
    main()
