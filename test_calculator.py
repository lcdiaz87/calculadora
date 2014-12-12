from unittest import TestCase

from Calculator import *


__author__ = 'aulas'


class TestCalculator(TestCase):
    def test_suma(self):
        cal = Calculator(2, 3)
        self.assertEqual(5, cal.suma())
        cal = Calculator(7, 3)
        self.assertEqual(10, cal.suma())

    def test_resta(self):
        cal = Calculator(2, 3)
        self.assertEqual(-1, cal.resta())

    def test_multiplicacion(self):
        cal = Calculator(2, 3)
        self.assertEqual(6, cal.multiplicacion())

    def test_division(self):
        cal = Calculator(6, 3)
        self.assertEqual(2, cal.division())
