"""calculator_controller.py"""
from display_component import DisplayComponent


class CalculatorController:
    def __init__(self, model, display, display_var):
        self.model = model
        self.display = display
        self.display_var = display_var

    def handle_input(self, key):
        if key.isdigit() or key in "+-*/.^()":
            self.display.append_to_expression(key)
        elif key == "=":
            expression = self.display.get_expression()
            expression = expression.replace('^', '**')
            result = self.model.evaluate_expression(expression)
            if result is not None:
                self.display.clear()
                self.display.append_to_expression(str(result))
        elif key == "DEL":
            self.display.delete_last()
        elif key == "C":
            self.display.clear()
        # Handle other keys and functions here
        self.display_var.set(self.display.get_expression())
