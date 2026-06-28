import random

choice = ("Rock", "Paper", "Scissor")
user = None
computer = random.choice(choice)
running = True

while running:
    while user not in choice:
        user = input("Rock-Paper-Scissor: ")

    print(f"User's Choice: {user}")
    print(f"Computer Choice: {computer}")

    if user == computer:
        print("It's A Tie!")
    elif user == "Rock" and computer == "Scissor":
        print("User Wins!")    
    elif user == "Paper" and computer == "Rock":
        print("User Wins!")    
    elif user == "Scissor" and computer == "Paper":
        print("User Wins!")  
    else:
        print("Computer Wins!")

    if not input("Play Again?[y/n]: ").lower() == "y":
        running = False
print("Thanks For Playing!")                          