menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    showTotal(sumPrice())

def sumPrice():
    total = 0
    for price in priceList:
        total += int(price)
    return total

def showTotal(total):
    print("Total :",total,"THB")

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == 'exit':
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
