import tkinter as tk
from tkinter import ttk

# Define classes for each method
class InterpolationMethod(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # Label for the page
        label = tk.Label(self, text="Lagrange Interpolation", font=("Arial", 16))
        label.pack(pady=10)

        # Entry for x-values
        x_label = tk.Label(self, text="Enter x-values (comma-separated):")
        x_label.pack(pady=(0,5))
        self.x_entry = tk.Entry(self)
        self.x_entry.pack()

        # Entry for f(x)-values
        fx_label = tk.Label(self, text="Enter f(x)-values (comma-separated):")
        fx_label.pack(pady=(0,5))
        self.fx_entry = tk.Entry(self)
        self.fx_entry.pack()
        
        # Entry for interpolation point
        interp_point_label = tk.Label(self, text="Enter interpolation point (x-value):")
        interp_point_label.pack(pady=(0,5))
        self.interp_point_entry = tk.Entry(self)
        self.interp_point_entry.pack()

        # Output field
        self.output_label = tk.Label(self, text="Interpolated value will appear here", bg="white", relief="sunken", width=40, height=2)
        self.output_label.pack(pady=10)

        # Compute button
        compute_button = tk.Button(self, text="Compute", command=self.compute_interpolation)
        compute_button.pack()

    def compute_interpolation(self):
        # Get user input from the entry fields
        x_values_str = self.x_entry.get()
        fx_values_str = self.fx_entry.get()
        interp_point_str = self.interp_point_entry.get()

        try:
            # Convert user input into appropriate data types
            x_values = [float(i.strip()) for i in x_values_str.split(',')]
            fx_values = [float(i.strip()) for i in fx_values_str.split(',')]
            interp_point = float(interp_point_str)
            
            # Check if user has entered the same number of x and f(x) values
            if len(x_values) != len(fx_values):
                self.output_label.config(text="Error: The number of x-values and f(x)-values must be the same.")
                return
            
        except ValueError:
            # Update the output field with the error message
            self.output_label.config(text="Error: Please enter valid numbers.")
            
        # Use the lagrange interpolation method
        try:
            interpolated_value = self.lagrange_interpolation(interp_point, x_values, fx_values)
            self.output_label.config(text=f"Interpolated value: {interpolated_value}")
        except Exception as e:
            self.output_label.config(text=f"An error occurred: {e}")
            
        # Update the output field with the interpolated value
        self.output_label.config(text=f"Interpolated value: {interpolated_value}")

    def lagrange_interpolation(self, value, data_points, f_values):
        n = len(data_points)
        interpolated_value = 0.0
        for i in range(n):
            lagrangian = 1.0
            for j in range(n):
                if j != i:
                    lagrangian *= (value - data_points[j]) / (data_points[i] - data_points[j])
            interpolated_value += lagrangian * f_values[i]
        return interpolated_value

class TrapezoidalMethod(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # Label for the page
        label = tk.Label(self, text="Trapezoidal Rule Integration", font=("Arial", 16))
        label.pack(pady=10)

        # Entry for x-values
        x_label = tk.Label(self, text="Enter x-values (comma-separated):")
        x_label.pack(pady=(0,5))
        self.x_entry = tk.Entry(self)
        self.x_entry.pack()

        # Entry for f(x)-values
        fx_label = tk.Label(self, text="Enter f(x)-values (comma-separated):")
        fx_label.pack(pady=(0,5))
        self.fx_entry = tk.Entry(self)
        self.fx_entry.pack()
        
        # Output field for the result
        self.output_label = tk.Label(self, text="Result of integration will appear here", bg="white", relief="sunken", width=40, height=2)
        self.output_label.pack(pady=10)

        # Compute button
        compute_button = tk.Button(self, text="Compute", command=self.compute_trapezoidal)
        compute_button.pack()

    def compute_trapezoidal(self):
        # Get user input from the entry fields
        x_values_str = self.x_entry.get()
        fx_values_str = self.fx_entry.get()

        try:
            # Convert user input into appropriate data types
            x_values = [float(i.strip()) for i in x_values_str.split(',')]
            fx_values = [float(i.strip()) for i in fx_values_str.split(',')]
            
            # Check if user has entered the same number of x and f(x) values
            if len(x_values) != len(fx_values):
                self.output_label.config(text="Error: The number of x-values and f(x)-values must be the same.")
                return

            # Perform the trapezoidal rule integration
            result = self.trapezoidal_rule(x_values, fx_values)
            self.output_label.config(text=f"Result of integration: {result}")

        except ValueError:
            self.output_label.config(text="Error: Please enter valid numbers.")

    def trapezoidal_rule(self, x_values, fx_values):
        # Implement the trapezoidal rule here
        n = len(x_values)
        h = (x_values[-1] - x_values[0]) / (n - 1)
        result = h * (0.5 * fx_values[0] + sum(fx_values[1:-1]) + 0.5 * fx_values[-1])
        return result


class SimpsonMethod(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # Label for the page
        label = tk.Label(self, text="Simpson's Rule Integration", font=("Arial", 16))
        label.pack(pady=10)

        # Entry for x-values
        x_label = tk.Label(self, text="Enter x-values (comma-separated):")
        x_label.pack(pady=(0,5))
        self.x_entry = tk.Entry(self)
        self.x_entry.pack()

        # Entry for f(x)-values
        fx_label = tk.Label(self, text="Enter f(x)-values (comma-separated):")
        fx_label.pack(pady=(0,5))
        self.fx_entry = tk.Entry(self)
        self.fx_entry.pack()
        
        # Output field for the result
        self.output_label = tk.Label(self, text="Result of integration will appear here", bg="white", relief="sunken", width=40, height=2)
        self.output_label.pack(pady=10)

        # Compute button
        compute_button = tk.Button(self, text="Compute", command=self.compute_simpsons)
        compute_button.pack()
        
    def compute_simpsons(self):
        # Get user input from the entry fields
        x_values_str = self.x_entry.get()
        fx_values_str = self.fx_entry.get()

        try:
            # Convert user input into appropriate data types
            x_values = [float(i.strip()) for i in x_values_str.split(',')]
            fx_values = [float(i.strip()) for i in fx_values_str.split(',')]
            
            # Check if user has entered an odd number of points
            if len(x_values) % 2 == 0:
                self.output_label.config(text="Error: Simpson's rule requires an odd number of points.")
                return

            # Perform the Simpson's rule integration
            result = self.simpsons_rule(x_values, fx_values)
            self.output_label.config(text=f"Result of integration: {result}")

        except ValueError:
            self.output_label.config(text="Error: Please enter valid numbers.")

    def simpsons_rule(self, x_values, fx_values):
        # Implement Simpson's rule here
        n = len(x_values) - 1
        h = (x_values[-1] - x_values[0]) / n
        odd_sum = sum(fx_values[i] for i in range(1, n, 2))
        even_sum = sum(fx_values[i] for i in range(2, n-1, 2))
        result = (h/3) * (fx_values[0] + 4*odd_sum + 2*even_sum + fx_values[-1])
        return result

# Main application class
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Project 5")
        self.geometry("400x450")

        # Dropdown menu options
        self.methods = {"Interpolation Method": InterpolationMethod,
                        "Trapezoidal Method": TrapezoidalMethod,
                        "Simpson's Method": SimpsonMethod}

        # Dropdown menu
        self.method_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.method_var, values=list(self.methods.keys()))
        self.dropdown.pack()
        self.dropdown.bind('<<ComboboxSelected>>', self.on_select)

        # Frame for method display
        self.method_frame = None

    def on_select(self, event=None):
        if self.method_frame:
            self.method_frame.pack_forget()

        selected_method = self.methods[self.method_var.get()]
        self.method_frame = selected_method(self)
        self.method_frame.pack()

# Run the application
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
