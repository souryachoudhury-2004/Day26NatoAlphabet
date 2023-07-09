import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Using dictionary comprehension to create the requisite dictionary from pandas dataframe
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

# Takes word from user and prints phonetic alphabet code word
word = input("Enter a word:")
code_word = [alphabet_dict[letter.upper()] for letter in word]

print(f"The phonetic code word for {word} is:")
print(code_word)

