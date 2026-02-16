import pytest
from app.calculation import (
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    CalculationFactory,
)


@pytest.mark.parametrize("cls,a,b,result", [
    (AddCalculation, 1, 2, 3),
    (SubtractCalculation, 5, 2, 3),
    (MultiplyCalculation, 2, 3, 6),
    (DivideCalculation, 6, 3, 2),
])
def test_calculation_classes(cls, a, b, result):
    calc = cls(a, b)
    assert calc.get_result() == result


@pytest.mark.parametrize("op,cls", [
    ("add", AddCalculation),
    ("subtract", SubtractCalculation),
    ("multiply", MultiplyCalculation),
    ("divide", DivideCalculation),
])
def test_factory(op, cls):
    calc = CalculationFactory.create(op, 1, 1)
    assert isinstance(calc, cls)


def test_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("invalid", 1, 2)
