import random
from art import logo

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
'''crypt_command = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n").lower()
code_msg = input( "Type Your message : \n" )
shift = int(input( "Type the shift number : \n" ))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for text in original_text:
        shifted_position = letters.index(text) + shift_amount
        shifted_position = shifted_position % len(letters)

        cipher_text += letters[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")


def decrypt (original_text, shift_amount):
    return_text = ""
    for text in original_text:
        shifted_position = letters.index(text)-shift_amount
        shifted_position %= len(letters)

        return_text += letters[shifted_position]

    print( f"Here is the decoded result: {return_text}" )'''


def caesar(original_text, shift_amount, direction):
    return_text = ""
    if direction == "decode":
        shift_amount *= -1  # change the sign
    for text in original_text:
        if text not in letters:
            return_text += text
        else:

            shifted_position = letters.index( text ) + shift_amount
            shifted_position %= len( letters )
            return_text += letters[shifted_position]

    print( f"Here is the {direction}d result: {return_text}" )


def caeser_cipher_game():
    should_continue = True

    while should_continue:
        crypt_command = input( "Type 'encode' to encrypt, type 'decode' to decrypt : \n" ).lower()
        code_msg = input( "Type Your message : \n" )
        shift = int( input( "Type the shift number : \n" ) )
        caesar( original_text=code_msg, shift_amount=shift, direction=crypt_command )

        restart = input( "Type 'yes' if you want to continue again. Otherwise, type 'no'." ).lower()
        if restart == 'no':
            should_continue = False
            print( "Goodbye" )


'''while should_continue:
    crypt_command = input( "Type 'encode' to encrypt, type 'decode' to decrypt : \n" ).lower()
    code_msg = input( "Type Your message : \n" )
    shift = int( input( "Type the shift number : \n" ) )

    input("Type 'yes' if you want to continue again. Otherwise, type 'no'.")


#print("You entered wrong command. Type 'encode' to encrypt, type 'decode' to decrypt.")'''

if __name__ == "__main__":
    print( logo )
    print( "Welcome to caeser cipher." )
    caeser_cipher_game()
