from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_end = False

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text = input("Heads up! Only letters are allowed. Type your word to process, no spaces:\n").lower()
        if len(text) >= 1 and text.isalpha():
            shift = input("Type the shift number to encode and decode with:\n")
            if shift.isnumeric():
                shift = int(shift) % 26
                caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
                restart = input("\nType 'yes' if you want to re-run. Type 'no' to exit.\n")
                if restart == "no":
                    should_end = True
                    print("Thanks for playing!")
            else:
                print('Oh no! Let us try again!')
        else:
            print('Wrong! Let us start all over again!')
    else:
        print('Oops! Please try again!')