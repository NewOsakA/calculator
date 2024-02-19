"""main.py: Display the calculator user interface."""
from calculator_ui import CalculatorUI


if __name__ == '__main__':
    keys = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '00', '0', '.']
    operator = list('*/+-=')
    operator2 = ["CLR", "+/-", "%"]
    advance = ["(", ")", "^", "mod", "exp", "ln", "log", "log2", "DEL", "sqrt"]
    ui = CalculatorUI(keys, operator, operator2, advance)
    ui.run()


