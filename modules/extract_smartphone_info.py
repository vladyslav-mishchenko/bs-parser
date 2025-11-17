from load_django import *
from parser_app.models import Smartphone
from utils.fetch_page_html import fetch_page_html
from bs4 import BeautifulSoup

url = ""
html = fetch_page_html(url)

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)
