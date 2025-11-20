def load_html_container(soup, selector):
    container = soup.select_one(selector)
    if not container:
        return None
    return container
