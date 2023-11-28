class Vigenere_modified:
    def __init__(self, month, year):
        self.key = self.create_key(month, year)
        self.key_index = 0

    def create_key(self, month, year):
        key = MONTHS[month - 1] + str(year)
        return key

    def encrypt(self, plaintext):
        ciphertext = ""
        for i, c in enumerate(plaintext):
            index = (CHARACTERS.find(c) + CHARACTERS.find(self.key[i % len(self.key)])) % len(CHARACTERS)  # noqa
            ciphertext += CHARACTERS[index]
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i, c in enumerate(ciphertext):
            index = (CHARACTERS.find(c) - CHARACTERS.find(self.key[i % len(self.key)])) % len(CHARACTERS)  # noqa
            plaintext += CHARACTERS[index]

        return plaintext


MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;'\"/\\<>(){}[]-=_+?!@#$%^&*~`"
