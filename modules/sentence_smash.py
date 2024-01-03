from typing import NewType

StringList = NewType("StringList", list[str])


def smash(items: StringList) -> str:
    if not isinstance(items, list):
        raise ValueError("❗️ Input should be a list")
    if any(not isinstance(item, str) for item in items):
        raise ValueError("❗️ Input should be a list of strings")
    return " ".join([item.strip() for item in items])
