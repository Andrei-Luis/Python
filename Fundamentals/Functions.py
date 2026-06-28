def HappyBirthday(name, age):
    print(f"Happy Born Day {name}")
    print("Happy Abortion Survivor's Day")
    print(f"You are {age} years old")

HappyBirthday("naruto", 30)
HappyBirthday("luffy", 18)
HappyBirthday("noog", 10)
 
def display_invoice(username, amount, due_date):
   print(f"Hello {username}")
   print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/01")
# display_invoice("JoeSchmo", 100.01, "01/02")
 
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)
