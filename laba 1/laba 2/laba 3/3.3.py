class Calculator:
    def __init__(self):
        self._expression = ""

    def set_expression(self, new_expression):
        self._expression = new_expression

    def append_symbol(self, symbol):
        self._expression += symbol

    def get_expression(self):
        return self._expression

    def get_last_symbol(self):
        if self._expression:
            return self._expression[-1]
        return None

    def remove_last_symbol(self):
        if self._expression:
            self._expression = self._expression[:-1]

if __name__ == "__main__":
    calc = Calculator()

    # Test cases
    calc.set_expression("10-5")
    print("Текущее выражение:", calc.get_expression())

    calc.append_symbol("=")
    print("Следующее выражение '=':", calc.get_expression())

    calc.append_symbol("5")
    print("Следующее выражение '5':", calc.get_expression())

    print("Последний символ:", calc.get_last_symbol())

    calc.remove_last_symbol()
    print("После удаления последнего символа:", calc.get_expression())