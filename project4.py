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
        x_values = list(x_values) + [x]
        fx = list(fx) + [interpolated_fx]

        # Sort the vectors based on x values
        combined = sorted(zip(x_values, fx))
        x_values, fx = zip(*combined)

    # Find indices for necessary points
    main = x_values.index(x)
    jump = x_values.index(next(filter(lambda val: val == x + h, x_values)))
    dbl_jump = x_values.index(next(filter(lambda val: val == x + 2 * h, x_values), 0))
    back = x_values.index(next(filter(lambda val: val == x - h, x_values), 0))

    # Calculate the derivative based on the chosen method
    # Forward difference formula
    if flag == 'a':
        return (fx[jump] - fx[main]) / h
    # 3 points forward difference formula
    elif flag == 'b':
        return (-fx[dbl_jump] + 4 * fx[jump] - 3 * fx[main]) / (2 * h)
    # 3 points centered difference formula
    elif flag == 'c':
        return (fx[jump] - fx[back]) / (2 * h)

    print("Invalid flag. Please choose 'a', 'b', or 'c.")
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

        # X value
        self.x_value = 0.26

        # Submit Button
        self.submit_button = tk.Button(self, text="Submit", command=self.perform_numerical_diff)
        self.submit_button.grid(row=1, column=0, columnspan=2)

        # Result Text Box
        self.result_text = tk.Text(self, height=3, width=30)
        self.result_text.grid(row=2, column=0, columnspan=2)

    def perform_numerical_diff(self):
        try:
            # Get user inputs
            method = self.method_var.get()

            # Data points and f(x) values for interpolation
            x_values = [0.15, 0.21, 0.23, 0.27, 0.32, 0.35]
            fx_values = [0.1761, 0.3222, 0.3617, 0.4314, 0.5051, 0.5441]

            # Step size for numerical differentiation
            h_step = 0.01

            # Perform interpolation for missing f(x) values
            for val in [self.x_value, self.x_value + h_step, self.x_value - h_step, self.x_value + 2 * h_step]:
                if val not in x_values:
                    interpolated_fx = lagrange(val, x_values, fx_values)
                    x_values = list(x_values) + [val]
                    fx_values = list(fx_values) + [interpolated_fx]

                    # Sort the vectors based on x values
                    combined = sorted(zip(x_values, fx_values))
                    x_values, fx_values = zip(*combined)

            # Perform numerical differentiation
            derivative_value = numerical_differentiation(self.x_value, x_values, fx_values, h_step, method)

            # Display result in the text box
            result_str = f"The derivative at x = {self.x_value} is: {derivative_value}"
            self.result_text.delete(1.0, tk.END)  # Clear previous content
            self.result_text.insert(tk.END, result_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    app = NumericalDifferentiationGUI()
    app.mainloop()
