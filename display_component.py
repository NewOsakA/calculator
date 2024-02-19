"""display_component.py"""


class DisplayComponent:
    def __init__(self):
        self.expression = "0"
        self.last_input = None

    def append_to_expression(self, value):
        # Update last input state based on the type of input
        if value.isdigit():
            self.last_input = "operand"
        elif value in "+-*/.":
            self.last_input = "operator"
        else:
            self.last_input = "function"

        # Append the value to the expression
        if self.expression == "0":
            self.expression = value
        else:
            self.expression += value

    def delete_last(self):
        if self.last_input == "function":
            # Find the index of the last occurrence of a function
            last_function_index = max(
                self.expression.rfind(func) for func in ["sqrt(", "log10(", "log2(", "ln(", "exp(", "mod"]
            )
            if last_function_index != -1:
                # Remove the function and update last_input
                self.expression = self.expression[:last_function_index]
                if not self.expression:
                    self.expression = "0"
                    self.last_input = None
                else:
                    self.last_input = "operator" if self.expression[-1] in "+-*/^" else "operand"
            else:
                # If there are no more functions, reset the expression
                self.expression = "0"
                self.last_input = None

        elif self.expression:
            self.expression = self.expression[:-1]
            if not self.expression:
                self.expression = "0"
                self.last_input = None
            else:
                if self.expression[-1].isdigit():
                    self.last_input = "operand"
                elif self.expression[-1] in "+-*/.^()":
                    self.last_input = "operator"
                else:
                    self.last_input = "function"

    def clear(self):
        self.expression = "0"
        self.last_input = None

    def get_expression(self):
        return self.expression
