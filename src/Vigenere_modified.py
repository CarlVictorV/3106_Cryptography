class Vigenere_modified:
    def __init__(self, month, year):
        self.string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;'\"/\\<>(){}[]-=_+?!@#$%^&*~`"
        self.key = self.create_key(month, year)
        self.key_index = 0

    def create_key(self, month, year):
        key = months[month - 1] + str(year)
        return key

    def encrypt(self, plaintext):
        ciphertext = ""
        for i, c in enumerate(plaintext):
            index = (self.string.find(
                c) + self.string.find(self.key[i % len(self.key)])) % len(self.string)
            ciphertext += self.string[index]
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i, c in enumerate(ciphertext):
            index = (self.string.find(
                c) - self.string.find(self.key[i % len(self.key)])) % len(self.string)
            plaintext += self.string[index]
        return plaintext


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def main():
    # Example usage:
    vigenere = Vigenere_modified(12, 2222)
    print("Key:", vigenere.key)
    plaintext = "448-43C9-A5A-A46-967-9A3-CA4-CA5-6BB-94C-4468-A34-98A-BC6-587-B43-499-B85-4B-435C-4363-799-67A-4AB-5AC-4348"
    encrypted_text = vigenere.encrypt(plaintext)
    print("Encrypted:", encrypted_text)
    decrypted_text = vigenere.decrypt(encrypted_text)
    print("Decrypted:", decrypted_text)


if __name__ == "__main__":
    main()
