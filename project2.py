import tkinter as tk
from tkinter import messagebox, Entry, Label, StringVar, Button
import numpy as np


class GaussAndJordan(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("THE LASSP")
        self.geometry("400x400")

        # Method selection
        self.method_label = Label(self, text="Select Method:")
        self.method_label.grid(row=0, column=0, sticky="e")
        self.method_var = StringVar(self)
        self.method_var.set("Gauss Elimination")  # set default value
        self.method_menu = tk.OptionMenu(
            self, self.method_var, "Gauss Elimination", "Gauss-Jordan Elimination"
        )
        self.method_menu.grid(row=0, column=1)

        # Submit Button
        self.submit_button = Button(self, text="Submit", command=self.show_matrix_input)
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def show_matrix_input(self):
        method = self.method_var.get()
        equation_count_window = EquationCountWindow(self, method)
        self.wait_window(equation_count_window)

        if equation_count_window.equation_count is not None:
            matrix_input_window = MatrixInputWindow(
                self, method, equation_count_window.equation_count
            )
            self.wait_window(matrix_input_window)

            if matrix_input_window.matrix is not None:
                matrix = matrix_input_window.matrix
                solutions = self.solve(method, matrix)
                SolutionWindow(self, solutions)

    def solve(self, method, matrix):
        if method == "Gauss Elimination":
            return gauss_elimination(matrix)
        elif method == "Gauss-Jordan Elimination":
            return gauss_jordan_elimination(matrix)

        # Default case, return empty list
        return []


class EquationCountWindow(tk.Toplevel):
    def __init__(self, parent, method):
        super().__init__(parent)

        self.title("Enter Equation Count")
        self.geometry("200x100")

        self.equation_count = None

        self.label = Label(self, text="Enter the number of equations:")
        self.label.pack()

        self.entry_var = StringVar(self)
        self.entry = Entry(self, textvariable=self.entry_var)
        self.entry.pack()

        self.submit_button = Button(
            self, text="Submit", command=self.submit_equation_count
        )
        self.submit_button.pack()

        self.method = method

    def submit_equation_count(self):
        try:
            self.equation_count = int(self.entry_var.get())
            if self.equation_count > 0:
                self.destroy()
            else:
                messagebox.showerror("Error", "Please enter a valid positive integer.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer.")


class MatrixInputWindow(tk.Toplevel):
    def __init__(self, parent, method, equation_count):
        super().__init__(parent)

        self.title("Matrix Input")
        self.geometry("400x400")

        self.method = method
        self.equation_count = equation_count

        self.matrix = None

        self.entry_vars = []

        for i in range(equation_count):
            row_vars = []
            for j in range(equation_count + 1):
                var = StringVar(self)
                entry = Entry(self, textvariable=var)
                entry.grid(row=i, column=j)
                row_vars.append(var)
            self.entry_vars.append(row_vars)

        self.submit_button = Button(self, text="Submit", command=self.submit_matrix)
        self.submit_button.grid(
            row=equation_count, column=0, columnspan=equation_count + 1
        )

    def submit_matrix(self):
        self.matrix = np.zeros(
            (self.equation_count, self.equation_count + 1), dtype=float
        )
        for i in range(self.equation_count):
            for j in range(self.equation_count + 1):
                value = self.entry_vars[i][j].get().strip()
                if value:
                    try:
                        self.matrix[i][j] = float(value)
                    except ValueError:
                        messagebox.showerror(
                            "Error", "Please enter valid numbers in each field."
                        )
                        return
                else:
                    messagebox.showerror(
                        "Error", "Please enter a value for all matrix elements."
                    )
                    return
        self.destroy()


class SolutionWindow(tk.Toplevel):
    def __init__(self, parent, solutions):
        super().__init__(parent)

        self.title("Solution")
        self.geometry("200x150")

        label = Label(self, text="Solutions:")
        label.pack()

        for i, solution in enumerate(solutions):
            label = Label(self, text=f"x{i + 1} = {solution}")
            label.pack()


def gauss_elimination(matrix):
    n = len(matrix)
    solutions = [0] * n

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    for i in range(n - 1, -1, -1):
        sum_val = sum(matrix[i][j] * solutions[j] for j in range(i + 1, n))
        solutions[i] = (matrix[i][n] - sum_val) / matrix[i][i]

    return solutions


def gauss_jordan_elimination(matrix):
    n = len(matrix)
    solutions = [0] * n

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j

        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        pivot_val = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot_val

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i):
            ratio = matrix[j][i]
            for k in range(i, n + 1):
                matrix[j][k] -= ratio * matrix[i][k]

    solutions = [matrix[i][n] for i in range(n)]

    return solutions


if __name__ == "__main__":
    app = GaussAndJordan()
    app.mainloop()
