"""calculator_model.py"""


class CalculatorModel:
    def __init__(self):
        self.history = []

    def evaluate_expression(self, expression):
        """eval normal expression"""
        try:
            result = eval(expression)
            self.history.append((expression, result))
            return expression, result
        except Exception as e:
            return None

    def clear_history(self):
        """clear history"""
        self.history = []

    def get_history(self):
        """get history"""
        return self.history
