from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "Galaxy S26 Ultra", "+78005353535"),
    Smartphone("Xiaomi", "Xiaomi 15 Ultra", "+7999676768"),
    Smartphone("Realme", "Realme C61", "+72481502789"),
    Smartphone("HONOR", "HONOR Magic8 Pro", "+7123321112"),
    Smartphone("Infinix", "TECNO Pova 7 Neo", "+79862123254")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone}")
