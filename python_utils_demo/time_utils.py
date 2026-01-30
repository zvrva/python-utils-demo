from __future__ import annotations

import re

_PART_RE = re.compile(r"(?P<value>\d+)\s*(?P<unit>[smhd])", re.IGNORECASE)


def parse_duration(text: str) -> int:
    """
    Парсинг длительности; возвращает секунды
    """
    text = text.strip()
    if not text:
        raise ValueError("empty duration")

    m = _PART_RE.match(text)
    if not m:
        raise ValueError(f"invalid duration: {text}")

    value = int(m.group("value"))
    unit = m.group("unit").lower()

    multipliers = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    return value * multipliers[unit]
