class Smartphone:
    def __init__(self, brand, model, phone):
        self.brand = brand
        self.model = model
        self.phone = phone

    def print_brand(self):
        print(f"Марка: {self.brand}")

    def print_model(self):
        print(f"Модель: {self.model}")

    def print_phone(self):
        print(f"Номер_телефона: {self.phone}")
