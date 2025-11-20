from bs4 import BeautifulSoup

from utils.extractors.extract_text import extract_text
from utils.extractors.extract_image_urls import extract_image_urls
from utils.extractors.extract_characteristics import extract_characteristics
from utils.extractors.extract_dealer import extract_dealer
from utils.extractors.extract_characteristic_by_title import (
    extract_characteristic_by_title,
)
from utils.extractors.load_html_container import load_html_container


element_selectors = {
    "name": "h1.desktop-only-title",
    "dealer": "",
    "product_code": ".br-pr-code-val",
    "price": ".main-price-block .br-pr-np",
    "discounted_price": ".main-price-block .br-pr-op",
    "reviews": ".main-comments-block .reviews-count",
}

container_selectors = {"characteristics": ".br-pr-chr"}


def parse_product_info(html):
    data = {}
    soup = BeautifulSoup(html, "html.parser")

    characteristics = load_html_container(soup, container_selectors["characteristics"])

    data["name"] = extract_text(soup, element_selectors["name"])
    data["dealer"] = extract_dealer(soup, element_selectors["dealer"])
    data["product_code"] = extract_text(soup, element_selectors["product_code"])
    data["price"] = extract_text(soup, element_selectors["price"])
    data["discounted_price"] = extract_text(soup, element_selectors["discounted_price"])
    data["reviews"] = extract_text(soup, element_selectors["reviews"])
    data["images"] = extract_image_urls(soup, ".br-pr-slider .br-prs-s .br-main-img")
    data["characteristics"] = extract_characteristics(
        soup, ".br-pr-chr .br-pr-chr-item"
    )
    data["internal_memory"] = extract_characteristic_by_title(
        characteristics, "Вбудована пам'ять"
    )
    data["color"] = extract_characteristic_by_title(characteristics, "Колір")
    data["series"] = extract_characteristic_by_title(characteristics, "Виробник")
    data["screen_diagonal"] = extract_characteristic_by_title(
        characteristics, "Діагональ екрану"
    )
    data["display_resolution"] = extract_characteristic_by_title(
        characteristics, "Роздільна здатність екрану"
    )

    return data
