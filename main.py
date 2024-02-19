"""main.py: Display the calculator user interface."""
from calculator_ui import CalculatorUI
from calculator_model import CalculatorModel
from display_component import DisplayComponent
from calculator_controller import CalculatorController


if __name__ == '__main__':
    keys_dict = {
        'keys': ['7', '8', '9', '4', '5', '6', '1', '2', '3', '00', '0', '.'],
        'operator': list('*/+-='),
        'operator2': ["CLR", "+/-", "%"],
        'advance': ["(", ")", "^", "mod", "exp", "ln", "log", "log2", "DEL", "sqrt"]
    }
    # injection part
    model = CalculatorModel()
    display = DisplayComponent()
    ui = CalculatorUI(keys_dict, model, display)
    controller = CalculatorController(model, display, ui.display_var, ui)
    ui.controller = controller
    ui.run()


