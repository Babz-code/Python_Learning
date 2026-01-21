
import pandas
#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_data)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_code():
    name = input("what is your name?").upper()
    try:
        output = [new_data[n] for n in name]
    except KeyError:
        print("Sorry, you cannot enter an integer")
        generate_code()
    else:
        print(output)

generate_code()