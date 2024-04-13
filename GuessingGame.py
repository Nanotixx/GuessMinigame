import random
print("GuessingGame By: Nanotixx.\n\n | Guess a number between 1-100!\n | Type 420 to exit. \n")


while True:
    try:
        est = random.randint(1, 100)
        pick = int(input("Guess a number: "))
        if pick == 420:
            break
        if pick >= 100 or pick <= 0:
            print("Can't exceed below 0 or above 100.")
            break
        if pick == est:
            print("You Guessed What I Said!")
            break
        print(est)
    except ValueError:
        print("Digits are only allowed!")