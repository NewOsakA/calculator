"""calculator_ui.py"""
import tkinter as tk
from tkinter import ttk
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
        self.history_expression_var = tk.StringVar()
        self.history_result_var = tk.StringVar()
        # self.display_frame = self.make_display("0")
        self.controller = CalculatorController(self.model, self.display, self.display_var, self)
        self.init_component()

    def init_component(self):
        """init component"""
        # define
        padding = {"padx": 5, "pady": 5}
        size = {"width": 10, "height": 1}
        option1 = {"font": ("Arial", 30), "bg": "black", "fg": "yellow"}
        option2 = {"font": ("Arial", 15)}
        self.display_var.set("0")

        # display and history
        self.display_frame = tk.Frame(self)
        self.display_label = tk.Label(self.display_frame, height=2, text="0",
                                      textvariable=self.display_var, **option1, anchor=tk.E)
        self.display_label.grid(row=0, column=0, columnspan=3, padx=2, pady=2, sticky=tk.EW)
        self.history1 = ttk.Combobox(self.display_frame, textvariable=self.history_expression_var,
                                     **option2, **size, state="readonly")
        self.history1.grid(row=1, column=0, **padding, sticky=tk.NSEW)
        self.equal = tk.Label(self.display_frame, text="=", **option2)
        self.equal.grid(row=1, column=1, **padding, sticky=tk.NSEW)
        self.history2 = ttk.Combobox(self.display_frame, textvariable=self.history_result_var,
                                     **option2, **size, state="readonly")
        self.history2.grid(row=1, column=2, **padding, sticky=tk.NSEW)

        # button
        group1 = tk.Frame(self)
        key_frame = Keypad(group1, keynames=self.num_pad, columns=3)
        operator_frame = Keypad(self, keynames=self.operator, columns=1)
        operator2_frame = Keypad(group1, keynames=self.operator2, columns=3)
        advance_frame = Keypad(self, keynames=self.advance, columns=2)

        # layout and config
        self.display_frame.grid_columnconfigure(0, weight=1)
        self.display_frame.grid_rowconfigure(0, weight=0)
        self.display_frame.grid(row=0, column=0, columnspan=3, **padding, sticky=tk.NSEW)
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
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("History.TCombobox", fg="blue", bg="lightgray")
        self.history1.config(style="History.TCombobox")

        # bind
        key_frame.bind('<Button>', self.handle_press)
        operator_frame.bind('<Button>', self.handle_press)
        operator2_frame.bind('<Button>', self.handle_press)
        advance_frame.bind('<Button>', self.handle_press)
        self.history1.bind("<<ComboboxSelected>>", lambda event: self.handle_history(event, self.history1))
        self.history2.bind("<<ComboboxSelected>>", lambda event: self.handle_history(event, self.history2))

    def handle_press(self, event):
        """Handle button press"""
        key = event.widget["text"]
        self.controller.handle_input(key)

    def handle_history(self, event, combobox):
        """sync 2 comboboxes together and pass selected history to display"""
        # Sync to the other combobox
        index = combobox.current()
        if combobox == self.history1:
            other_combobox = self.history2
        else:
            other_combobox = self.history1
        other_combobox.current(index)

        # Make it display
        self.display_var.set(combobox.get())
        self.display.clear()
        self.display.append_to_expression(combobox.get())

    def restore_display_color(self):
        """Restore the original color of the display"""
        self.display_label.config(fg="yellow")

    def update_history_comboboxes(self):
        """Update values in history comboboxes"""
        self.history1['values'] = [i[0] for i in self.model.get_history()]
        self.history2['values'] = [i[1] for i in self.model.get_history()]

    def run(self):
        """run the script"""
        self.mainloop()
