import random
from art import logo, vs
from game_data import data

def format_name(variable):
    for_name = variable["name"]
    for_descr = variable["description"]
    for_country = variable["country"]
    return f"{for_name}, a {for_descr}, from {for_country}"

def check_ans(user_guess, check_a, check_b):
    if check_a > check_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_continues = True
first_person_condition = True

while game_continues:
    if first_person_condition:
        first_person = random.choice(data)
    else:
        first_person = second_person

    second_person = random.choice(data)
    if first_person == second_person:
        second_person = random.choice(data)

    print(f"Compare A: {format_name(first_person)}.")
    print(vs)
    print(f"Compare B: {format_name(second_person)}.")

    guess = input("Who has more followers? 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)

    a_count = first_person["follower_count"]
    b_count = second_person["follower_count"]

    is_correct = check_ans(guess, a_count, b_count)

    if is_correct:
        score += 1
        first_person_condition = False
        print(f"You got it right, your score is {score}")
    else:
        print(f"Sorry you got it wrong, your score is {score}")
        game_continues = False