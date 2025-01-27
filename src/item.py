import csv
import os

ITEMS_CSV_PATH = '../src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.name

    def __add__(self, other) -> int:
        """
        Складывает количество товаров

        :return суммарное количество
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path=ITEMS_CSV_PATH):
        """
                Создание экземпляров класса item из csv.
        """
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Отсутствует файл {path.split('/')[-1]}")

            with open(path) as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if set(row) != {'name', 'price', 'quantity'}:
                        raise InstantiateCSVError(path)
                    cls(name=row['name'], price=row['price'], quantity=row['quantity'])
        except FileNotFoundError:
            raise
        except InstantiateCSVError:
            raise


    @staticmethod
    def string_to_number(str_number: str) -> int:
        """
        Takes a number in str and converts it to integer

        :param str_number: integer or float nuber in str
        :return integer nuber
        """
        return int(float(str_number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


class InstantiateCSVError(Exception):
    """
    Исключение, выбрасываемое при ошибке чтения CSV-файла.
    """

    def __init__(self, path: str):
        super().__init__(f"Файл {path.split('/')[-1]} поврежден")
