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
