# This is a ROT13 decrypt program.

Normal_Array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

ROT13_Array = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
               "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]


def rot13_encrypt(decrypted_value=[]):
    # Convert these variables in Global for use it in this scope.
    global Normal_Array, ROT13_Array

    # Create a new variable to save the ROT13 code in understandable text.
    new_value = ""

    # Take each char in the list "decrypted_value" wich will be search in the list "Normal_Array".
    for decrypted_char in decrypted_value:

        # Verify if "decrypted_char" is in "ROT13_Array".
        # If it does not exist it means that it is a special character which will not be encrypted.
        if decrypted_char in Normal_Array:

            # This number will indicate the index where the "decrypted_char" is contained in the list "Normal_Array".
            number = ROT13_Array.index(decrypted_char)

            for Normal_char in Normal_Array:

                # if the index in list "ROT13_Array" is equal to the index in list "Normal_Array" then we do an append.
                if Normal_Array.index(Normal_char) == number:
                    new_value = new_value + Normal_char
        else:
            new_value = new_value + decrypted_char

    # Return the complete variable.
    return new_value


def rot13_decrypt(encrypt_value=[]):
    # Convert these variables in Global for use it in this scope.
    global Normal_Array, ROT13_Array

    # Create a new variable to save the ROT13 code in understandable text.
    new_value = ""

    # Take each char in the list "encrypt_value" wich will be search in the list "Normal_Array".
    for encrypt_char in encrypt_value:

        # Verify if "encrypt_char" is in "Normal_Array".
        # If it does not exist it means that it is a special character which will not be decrypted.
        if encrypt_char in Normal_Array:

            # This number will indicate the index where the "encrypt_char" is contained in the list "Normal_Array".
            number = Normal_Array.index(encrypt_char)

            for ROT13_char in ROT13_Array:

                # if the index in list "Normal_Array" is equal to the index in list "ROT13_Array" then we do an append.
                if ROT13_Array.index(ROT13_char) == number:
                    new_value = new_value + ROT13_char
        else:
            new_value = new_value + encrypt_char

    # Return the complete variable.
    return new_value


while True:

    option = input("Select an option:\n"
                   "[1] Normal to ROT13\n"
                   "[2] ROT13 to Normal\n")

    if option == '1':

        Normal_value = input("Enter the text to encrypt: ")

        # Convert the variable "Normal_value" into a list.
        value_list = list(Normal_value)

        print(rot13_encrypt(value_list))
        break

    elif option == '2':

        ROT13_value = input("Enter the text to decrypt: ")

        # Convert the variable "Normal_value" into a list.
        value_list = list(ROT13_value)

        print(rot13_decrypt(value_list))
        break

    else:
        print("\nOnly '1' or '2'!!\n")