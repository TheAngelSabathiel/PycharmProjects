alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

#def encrypt(original_text, shift_amount):
    #cipher_text = ""
    #for letter in original_text:
        #shifted_position = alphabet.index(letter) + shift_amount
        #shifted_position %= len(alphabet)
        #cipher_text += alphabet[shifted_position]
    #print(f"Here is the encoded result: {cipher_text}")

#encrypt(original_text=text, shift_amount=shift)

def encrypt(original_text, shift_amount):
    encoded_text = ""
    encoded_text_list = []
    for count in range(len(original_text)):
        alphabet.index(original_text[count])
        if alphabet.index(original_text[count]) + shift_amount > 25:
            encoded_text_list.append(alphabet[alphabet.index(original_text[count]) + shift_amount - 26])
        else:
            encoded_text_list.append(alphabet[alphabet.index(original_text[count]) + shift_amount])
    for letter in encoded_text_list:
        encoded_text += letter
    print(f"Here is the encoded result: {encoded_text}")

def decrypt(original_text, shift_amount):
    decoded_text = ""
    decoded_text_list = []
    for count in range(len(original_text)):
        alphabet.index(original_text[count])
        if alphabet.index(original_text[count]) - shift_amount < 0:
            decoded_text_list.append(alphabet[alphabet.index(original_text[count]) - shift_amount + 26])
        else:
            decoded_text_list.append(alphabet[alphabet.index(original_text[count]) - shift_amount])
    for letter in decoded_text_list:
        decoded_text += letter
    print(f"Here is the decoded result: {decoded_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    output_text_list = []
    shift_amount %= 26
    if encode_or_decode == "decode":
        shift_amount *= -1
    for count in range(len(original_text)):
        alphabet.index(original_text[count])
        output_text_list.append(alphabet[alphabet.index(original_text[count]) + shift_amount])
    for letter in output_text_list:
        output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(text, shift, direction)

