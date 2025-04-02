PLACEHOLDER_NAME = "[name]"

with open ("DAY 24/Mail merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open ("DAY 24/Mail merge/Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER_NAME, stripped_name)
        with open (f"DAY 24/Mail merge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
