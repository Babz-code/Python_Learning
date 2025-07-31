import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_choice = random.sample(cards, 2)
print(f"Your cards are: {user_choice}")

comp_choice = random.sample(cards, 2)
print(f"Computer's first card is: {comp_choice[0]}")

another_number = input("Do you want to get another number? type 'y' for Yes or 'n' for No: ").lower()

u_c_name = sum(user_choice)
c_c_name = sum(comp_choice)

if another_number == "n":
    if c_c_name < u_c_name <= 21:
        print(f"Your final hand is: {user_choice}")
        print(f"Computer's final hand is: {comp_choice}")
        print("You win")
    else:
        print(f"Your final hand is: {user_choice}")
        print(f"Computer's final hand is: {comp_choice}")
        print("Computer wins")

elif another_number == "y":
    user_choice2 = random.sample(cards, 1)
    user_choice += user_choice2
    u2_c2_name = sum(user_choice)

    if sum(comp_choice) <= 17:
        comp_choice2 = random.sample(cards, 1)
        comp_choice += comp_choice2
        c2_c2_name = sum(comp_choice)

        if c2_c2_name < u2_c2_name <= 21:
            print(f"Your final hand is: {user_choice}")
            print(f"Computer's final hand is: {comp_choice}")
            print("You win")
        else:
            print(f"Your final hand is: {user_choice}")
            print(f"Computer's final hand is: {comp_choice}")
            print("Computer wins")
    else:
        if c_c_name < u2_c2_name <= 21:
            print(f"Your final hand is: {user_choice}")
            print(f"Computer's final hand is: {comp_choice}")
            print("You win")

        else:
            print(f"Your final hand is: {user_choice}")
            print(f"Computer's final hand is: {comp_choice}")
            print("Computer wins")
