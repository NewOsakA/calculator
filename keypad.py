"""keypad.py"""
import tkinter as tk


class Keypad(tk.Frame):
    """construct keypad that can configure"""
    def __init__(self, parent, keynames=None, columns=1, button_width=1, button_height=2, **kwargs):
        super().__init__()
        if keynames is None:
            keynames = []
        self.keynames = keynames
        self.buttons = []
        self.button_width = button_width
        self.button_height = button_height
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list"""
        for i, key in enumerate(self.keynames):
            col = i % columns
            row = i // columns
            button = tk.Button(self, text=key, width=self.button_width, height=self.button_height)
            button.grid(row=row + 1, column=col + 1, padx=5, pady=5, sticky=tk.NSEW)
            self.grid_columnconfigure(col + 1, weight=1)
            self.grid_rowconfigure(row + 1, weight=1)
            self.buttons.append(button)

    def bind(self, sequence, func, add=None):
        """Bind an event handler to an event sequence."""
        for button in self.buttons:
            button.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons using dictionary syntax."""
        if key == 'font':
            self.configure(font=value)
        else:
            super().__setitem__(key, value)

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values from buttons."""
        values = set()
        for button in self.buttons:
            values.add(button.cget(key))

        if len(values) == 1:
            return values.pop()
        raise ValueError

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons."""
        font = kwargs.pop('font', None)
        fg = kwargs.pop('fg', None)
        super().configure(cnf, **kwargs)
        for button in self.buttons:
            if font:
                button.configure(font=font)
            if fg:
                button.configure(fg=fg)

    @property
    def frame(self):
        """returns a reference to  the superclass object for this keypad"""
        return self
