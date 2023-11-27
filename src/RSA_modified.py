import random


class RSA_Create():
    def __init__(self, p_month, q_day):
        p = self.get_nearest_prime_for_months(p_month)
        q = self.get_nearest_prime_for_days(q_day)
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

    def decrypt(self, ciphertext):
        print(ciphertext)
        # Unpack the key into its components
        key, n = self.private_key
        # Generate the plaintext based on the ciphertext and key using a^b mod m
        aux = [str(pow(char, key, n)) for char in ciphertext]
        print(aux)
        # Return the array of bytes as a string
        plain = [chr(int(char2)) for char2 in aux]
        print(plain)
        return ''.join(plain)

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

    # TODO: Find a better way to do this
    def get_nearest_prime_for_months(self, months):
        prime = 0
        # Starting from 200
        if months == 1:
            prime = 211
        elif months == 2:
            prime = 223
        elif months == 3:
            prime = 227
        elif months == 4:
            prime = 229
        elif months == 5:
            prime = 233
        elif months == 6:
            prime = 239
        elif months == 7:
            prime = 241
        elif months == 8:
            prime = 251
        elif months == 9:
            prime = 257
        elif months == 10:
            prime = 263
        elif months == 11:
            prime = 269
        elif months == 12:
            prime = 271
        return prime

    def get_nearest_prime_for_days(self, days):
        prime = 0
        if days == 1:
            prime = 2
        elif days == 2:
            prime = 3
        elif days == 3:
            prime = 5
        elif days == 4:
            prime = 7
        elif days == 5:
            prime = 11
        elif days == 6:
            prime = 13
        elif days == 7:
            prime = 17
        elif days == 8:
            prime = 19
        elif days == 9:
            prime = 23
        elif days == 10:
            prime = 29
        elif days == 11:
            prime = 31
        elif days == 12:
            prime = 37
        elif days == 13:
            prime = 41
        elif days == 14:
            prime = 43
        elif days == 15:
            prime = 47
        elif days == 16:
            prime = 53
        elif days == 17:
            prime = 59
        elif days == 18:
            prime = 61
        elif days == 19:
            prime = 67
        elif days == 20:
            prime = 71
        elif days == 21:
            prime = 73
        elif days == 22:
            prime = 79
        elif days == 23:
            prime = 83
        elif days == 24:
            prime = 89
        elif days == 25:
            prime = 97
        elif days == 26:
            prime = 101
        elif days == 27:
            prime = 103
        elif days == 28:
            prime = 107
        elif days == 29:
            prime = 109
        elif days == 30:
            prime = 113
        elif days == 31:
            prime = 127
        else:
            prime = 131
        return prime

    # New Implementation


class RSA_Decrypt():
    def __init__(self, private_key, modulus):
        self.private_key = private_key
        self.modulus = modulus

    def decrypt2(self, ciphertext):
        print(ciphertext)
        # Unpack the key into its components
        key, n = self.private_key
        # Generate the plaintext based on the ciphertext and key using a^b mod m
        aux = [str(pow(char, key, n)) for char in ciphertext]
        print(aux)
        # Return the array of bytes as a string
        plain = [chr(int(char2)) for char2 in aux]
        print(plain)
        return ''.join(plain)
