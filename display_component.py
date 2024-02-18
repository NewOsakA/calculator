"""display_component.py"""


class DisplayComponent:
    def __init__(self):
        self.expression = "0"

    def append_to_expression(self, value):
        if self.expression == "0":
            self.expression = value
        else:
            self.expression += value

    def delete_last(self):
        if self.expression:
            self.expression = self.expression[:-1]
            # If the expression becomes empty after deletion, set it to "0"
            if not self.expression:
                self.expression = "0"

    def clear(self):
        self.expression = "0"

    def get_expression(self):
        return self.expression
