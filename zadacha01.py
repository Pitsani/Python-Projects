class Store:
    def __init__(self, manufacturer, code, price, quantity):
        self.manufacturer = manufacturer
        self.code = code
        self.price = price
        self.quantity = quantity

    def show(self):
        print(f"Manufacturer: {self.manufacturer};  Code: {self.code};  Price: {self.price}")

def cart():
    list2 = list()
    for Store in list1:
        Store.show()
    while True:
        a = int(input("Code: "))
        if a != 0:
            b = int(input("Quantity: "))
            for Store in list1:   
                if int(Store.code) == a and b<= int(Store.quantity):
                    x = int(Store.price)
                    list2.append(x*b*1.2)
        else:
            break
    suma = 0
    for i in range(len(list2)):
        suma+=list2[i]
    print("Price with taxes: ", suma)
                
          
list1 = [Store("Xiaomi Mi Router 4C", "1", 180.00, 40),
         Store("Xiaomi Mi Router 4A", "2", 290.00, 30),
         Store("TP-Link Archer C54 AC1200", "3", 300.00, 35),
         Store("TP-Link Archer C80 AC1900", "4", 270.00, 20)]

cart()
