import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Function to create the main window
def create_main_window():
    global win  # Make 'win' a global variable
    win = tk.Tk()
    win.title("Main Window")
    win.geometry("500x400")
    return win

# Function to set up the form in the main window
def setup_form(win):
    # Labels
    label1 = tk.Label(win, text="Welcome to the Tkinter Application", font=("Arial", 14))
    label1.pack(pady=10)

    # Displaying an image in the main window
    global main_image
    main_image = PhotoImage(file="download.png")
    image_label = tk.Label(win, image=main_image)
    image_label.pack(pady=10)

    name_label = tk.Label(win, text="Name:")
    name_label.pack(pady=5)

    global name_entry
    name_entry = tk.Entry(win)
    name_entry.pack(pady=5)

    age_label = tk.Label(win, text="Age:")  # Changed 'app' to 'win' here
    age_label.pack(pady=5)

    global age_entry
    age_entry = tk.Entry(win)
    age_entry.pack(pady=5)

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    age = age_entry.get()

    if not name or not age:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Input Error", "Age must be a number.")
        return

    messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}")

# Function to open the second window
def open_second_window():
    global win  # Make sure 'win' is globally accessible
    second_window = tk.Toplevel(win)
    second_window.title("Second Window")
    second_window.geometry("300x300")

    label = tk.Label(second_window, text="This is the second window!", font=("Arial", 12))
    label.pack(pady=10)

    # Adding an image in the second window
    global second_image
    second_image = PhotoImage(file="img_1.png")  # Make sure the file path is correct
    img_label = tk.Label(second_window, image=second_image)
    img_label.pack(pady=10)

    close_button = tk.Button(second_window, text="Close", command=second_window.destroy)
    close_button.pack(pady=10)

# Function to set up buttons in the main window
def setup_buttons(win):
    submit_button = tk.Button(win, text="Submit", command=submit_form)
    submit_button.pack(pady=10)

    second_window_button = tk.Button(win, text="Open Second Window", command=open_second_window)
    second_window_button.pack(pady=10)

    exit_button = tk.Button(win, text="Exit", command=win.quit)
    exit_button.pack(pady=10)

# Main program
win = create_main_window()
setup_form(win)
setup_buttons(win)
win.mainloop()
