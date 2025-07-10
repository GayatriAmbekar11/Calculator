from tkinter import *

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Calculator")
        self.root.wm_geometry("500x300+100+100")
        self.root.configure(bg="#f0f8ff")

        self.operator = None

        label_font = ('Helvetica', 12, 'bold')
        entry_font = ('Helvetica', 14)

        self.lblnum1 = Label(master=self.root, text="Num 1:", font=label_font, bg="#f0f8ff")
        self.lblnum1.place(x=30, y=20, width=70, height=25)
        self.ennum1 = Entry(master=self.root, font=entry_font, justify='center')
        self.ennum1.place(x=30, y=50, width=90, height=30)

        self.lblnum2 = Label(master=self.root, text="Num 2:", font=label_font, bg="#f0f8ff")
        self.lblnum2.place(x=140, y=20, width=70, height=25)
        self.ennum2 = Entry(master=self.root, font=entry_font, justify='center')
        self.ennum2.place(x=140, y=50, width=90, height=30)

        self.lbloperator = Label(master=self.root, text="Operator:", font=label_font, bg="#f0f8ff")
        self.lbloperator.place(x=250, y=20, width=80, height=25)
        self.enoperator = Entry(master=self.root, font=entry_font, justify='center')
        self.enoperator.place(x=250, y=50, width=90, height=30)

        self.lblresult = Label(master=self.root, text="Result:", font=label_font, bg="#f0f8ff")
        self.lblresult.place(x=360, y=20, width=70, height=25)
        self.enresult = Entry(master=self.root, font=entry_font, justify='center', state='normal')
        self.enresult.place(x=360, y=50, width=90, height=30)

        btn_bg = "#e6f2ff"
        btn_font = ('Helvetica', 12)

        # Operator Buttons
        self.add_button = Button(self.root, text="+", font=btn_font, bg=btn_bg, command=lambda: self.set_operator("+"))
        self.add_button.place(x=30, y=100, width=60, height=30)

        self.sub_button = Button(self.root, text="-", font=btn_font, bg=btn_bg, command=lambda: self.set_operator("-"))
        self.sub_button.place(x=110, y=100, width=60, height=30)

        self.mul_button = Button(self.root, text="*", font=btn_font, bg=btn_bg, command=lambda: self.set_operator("*"))
        self.mul_button.place(x=190, y=100, width=60, height=30)

        self.div_button = Button(self.root, text="/", font=btn_font, bg=btn_bg, command=lambda: self.set_operator("/"))
        self.div_button.place(x=270, y=100, width=60, height=30)

        self.mod_button = Button(self.root, text="%", font=btn_font, bg=btn_bg, command=lambda: self.set_operator("%"))
        self.mod_button.place(x=350, y=100, width=60, height=30)

        self.floordiv_button = Button(self.root, text="//", font=btn_font, bg=btn_bg, command=lambda: self.set_operator("//"))
        self.floordiv_button.place(x=430, y=100, width=60, height=30)

        self.equals_button = Button(self.root, text="=", font=btn_font, bg="#d1ffd6", command=self.display_result)
        self.equals_button.place(x=150, y=160, width=80, height=35)

        self.btnclr = Button(master=self.root, text="Clear", font=btn_font, bg="#ffcccc", command=self.clear)
        self.btnclr.place(x=260, y=160, width=80, height=35)

        self.root.mainloop()

    def set_operator(self, operator):
        self.operator = operator
        self.enoperator.delete(0, END)
        self.enoperator.insert(0, operator)

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

    def mod(self, num1, num2):
        return num1 % num2

    def fdiv(self, num1, num2):
        return num1 // num2

    def clear(self):
        self.ennum1.delete(0, END)
        self.ennum2.delete(0, END)
        self.enresult.delete(0, END)
        self.enoperator.delete(0, END)
        self.operator = None

    def display_result(self):
        num1 = int(self.ennum1.get())
        num2 = int(self.ennum2.get())
        operator = self.operator

        if operator == "+":
            result = self.add(num1, num2)
        elif operator == "-":
            result = self.sub(num1, num2)
        elif operator == "*":
            result = self.mul(num1, num2)
        elif operator == "/":
            result = self.div(num1, num2)
        elif operator == "%":
            result = self.mod(num1, num2)
        elif operator == "//":
            result = self.fdiv(num1, num2)

        self.enresult.delete(0, END)
        self.enresult.insert(0, str(result))


if __name__ == '__main__':
    g = Gui()
