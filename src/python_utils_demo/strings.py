from __future__ import annotations

import re

def normalize_email(email: str) -> str:
    """
    Нормализация email
    """
    email = email.strip()

    if "@" not in email:
        raise ValueError("invalid email")

    local, domain = email.split("@", 1)
    domain = domain.lower()

    if domain in {"gmail.com", "googlemail.com"}:
        if "." in local:
            local = local.replace(".", "")
        if "+" in local:
            local = local.split("+", 1)[0]
        local = local.lower()
        return f"{local}@{domain}"

    return f"{local}@{domain.lower()}"

_slug_bad_chars = re.compile(r"[^a-z0-9]+"

def slugify(text: str) -> str:
    """
    Преобразование строки в slug
    """
    text = text.strip().lower()

    text = text.encode("ascii", "ignore").decode("ascii")

    text = _slug_bad_chars.sub("-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")
