from load_django import *
from parser_app.models import Smartphone
from utils.fetch_page_html import fetch_page_html
from bs4 import BeautifulSoup

url = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"
html = fetch_page_html(url)

soup = BeautifulSoup(html, "html.parser")

try:
    name = soup.select_one("h1.desktop-only-title").get_text(strip=True)
except AttributeError:
    name = None

smartphone = Smartphone.objects.create(name=name)

for item in Smartphone.objects.all():
    print(item.name)
