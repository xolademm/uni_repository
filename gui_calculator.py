import tkinter as tk
from tkinter import messagebox

# Creating files
f1 = open("C:\\Users\\user\\Documents\\operations.txt", "r+")
c1 = f1.read()

mem = []

# Create GUI window
root = tk.Tk()
root.title("Calculator GUI")
root.geometry("400x400")

def perform_operation(op, a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return
    
    # Addition
    if op == 1:
        result = addition(a, b)
    # Subtraction
    elif op == 2:
        result = subtraction(a, b)
    # Multiplication
    elif op == 3:
        result = multiplication(a, b)
    # Division
    elif op == 4:
        result = division(a, b)
    # Nth Root
    elif op == 5:
        result = nth_root(a, b)
    # Exponents
    elif op == 6:
        result = exponents(a, b)
    # Modulo
    elif op == 7:
        result = modulo(a, b)
    # Integer Division
    elif op == 8:
        result = integer_division(a, b)
    else:
        result = "Invalid operation"
    
    result_label.config(text=f"Result: {result}")
    SaveAll()

# Functions from your existing code
def addition(a, b):
    mem.append(f'{a} + {b} = {a+b}')
    return a + b

def subtraction(a, b):
    mem.append(f'{a} - {b} = {a-b}')
    return a - b

def multiplication(a, b):
    mem.append(f'{a} * {b} = {a*b}')
    return a * b

def division(a, b):
    if b == 0:
        return "division by 0 not possible"
    else:
        mem.append(f'{a} / {b} = {a/b}')
        return a / b

def nth_root(a, n):
    if n == 0:
        return "division by 0 not possible"
    else:
        mem.append(f'{n}th root of {a} = {a **(1/n)}')
        return a ** (1 / n)

def exponents(a, b):
    mem.append(f'{a} to the power {b} = {a**b}')
    return a ** b

def modulo(a, b):
    if b == 0:
        return "division by 0 not possible"
    else:
        mem.append(f'{a} modulo {b} = {a%b}')
        return a % b

def integer_division(a, b):
    if b == 0:
        return "division by 0 not possible"
    else:
        mem.append(f'{a} divided by {b} rounded down = {a//b}')
        return a // b

# Save all operation logs to file
def SaveAll():
    with open("C:\\Users\\user\\Documents\\operations.txt", "a") as f:
        f.write("\n".join(mem) + "\n")

# Delete all data from the file
def DeleteAll():
    option = messagebox.askyesno("Delete Data", "Do you want to delete all data in file?")
    if option:
        with open("C:\\Users\\user\\Documents\\operations.txt", "w") as f:
            f.truncate()  # Clears the file content
        messagebox.showinfo("Deleted", "All saved information has been deleted.")
    else:
        return

# GUI Components
a_label = tk.Label(root, text="First Value:")
a_label.pack()

a_entry = tk.Entry(root)
a_entry.pack()

b_label = tk.Label(root, text="Second Value:")
b_label.pack()

b_entry = tk.Entry(root)
b_entry.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Create buttons for each operation
tk.Button(root, text="Addition", command=lambda: perform_operation(1, a_entry.get(), b_entry.get())).pack()
tk.Button(root, text="Subtraction", command=lambda: perform_operation(2, a_entry.get(), b_entry.get())).pack()
tk.Button(root, text="Multiplication", command=lambda: perform_operation(3, a_entry.get(), b_entry.get())).pack()
tk.Button(root, text="Division", command=lambda: perform_operation(4, a_entry.get(), b_entry.get())).pack()
tk.Button(root, text="Nth Root", command=lambda: perform_operation(5, a_entry.get(), b_entry.get())).pack()
tk.Button(root, text="Exponents", command=lambda: perform_operation(6, a_entry.get(), b_entry.get())).pack()
tk.Button(root, text="Modulo", command=lambda: perform_operation(7, a_entry.get(), b_entry.get())).pack()
tk.Button(root, text="Integer Division", command=lambda: perform_operation(8, a_entry.get(), b_entry.get())).pack()

# Button to delete all saved data
tk.Button(root, text="Delete All", command=DeleteAll).pack()

# Run the tkinter event loop
root.mainloop()
