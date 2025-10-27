# gui_bmi_calculator.py

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter positive numbers only.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter numeric values.")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.config(bg="#f0f0f0")

# Title label
tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Weight input
tk.Label(root, text="Weight (kg):", bg="#f0f0f0").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Height input
tk.Label(root, text="Height (m):", bg="#f0f0f0").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white").pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
