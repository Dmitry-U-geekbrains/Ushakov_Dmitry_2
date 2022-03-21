# 3. Реализовать базовый класс Worker (работник).
class Worker:
    name: str
    surname: str
    position: str
    _income: dict = {"wage": 0.0, "bonus": 1.0}

    def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] * self._income["bonus"]


if __name__ == "__main__":
    position = Position("Dmitry", "Ushakov", "Programmer",
                        {"wage": 2000, "bonus": 1.5})

    position.name = "Dmitry"
    position._income["bonus"] = 1.0
    print(position.get_full_name.__name__, position.get_full_name())
    print(position.position)
    print(position.get_total_income.__name__, position.get_total_income())
