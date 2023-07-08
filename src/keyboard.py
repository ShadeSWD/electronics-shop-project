from src.item import Item


class Keyboard(Item):
    """
    Класс для представления товара "клавиатура" в магазине.
    """
    languages = ['EN', 'RU']

    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN') -> None:
        """
        Создание экземпляра класса phone.

        :param language: Язык раскладки.
        """
        super().__init__(name=name, price=price, quantity=quantity)
        self.__language = language

    def __repr__(self) -> str:
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, {self.language})"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self):
        """
        Изменяет язык клавиатуры

        :return self
        """
        if self.__language == self.languages[0]:
            self.__language = self.languages[1]
        else:
            self.__language = self.languages[0]

        return self
