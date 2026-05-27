#PyPassword Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))   
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passowrd=""
for letter in range(1,nr_letters+1):
    letter2=random.choice(letters)
    passowrd+=letter2
for symbol in range(1,nr_symbols+1):
    symbol2=random.choice(symbols) 
    passowrd+=symbol2   
for num in range(1,nr_numbers+1):
    num2=random.choice(numbers) 
    passowrd+=num2
pass2=list(passowrd)
random.shuffle(pass2)
password_final = "".join(pass2)
print(f"Your password is: {password_final}")