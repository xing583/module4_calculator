from abc import ABC, abstractmethod
from app.operation import Operation


class Calculation(ABC):
    """Abstract base class for calculations."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def get_result(self):
        pass  # pragma: no cover



class AddCalculation(Calculation):
    def get_result(self):
        return Operation.add(self.a, self.b)


class SubtractCalculation(Calculation):
    def get_result(self):
        return Operation.subtract(self.a, self.b)


class MultiplyCalculation(Calculation):
    def get_result(self):
        return Operation.multiply(self.a, self.b)


class DivideCalculation(Calculation):
    def get_result(self):
        return Operation.divide(self.a, self.b)


class CalculationFactory:
    """Factory to create calculation instances based on operation name."""

    @staticmethod
    def create(operation, a, b):
        op = operation.strip().lower()

        if op == "add":
            return AddCalculation(a, b)
        if op == "subtract":
            return SubtractCalculation(a, b)
        if op == "multiply":
            return MultiplyCalculation(a, b)
        if op == "divide":
            return DivideCalculation(a, b)

        raise ValueError(f"Unsupported operation: {operation}")
