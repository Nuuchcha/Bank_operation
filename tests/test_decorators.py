import os.path
import sys

from src.decorators import log


def test_log_division_zero_in_file() -> None:
    """Тестирование декоратора на вывод в файл ошибки выполнения функции"""

    @log('my_log.log')
    def my_function(x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif not (type(x), type(y) in (int, float)):
            raise TypeError("Value must be an integer or float")
        else:
            return x / y

    my_function(2, 0)
    with open('my_log.log', 'r', encoding='utf-8') as f:
        assert f.readlines()[-1][-77:] == ("my_function error: Cannot divide by zero. Inputs: (2, 0), {} | Time: 0:00:00\n")


def test_log_positive_in_file() -> None:
    """Тестирование декоратора на вывод в файл положительного выполнения функции"""

    @log('my_log.log')
    def my_function(x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif not (type(x), type(y) in (int, float)):
            raise TypeError("Value must be an integer or float")
        else:
            return x / y

    my_function(2, 3)
    with open('my_log.log', 'r', encoding='utf-8') as f:
        assert f.readlines()[-1][-32:] == ("my_function ok | Time: 0:00:00\n")


def test_log_negative_zero_in_console(capsys) -> None:
    """Тестирование декоратора на вывод ошибки выполнения функции в консоль"""

    @log()
    def my_function(x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif not (type(x), type(y) in (int, float)):
            raise TypeError("Value must be an integer or float")
        else:
            return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert "my_function error: Cannot divide by zero" in captured.out


def test_log_positive_in_console(capsys) -> None:
    """Тестирование декоратора на вывод положительного выполнения функции в консоль"""

    @log()
    def my_function(x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif not (type(x), type(y) in (int, float)):
            raise TypeError("Value must be an integer or float")
        else:
            return x / y

    my_function(2, 3)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out
