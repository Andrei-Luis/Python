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
    print("Enter a valid operator!")

print(f"Final number: {round(sum, 3)}")  

print("")

unit = input("Kilograms or Pounds (K or L): ")
weight = float(input("Your Weight: "))

if unit == "K":
    weight *= 2.205
    unit = "Lbs"
    print(f"Your weight is: {weight:.1f} {unit}")            

elif unit == "L":
    weight /= 2.205
    unit = "Kgs"
    print(f"Your weight is: {weight:.1f} {unit}")            

else:
    print(f"{unit} was not valid")

print("Obese" if weight >= 200 else "Not Obese")    
