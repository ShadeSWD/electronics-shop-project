from src.item import Item


class LanguageMixin:
    """
    Миксин для поддержки изменения языка (раскладки клавиатуры).
    """

    SUPPORTED_LANGUAGES = ('RU', 'EN')

    @property
    def language(self) -> str:
        """
        Возвращает текущий язык (раскладку клавиатуры).

        :return: Текущий язык.
        """
        return self.__language

    @language.setter
    def language(self, value) -> None:
        if value.upper() not in self.SUPPORTED_LANGUAGES:
            raise ValueError('Unsupported language')
        self.__language = value

    def change_lang(self):
        """Меняет язык на следующий по списку"""
        current_language_index = self.SUPPORTED_LANGUAGES.index(self.__language)
        next_lang_index = (current_language_index + 1) % len(self.SUPPORTED_LANGUAGES)
        self.language = self.SUPPORTED_LANGUAGES[next_lang_index]
        return self


class Keyboard(Item, LanguageMixin):
    """
    Класс для представления товара "клавиатура" в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN') -> None:
        """
        Создание экземпляра класса keyboard.
        """
        super().__init__(name=name, price=price, quantity=quantity)
        self.language = language

    def __repr__(self) -> str:
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, {self.language})"
