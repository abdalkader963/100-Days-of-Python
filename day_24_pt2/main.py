with open("C:/Users/E-store/Desktop/py_journey/100-Days-of-Python/day_24_pt2/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("C:/Users/E-store/Desktop/py_journey/100-Days-of-Python/day_24_pt2/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read() 

for name in names:
    clean_name = name.strip()
    new_letter = letter_content.replace("[name]", clean_name)
    with open(f"C:/Users/E-store/Desktop/py_journey/100-Days-of-Python/day_24_pt2/Output/ReadyToSend/letter_for_{clean_name}.txt", mode="w") as output_file:
        output_file.write(new_letter)