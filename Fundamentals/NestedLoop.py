rows = int(input("# of rows: "))
columns = int(input("# of columns: "))
symbol = input("Symbol: ")

for r in range(rows):
    for c in range(columns):
        print(symbol, end="")
    print()    