import random
import string
def generate_password(min_lenght, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    character = letters
    if numbers:
        character += digits
    if special_character:
        character += special

    pwd = ""
    meets_crieteria = False
    has_number=False
    has_special= False

    while not meets_crieteria or len(pwd) < min_lenght:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_crieteria  = True
        if numbers:
            meets_crieteria = has_number
        if special_character:
            meets_crieteria = meets_crieteria and has_special
    return pwd
min_lenght = int(input("enter minimum lenght"))
has_number = input("do you want numbers(y/n)").lower() == "y"
has_special = input("do you want special character(y/n)").lower() == "y"
pwd = generate_password(min_lenght,has_number,has_special)
print("the generated password is:",pwd)


