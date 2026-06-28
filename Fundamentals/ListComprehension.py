
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squared = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squared)

codingLanguages = ["java", "python", "cplusplus", "gdscript", "html"]
codingChar = [lang[0] for lang in codingLanguages]

print(codingChar)

numbers = [1, -2, 3, -4, -5, 6, 7, 8, -9, -10]
positveNum = [num for num in numbers if num >= 0]
negativeNum = [num for num in numbers if num < 0]
evenNum = [num for num in numbers if num % 2 == 0]
oddNum = [num for num in numbers if num % 2 == 1]


print(positveNum)
print(negativeNum)
print(evenNum)
print(oddNum)

grades = [91, 72, 84, 95, 64, 75, 89, 94, 69, 73]
passingGrades = [grade for grade in grades if grade >= 75]

print(passingGrades)
