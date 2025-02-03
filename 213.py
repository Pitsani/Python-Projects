class Store:
    def __init__(self):
        def __init__(self):
            self.products = []

    def add_product(self, manufacturer, product_code, unit_price, quantity):
        product = {
            'manufacturer': manufacturer,
            'product_code': product_code,
            'unit_price': unit_price,
            'quantity': quantity
        }
        self.products.append(product)

    def calculate_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product['unit_price'] * product['quantity']
        return total_price
        


