import pandas as pd
data=pd.read_csv("day_26/nato_phonetic_alphabet.csv")
dic = {row.letter : row.code for (index,row) in data.iterrows()}
user = input("Enter a word: ").upper()
user_word = [dic[letter] for letter in user]
print(user_word)

