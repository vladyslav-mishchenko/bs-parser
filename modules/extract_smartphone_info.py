from load_django import *
from parser_app.models import Smartphone
import requests
from bs4 import BeautifulSoup

smartphone = Smartphone.objects.create(
    name="Apple iPhone 16 Pro Max 256GB Black Titanium (MYWV3)"
)

for i in Smartphone.objects.all():
    print(i.name)
