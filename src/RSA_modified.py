import os
import random


class RSA_Create():
    def __init__(self, p_month, q_day):
        p, q = self.create_p_q(p_month, q_day)
        public_key, private_key = self.generate_key_pair(p, q)
        self.public_key = public_key
        self.private_key = private_key


    # Pairing
    def generate_key_pair(self, p, q):

        # n = pq
        n = p * q

        # Phi is the totient of n
        phi = (p-1) * (q-1)

        # Choose an integer e such that e and phi(n) are coprime
        e = random.randrange(1, phi)

        # Use Euclid's Algorithm to verify that e and phi(n) are coprime
        g = self.gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = self.gcd(e, phi)

        # Use Extended Euclid's Algorithm to generate the private key
        d = self.multiplicative_inverse(e, phi)

        # Return public and private key_pair
        return ((e, n), (d, n))

    # Encryption
    def encrypt(self, plaintext):
        # Unpack the key into its components
        key, n = self.public_key
        # Convert each letter in the plaintext to numbers based on the character using a^b mod m
        cipher = [pow(ord(char), key, n) for char in plaintext]
        # Return the array of bytes
        return cipher

    # GENERAL FUNCTIONS

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def multiplicative_inverse(self, e, phi):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi

        while e > 0:
            temp1 = temp_phi//e
            temp2 = temp_phi - temp1 * e
            temp_phi = e
            e = temp2

            x = x2 - temp1 * x1
            y = d - temp1 * y1

            x2 = x1
            x1 = x
            d = y1
            y1 = y

        if temp_phi == 1:
            return d + phi

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

    def create_p_q(self, p_month, q_day):
        if os.name == 'nt':
            primes_file_path = 'src\primes.txt'
        else:
            primes_file_path = 'src/primes.txt'

        max_index = 9600  # Adjust this according to your prime file size

        p_index = (p_month + random.randint(1, 100)) * \
            (q_day + random.randint(1, 100)) % max_index
        q_index = (q_day + random.randint(1, 100)) * \
            (p_month + random.randint(1, 100)) % max_index

        p = self.get_prime_at_index(primes_file_path, p_index)
        q = self.get_prime_at_index(primes_file_path, q_index)

        while p == q:
            q_index = (q_index + 1) % max_index
            q = self.get_prime_at_index(primes_file_path, q_index)
        return p, q

    def get_prime_at_index(self, file_path, index):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if 0 <= index < len(lines):
                return int(lines[index].strip())
            else:
                raise IndexError("Index out of range")


class RSA_Decrypt():
    def __init__(self, private_key, modulus):
        self.private_key = private_key
        self.modulus = modulus

    def decrypt23(self, ciphertext):
        print("Decrypting")
        print(ciphertext)
        # Unpack the key into its components
        key, n = self.private_key, self.modulus
        # Generate the plaintext based on the ciphertext and key using a^b mod m
        aux = [str(pow(char, key, n)) for char in ciphertext]
        print(aux)
        # Return the array of bytes as a string
        plain = [chr(int(char2)) for char2 in aux]
        print(plain)
        return ''.join(plain)

    def decrypt(self, ciphertext):
        # Unpack the key into its components
        key, n = self.private_key, self.modulus
        # Take the ciphertext and convert it to a list
        ciphertext = ciphertext.split("-")
        ciphertext = list(map(int, ciphertext))
        # Generate the plaintext based on the ciphertext and key using a^b mod m
        aux = [str(pow(char, key, n)) for char in ciphertext]
        # Return the array of bytes as a string
        plain = [chr(int(char2)) for char2 in aux]
        return ''.join(plain)


def main():
    rsa2 = RSA_Decrypt(106364327, 89836433)
    print(rsa2.decrypt("14805175-28486379-87145381-88883360-13323734-81948887-56950187-10013935-65954115-77859389-87145381-13323734-81948887-56950187-88883360-88883360-28486379-10013935-70485224-87145381-28486379-79574321"))


if __name__ == "__main__":
    main()
