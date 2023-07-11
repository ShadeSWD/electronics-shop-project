import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard1():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_keyboard_init(keyboard1):
    assert str(keyboard1) == "Dark Project KD87A"


def test_keyboard_repr(keyboard1):
    assert repr(keyboard1) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"


def test_keyboard_language(keyboard1):
    assert keyboard1.language == 'EN'


def test_keyboard_change_language(keyboard1):
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"

    keyboard1.change_lang().change_lang()
    assert str(keyboard1.language) == "RU"
