import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class ExcelAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Excel Analyzer")
        self.geometry("600x400")
        self.df = None  # Will hold our DataFrame
        
        # Create button to upload Excel file
        self.load_button = tk.Button(self, text="Upload Excel File", command=self.load_file)
        self.load_button.pack(pady=10)
        
        # Frame to hold controls for selecting a header and an operation
        self.control_frame = tk.Frame(self)
        self.control_frame.pack(pady=20)
        
        # Label and combobox to choose a column (header)
        self.column_label = tk.Label(self.control_frame, text="Select Column:")
        self.column_label.grid(row=0, column=0, padx=5, pady=5)
        self.column_combobox = ttk.Combobox(self.control_frame, state="readonly")
        self.column_combobox.grid(row=0, column=1, padx=5, pady=5)
        
        # Label for operation selection
        self.operation_label = tk.Label(self.control_frame, text="Select Operation:")
        self.operation_label.grid(row=1, column=0, padx=5, pady=5)
        
        # Radio buttons for selecting the operation: Mean, Max, or Min
        self.operation_var = tk.StringVar(value="mean")
        self.mean_radio = tk.Radiobutton(self.control_frame, text="Mean", variable=self.operation_var, value="mean")
        self.mean_radio.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.max_radio = tk.Radiobutton(self.control_frame, text="Max", variable=self.operation_var, value="max")
        self.max_radio.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.min_radio = tk.Radiobutton(self.control_frame, text="Min", variable=self.operation_var, value="min")
        self.min_radio.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        
        # Button to calculate the chosen operation for the selected header
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_value)
        self.calculate_button.pack(pady=10)
        
        # Label to display the result
        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
        if file_path:
            try:
                # Load the Excel file into a pandas DataFrame
                self.df = pd.read_excel(file_path)
                headers = list(self.df.columns)
                # Update the combobox with headers from the DataFrame
                self.column_combobox['values'] = headers
                if headers:
                    self.column_combobox.current(0)
                messagebox.showinfo("Success", "Excel file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load Excel file: {e}")

    def calculate_value(self):
        # Ensure that an Excel file has been loaded
        if self.df is None:
            messagebox.showwarning("Warning", "Please upload an Excel file first.")
            return
        
        selected_column = self.column_combobox.get()
        if not selected_column:
            messagebox.showwarning("Warning", "Please select a column.")
            return
        
        # Convert the selected column's data to numeric (this will convert non-numeric values to NaN)
        try:
            data = pd.to_numeric(self.df[selected_column], errors='coerce')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert column data to numeric: {e}")
            return
        
        # Check if the entire column failed to convert into a numeric type
        if data.isnull().all():
            messagebox.showerror("Error", "Selected column does not contain numeric data.")
            return
        
        # Perform the selected operation on the numeric data
        operation = self.operation_var.get()
        if operation == "mean":
            result = data.mean()
        elif operation == "max":
            result = data.max()
        elif operation == "min":
            result = data.min()
        else:
            result = None
        
        # Update the result label with the computed value
        if result is not None:
            self.result_label.config(text=f"{operation.capitalize()} of '{selected_column}': {result}")
        else:
            self.result_label.config(text="Invalid Operation Selected")
        
if __name__ == "__main__":
    app = ExcelAnalyzer()
    app.mainloop()
