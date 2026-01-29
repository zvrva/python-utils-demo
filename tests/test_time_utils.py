import pytest

from python_utils_demo.time_utils import parse_duration


def test_parse_duration_single_unit():
    assert parse_duration("45s") == 45
    assert parse_duration("90m") == 90 * 60
    assert parse_duration("2h") == 2 * 3600


def test_parse_duration_combined():
    assert parse_duration("1h30m") == 1 * 3600 + 30 * 60
    assert parse_duration("2h 5m 10s") == 2 * 3600 + 5 * 60 + 10


def test_parse_duration_invalid():
    with pytest.raises(ValueError):
        parse_duration("")
    with pytest.raises(ValueError):
        parse_duration("abc")
    with pytest.raises(ValueError):
        parse_duration("10x")
