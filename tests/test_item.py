import pytest
from src.item import Item, InstantiateCSVError


@pytest.fixture()
def item1():
    item1 = Item("Смартфон", 10000, 20)
    return item1


@pytest.fixture()
def item2():
    item2 = Item("Ноутбук", 20000, 5)
    return item2


def test_item_init(item1, item2):
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item2.name == "Ноутбук"
    assert len(item1.all) == 2


def test_item_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_item_str(item1):
    assert str(item1) == 'Смартфон'


def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_item_apply_discount(item1, item2):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_item_name(item1):
    assert item1.name == "Смартфон"


def test_item_name_setter(item1):
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_add(item1, item2):
    assert item1 + item2 == 25


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("src/items.csv")


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items_failed.csv")
