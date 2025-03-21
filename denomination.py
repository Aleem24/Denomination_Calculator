import tkinter as tk
from tkinter import messagebox

# Denominations (in descending order)
DENOMINATIONS = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

def calculate_denominations():
    try:
        amount  = int(amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Error","Please enter a valid positive amount.")
            return
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Amount: ৳{amount}\n\n")

        remaining_amount = amount
        for denomination in DENOMINATIONS:
            count = remaining_amount // denomination
            remaining_amount = remaining_amount%denomination
            result_text.insert(tk.END, f"৳{denomination}: {count} notes\n")
        
    except ValueError:
        messagebox.showerror("Error","Please enter a valid numeric amount.")

# Create the main window
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x300")

# Label and Entry for amount
amount_label = tk.Label(root, text="Enter Amount (৳):")
amount_label.pack(pady=10)

amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Button to calculate denominations
calculate_button = tk.Button(root, text="Calculate", command=calculate_denominations)
calculate_button.pack(pady=10)

# Text widget to display results

result_text = tk.Text(root, height=10, width=40)
result_text.pack(pady=10)

# Start the main event loop
root.mainloop()


        
    
        

