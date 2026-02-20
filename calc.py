import tkinter as tk

def add_to_display(value):
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

app = tk.Tk()
app.title("Calculator")

display = tk.Entry(app, width=20, font=("Arial", 18), justify="right")
display.grid(row=0, column=0, columnspan=4)

button_layout = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for text, row, col in button_layout:
    action = calculate_result if text == "=" else lambda t=text: add_to_display(t)
    tk.Button(app, text=text, width=5, height=2, command=action).grid(row=row, column=col)

tk.Button(app, text="C", width=22, height=2, command=clear_display).grid(row=5, column=0, columnspan=4)

app.mainloop()