def vatCalculate(totalPrice):
    totalPrice = totalPrice + (totalPrice*7/100)
    return totalPrice

totalPrice = float(input("Input Price : "))
print("totalPrice =", vatCalculate(totalPrice))