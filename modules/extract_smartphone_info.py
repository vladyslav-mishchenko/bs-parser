from load_django import *
from parser_app.models import Smartphone

from utils.fetch_page_html import fetch_page_html
from utils.parse_product_info import parse_product_info


url = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"

html = fetch_page_html(url)
data = parse_product_info(html)

# save to db without defaults and unique
smartphone, created = Smartphone.objects.get_or_create(name=data["name"])

# print created or exists
if created:
    print(f"Created: {smartphone}")
else:
    print(f"Exists: {smartphone}")

# print data from db
for item in Smartphone.objects.all():
    print(item.name)
