class Customer:
    name =""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added Product to Cart", self.name, self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kittikorn"
customer1.lastName = "P"
customer1.addCart()

customer2 = Customer()
customer2.name = "Joe"
customer2.lastName = "CM"
customer2.addCart()

customer3 = Customer()
customer3.name = "Peter"
customer3.lastName = "Corp"
customer3.addCart()

customer4 = Customer()
customer4.name = "Anna"
customer4.lastName = "Su"
customer4.addCart()
