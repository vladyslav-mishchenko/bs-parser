def extract_text(soup, selector):
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else None
