x = float(input("Enter #1: "))
op = str(input("+ - * /: "))
y = float(input("Enter #2: "))

if op == "+":
    sum = x + y

elif op == "-":
    sum = x - y

elif op == "*":
    sum = x * y

elif op == "/":
    sum = x / y    

else:
    print("Enter a valid operation!")

print(f"Final number: {sum}")  