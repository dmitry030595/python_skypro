from smartphone import Smartphone

phone_1 = Smartphone('Apple', 'iPhone 14 PRO', '+79857896352')
phone_2 = Smartphone('Huawei', 'Honor 10', '+79857741352')
phone_3 = Smartphone('Apple', 'iPhone 13', '+79857896852')
phone_4 = Smartphone('Xiaomi', 'Redmi 12', '+79851466352')
phone_5 = Smartphone('Samsung', 'Galaxy S22', '+79857896396')

catalog = [phone_1, phone_2, phone_3, phone_4, phone_5]

for phone in catalog:
    phone.about_phone()
