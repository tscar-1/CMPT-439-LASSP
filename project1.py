import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Define symbolic variable for sympy
x = sp.symbols("x")

# Bisection method
def bisection(x1, x2, delta, flag, func):
    def f_val(val):
        return float(func(val))

    iter = 0

    if func(x1) * func(x2) >= 0:
        raise ValueError("Brackets x1 and x2 are not correct")

    while True:
        iter += 1
        x3 = (x1 + x2) / 2

        if func(x3) == 0:
            break

        if func(x1) * func(x3) < 0:
            x2 = x3
            x4 = x1
        else:
            x1 = x3
            x4 = x2

        if flag == 1:
            error = abs(x3 - x4)
        elif flag == 2:
            error = abs(x3 - x4) / abs(x3)
        else:  # flag 3
            error = abs(func(x3))

        if error < delta:
            root = x3
            break

    return root, iter


# secant method
def secant(x1, x2, delta, flag, func):
    def f_val(val):
        return float(func(val))

    iter = 0

    if abs(func(x1)) < abs(func(x2)):
        x1, x2 = x2, x1  # Swap x1 and x2

    while True:
        iter += 1
        x3 = x2 - (func(x2) * (x1 - x2)) / (func(x1) - func(x2))

        x1 = x2
        x2 = x3

        if func(x3) == 0:
            break

        if flag == 1:
            error = abs(x1 - x2)
        elif flag == 2:
            error = abs(x1 - x2) / abs(x2)
        else:  # flag 3
            error = abs(func(x2))

        if error < delta:
            root = x3
            break

    return x3, iter


# false-position method
def false_position(x1, x2, delta, flag, func):
    def f_val(val):
        return float(func(val))

    iter = 0

    if func(x1) * func(x2) >= 0:
        raise ValueError("Incorrect x1 and x2. Enter new x0, x1: ")
        swap(x2, x3)

    x = x1  # Initialize x to x1

    while True:
        iter += 1

        # Calculate x2 using the false position formula
        x3 = x2 - func(x2) * ((x1 - x2)) / (func(x1) - func(x2))

        if func(x3) == 0:
            break

        if func(x1) * func(x3) < 0:
            x2 = x3
        else:
            x1 = x3

        if flag == 1:
            error = abs(x - x3)
            if abs(x - x3) <= delta:
                root = x3
            else:
                x = x3
        elif flag == 2:
            error = abs((x - x3) / x3)
        else:  # flag 3
            error = abs(func(x3))

        # Stopping Criteria
        if error < delta:
            root = x3
            break

        x = x3

    return root, iter


# newton method
def newton(x0, delta, flag, func, func_prime):
    def f_val(val):
        return float(func(val))

    iter = 0

    while True:
        if func(x0) == 0:
            root = 0

        if func_prime(x0) == 0:
            raise ValueError("Since func_prime(x0) is 0, enter a new x0. ")

        iter += 1
        root = x0

        x1 = x0 - func(x0) / func_prime(x0)  # Use the derivative function
        x0 = x1

        if flag == 1:
            error = abs(x1 - root)
        elif flag == 2:
            error = abs(x1 - root) / abs(x1)
        else:  # flag 3
            error = abs(func(x1))

        if error < delta:
            root = x1
            break
        # print(x0)
    return root, iter


predefined_functions = {
    "Function 1 - 2sin(x) - e^x/4 - 1": 2 * sp.sin(x) - sp.exp(x) / 4 - 1,
    "Function 2 - cos(2x) + sin(3x)": sp.cos(2 * x) + sp.sin(3 * x),
    "Function 3 - e^(cos(2x) + sin(3x)) - 3cos(x) - 2sin(x)": sp.exp(
        sp.cos(2 * x) + sp.sin(3 * x)
    )
    - 3 * sp.cos(x)
    - 2 * sp.sin(x),
    "Function 4 - e^2cos(x) + 3sin(0.5x) - 4": sp.exp(2 * sp.cos(x))
    + 3 * sp.sin(0.5 * x)
    - 4,
    "Function 5 - 4sin(x) - sqrt(x) + ln(2x)": 4 * sp.sin(x)
    - sp.sqrt(x)
    + sp.log(2 * x),
}


