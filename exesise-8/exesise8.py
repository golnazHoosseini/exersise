import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        total = float(entry_total.get())
        people = int(entry_people.get())

        if people <= 0:
            raise ValueError("Number of people must be greater than zero")

        share = total / people
        messagebox.showinfo("result", f"each person pays: {share:.0f} toman")

    except ValueError:
        messagebox.showwarning("input error", "please enter valid numbers. number of people must be a positive integer")

root = tk.Tk()
root.title("Dong Calculator")

tk.Label(root, text="total:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="number of people:").grid(row=1, column=0, padx=10, pady=5)

entry_total = tk.Entry(root)
entry_total.grid(row=0, column=1, padx=10, pady=5)

entry_people = tk.Entry(root)
entry_people.grid(row=1, column=1, padx=10, pady=5)

btn = tk.Button(root, text="calculate share", command=calculate)
btn.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()
