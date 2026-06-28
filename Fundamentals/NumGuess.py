import random

min = int(input("Minumum range: "))
max = int(input("Maximum range: "))

ranNum = random.randint(min, max)
guesses = 0

while True:
    userGuess = input(f"Guess a number between {min}-{max}: ")
    guesses += 1

    if userGuess.isdigit():
        userGuess = int(userGuess)
        guesses += 1
        pass

        if userGuess > max or userGuess < min:
           print("Out Of Range!") 

        elif userGuess > ranNum:
            print("HOT!")

        elif userGuess < ranNum:
            print("COLD!")

        else:
            print(f"Correct! It's #{str(userGuess)}")
            print(f"It took you {str(guesses)} attempts")        
            break

    else:
        print("Invalid Guess!")
        print(f"Select between {min}-{max}")