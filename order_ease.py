import tkinter as tk
from tkinter import messagebox

def on_order():
    # Placeholder function for order button
    messagebox.showinfo("Order", "Your order has been placed!")

def on_exit():
    # Placeholder function for exit button
    root.quit()

# Create the main window
root = tk.Tk()
root.title("OrderEase - Pizza Ordering System")

# Create a label
label = tk.Label(root, text="Welcome to OrderEase!")
label.pack()

# Create an order button
order_button = tk.Button(root, text="Place Order", command=on_order)
order_button.pack()

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()

# Start the main loop
root.mainloop()
