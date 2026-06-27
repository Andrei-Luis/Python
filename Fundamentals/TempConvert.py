unit = input("(C/F): ")
temp = float(input("Temperature: "))

if unit == "C":
    temp = (temp * (9 / 5)) + 32 
elif unit == "F":    
    temp