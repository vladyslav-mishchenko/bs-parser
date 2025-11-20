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
