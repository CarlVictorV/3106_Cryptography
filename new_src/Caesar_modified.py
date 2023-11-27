class Caesar():

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        cipher = ''
        # Split the numbers based on the hyphen delimiter
        nums = plaintext.split('-')
        for num in nums:
            # Perform Caesar encryption on each number
            cipher += str((int(num) + self.key) % 256) + '-'
        return cipher.rstrip('-')  # Remove trailing hyphen

    def decrypt(self, ciphertext):
        plain = ''
        # Split the numbers based on the hyphen delimiter
        nums = ciphertext.split('-')
        for num in nums:
            # Perform Caesar decryption on each number
            decrypted_num = (int(num) - self.key + 256) % 256  # Ensure positive result
            plain += str(decrypted_num) + '-'
        return plain.rstrip('-')  # Remove trailing hyphen


    def get_public_key(self):
        return self.key


def main():
    day = int(input("Enter the day of the month: "))
    caesar = Caesar(day)
    print("Public key: ", caesar.get_public_key())
    plaintext = input("Enter the plaintext: ")
    ciphertext = caesar.encrypt(plaintext)
    print("Ciphertext: ", ciphertext)
    print("Plaintext: ", caesar.decrypt(ciphertext))


if __name__ == "__main__":
    main()
