"""
Program kalkulatora z podstawowymi operacjami arytmetycznymi.
"""


class Calculator:
    """Prosty kalkulator, który obsługuje dwa operandy numeryczne."""

    def __init__(self, op1: float, op2: float) -> None:
        """Inicjalizacja dwóch operandów."""
        self.__op1 = float(op1)
        self.__op2 = float(op2)

    def sum(self) -> float:
        """Zwraca sumę dwóch operandów."""
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        """Zwraca różnicę dwóch operandów (op1 - op2)."""
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        """Zwraca iloczyn dwóch operandów."""
        return self.__op1 * self.__op2

    def divide(self) -> float:
        """Zwraca wynik dzielenia (op1 / op2)."""
        if self.__op2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero.")
        return self.__op1 / self.__op2

if __name__ == "__main__":
    calc = Calculator(10, 5)

    print("Sum:", calc.sum())
    print("Subtract:", calc.subtract())
    print("Multiply:", calc.multiply())
    print("Divide:", calc.divide())
