import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = int(input("What do you choose? Type 0 for rock, 1 for Paper and 2 for Scissors.\n"))

if rps == 0:
    print(rock + "Computer chose:")
    solution1 = random.randint(0, 2)
    if solution1 == 0:
        print(rock + "You draw")
    elif solution1 == 1:
        print(paper + "You lose")
    else:
        print(scissors + "You win")
elif rps == 1:
    print(paper + "Computer chose:")
    solution1 = random.randint(0, 2)
    if solution1 == 0:
        print(rock + "You win")
    elif solution1 == 1:
        print(paper + "You draw")
    else:
        print(scissors + "You lose")
elif rps == 2:
    print(scissors + "Computer chose:")
    solution1 = random.randint(0, 2)
    if solution1 == 0:
        print(rock + "You lose")
    elif solution1 == 1:
        print(paper + "You win")
    else:
        print(scissors + "You draw")
else:
    print("You've chosen wrong. You lose!")