# GUI Application
class RootFindingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("THE LASS")
        self.geometry("400x400")

        # Method selection
        self.method_label = tk.Label(self, text="Select Method:")
        self.method_label.pack()
        self.method_var = tk.StringVar(self)
        self.method_var.set("bisection")  # default value
        self.method_menu = tk.OptionMenu(
            self, self.method_var, "bisection", "secant", "false-position", "newton"
        )
        self.method_menu.pack()

        # Flag selection
        self.flag_label = tk.Label(self, text="Select Flag:")
        self.flag_label.pack()
        self.flag_var = tk.StringVar(self)
        self.flag_var.set("1")  # default value
        self.flag_menu = tk.OptionMenu(self, self.flag_var, "1", "2", "3")
        self.flag_menu.pack()

        # Left Bracket Entry
        self.left_bracket_label = tk.Label(self, text="Left Bracket (x0):")
        self.left_bracket_label.pack()
        self.left_bracket_entry = tk.Entry(self)
        self.left_bracket_entry.pack()

        # Right Bracket Entry
        self.right_bracket_label = tk.Label(self, text="Right Bracket (x1):")
        self.right_bracket_label.pack()
        self.right_bracket_entry = tk.Entry(self)
        self.right_bracket_entry.pack()

        # Function selection
        self.function_label = tk.Label(self, text="Select Function:")
        self.function_label.pack()
        self.function_var = tk.StringVar(self)
        self.function_var.set("Function 1")  # default value
        self.function_menu = tk.OptionMenu(
            self, self.function_var, *predefined_functions.keys()
        )
        self.function_menu.pack()

        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.find_root)
        self.submit_button.pack()

        self.method_var.trace("w", self.method_changed)

    def method_changed(self, *args):
        method = self.method_var.get()
        if method == "newton":
            # Hide right bracket entry when Newton method is selected
            self.right_bracket_label.pack_forget()
            self.right_bracket_entry.pack_forget()
        else:
            # Show right bracket entry for all other methods
            self.right_bracket_label.pack()
            self.right_bracket_entry.pack()

    def find_root(self):
        # Get user inputs
        method = self.method_var.get()
        flag = int(self.flag_var.get())
        left_bracket = float(self.left_bracket_entry.get())
        right_bracket = float(self.right_bracket_entry.get())
        selected_function = predefined_functions[self.function_var.get()]

        # Create a lambda function for numerical evaluation
        func = sp.lambdify(x, selected_function, "numpy")
        func_prime = sp.lambdify(x, sp.diff(selected_function, x), "numpy")

        # Call the corresponding method
        if method == "bisection":
            try:
                root, iterations = bisection(
                    left_bracket, right_bracket, 1e-6, flag, func
                )
                messagebox.showinfo(
                    "Result", f"Root is: {root}, and Iteration is: {iterations}"
                )
            except Exception as e:
                messagebox.showerror("Error", str(e))

        elif method == "secant":
            try:
                root, iterations = secant(left_bracket, right_bracket, 1e-6, flag, func)
                messagebox.showinfo(
                    "Result", f"Root is: {root}, and Iteration is: {iterations}"
                )
            except Exception as e:
                messagebox.showerror("Error", str(e))

        elif method == "false-position":
            try:
                root, iterations = false_position(
                    left_bracket, right_bracket, 1e-6, flag, func
                )
                messagebox.showinfo(
                    "Result", f"Root is: {root}, and Iteration is: {iterations}"
                )
            except Exception as e:
                messagebox.showerror("Error", str(e))

        elif method == "newton":
            initial_guess = float(
                self.left_bracket_entry.get()
            )  # Use left_bracket_entry as the initial guess for Newton's method
            try:
                root, iterations = newton(initial_guess, 1e-6, flag, func, func_prime)
                messagebox.showinfo(
                    "Result", f"Root is: {root}, and Iteration is: {iterations}"
                )
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Unknown method selected.")


# Run the application
if __name__ == "__main__":
    app = RootFindingApp()
    app.mainloop()
