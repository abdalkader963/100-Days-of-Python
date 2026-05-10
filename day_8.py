#caesar cipher 
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
should_continue=True
def encrypt():
        cipher=""
        for letter in text:
            if letter in alphabet:
                postion= alphabet.index(letter)
                new_postion= (postion+shift) %26
                final=alphabet[new_postion]
                cipher+=final
        print(f"your encoded results is {cipher}")
def decrypt ():
        cipher_decrypt=""
        for letter in text:
            if letter in alphabet:
                postion=alphabet.index(letter)
                new_pos=(postion - shift) %26
                final=alphabet[new_pos]
                cipher_decrypt+=final
        print(f"your decoded results is {cipher_decrypt}")            
while should_continue:
    order=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))    
    if order == "encode":
        encrypt()
    elif order == "decode":
        decrypt()
    else:
        print("false input, pleas try again")  
    result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "yes":
        should_continue=True
    elif result == "no":
        should_continue= False
        print("good buy!")


