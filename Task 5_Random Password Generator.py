import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return

    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")


length_var = tk.IntVar(value=12)
password_var = tk.StringVar()
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


tk.Label(root, text="Password Length:").pack()
tk.Entry(root, textvariable=length_var).pack()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack()
tk.Entry(root, textvariable=password_var, state='readonly', width=30).pack()
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
