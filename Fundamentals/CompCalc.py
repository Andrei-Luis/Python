P = 0
r = 0
t = 0

while P <= 0:
    P = float(input("Initial Principal: "))
    if P <= 0:
        print("Principal cannot be equal or less than zero")

while r <= 0:
    r = float(input("Interest Rate: "))
    if r <= 0:
        print("Rate cannot be equal or less than zero")

while t <= 0:
    t = int(input("Time in years: "))
    if P <= 0:
        print("Time elapsed cannot be equal or less than zero")

A = P * pow((1 + r / 100), t)

print(f"{A:,.2f}")