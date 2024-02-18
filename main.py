"""Display the calculator user interface."""
from calculator_ui import CalculatorUI


if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    keys = list('789456123 0.')
    operator = list('*/+-^=')
    operator2 = ["C", "+/-", "%"]
    advance = ["(", ")", "exp", "ln", "log", "log2", "sqrt"]
    ui = CalculatorUI(keys, operator, operator2, advance)
    ui.run()


