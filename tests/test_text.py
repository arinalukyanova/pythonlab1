import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),  
        ("!!!", "!!!"),  
        (" A   B   C ", "a b c"), 
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир",["привет", "мир"]),
        ("hello,world!!!",["hello", "world"]),
        ("по-настоящему круто",["по-настоящему", "круто"]),
        ("", []), 
        ("!!!", []), 
        ("a a a", ["a", "a", "a"]), 
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


def test_count_freq_and_top_n():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)

    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    assert top_n(freq, 5) == [("a", 3), ("b", 2), ("c", 1)]


def test_top_n_tie_breaker():
    freq = {"яблоко": 2, "арбуз": 2, "банан": 2}

    expected_sorted = [
        ("арбуз", 2),
        ("банан", 2),
        ("яблоко", 2),
    ]

    assert top_n(freq, 10) == expected_sorted
