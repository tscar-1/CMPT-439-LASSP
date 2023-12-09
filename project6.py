import tkinter as tk
from tkinter import messagebox
import sympy as sp

x = sp.symbols("x")


def goldenSectionmin(a, b, func):
    gs = 1.618
    delta = 0.000001
    iter = 0
    x1 = b - ((b - a) / gs)
    x2 = a + ((b - a) / gs)
    y1 = func(x1)
    y2 = func(x2)

    while abs(b - a) > delta:
        iter += 1
        if y1 >= y2:
            a = x1
            x1 = x2
            x2 = a + ((b - a) / gs)
            y1 = func(x1)
            y2 = func(x2)
        else:
            b = x2
            x2 = x1
            x1 = b - ((b - a) / gs)
            y1 = func(x1)
            y2 = func(x2)

    x_min = (a + b) / 2
    f_min = func(x_min)
    return x_min, f_min, iter


def goldenSectionmax(a, b, func):
    gs = 1.618
    delta = 0.000001
    iter = 0
    x1 = b - ((b - a) / gs)
    x2 = a + ((b - a) / gs)
    y1 = func(x1)
    y2 = func(x2)

    while abs(b - a) > delta:
        iter += 1
        if y1 <= y2:
            a = x1
            x1 = x2
            x2 = a + ((b - a) / gs)
            y1 = func(x1)
            y2 = func(x2)
        else:
            b = x2
            x2 = x1
            x1 = b - ((b - a) / gs)
            y1 = func(x1)
            y2 = func(x2)

    x_max = (a + b) / 2
    f_max = func(x_max)
    return x_max, f_max, iter


def newton_method(x0, func, func_prime, func_prime2):
    delta = 0.000001
    iter = 0
    while True:
        iter += 1
        x_prime_value = func_prime(x0)
        x_prime2_value = func_prime2(x0)
        if x_prime2_value == 0:
            raise ValueError("Newton's method fails.")
        x1 = x0 - x_prime_value / x_prime2_value
        if abs(x1 - x0) < delta:
            break
        x0 = x1

    f_min = func(x0)
    return x0, f_min, iter


predefined_functions = {
    "Function 1: x^3 -4x": (x**3) - (4 * x),
    "Function 2: -sin(x) + cos(x^2)": -sp.sin(x) + sp.cos(x**2),
}


class FindingMinMax(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("THE LASS")
        self.geometry("400x400")

        self.method_label = tk.Label(self, text="Select Method:")
        self.method_label.grid(row=0, column=0, sticky="e")
        self.method_var = tk.StringVar(self)
        self.method_var.set("golden Section min")
        self.method_menu = tk.OptionMenu(
            self,
            self.method_var,
            "golden section min",
            "golden section max",
            "newton min",
            "newton max",
        )
        self.method_menu.grid(row=0, column=1)

        self.left_bracket_label = tk.Label(self, text="Left Bracket (x0):")
        self.left_bracket_label.grid(row=1, column=0, sticky="e")
        self.left_bracket_entry = tk.Entry(self)
        self.left_bracket_entry.grid(row=1, column=1)

        self.right_bracket_label = tk.Label(self, text="Right Bracket (x1):")
        self.right_bracket_label.grid(row=2, column=0, sticky="e")
        self.right_bracket_entry = tk.Entry(self)
        self.right_bracket_entry.grid(row=2, column=1)

        self.function_label = tk.Label(self, text="Select Function:")
        self.function_label.grid(row=3, column=0, sticky="e")
        self.function_var = tk.StringVar(self)
        self.function_var.set("Function 1")
        self.function_menu = tk.OptionMenu(
            self, self.function_var, *predefined_functions.keys()
        )
        self.function_menu.grid(row=3, column=1, sticky="w")

        self.submit_button = tk.Button(self, text="Submit", command=self.find_min)
        self.submit_button.grid(row=4, column=0, columnspan=2)

        self.method_var.trace("w", self.method_changed)

        self.mainloop()

    def method_changed(self, *args):
        method = self.method_var.get()
        if "newton" in method.lower():
            self.right_bracket_label.grid_remove()
            self.right_bracket_entry.grid_remove()
        else:
            self.right_bracket_label.grid()
            self.right_bracket_entry.grid()

    def find_min(self):
        # Initialize variables to None or some default value
        x_result = None
        f_result = None
        iter_result = 0
        try:
            method = self.method_var.get()
            left_bracket = float(self.left_bracket_entry.get())
            right_bracket = (
                float(self.right_bracket_entry.get())
                if self.right_bracket_entry.get() and "newton" not in method.lower()
                else None
            )
            selected_function = predefined_functions[self.function_var.get()]

            func = sp.lambdify(x, selected_function, "numpy")
            func_prime = sp.lambdify(x, sp.diff(selected_function, x), "numpy")
            func_prime2 = sp.lambdify(
                x, sp.diff(sp.diff(selected_function, x), x), "numpy"
            )

            if method == "golden section min":
                x_result, f_result, iter_result = goldenSectionmin(
                    left_bracket, right_bracket, func
                )
            elif method == "golden section max":
                x_result, f_result, iter_result = goldenSectionmax(
                    left_bracket, right_bracket, func
                )
            elif method == "newton min":
                if left_bracket is not None:
                    x_result, f_result, iter_result = newton_method(
                        left_bracket, func, func_prime, func_prime2
                    )
                else:
                    raise ValueError(
                        "Please enter a valid initial guess for Newton's method."
                    )
            elif method == "newton max":
                if left_bracket is not None:
                    x_result, f_result, iter_result = newton_method(
                        left_bracket, func, func_prime, func_prime2
                    )
                else:
                    raise ValueError(
                        "Please enter a valid initial guess for Newton's method."
                    )
            else:
                raise ValueError("Invalid method selected.")

            if x_result is not None and f_result is not None:
                messagebox.showinfo(
                    "Result",
                    f"x = {x_result}, f(x) = {f_result}, iterations = {iter_result}",
                )
            else:
                messagebox.showwarning("Result", "No result was calculated.")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Instantiate the class to run the program
FindingMinMax()
