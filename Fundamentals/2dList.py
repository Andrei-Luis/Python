codingLanguages = [["C#", "C++", "GDScript", "Lua", "JavaScript"],
                   ["HTML", "CSS", "JavaScript", "SQL", "PHP"],
                   ["Ruby", "JavaScript", "Java", "C#", "Python"]]

for type in codingLanguages:
    for language in type:
        print(language, end=" ")
    print()    

numPad = (("1","2","3"),
          ("4","5","6"),
          ("7","8","9"),
          ("*","0","#"))    

for row in numPad:
    for col in row:
        print(col, end=" ")
    print() 