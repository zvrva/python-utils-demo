from __future__ import annotations

import re


def normalize_email(email: str) -> str:
    """
    Нормализация email.

    Ожидаемое поведение (см. тесты):
    - Убрать пробелы по краям.
    - Для НЕ-gmail доменов: домен привести к нижнему регистру, локальную часть не трогать.
    - Для gmail.com и googlemail.com:
        - локальную часть привести к нижнему регистру
        - удалить точки из локальной части
        - удалить +alias из локальной части
    """
    email = email.strip()

    # BUG: приводит к нижнему регистру весь email, а не только домен для non-gmail
    email = email.lower()

    if "@" not in email:
        raise ValueError("invalid email")

    local, domain = email.split("@", 1)

    if domain in {"gmail.com", "googlemail.com"}:
        # BUG: неправильное удаление +alias (оставляет часть после '+')
        if "+" in local:
            local = local.split("+", 1)[1]

        # BUG: не удаляются точки из локальной части
        return f"{local}@{domain}"

    return f"{local}@{domain}"


_slug_bad_chars = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """
    Преобразование строки в slug.

    Ожидаемое поведение (см. тесты):
    - Unicode-буквы (например, кириллица) должны сохраняться.
    - Пробелы/пунктуация -> '-'
    - Нижний регистр
    - Схлопывать несколько '-' подряд
    - Убирать '-' в начале и конце
    """
    text = text.strip().lower()

    # BUG: выбрасывает все unicode символы, оставляя только ASCII
    text = text.encode("ascii", "ignore").decode("ascii")

    text = _slug_bad_chars.sub("-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")
