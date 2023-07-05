import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a label for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=10)

# Create an entry field for password length
length_entry = tk.Entry(window)
length_entry.pack()

# Create a button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create an entry field to display the generated password
password_entry = tk.Entry(window)
password_entry.pack()

window.mainloop()
