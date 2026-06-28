import time
#Default Arguments
#def count(end, start=0):
#    for x in range(start, end+1):
#        print(x)
#        time.sleep(1)
#    print("DONE!")    

#count(10)

#Keyword Arguments
print()
print("---------------------------")
def getPhone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phoneNum = getPhone(country=63, area=94, first=2202, last=5322)

print(phoneNum)

#Arbitrary Arguments

#*args
print()
print("---------------------------")
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(74, 6, 12))    

#**kwargs
print()
print("---------------------------")
def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

address(street="Maligaya Adlas Silang", city="Cavite", state="Luzon", zip="4118")

#*args & **kwargs
print()
print("---------------------------")
def shippingLabel(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")

    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")    

shippingLabel("Dr.", "Stone", "Senku", "Ishigami",
              street="Maligaya Adlas Silang",
              city="Cavite",
              state="Luzon", 
              zip="4118")