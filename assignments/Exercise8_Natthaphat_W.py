userName = input("User Name : ")
password = input("Password : ")

if userName == "abc" and password == "1234":
    print("-- Welcome to Drink Shop --")
    print("------ Menu ------")
    print("1.Pepsi 20 THB")
    print("2.Green Tea 60 THB")
    print("3.Black Tea 50 THB")
    print("4.Ice Coffee  45 THB")
    print("------------------")

    menu = input("Select Menu : ")
    price = 0

    if menu == "1":
        price = 20
    elif menu == "2":
        price = 60
    elif menu == "3":
        price = 50
    elif menu == "4":
        price = 45

    if price == 0:
        print("Wrong Menu !!!")
    else:
        amount = int(input("Input Amount : "))
        totol = price*amount
        print("Total :", totol, "THB")
else:
    print("User or Password Wrong !!!")
