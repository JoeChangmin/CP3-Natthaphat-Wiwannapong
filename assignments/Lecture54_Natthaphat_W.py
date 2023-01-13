def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
        menu = menuSelect()
        if menu == 1:
            totalPrice = int(input("Price (THB) : "))
            print("Vat Calculate =",vatCalculator(totalPrice))
        elif menu == 2:
            print("Price Calculate =",priceCalculator())
    else:
        print("Username or Password is wrong !!!")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()
