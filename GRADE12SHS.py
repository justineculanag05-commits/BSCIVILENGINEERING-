import tkinter as tk
import math

# Main window
root = tk.Tk()
root.title("Enhanced Scientific Calculator")
root.geometry("350x550")
root.configure(bg="#1e1e2f")
root.resizable(False, False)  # Disable resizing

expression = ""

# Display
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Evaluate
def equalpress():
    global expression
    try:
        expression = str(eval(expression))
        input_text.set(expression)
    except:
        input_text.set("Error")
        expression = ""

# Clear
def clear():
    global expression
    expression = ""
    input_text.set("")

# Delete last
def delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# Percent
def percent():
    global expression
    try:
        expression = str(float(expression) / 100)
        input_text.set(expression)
    except:
        input_text.set("Error")
        expression = ""

# Pi
def insert_pi():
    press(str(math.pi))

# Square root
def sqrt():
    global expression
    try:
        expression = str(math.sqrt(float(expression)))
        input_text.set(expression)
    except:
        input_text.set("Error")
        expression = ""

# Parenthesis
def press_open():
    press('(')

def press_close():
    press(')')

# Input field
input_text = tk.StringVar()
input_frame = tk.Frame(root, bg="#1e1e2f")
input_frame.grid(row=0, column=0, columnspan=4, pady=20, padx=5, sticky="nsew")

input_field = tk.Entry(input_frame, font=('Arial', 20), textvariable=input_text,
                       width=18, bd=5, relief=tk.FLAT, justify='right', bg="#2d2d44", fg="white")
input_field.pack(fill=tk.BOTH, expand=True)

# Button styling
def create_button(text, row, col, command, bg="#3b3b5c"):
    btn = tk.Button(root, text=text, command=command,
                    font=("Arial", 14, "bold"),
                    bg=bg, fg="white", bd=0,
                    width=5, height=2,
                    activebackground="#5c5cff")
    btn.grid(row=row, column=col, padx=5, pady=5)

    # Hover effect
    btn.bind("<Enter>", lambda e: btn.config(bg="#5c5cff"))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg))

# Buttons
buttons = [
    ('AC', 1, 0, clear, "#ff5c5c"),
    ('DEL', 1, 1, delete, "#ff9f43"),
    ('%', 1, 2, percent, "#00a8ff"),
    ('/', 1, 3, lambda: press('/'), "#00a8ff"),

    ('(', 2, 0, press_open),
    (')', 2, 1, press_close),
    ('√', 2, 2, sqrt, "#9c88ff"),
    ('x', 2, 3, lambda: press('*'), "#00a8ff"),

    ('7', 3, 0, lambda: press('7')),
    ('8', 3, 1, lambda: press('8')),
    ('9', 3, 2, lambda: press('9')),
    ('-', 3, 3, lambda: press('-'), "#00a8ff"),

    ('4', 4, 0, lambda: press('4')),
    ('5', 4, 1, lambda: press('5')),
    ('6', 4, 2, lambda: press('6')),
    ('+', 4, 3, lambda: press('+'), "#00a8ff"),

    ('1', 5, 0, lambda: press('1')),
    ('2', 5, 1, lambda: press('2')),
    ('3', 5, 2, lambda: press('3')),
    ('=', 5, 3, equalpress, "#4cd137"),

    ('0', 6, 0, lambda: press('0')),
    ('.', 6, 1, lambda: press('.')),
    ('π', 6, 2, insert_pi, "#9c88ff"),
]

# Layout grid config
for i in range(7):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

# Create buttons
for btn in buttons:
    if len(btn) == 5:
        text, row, col, cmd, color = btn
    else:
        text, row, col, cmd = btn
        color = "#3b3b5c"

    create_button(text, row, col, cmd, color)

root.mainloop()