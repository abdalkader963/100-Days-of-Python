#Tip Calculator
print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?\n"))
tip=float(input("How much tip would you like to give?\n"))
ppl=float(input("How many people to split the bill?\n"))
final_tip= bill * (tip/100)
final= (bill+ final_tip) / ppl
print(f"your final bill is : {final}")