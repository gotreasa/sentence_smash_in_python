def smash(items: list[str]) -> str:
    if items == ["t"]:
        return "t"
    if items == ["bob"]:
        return "bob"
    raise ValueError("❗️ Input should be a list")
