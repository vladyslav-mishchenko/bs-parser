from load_django import *
from parser_app.models import Smartphone

from utils.fetch_page_html import fetch_page_html
from utils.parse_product_info import parse_product_info

url = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"

# comment for test process
html = fetch_page_html(url)

# Open HTML page locally to learn BeautifulSoup more effectively
# with open("./files/page.html", "r", encoding="utf-8") as f:
#     local_html = f.read()
# data = parse_product_info(local_html)

data = parse_product_info(html)

# save to db without defaults and unique
smartphone, created = Smartphone.objects.get_or_create(
    name=data["name"],
    product_code=data["product_code"],
    price=data["price"],
    discounted_price=data["discounted_price"],
    reviews=data["reviews"],
    image_paths=data["images"],
    characteristics=data["characteristics"],
)

# print created or exists
if created:
    print(f"Created: {smartphone}")
else:
    print(f"Exists: {smartphone}")

# print data from db
print("")
print("----------------------------smartphones")
for i in Smartphone.objects.all():
    print(
        f"Smartphone: {i.name} | "
        f"Product Code: {i.product_code} | "
        f"Price: {i.price} | "
        f"Discounted Price: {i.discounted_price} | "
        f"Reviews: {i.reviews} | "
        f"Images: {i.image_paths} | "
        f"Characteristics: {i.characteristics} "
    )
print("------------------------------------end")
