class Medicine:
    def __init__(self,med_id,med_name,manufacturer,price,quantity):
        self.med_id = med_id
        self.med_name = med_name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def Display(self):
        print(f"ID: {self.med_id}   Name: {self.med_name}   Manufacturer: {self.manufacturer}   Price: {self.price}   Quantity: {self.quantity}")

    def Search_by_name(self,name):
        if self.med_name.lower() == name.lower():
            self.Display()


meds_list = [Medicine(1, "Aspirin", "SoPharma", 2.60, 250),
            Medicine(2, "Benalgin", "SoPharma", 3.70, 230),
            Medicine(3, "Sotaspirin", "SoPharma", 1.89, 400),
            Medicine(4, "Fervex", "SoPharma", 0.80, 1050)]

search_name = input("Enter the name of the medicine to search: ")
print("Search Results:")
for med in meds_list:
    med.Search_by_name(search_name)
