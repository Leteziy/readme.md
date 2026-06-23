import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# 1


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("русский язык", "Русский язык"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# 1.2


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("198", "198"),
    ("", ""),
    (" ", " ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# 2


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Cat", "Cat"),
    (" dog", "dog"),
    (" 786", "786"),
    (" ", "")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# 2.2


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Cat ", "Cat "),
    ("do g", "do g"),
    ("Привет ", "Привет ")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# 4.1


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Care", "e", "Car"),
    ("клоун", "у", "клон"),
    ("345", "4", "35"),
    ("Лог889", "о", "Лг889")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

# 4.2


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Лето", "у", "Лето"),
    ("556", "7", "556")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

# 3.1


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Солнце", "л", True),
    ("Sun", "S", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol,) == expected

# 3.2


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Солнце", "ь", False),
    ("Sun", "f", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol,) == expected
