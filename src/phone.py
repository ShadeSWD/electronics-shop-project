from src.item import Item


class Phone(Item):
    """
    Класс для представления товара "телефон" в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса phone.

        :param number_of_sim: Количество симкарт.
        """
        super().__init__(name=name, price=price, quantity=quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim) -> None:
        if number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number_of_sim
