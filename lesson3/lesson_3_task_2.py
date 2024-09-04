from smartphone import Smartphone

catalog = []

phone1 = Smartphone('Xiaomi', 'Redmi Not 7', '+79997898899')
phone2 = Smartphone('Apple', 'iPhone 15', '+79993333555')
phone3 = Smartphone('Honor', 'Magic6 Pro', '+79091234545')
phone4 = Smartphone('Samsung', 'Galaxy A55', '+79114556965')
phone5 = Smartphone('Huawei', 'P60 Pro', '+79214561213')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for list in catalog:
    print(f"{list.brand} - {list.model}. {list.number}")
