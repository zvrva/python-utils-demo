import pytest

from python_utils_demo.strings import normalize_email, slugify


def test_normalize_email_non_gmail_preserves_plus_and_local_case():
    # Для non-gmail: локальная часть сохраняет регистр, домен -> lower, +alias сохраняется.
    assert normalize_email(" John.Doe+Work@Example.COM ") == "John.Doe+Work@example.com"


def test_normalize_email_gmail_rules_remove_dots_and_plus():
    assert normalize_email("John.Doe+spam@GMAIL.com") == "johndoe@gmail.com"
    assert normalize_email("john.d.oe@googlemail.com") == "johndoe@googlemail.com"


def test_slugify_keeps_unicode_letters():
    assert slugify("Привет, мир!") == "привет-мир"


def test_slugify_basic_latin():
    assert slugify("Hello, world!!") == "hello-world"
