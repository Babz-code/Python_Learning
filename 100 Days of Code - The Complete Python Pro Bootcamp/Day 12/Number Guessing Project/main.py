import random
import art
print(art.logo)

print("Welcome to the number choosing game!")
print("I'm thinking of a number between 1 and 100")

chosen = random.randint(1, 100)
# print(chosen)
lives = 0

game_mode = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
if game_mode == 'easy':
    lives = 10
else:
    lives = 5

#print(chosen)
game_over = False

while not game_over:
    user_choice = int(input("Can you guess what i'm thinking?"))

    if user_choice > chosen and game_mode == "easy":
        lives -= 1
        print(f"Wrong, Number is too high. You have {lives} lives remaining")
    elif user_choice > chosen and game_mode == "hard":
        lives -= 1
        print(f"Wrong, Number is too high. You have {lives} lives remaining")
    elif user_choice < chosen and game_mode == "easy":
        lives -= 1
        print(f"Wrong, Number is too low. You have {lives} lives remaining")
    elif user_choice < chosen and game_mode == "hard":
        lives -= 1
        print(f"Wrong, Number is too low. You have {lives} lives remaining")
    elif user_choice == chosen:
        game_over = True
        print("Your guess is right. You win")

    if lives == 0:
        game_over = True
        print("Game Over!")

