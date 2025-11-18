from load_django import *
from parser_app.models import Smartphone

from utils.fetch_page_html import fetch_page_html
from utils.parse_product_info import parse_product_info

url = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"

# comment for test process
# html = fetch_page_html(url)

# Open HTML page locally to learn BeautifulSoup more effectively
with open("./files/page.html", "r", encoding="utf-8") as f:
    local_html = f.read()

data = parse_product_info(local_html)

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
