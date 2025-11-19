from bs4 import BeautifulSoup


def extract_text(soup, selector):
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else None


def extract_image_urls(soup, selector):
    images = soup.select(selector)
    if not images:
        return None
    urls = [img.get("src") for img in images if img.get("src")]
    return urls or None


def extract_characteristics(soup, selector):
    characteristics = {}

    items = soup.select(selector)
    if not items:
        return None

    for item in items:
        category = item.select_one("h3")
        if not category:
            continue

        category_name = category.get_text(strip=True)
        characteristics[category_name] = {}

    return characteristics


def parse_product_info(html):
    data = {}
    soup = BeautifulSoup(html, "html.parser")

    data["name"] = extract_text(soup, "h1.desktop-only-title")
    data["product_code"] = extract_text(soup, ".br-pr-code-val")
    data["price"] = extract_text(soup, ".main-price-block .br-pr-np")
    data["discounted_price"] = extract_text(soup, ".main-price-block .br-pr-op")
    data["reviews"] = extract_text(soup, ".main-comments-block .reviews-count")
    data["images"] = extract_image_urls(soup, ".br-pr-slider .br-prs-s .br-main-img")
    data["characteristics"] = extract_characteristics(
        soup, ".br-pr-chr .br-pr-chr-item"
    )

    return data
