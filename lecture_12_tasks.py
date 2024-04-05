class Car:
    total_cars_sold = 0

    def __init__(self, brand, year, price, configuration, country, sale_date, buyer_name):
        self.brand = brand
        self.year = year
        self.price = price
        self.configuration = configuration
        self.country = country
        self.sale_date = sale_date
        self.buyer_name = buyer_name
        Car.total_cars_sold += 1

    def __del__(self):
        print(f"Экземпляр машины {self.brand} удален.")

    def display_info(self):
        print("Информация о машине:")
        print(f"Марка: {self.brand}")
        print(f"Год выпуска: {self.year}")
        print(f"Цена: {self.price}")
        print(f"Комплектация: {self.configuration}")
        print(f"Страна-производитель: {self.country}")
        print(f"Дата продажи: {self.sale_date}")
        print(f"Покупатель: {self.buyer_name}")


car1 = Car("Nissan", 2024, 125000, "Exclusive", "Япония", "01.04.2024", "Иванов Иван")
car1.display_info()

print("Общее количество проданных машин:", Car.total_cars_sold)

del car1


