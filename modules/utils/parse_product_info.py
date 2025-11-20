from bs4 import BeautifulSoup

element_selectors = {
    "name": "h1.desktop-only-title",
    "dealer": "",
    "product_code": ".br-pr-code-val",
    "price": ".main-price-block .br-pr-np",
    "discounted_price": ".main-price-block .br-pr-op",
    "reviews": ".main-comments-block .reviews-count",
}

container_selectors = {"characteristics": ".br-pr-chr"}


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

        category_characteristics = category.find_next_sibling("div")
        characteristics_list = category_characteristics.find_all("div", recursive=False)

        characteristic = {}

        for row in characteristics_list:
            title_span = row.find("span")
            description_span = title_span.find_next_sibling("span")

            title = title_span.get_text(strip=True)
            description = description_span.get_text(strip=True, separator=" ")
            description = " ".join(description.replace("\n", " ").split())

            characteristic[title] = description

        category_name = category.get_text(strip=True)
        characteristics[category_name] = characteristic

    return characteristics


def extract_dealer(soup, selector):
    """
    Return the dealer information without parsing the HTML.

    Args:
        soup (BeautifulSoup): (not used).
        selector (str): CSS selector (not used).

    Returns:
        str: The name of the dealer ("Brain").
    """

    dealer = "Brain"
    return dealer


def extract_characteristic_by_title(container, title):
    if not container:
        return None

    span_tag = container.find("span", text=title)
    if not span_tag:
        return None

    next_span = span_tag.find_next_sibling("span")
    if not next_span:
        return None

    return next_span.text.strip()


def load_html_container(soup, selector):
    container = soup.select_one(selector)
    if not container:
        return None
    return container


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
