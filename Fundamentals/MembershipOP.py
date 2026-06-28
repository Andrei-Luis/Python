epsteinList = {"Bill Clinton", "Donald Trump", "Prince Andrew", 
            "Bill Gates", "Stephen Hawking", "Michael Jackson", 
            "Elon Musk", "Naomi", "Campbell David", 
            "Copperfield Cameron", "Diaz Leonardo", "Di Caprio Kevin", 
            "Spacey Noam", "Chomsky Larry", "Summers Richard Branson"}

inList = input("Find from the Epstein list: ")

if inList in epsteinList:
    print(f"{inList} is on the Epstein List!")
else:
    print(f"{inList} is not on the Epstein List!")

while True:
    gmail = input("Enter Your Email: ")
    if "@" in gmail and "."  in gmail:
        print("Valid Email")
        break
    else:
        print("Invalid Email")    