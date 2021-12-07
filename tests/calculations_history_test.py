""" Imports calculations class """
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction


@pytest.fixture
def fixture_clear_history():
    """Function runs each time a test method runs"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


def test_calculations_history_static_property(fixture_clear_history):
    """Testing the number of calculations in the history"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Add calculations to history
    addition = Addition(1, (1,))
    subtraction = Subtraction(2, (1, ))
    Calculations.add_history(addition)
    Calculations.add_history(subtraction)
    assert Calculations.count_history() == 2


def test_calculations_get_first_element_in_history(fixture_clear_history):
    """Testing getting the first result from the history"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Add calculations to history
    addition = Addition(1, (1,))
    subtraction = Subtraction(2, (1,))
    Calculations.add_history(addition)
    Calculations.add_history(subtraction)
    assert Calculations.get_first_calculation() == 2


def test_calculator_get_last_element_in_history(fixture_clear_history):
    """Testing getting the last result from the history"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Add calculations to history
    addition = Addition(1, (1,))
    subtraction = Subtraction(2, (1,))
    Calculations.add_history(addition)
    Calculations.add_history(subtraction)
    assert Calculations.get_last_calculation() == 1


def test_calculator_delete_history(fixture_clear_history):
    """Testing deleting an item in the history"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Add calculations to history
    addition = Addition(1, (1,))
    subtraction = Subtraction(2, (1,))
    Calculations.add_history(addition)
    Calculations.add_history(subtraction)
    Calculations.delete_history(0)
    # Checking that the element index went from index 1 to index 0
    assert Calculations.history[0].get_result() == 1


def test_calculator_clear_history(fixture_clear_history):
    """Testing clearing the history"""
    # pylint: disable=unused-argument, redefined-outer-name
    # Add calculations to history
    addition = Addition(1, (1,))
    subtraction = Subtraction(2, (1,))
    Calculations.add_history(addition)
    Calculations.add_history(subtraction)
    Calculations.clear_history()
    assert True
