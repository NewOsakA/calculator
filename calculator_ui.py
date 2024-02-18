import tkinter as tk
from keypad import Keypad
from calculator_model import CalculatorModel
from display_component import DisplayComponent
from calculator_controller import CalculatorController


class CalculatorUI(tk.Tk):
    """Calculator UI"""
    def __init__(self, num_pad, operator_pad, operator_pad2, advance_pad):
        super().__init__()
        self.title("Calculator")
        self.num_pad = num_pad
        self.operator = operator_pad
        self.operator2 = operator_pad2
        self.advance = advance_pad

        self.model = CalculatorModel()
        self.display = DisplayComponent()
        self.display_var = tk.StringVar()
        self.controller = CalculatorController(self.model, self.display, self.display_var)
        self.init_component()
        self.display_var.set("0")

    def init_component(self):
        """init component"""
        # define
        padding = {"padx": 5, "pady": 5}
        self.display = self.make_display("0")
        group1 = tk.Frame(self)

        key_frame = Keypad(group1, keynames=self.num_pad, columns=3)
        operator_frame = Keypad(self, keynames=self.operator, columns=1)
        operator2_frame = Keypad(group1, keynames=self.operator2, columns=3)
        advance_frame = Keypad(self, keynames=self.advance, columns=1)

        # layout and config
        self.display.grid(row=0, column=0, columnspan=3, **padding, sticky=tk.NSEW)
        key_frame.grid(row=2, column=0, **padding, sticky=tk.NSEW)
        operator_frame.grid(row=1, column=1, **padding, sticky=tk.NSEW, rowspan=2)
        operator2_frame.grid(row=1, column=0, **padding, sticky=tk.NSEW)
        group1.grid(row=1, column=0, **padding, sticky=tk.NSEW)
        advance_frame.grid(row=1, column=2, **padding, sticky=tk.NSEW, rowspan=2)

        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        key_frame["font"] = ("Monospace", 16)
        operator_frame["font"] = ("Monospace", 16)
        operator2_frame["font"] = ("Monospace", 16)
        advance_frame["font"] = ("Monospace", 16)
        key_frame.frame.configure(bg="gray", fg="green")
        operator_frame.frame.configure(bg="gray", fg="blue")
        operator2_frame.frame.configure(bg="gray", fg="blue")
        advance_frame.frame.configure(bg="gray", fg="blue")

        # bind
        key_frame.bind('<Button>', self.handle_press)
        operator_frame.bind('<Button>', self.handle_press)
        operator2_frame.bind('<Button>', self.handle_press)
        advance_frame.bind('<Button>', self.handle_press)


    def make_display(self, text):
        """make display flied"""
        frame = tk.Frame(self)
        option = {"font": ("Arial", 30), "bg": "black", "fg": "yellow"}
        display = tk.Label(frame, height=2, text=text, textvariable=self.display_var, **option, anchor=tk.E)
        display.grid(row=0, column=0, padx=2, pady=2, sticky=tk.EW)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=0)

        return frame

    def handle_press(self, event):
        """Handle button press"""
        key = event.widget["text"]
        print("Pressed key:", key)
        self.controller.handle_input(key)

    def run(self):
        """run the script"""
        self.mainloop()
