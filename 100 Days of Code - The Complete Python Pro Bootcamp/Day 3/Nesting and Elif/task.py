maths_score = int(input("what is your math score?"))
english_score = int(input("what is your eng score?"))

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
elif english_score >= 90:
    print("You're good at english")