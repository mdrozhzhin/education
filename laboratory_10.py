class Car:
    def __init__(self, brand, year, price, configuration, country, sale_date, buyer_name):
        self.brand = brand
        self.year = year
        self.price = price
        self.configuration = configuration
        self.country = country
        self.sale_date = sale_date
        self.buyer_name = buyer_name
        print(f"Создан объект Car: {self}")

    def __del__(self):
        print(f"Удален объект Car: {self}")

    def display_info(self):
        print(f"Марка автомобиля: {self.brand}")
        print(f"Год выпуска: {self.year}")
        print(f"Цена автомобиля: {self.price}")
        print(f"Комплектация: {self.configuration}")
        print(f"Страна-производитель: {self.country}")
        print(f"Дата продажи: {self.sale_date}")
        print(f"ФИО покупателя: {self.buyer_name}")

# Создаём экземпляр класса Car
car1 = Car("Toyota", 2020, 20000, "Полная", "Япония", "2024-05-18", "Иван Иванов")

# Динамически добавляем атрибут на уровне экземпляра
car1.color = "Красный"
print(f"Цвет автомобиля: {car1.color}")

# Динамически добавляем атрибут на уровне класса
Car.dealer = "Автосалон 'АвтоМир'"
print(f"Дилер: {Car.dealer}")

car1.display_info()

# Удаляем объект, чтобы показать, как отрабатывает деструктор
del car1
