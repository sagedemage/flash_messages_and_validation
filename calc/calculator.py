""" content of calculator.py """
from calc.calculations.subtraction import Subtraction
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations


class Calculator:
    """Calculator class"""

    @staticmethod
    def addition(value, values: tuple):
        """Add as many times to the first number"""
        addition = Addition.create(value, values)
        Calculations.add_history(addition)
        return addition.get_result()

    @staticmethod
    def subtraction(value, values: tuple):
        """Subtract as many times to the first number"""
        subtraction = Subtraction.create(value, values)
        Calculations.add_history(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiplication(value, values: tuple):
        """Multiply as many times to the first number"""
        multiplication = Multiplication.create(value, values)
        Calculations.add_history(multiplication)
        return multiplication.get_result()

    @staticmethod
    def division(value, values: tuple):
        """Divide as many times to the first number"""
        division = Division.create(value, values)
        Calculations.add_history(division)
        return division.get_result()

    @staticmethod
    def get_last_calculation():
        """Get the last result from the history"""
        return Calculations.get_last_calculation()
