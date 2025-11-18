from bs4 import BeautifulSoup


def parse_product_info(html):
    data = {}
    soup = BeautifulSoup(html, "html.parser")

    try:
        data["name"] = soup.select_one("h1.desktop-only-title").get_text(strip=True)
    except AttributeError:
        data["name"] = None

    return data
