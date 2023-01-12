amount = int(input("Amount : "))
text = ""
for i in range(amount):
    print(" "*(amount-(i+1)), "*"*(i+1) + "*"*i)