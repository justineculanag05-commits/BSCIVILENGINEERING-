import tkinter as tk
import math

root = tk.Tk()
root.title("Aji's Calculator")
root.geometry("360x470")  
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# ---------------- Functions ----------------
def calculate():
    try:
        expression = entry_screen.get()
        expression = expression.replace("%", "/100")
        expression = expression.replace("π", str(math.pi))
        
        result = eval(expression)
        entry_screen.delete(0, tk.END)
        entry_screen.insert(0, str(result))
    except:
        entry_screen.delete(0, tk.END)
        entry_screen.insert(0, "Error")

def click_button(item):
    current = entry_screen.get()
    entry_screen.delete(0, tk.END)
    entry_screen.insert(0, current + str(item))

def clear():
    entry_screen.delete(0, tk.END)

def backspace():
    current = entry_screen.get()
    entry_screen.delete(0, tk.END)
    entry_screen.insert(0, current[:-1])

# ---------------- Hover ----------------
def on_enter(e):
    e.widget['bg'] = "#666666"

def on_leave(e):
    e.widget['bg'] = e.widget.default_bg

# ---------------- Entry ----------------
entry_screen = tk.Entry(
    root,
    font=("Segoe UI", 24),
    justify='right',
    bd=0,
    bg="#2a2a3d",
    fg="white",
    insertbackground="white"
)
entry_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

# ---------------- Button -----------------
def create_button(text, row, col, command=None, bg="#3a3a5a"):
    btn = tk.Button(
        root,
        text=text,
        width=6,
        height=2,
        font=("Segoe UI", 13),
        bg=bg,
        fg="white",
        activebackground="#888888",
        relief="raised",        # umbok effect po sya sir
        bd=4,                   # thickness = parang shadow
        command=command if command else lambda: click_button(text)
    )
    
    btn.grid(row=row, column=col, padx=3, pady=3)  #spacing lang
    
    btn.default_bg = bg
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# ---------------- Buttons ----------------
create_button("C", 1, 0, clear, bg="#ff4d4d")
create_button("π", 1, 1, lambda: click_button("π"))
create_button("/", 1, 2)
create_button("←", 1, 3, backspace, bg="#ff4d4d")

create_button("7", 2, 0)
create_button("8", 2, 1)
create_button("9", 2, 2)
create_button("*", 2, 3)

create_button("4", 3, 0)
create_button("5", 3, 1)
create_button("6", 3, 2)
create_button("-", 3, 3)

create_button("1", 4, 0)
create_button("2", 4, 1)
create_button("3", 4, 2)
create_button("+", 4, 3)

create_button("0", 5, 0)
create_button(".", 5, 1)
create_button("=", 5, 2, calculate, bg="#4CAF50")
create_button("%", 5, 3)

root.mainloop()
