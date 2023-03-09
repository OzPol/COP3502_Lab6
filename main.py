"""Ozlem Polat"""

def encode(original_password):
    encoded_password = ""
    for digit in original_password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password

def decode(encoded_password):
    #Added by Melissa Mankewich
    decoded_password = ''
    for digit in encoded_password:
        new_digit = str((int(digit) - 3) % 10)
        decoded_password += new_digit
    return decoded_password
#Adding a comment to the file pulled from GitHub

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = input("Please enter an option: ")
        if option == "1":
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!\n")
            
        elif option == "2":
            decoded_password = decode(encoded_password)
            print("The encoded password is", encoded_password, "and the original password is "+decoded_password+".\n")
        elif option == "3":            
            break
        else:
            print("Invalid option, please enter 1-3.")

if __name__ == "__main__":
    main()