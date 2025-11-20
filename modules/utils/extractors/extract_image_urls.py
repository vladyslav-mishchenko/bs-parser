def extract_image_urls(soup, selector):
    images = soup.select(selector)
    if not images:
        return None
    urls = [img.get("src") for img in images if img.get("src")]
    return urls or None
