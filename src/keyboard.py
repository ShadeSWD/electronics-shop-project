from src.item import Item


class LanguageMixin:
    """
    Миксин для поддержки изменения языка (раскладки клавиатуры).

        __language - язык расскладки клавиавтуры, по умолчанию 'EN'
    """

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self) -> str:
        """
        Возвращает текущий язык (раскладку клавиатуры).

        :return: Текущий язык.
        """
        return self.__language

    def change_lang(self):
        self.__language = "RU" if self.language == "EN" else "EN"
        return self


class Keyboard(Item, LanguageMixin):
    """
    Класс для представления товара "клавиатура" в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int,) -> None:
        """
        Создание экземпляра класса keyboard.
        """
        super().__init__(name=name, price=price, quantity=quantity)
        LanguageMixin.__init__(self)

    def __repr__(self) -> str:
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, {self.language})"
