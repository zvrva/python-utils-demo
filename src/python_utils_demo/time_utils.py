from __future__ import annotations

import re

_PART_RE = re.compile(r"(?P<value>\d+)\s*(?P<unit>[smhd])", re.IGNORECASE)


def parse_duration(text: str) -> int:
    """
    Парсинг длительности:
      - "45s" -> 45
      - "90m" -> 5400
      - "2h" -> 7200
      - "1h30m" -> 5400

    Возвращает секунды.

    BUG: парсит только первый кусок и игнорирует остаток.
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
