class Caesar():

    def __init__(self, key):
        self.key = key
        self.characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def encrypt(self, plaintext):      
        ciphertext = ""
        for i in plaintext:
            if i == "-":
                ciphertext += "-"
            else:
                ciphertext += self.adder(i)

                
        
        return ciphertext
                

    def adder(self, char):
        # THIS IS THE FUNCTION THAT ADDS THE KEY TO THE PLAINTEXT
        # It will take the char and add the key to it
        # It will return the new char
        # THe logic here is that the character that can be used are 
        # 0-9 and A-Z and a-z
        # So the logic is that if the character is a number then it will add the key to it
        # Depending of the value of the key and the character it will return the new character
        # If the character is a letter then it will add the key to it
        # Depending of the value of the key and the character it will return the new character
        #convert char to int
        num = int(char)
        hold = num + self.key
        return self.characters[hold]

    def subtractor(self, char):

        num = self.characters.index(char)
        hold = num  - self.key
        return self.characters[hold]



    

    def decrypt(self, ciphertext):
        plaintext = ""
        for i in ciphertext:
            if i == "-":
                plaintext += "-"
            else:
                plaintext += self.subtractor(i)
            
        
        return plaintext
        

       


    def get_public_key(self):
        return self.key


def main():
    day = int(input("Enter the day of the month: "))
    caesar = Caesar(day)
    print("Public key: ", caesar.get_public_key())
    # plaintext = input("Enter the plaintext: ")
    plaintext = "13-24-355-43-52"
    print("Plaintext: ", plaintext)
    ciphertext = caesar.encrypt(plaintext)
    print("Ciphertext: ", ciphertext)
    plaintext = caesar.decrypt(ciphertext)
    print("Plaintext: ", plaintext)


if __name__ == "__main__":
    main()
