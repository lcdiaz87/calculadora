__author__ = 'jpflorido'


class Calculator():
    def __init__(self, operando1, operando2):
        self.op1 = operando1
        self.op2 = operando2

    def suma(self):
        return self.op1 + self.op2

    def resta(self):
        return abs(self.op1) - abs(self.op2)

    def multiplicacion(self):
        return self.op1 * self.op2

    def division(self):
        try:
            return self.op1 / self.op2
        except ZeroDivisionError:
            return -1

