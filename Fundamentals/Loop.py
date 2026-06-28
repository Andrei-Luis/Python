name = input("Enter Your Name: ")
counter = 0

while name == "" and counter < 2:
    counter += 1
    print("Please enter Your name")    
    print("")
    name = input("Enter Your Name: ")

    if counter == 2:
        print("You are out of attempts")
    elif not name == "":
        print(f"Hello {name}")

print("============================================")
numbers = "Andrei", "Luis", "Nablo", "Andrie", "AndreiLuis", "Drei", "Drie", "Zid", "Nox", "Shoyo", "Dreii", "Zidd", "Rando",

for x in range(1, 21):
    if x == 13:
        print("UNLUCKY")
        continue
    else:
        print(x)