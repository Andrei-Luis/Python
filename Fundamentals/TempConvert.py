unit = input("(C/F): ")
temp = float(input("Temperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"Temperature in Fahrenheit is: {temp}F")

elif unit == "F":    
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Temperature in Celsius is: {temp}C")
