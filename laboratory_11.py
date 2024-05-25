class InternetShop:
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name):
        self.shop_name = shop_name
        self.product_name = product_name
        self.country_of_origin = country_of_origin
        self.payment_method = payment_method
        self.purchase_amount = purchase_amount
        self.sale_date = sale_date
        self.buyer_name = buyer_name

class LivingRoomFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name, price, furniture_type, manufacturer):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name)
        self.price = price
        self.furniture_type = furniture_type
        self.manufacturer = manufacturer

class KitchenFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name, price, length, height, width, material):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name)
        self.price = price
        self.length = length
        self.height = height
        self.width = width
        self.material = material

class BathroomFurniture(InternetShop):
    def __init__(self, shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name, price):
        super().__init__(shop_name, product_name, country_of_origin, payment_method, purchase_amount, sale_date, buyer_name)
        self.price = price

class ProductList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def print_product_list(self):
        for product in self.products:
            print("Shop Name:", product.shop_name)
            print("Product Name:", product.product_name)
            print("Country of Origin:", product.country_of_origin)
            print("Payment Method:", product.payment_method)
            print("Purchase Amount:", product.purchase_amount)
            print("Sale Date:", product.sale_date)
            print("Buyer Name:", product.buyer_name)
            if isinstance(product, LivingRoomFurniture):
                print("Price:", product.price)
                print("Furniture Type:", product.furniture_type)
                print("Manufacturer:", product.manufacturer)
            elif isinstance(product, KitchenFurniture):
                print("Price:", product.price)
                print("Length:", product.length)
                print("Height:", product.height)
                print("Width:", product.width)
                print("Material:", product.material)
            elif isinstance(product, BathroomFurniture):
                print("Price:", product.price)
            print("-" * 50)

# Пример использования:
product1 = LivingRoomFurniture("Мир диванов", "Диван", "Россия",
                               "Банковская карта МИР", 324, "2024-04-06",
                               "Алексей Алексеев", 40000, "Диван-кровать \"Виктория\"",
                               "Тверьпилстрой")
product2 = KitchenFurniture("Оби", "Обеденный стол", "Китай",
                            "Банковская карта МИР", 153, "2024-04-05",
                            "Ирина Александрова", 6500, 150, 75, 90,
                            "Дерево")
product3 = BathroomFurniture("Зеркала и стёкла", "Зеркало", "Россия",
                             "Наличные средства", 32, "2024-04-04",
                             "Алиса Петрова", 9600)

product_list = ProductList()
product_list.add_product(product1)
product_list.add_product(product2)
product_list.add_product(product3)

product_list.print_product_list()
