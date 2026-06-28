languages = {"C++": 6,
             "Java": 12,
             "Python": 12,
             "HTML": 1,
             "CSS": 3,
             "GDScript": 1,
             "Arduino": 10,
             "JavaScript": 12}

learned = []
total = 0

for key, value in languages.items():
    print(f"{key:10} = {value} hours")

while True:
    Llearned = input("Language you learned (q to quit): ")
    if Llearned == "q":
        break 
    elif languages.get(Llearned) is not None:
        learned.append(Llearned)

for Llearned in learned:
    total += languages.get(Llearned)   
    print(Llearned, end=" ")

print()
print(f"Total time:{total} hours")