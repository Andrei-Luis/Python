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
