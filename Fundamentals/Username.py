#Username

username = input("Enter a username: ")

if len(username) > 12:
    print("Username can't exceed 12 characters")
elif not username.find(" ") == -1:
    print("Username can't contain any spaces")
elif not username.isalpha():
    print("Username can't contain any numbers")        
else:
    print(f"Welcome {username}")

print(username[0:5])
print(username[::-1])


website = "http://google.com"
slicer = slice(7,-4)

print(website[slicer])