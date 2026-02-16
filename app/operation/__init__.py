class Operation:
    """Basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        # EAFP：先执行，再处理错误（这里直接抛异常给上层处理）
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
