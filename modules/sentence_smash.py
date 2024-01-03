def smash(items: list[str]) -> str:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    return " ".join(items)
