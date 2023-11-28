from Management import management_plain_to_cipher as mptc
from Management import management_cipher_to_plain as mctp
from in_out import in_out_cipher as ioc
from in_out import in_out_plain as iop


def main():
    # Ask the user if they want to encrypt or decrypt a file
    print("Welcome to the file encryption/decryption program!")
    print("Would you like to encrypt or decrypt a file?")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter your choice: ")

    # Get the user's choice
    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    else:
        print("Invalid choice")

    print("Thank you for using the file encryption/decryption program!")


def encrypt():
    # Give reminders
    print("Make sure the file is in the input folder")
    # Ask the user for the file name
    file_name = input("Enter the file name: ")

    # Ask the user for the day, month, and year
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))

    # Check if the date is valid
    if day < 1 or day > 31:
        print("Invalid day")
        return
    if month < 1 or month > 12:
        print("Invalid month")
        return
    if year < 0:
        print("Invalid year")
        return

    # Initialize the input/output class
    in_out = iop(file_name, month, day, year)
    mptc_encrypt = mptc(in_out)
    mptc_encrypt.encrypt()

    # Tell the user the file was encrypted
    print("File encrypted successfully!")
    print("The Encrypted File is located in the output folder")


def decrypt():
    # Give reminders
    print("Make sure the file is in the input folder")
    # Ask the user for the file name
    file_name = input("Enter the file name: ")

    print("Note: This assumes the file was encrypted using this program and contains the correct metadata")

    # Initialize the input/output class
    in_out = ioc(file_name)
    mctp_decrypt = mctp(in_out)
    mctp_decrypt.decrypt()

    # Tell the user the file was decrypted
    print("File decrypted successfully!")
    print("The Decrypted File is located in the output folder")



if __name__ == "__main__":
    main()