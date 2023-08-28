import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_label.config(text="Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=generated_password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create GUI components
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
password_label = tk.Label(root, text="", font=("Helvetica", 16))

# Place GUI components on the window
length_label.pack(pady=10)
length_entry.pack(pady=5)
generate_button.pack(pady=10)
password_label.pack()

# Start GUI loop
root.mainloop()
