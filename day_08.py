alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher += alphabet[new_position]
        else:
            cipher += letter
    print(f"Your encoded result is: {cipher}")

def decrypt(cipher_text, shift_amount):
    decipher = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            decipher += alphabet[new_position]
        else:
            decipher += letter
    print(f"Your decoded result is: {decipher}")

should_continue = True

while should_continue:
    order = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if order == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif order == "decode":
        decrypt(cipher_text=text, shift_amount=shift)
    else:
        print("Invalid input, please try again.")

    result = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye!")


