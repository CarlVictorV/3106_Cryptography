import os
from Management import management_plain_to_cipher as mptc
from Management import management_cipher_to_plain as mctp
from in_out import in_out_cipher as ioc
from in_out import in_out_plain as iop


def main():
    print("Welcome to the file encryption/decryption program!")
    while True:
        print("Would you like to encrypt or decrypt a file?")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Enter your choice: ")

        if choice == "1":
            encrypt()
            break
        elif choice == "2":
            decrypt()
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the file encryption/decryption program!")


def validate_date(day, month, year):
    if day < 1 or day > 31:
        print("Invalid day")
        return False
    if month < 1 or month > 12:
        print("Invalid month")
        return False
    if year < 0:
        print("Invalid year")
        return False
    return True


def encrypt():
    print("\nMake sure the file is in the input folder")
    file_name = input("Enter the file name: ")

    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))

    if not validate_date(day, month, year):
        return

    in_out = iop(file_name, month, day, year)
    mptc_encrypt = mptc(in_out)
    try:
        mptc_encrypt.encrypt()
        print("\nFile encrypted successfully!")
        print("The Encrypted File is located in the output folder")
    except Exception as e:
        print(f"Encryption failed: {e}")


def decrypt():
    print("\nMake sure the file is in the input folder")
    file_name = input("Enter the file name: ")

    print("Note: This assumes the file was encrypted using this program and contains the correct metadata")

    in_out = ioc(file_name)
    mctp_decrypt = mctp(in_out)
    mctp_decrypt.decrypt()

    print("\nFile decrypted successfully!")
    print("The Decrypted File is located in the output folder")


if __name__ == "__main__":
    main()
