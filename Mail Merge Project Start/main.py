PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    mail_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    final_letter = starting_letter.read()
    for name in mail_names:
        stripped_name = name.strip()
        new_letter = final_letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}'s Final_letter.docx", mode = "w") as final_copy:
            final_copy.write(new_letter)


#Save the letters in the folder "ReadyToSend".
