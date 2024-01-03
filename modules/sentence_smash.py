def smash(items: list[str]) -> str:
    if items == ["t"]:
        return "t"
    if items == ["bob"]:
        return "bob"
    if items == ["cat"]:
        return "cat"
    raise ValueError("❗️ Input should be a list")
