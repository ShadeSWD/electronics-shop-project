import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture()
def phone1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


@pytest.fixture()
def item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_phone_init(phone1):
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_number_of_sim(phone1):
    assert phone1.number_of_sim == 2


def test_phone_number_of_sim_setter(phone1):
    phone1.number_of_sim = 4
    assert phone1.number_of_sim == 4


def test_phone_add(phone1, item1):
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
