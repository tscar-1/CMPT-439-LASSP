import tkinter as tk
from tkinter import messagebox

def lagrange(value, data_points, f):
    n = len(data_points)
    interpolated_value = 0.0

    for i in range(n):
        lagrangian = 1.0
        for j in range(n):
            if j != i:
                lagrangian *= (value - data_points[j]) / (data_points[i] - data_points[j])
        interpolated_value += lagrangian * f[i]

    return interpolated_value

def numerical_differentiation(x, x_values, fx, h, flag):

    # Interpolate missing f(x) values if necessary
    if x not in x_values:
        interpolated_fx = lagrange(x, x_values, fx)
        x_values.append(x)
        fx.append(interpolated_fx)

        # Sort the vectors based on x values
        combined = sorted(zip(x_values, fx))
        x_values, fx = zip(*combined)

    try:
        # Find indices for necessary points
        main = x_values.index(x)
        jump = x_values.index(next((val for val in x_values if val == x + h), 0))

        dbl_jump_candidates = [i for i, val in enumerate(x_values) if abs(val - (x + 2 * h)) < 1e-10]
        dbl_jump = dbl_jump_candidates[0] if dbl_jump_candidates else 0

        back_candidates = [i for i, val in enumerate(x_values) if abs(val - (x - h)) < 1e-10]
        back = back_candidates[0] if back_candidates else 0

        # Calculate the derivative based on the chosen method
        # Forward difference formula
        if flag == 'a':
            return (fx[jump] - fx[main]) / h
        # 3 points forward difference formula
        elif flag == 'b':
            return (-fx[jump + 1] + 4 * fx[jump] - 3 * fx[main]) / (2 * h)
            

        # 3 points centered difference formula
        elif flag == 'c':
            if jump + 1 < len(fx) and back - 1 >= 0:
                return (fx[jump + 1] - fx[back - 1]) / (2 * h)
            else:
                print("Insufficient data points for 3 points centered difference formula.")
                return 0.0




        print("Invalid flag. Please choose 'a', 'b', or 'c.")
        return 0.0
    except ValueError:
        print(f"Error: x = {x} not found in x_values.")
        return 0.0



class NumericalDifferentiationGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Numerical Differentiation")
        self.geometry("400x400")

        # Method selection
        self.method_label = tk.Label(self, text="Select Method:")
        self.method_label.grid(row=0, column=0, sticky="e")
        self.method_var = tk.StringVar(self)
        self.method_var.set("a")  # Set default value
        self.method_menu = tk.OptionMenu(self, self.method_var, "a", "b", "c")
        self.method_menu.grid(row=0, column=1)

        # X Value Entry
        self.x_label = tk.Label(self, text="Enter x value:")
        self.x_label.grid(row=1, column=0, sticky="e")
        self.x_entry = tk.Entry(self)
        self.x_entry.grid(row=1, column=1)

        # X Values Entry
        self.x_values_label = tk.Label(self, text="Enter x values (comma-separated):")
        self.x_values_label.grid(row=2, column=0, sticky="e")
        self.x_values_entry = tk.Entry(self)
        self.x_values_entry.grid(row=2, column=1)

        # FX Values Entry
        self.fx_values_label = tk.Label(self, text="Enter fx values (comma-separated):")
        self.fx_values_label.grid(row=3, column=0, sticky="e")
        self.fx_values_entry = tk.Entry(self)
        self.fx_values_entry.grid(row=3, column=1)

        # H Value Entry
        self.h_label = tk.Label(self, text="Enter h value:")
        self.h_label.grid(row=4, column=0, sticky="e")
        self.h_entry = tk.Entry(self)
        self.h_entry.grid(row=4, column=1)

        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.perform_numerical_diff)
        self.submit_button.grid(row=5, column=0, columnspan=2)

    def perform_numerical_diff(self):
        try:
            # Get user inputs
            method = self.method_var.get()
            x_value = float(self.x_entry.get())
            x_values = [float(x) for x in self.x_values_entry.get().split(",")]
            fx_values = [float(fx) for fx in self.fx_values_entry.get().split(",")]
            h_value = float(self.h_entry.get())

            # Perform numerical differentiation
            derivative_value = numerical_differentiation(x_value, x_values, fx_values, h_value, method)

            # Show result in a new window
            self.show_result(x_value, derivative_value)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

    def show_result(self, x_value, derivative_value):
        result_window = tk.Toplevel(self)
        result_window.title("Result")

        result_label = tk.Label(result_window, text=f"The derivative at x = {x_value} is: {derivative_value}")
        result_label.pack()

if __name__ == "__main__":
    app = NumericalDifferentiationGUI()
    app.mainloop()
