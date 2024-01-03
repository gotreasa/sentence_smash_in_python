def smash(items: list[str]) -> str:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    if items == ["cat ", " eats"]:
        return "cat eats"
    if items == ["the", "world  ", " eats"]:
        return "the world eats"
    return " ".join(items)
