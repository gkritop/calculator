from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("510x640")
        master.config(bg="black")
        master.resizable(False, False)
        
        self.equation = StringVar()
        self.entry_value = ""
        
        Entry(master, width=16, bg="white", font=("Arial", 24), textvariable=self.equation, bd=0, insertwidth=4, justify='right', fg="black").grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            if text in ['C', '=']:
                Button(master, text=text, width=6, height=3, bg="grey", font=("Arial", 18), command=lambda t=text: self.click(t), fg="black").grid(row=row, column=col, padx=5, pady=5)
            else:
                Button(master, text=text, width=6, height=3, bg="orange", font=("Arial", 18), command=lambda t=text: self.click(t), fg="white").grid(row=row, column=col, padx=5, pady=5)

    def click(self, value):
        if value == 'C':
            self.clear()
        elif value == '=':
            self.solve()
        else:
            self.show(value)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)
        
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

root = Tk()
calculator = Calculator(root)
root.mainloop()
