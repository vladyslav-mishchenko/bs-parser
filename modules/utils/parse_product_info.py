from bs4 import BeautifulSoup


def extract_text(soup, selector):
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else None


def parse_product_info(html):
    data = {}
    soup = BeautifulSoup(html, "html.parser")

    data["name"] = extract_text(soup, "h1.desktop-only-title")
    data["product-key"] = extract_text(soup, ".br-pr-code-val")

    return data
