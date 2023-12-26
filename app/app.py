import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Add your authentication logic here
    # For simplicity, let's use a hardcoded username and password
    if username == "user" and password == "pass":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create and place widgets (labels, entry fields, buttons) in the window
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_password = tk.Entry(root, show="*")  # Use show="*" to hide the password
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
