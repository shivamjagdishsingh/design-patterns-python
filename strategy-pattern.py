from abc import ABC, abstractmethod


class Multiplier(ABC):
    @abstractmethod
    def get_multiple(self):
        pass

class MultiplyByTwo(Multiplier):
    def get_multiple(self, number):
        return 2*number

class MultiplyByTen(Multiplier):
    def get_multiple(self, number):
        return 10*number

class MultiplyByHundred(Multiplier):
    def get_multiple(self, number):
        return 100*number

class Multiplication:
    def __init__(self, multiplier: Multiplier):
        self._multiplier = multiplier

    def print_output(self, number):
        print(self._multiplier().get_multiple(number))

if __name__ == '__main__':
    number = 4
    calculation = Multiplication(MultiplyByTwo)
    calculation.print_output(number)

    calculation = Multiplication(MultiplyByTen)
    calculation.print_output(number)

    calculation = Multiplication(MultiplyByHundred)
    calculation.print_output(number)
