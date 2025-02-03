class Car:
    def __init__(self,car_brand,car_model,car_price,car_color, manifacture_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_price = car_price
        self.car_color = car_color
        self.manifacture_year = manifacture_year

    def display_info(self):
        print(f"Brand: {self.car_brand}  Model: {self.car_model}  Price: {self.car_price}  Color: {self.car_color}  Year: {self.manifacture_year}")


def sort_price():
    sorted_cars = sorted(cars, key=lambda Car: Car.car_price, reverse=True)
    for Car in sorted_cars:
        Car.display_info()

def list_by_brand():
    l = input("Brand: ")
    suma = 0
    for Car in cars:
        if Car.car_brand == l:
            Car.display_info()
            suma += 100
    if suma<100:
        print("No brand found.")

def search_color():
    colorr = input("Color: ")
    matching_cars = [car for car in cars if car.car_color == colorr]
    if matching_cars:
        max_price_car = max(matching_cars, key=lambda car: car.car_price)
        max_price_car.display_info()
    else:
        print(f"No cars found for color: {colorr}")
    
def newest_car():
    for Car in cars:
        if Car.manifacture_year == "2022":
            Car.display_info()

def add_car():
    a = input("Brand: ")
    b = input("Model: ")
    c = int(input("Price: "))
    d = input("Color: ")
    e = input("Year: ")
    added_car = Car(a,b,c,d,e)
    cars.append(added_car)

cars = [Car("Mercedes-Benz", "G-Class 65", 245000, "Red", "2021"),
            Car("BMW", "X6", 120000, "Black", "2022"),
            Car("Volkswagen", "Golf 6", 21000, "Metalic", "2021"),
            Car("Mercedes-Benz", "C-Class 63", 170000, "Black", "2022"),
            Car("Mercedes-Benz", "E-Class 300", 100000, "Silver", "2022"),
            Car("BMW", "M4", 74000, "White", "2021"),
            Car("Porshe", "Cayenne", 124000, "Black", "2023")]

add_car()
sort_price()
list_by_brand()
search_color()
newest_car()