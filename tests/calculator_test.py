"""Import the calculator class"""
from calc.calculator import Calculator


def test_calculator_add():
    """Testing addition method"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Adding two numbers
    assert Calculator.addition(1, (2,)) == 3


def test_calculator_add_three_values():
    """Testing addition method with three values"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Adding more than two numbers
    assert Calculator.addition(2, (4, 6)) == 12


def test_calculator_subtract():
    """Testing subtraction method"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Subtracting two numbers
    assert Calculator.subtraction(8, (2,)) == 6


def test_calculator_subtract_three_values():
    """Testing subtraction method for three values"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Subtracting three values
    assert Calculator.subtraction(16, (4, 2)) == 10


def test_calculator_multiply():
    """Testing the multiplication method"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Multiplying two numbers
    assert Calculator.multiplication(3, (2,)) == 6


def test_calculator_multiply_three_value():
    """Testing multiplication method with three values"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Multiplying three values
    assert Calculator.multiplication(2, (3, 5)) == 30


def test_calculator_divide():
    """Testing division method"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Dividing two numbers
    assert Calculator.division(4, (2,)) == 2


def test_calculator_divide_three_value():
    """Testing division method by three values"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Dividing three values
    assert Calculator.division(50, (5, 2)) == 5


def test_calculator_divide_by_zero():
    """Testing division by zero"""
    # pylint: disable=unused-argument, redefined-outer-name

    # Dividing by zero
    assert Calculator.division(5, (0,)) is None
    assert Calculator.division(5, (0, 0)) is None


def test_calculator_last_calculation():
    """Testing getting the last calculation in history"""
    assert Calculator.get_last_calculation() is None
