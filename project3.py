import tkinter as tk
from tkinter import messagebox, Entry, StringVar, Button, Toplevel
import numpy as np
import math


def gaussSeidel(augMtx, delta, flag):
    n = len(augMtx)  # gets row size of augmented matrix
    prevSoln = np.zeros(
        n
    )  # initialization of starting approximation vector (set to [0, 0, 0] by default)
    currSoln = np.zeros(n)  # initialization of solution vector

    # loop runs until specified stopping criteria is reached
    while True:
        mae = 0  # initialization of the mean absolute error
        rmse = 0  # initialization of the root mean square error

        # loop through the coefficients in each equation
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += (
                        augMtx[i][j] * currSoln[j]
                    )  # use the values from the current solution to compute the sum
            currSoln[i] = (augMtx[i][n] - sum) / augMtx[i][
                i
            ]  # computes the new approximation

        # computes errors based on current and previous approximations
        for i in range(n):
            mae += abs(currSoln[i] - prevSoln[i])
            rmse += math.pow(currSoln[i] - prevSoln[i], 2)

        if flag == 1:  # approximate mean absolute error
            if mae / n < delta:
                return currSoln
        elif flag == 2:  # approximate root mean square error
            if np.sqrt(rmse / n) < delta:
                return currSoln
        elif flag == 3:  # true mean absolute error
            if mae < delta:
                return currSoln
        elif flag == 4:  # true root mean square error
            if np.sqrt(rmse) < delta:
                return currSoln

        # copies the current solution to the previous solution for the next iteration
        prevSoln = np.copy(currSoln)


def jacobi(augMtx, delta, flag):
    n = len(augMtx)  # gets row size of augmented matrix
    prevSoln = np.zeros(
        n
    )  # initialization of starting approximation vector (set to [0, 0, 0] by default)
    currSoln = np.zeros(n)  # initialization of solution vector

    # loop runs until specified stopping criteria is reached
    while True:
        mae = 0  # initialization of the mean absolute error
        rmse = 0  # initialization of the root mean square error

        # loop through the coefficients in each equation
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += (
                        augMtx[i][j] * prevSoln[j]
                    )  # use the values from the previous solution to compute the sum
            currSoln[i] = (augMtx[i][n] - sum) / augMtx[i][
                i
            ]  # computes the new approximation

        # computes errors based on current and previous approximations
        for i in range(n):
            mae += abs(currSoln[i] - prevSoln[i])
            rmse += math.pow(currSoln[i] - prevSoln[i], 2)

        if flag == 1:  # approximate mean absolute error
            if mae / n < delta:
                return currSoln
        elif flag == 2:  # approximate root mean square error
            if math.sqrt(rmse / n) < delta:
                return currSoln
        elif flag == 3:  # true mean absolute error
            if mae < delta:
                return currSoln
        elif flag == 4:  # true root mean square error
            if math.sqrt(rmse) < delta:
                return currSoln

        # copies the current solution to the previous solution for the next iteration
        prevSoln = np.copy(currSoln)


class MatrixInputWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Matrix Input")
        self.geometry("400x400")

        self.matrix_size = None
        self.matrix = None

        self.size_label = tk.Label(self, text="Enter the number of equations:")
        self.size_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.size_entry = Entry(self)
        self.size_entry.grid(row=1, column=0, columnspan=2, pady=5)

        self.submit_size_button = Button(self, text="Submit", command=self.submit_size)
        self.submit_size_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.entry_vars = []

    def submit_size(self):
        try:
            self.matrix_size = int(self.size_entry.get())
            if self.matrix_size <= 0:
                messagebox.showerror(
                    "Error", "Please enter a valid size greater than 0."
                )
                return

            for i in range(self.matrix_size):
                row_vars = []
                for j in range(self.matrix_size + 1):
                    var = StringVar(self)
                    entry = Entry(self, textvariable=var)
                    entry.grid(row=i + 3, column=j)
                    row_vars.append(var)
                self.entry_vars.append(row_vars)

            self.submit_matrix_button = Button(
                self, text="Submit Matrix", command=self.submit_matrix
            )
            self.submit_matrix_button.grid(
                row=self.matrix_size + 3,
                column=0,
                columnspan=self.matrix_size + 1,
                pady=10,
            )

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the size.")

    def submit_matrix(self):
        try:
            self.matrix = np.zeros(
                (self.matrix_size, self.matrix_size + 1), dtype=float
            )
            for i in range(self.matrix_size):
                for j in range(self.matrix_size + 1):
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

        except Exception as e:
            messagebox.showerror("Error", str(e))


class IterativeMethodsGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Iterative Methods")
        self.geometry("400x300")

        # Additional inputs
        self.delta_label = tk.Label(self, text="Enter the delta value:")
        self.delta_label.grid(row=0, column=0, pady=5)
        self.delta_entry = tk.Entry(self)
        self.delta_entry.grid(row=0, column=1, pady=5)

        self.stopping_criteria_var = tk.StringVar()
        self.stopping_criteria_var.set("Approximate Mean Absolute Error")
        self.stopping_criteria_label = tk.Label(self, text="Select Stopping Criteria:")
        self.stopping_criteria_label.grid(row=1, column=0, pady=5)
        self.stopping_criteria_menu = tk.OptionMenu(
            self,
            self.stopping_criteria_var,
            "Approximate Mean Absolute Error",
            "Approximate Root Mean Square Error",
            "True Mean Absolute Error",
            "True Root Mean Square Error",
        )
        self.stopping_criteria_menu.grid(row=1, column=1, pady=5)

        # Method selection
        self.method_var = tk.StringVar(self)
        self.method_var.set("Gauss-Seidel")  # set default value
        self.method_label = tk.Label(self, text="Select Method:")
        self.method_label.grid(row=2, column=0, pady=5)
        self.method_menu = tk.OptionMenu(
            self, self.method_var, "Gauss-Seidel", "Jacobi"
        )
        self.method_menu.grid(row=2, column=1, pady=5)

        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.execute)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Variables to store user input
        self.matrix_values = None

    def get_matrix_values_popup(self):
        matrix_input_window = MatrixInputWindow(self)
        self.wait_window(matrix_input_window)

        if matrix_input_window.matrix is not None:
            matrix_values = matrix_input_window.matrix
            messagebox.showinfo("Matrix Input", "Matrix values entered successfully.")
            return matrix_values
        else:
            return None

    def execute(self):
        try:
            delta = float(self.delta_entry.get())
            stopping_criteria = self.stopping_criteria_var.get()
            method = self.method_var.get()

            # Get matrix values through pop-up window
            matrix_values = self.get_matrix_values_popup()

            if matrix_values is None:
                messagebox.showerror("Error", "Matrix values are not entered.")
                return

            # Create a matrix with user-provided values
            aug_matrix = np.array(matrix_values)

            if method == "Gauss-Seidel":
                result = gaussSeidel(aug_matrix, delta, 1)
                result_str = ", ".join(
                    [f"x{i+1} = {result[i]:.4f}" for i in range(len(result))]
                )
                messagebox.showinfo(
                    "Result",
                    f"Gauss-Seidel solution using {stopping_criteria}: {result_str}",
                )
            elif method == "Jacobi":
                result = jacobi(aug_matrix, delta, 1)
                result_str = ", ".join(
                    [f"x{i+1} = {result[i]:.4f}" for i in range(len(result))]
                )
                messagebox.showinfo(
                    "Result", f"Jacobi solution using {stopping_criteria}: {result_str}"
                )
            else:
                messagebox.showerror("Error", "Invalid method selected.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = IterativeMethodsGUI()
    app.mainloop()
