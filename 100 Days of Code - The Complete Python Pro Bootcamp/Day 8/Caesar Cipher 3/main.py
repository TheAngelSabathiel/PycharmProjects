from art import logo

# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "!", "/", ",", ":", ";", "@", '"']

# TODO-2: What happens if the user enters a number/symbol/space?


#def caesar(original_text, shift_amount, encode_or_decode):
#    output_text = ""

#    for letter in original_text:
#        if encode_or_decode == "decode":
#            shift_amount *= -1

#        shifted_position = alphabet.index(letter) + shift_amount
#        shifted_position %= len(alphabet)
#        output_text += alphabet[shifted_position]
#    print(f"Here is the {encode_or_decode}d result: {output_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    output_text_list = []
    shift_amount %= 26
    if encode_or_decode == "decode":
        shift_amount *= -1
    for count in range(len(original_text)):
        if original_text[count] in alphabet:
            alphabet.index(original_text[count])
            output_text_list.append(alphabet[alphabet.index(original_text[count]) + shift_amount])
        else:
            output_text_list.append(original_text[count])
    for letter in output_text_list:
        output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

#caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
end_response = "yes"

while end_response == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = (input("Type the shift number:\n"))

    if direction != "encode" and direction != "decode":
        print("Wrong input. Please try again.")
    else:
        caesar(text, shift, direction)
    end_response = input("Do you want to start over? Yes or No?\n").lower()