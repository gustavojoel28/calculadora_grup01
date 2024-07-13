
import pytest
from src.calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(3, 2) == 5
    assert sumar(10, 0) == 10
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(3, 2) == 1
    assert restar(10, 5) == 5
    assert restar(0, 0) == 0

def test_multiplicar():
    assert multiplicar(3, 2) == 6
    assert multiplicar(10, 0) == 0
    assert multiplicar(0, 0) == 0

def test_dividir():
    assert dividir(4, 2) == 2
    assert dividir(9, 3) == 3
    with pytest.raises(ValueError):
        dividir(10, 0)
