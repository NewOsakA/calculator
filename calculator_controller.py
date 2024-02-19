"""calculator_controller.py"""
import math
import pygame


class CalculatorController:
    """handle the user input"""
    def __init__(self, model, display, display_var, ui):
        self.model = model
        self.display = display
        self.display_var = display_var
        self.ui = ui
        self.last_input = ""

    def handle_input(self, key):
        """handle the user input case by case"""
        if key.isdigit():
            self.display.append_to_expression(key)
            self.display.last_input = "operand"
        elif key in "+-*/.^()":
            self.display.append_to_expression(key)
            self.display.last_input = "operator"
        elif key == "=":
            expression = self.display.get_expression()
            expression = expression.replace('^', '**')
            original = expression
            if "sqrt" in expression:
                expression = expression.replace("sqrt", "math.sqrt")
                result = eval(expression)
                self.model.history.append((original, result))
            elif "log10" in expression:
                expression = expression.replace("log10", "math.log10")
                result = eval(expression)
                self.model.history.append((original, result))
            elif "log2" in expression:
                expression = expression.replace("log2", "math.log2")
                result = eval(expression)
                self.model.history.append((original, result))
            elif "ln" in expression:
                expression = expression.replace("ln", "math.log")
                result = eval(expression)
                self.model.history.append((original, result))
            elif "exp" in expression:
                expression = expression.replace("exp", "math.exp")
                result = eval(expression)
                self.model.history.append((original, result))
            elif "mod" in expression:
                expression = expression.replace("mod", "%")
                result = eval(expression)
                self.model.history.append((original, result))
            else:
                result = self.model.evaluate_expression(expression)

            if result is not None:
                self.display.clear()
                self.display.append_to_expression(str(result))

            self.display.last_input = "operand"

            # Check if the expression was valid
            if result is None:
                # Change the color of the display and play the error sound
                self.play_sound()
                self.ui.display_label.config(fg="red")
                self.ui.after(2000, self.ui.restore_display_color)
            else:
                # Update history expression and result
                self.ui.history_expression_var.set(self.model.history[-1][0])
                self.ui.history_result_var.set(self.model.history[-1][-1])
                # Update the display
                self.display.clear()
                if type(result) == tuple:
                    self.display.append_to_expression(str(result[1]))
                else:
                    self.display.append_to_expression(str(result))
                self.ui.update_history_comboboxes()

        elif key == "DEL":  # delete button
            self.display.delete_last()
        elif key == "CLR":  # clear button
            self.display.clear()
        elif key == "+/-":  # operate toggle + or -
            current = self.display.get_expression()
            if current and current[0] == '-':
                current = current[1:]
            else:
                current = '-' + current
            self.display.clear()
            self.display.append_to_expression(current)

        elif key == "%":  # Percentage button
            current = self.display.get_expression()
            try:
                result = float(current) / 100
            except ValueError:
                result = None
            if result is not None:
                self.display.clear()
                self.display.append_to_expression(str(result))

        elif key == "sqrt":  # Square root button
            if self.display.last_input == "operand":
                self.display.expression = "sqrt(" + self.display.expression + ")"
                self.display.last_input = "function"
            else:
                self.display.append_to_expression("sqrt(")

        elif key == "log":  # Logarithm Base 10 button
            if self.display.last_input == "operand":
                self.display.expression = "log10(" + self.display.expression + ")"
                self.display.last_input = "function"
            else:
                self.display.append_to_expression("log10(")

        elif key == "log2":  # Logarithm base 2 button
            if self.display.last_input == "operand":
                self.display.expression = "log2(" + self.display.expression + ")"
                self.display.last_input = "function"
            else:
                self.display.append_to_expression("log2(")

        elif key == "ln":  # Natural logarithm button
            if self.display.last_input == "operand":
                self.display.expression = "ln(" + self.display.expression + ")"
                self.display.last_input = "function"
            else:
                self.display.append_to_expression("ln(")

        elif key == "exp":  # Exponential function button
            if self.display.last_input == "operand":
                self.display.expression = "exp(" + self.display.expression + ")"
                self.display.last_input = "function"
            else:
                self.display.append_to_expression("exp(")

        elif key == "mod":  # Modulo button
            if self.display.last_input == "operand":
                self.display.append_to_expression("mod")
                self.display.last_input = "function"
            else:
                self.display.append_to_expression("mod")

        self.display_var.set(self.display.get_expression())

    def play_sound(self):
        """play an error sound effect"""
        pygame.mixer.init()
        pygame.mixer.music.load("error_sound.wav")
        pygame.mixer.music.play()
