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
    vigenere = Vigenere_modified(10, 2021)
    print("Key:", vigenere.key)

    encrypted_text = '\$uB$#rUlR2(dMEbgc30QS)#uCMfs31SR{?eC@%GS0SS`dHq#fs30nT{eLB?frnOPO\#vE$PKU2US\!LZbesU2S2QNuo?^JS1Qm\#JD@eHTl3PQ$upcecUT4T/!uoMfs31SR{?epcfsSQVO`@uFc*H22nP/?HEd%Jn0PSP%ID#Ps2OTT>dHZ!fI3TS1QNtq$eISPQ'
    print("Encrypted:", encrypted_text)
    decrypted_text = vigenere.decrypt(str(encrypted_text))
    print("Decrypted:", decrypted_text)


if __name__ == "__main__":
    main()
