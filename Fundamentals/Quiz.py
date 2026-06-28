questions = ("Question 1: What is a variable in programming?",
             "Question 2: Which of the following is an example of a loop?",
             "Question 3: What does a compiler do?",
             "Question 4: In programming, what is an array?",
             "Question 5: What is the primary purpose of a function?")

options = (("A) A permanent value that cannot be changed.", "B) A memory location used to store data that can be changed during program execution.", "C) A specific step in a flowchart.", "D) A function that returns a value"),
           ("A) if/else", "B) int" , "C) print()", "D) while" ),
           ("A) Converts the entire source code into machine code before running it.", "B) Runs the code line-by-line while looking at it.", "C) Fixes syntax errors in the code automatically.", "D) Stores data in an array."),
           ("A) A mathematical operation.", "B) A series of elements of the same type in contiguous memory locations.", "C) A type of loop.", "D) A block of reusable code."),
           ("A) To repeat a block of code continuously.", "B) To define an explicit data type.", "C) To group a set of statements so they can be reused and called multiple times.", "D) To terminate a program."))

answers = ("B", "D", "A", "B", "C")
guesses = []
score = 0
quesNum = 0

for question in questions:
    print(question)
    for option in options[quesNum]:
        print(option)

    guess = input(f"Your answer for #{quesNum + 1}: ").upper()    
    guesses.append(guess)
    if guess == answers[quesNum]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"{answers[quesNum]} is the correct answer")    

    quesNum += 1    
    print()
        

print("Answers: ", end=" ")
for answer  in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")