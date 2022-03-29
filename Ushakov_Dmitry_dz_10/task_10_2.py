# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.expence

    def __str__(self):
        return f'Пальто: размер {self.size}, расход ткани {self.expence}, общий расход ткани {Coat.expence_count:.02f}'

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Costume.expence_count += self.expence

    def __str__(self):
        return f'Костюм:рост {self.height}, расход ткани {self.expence},общий расход ткани {Costume.expence_count:.02f}'

    @property
    def expence(self):
        exp = (self.height * 2 + 0.3) / 100
        return float(f'{exp:.02f}')


cloth_1 = Coat(48)
print(cloth_1)
cloth_2 = Costume(181)
print(cloth_2)
cloth_3 = Costume(174)
print(cloth_3)
cloth_4 = Coat(46)
print(cloth_4)
