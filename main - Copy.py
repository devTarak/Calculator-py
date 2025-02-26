from tkinter import *
import math as m

window = Tk()
window.title("Engineering Calculator")
window.geometry("383x590+470+20")
window.config(bg="gray11")
window.resizable(False, False)
window.overrideredirect(1)
def close():
    window.destroy()
def clear():
    entry.delete(0, END)
def backspace():
    lastNumber = len(entry.get())-1
    entry.delete(lastNumber, END)
def press(value):
    lastNumber = len(entry.get())
    entry.insert(lastNumber, value)
def add(val1, val2):
    return float(val1) + float(val2)
def sub(val1, val2):
    return float(val1) - float(val2)
def mul(val1, val2):
    return float(val1) * float(val2)
def div(val1, val2):
    return float(val1) / float(val2)
def expression_break(sign, expression):
    values = expression.split(sign, 1)
    return values
def scientific(expression):
    data = expression_break("(", expression)
    if data[0] == "tan":
        return m.tan(float(data[1]))
    elif data[0] == "cos":
        return m.cos(float(data[1]))
    elif data[0] == "sin":
        return m.sin(float(data[1]))
    elif data[0] == "sqrt":
        return m.sqrt(float(data[1]))
    elif data[0] == "log":
        return m.log10(float(data[1]))
    elif data[0] == "ln":
        return m.log(float(data[1]))
    elif data[0] == "deg":
        return m.degrees(float(data[1]))
    elif data[0] == "rad":
        return m.radians(float(data[1]))
    elif data[0] == "factorial":
        return m.factorial(float(data[1]))
def equal():
    expression = entry.get()
    clear()
    try:
        if expression.find("(") > 0:
            result = scientific(expression)
        elif expression.find("pow") > 0:
            data = expression_break("pow", expression)
            result = m.pow(float(data[0]), float(data[1]))
        elif expression.find("rem") > 0:
            data = expression_break("rem", expression)
            result = m.remainder(float(data[0]), float(data[1]))
        elif expression.find("x") > 0:
            data = expression_break("x", expression)
            result = mul(data[0], data[1])
        elif expression.find("*") > 0:
            data = expression_break("*", expression)
            result = mul(data[0], data[1])
        elif expression.find("÷") > 0:
            data = expression_break("÷", expression)
            result = div(data[0], data[1])
        elif expression.find("/") > 0:
            data = expression_break("/", expression)
            result = div(data[0], data[1])
        elif expression.find("+") > 0:
            first = expression.find("+")
            second = expression.find("+", (first+1),(first+5))
            if first>second:
                data = expression_break("+", expression)
                result = add(data[0], data[1])
            else:
                result = add(expression[:second], expression[(second+1):])
        elif expression.find("-") > 0:
            sign =expression.rindex("-")
            result = sub(expression[0:sign], expression[(sign+1):])
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")
entry_string = StringVar()
entry = Entry(window, textvariable=entry_string, foreground="white", background="gray20", border=0, font=("Bahnschrift SemiBold", 20))
entry.grid(row=0, column=0, columnspan=4, ipady=15, sticky="nsew")
# Configure the grid column to expand
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
font_value = ("Calibri", 18)
keyFontColor = "DarkOrange1"
btn_Tan = Button(window, text="tan", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("tan("))
btn_Tan.grid(row=1, column=0, ipadx=0, ipady=5, sticky=E+W)
btn_Cos = Button(window, text="cos", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("cos("))
btn_Cos.grid(row=1, column=1, ipadx=0, ipady=5, sticky=E+W)
btn_Sin = Button(window, text="sin", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("sin("))
btn_Sin.grid(row=1, column=2, ipadx=0, ipady=5, sticky=E+W)
btn_sqrt = Button(window, text="Sqrt", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("sqrt("))
btn_sqrt.grid(row=1, column=3, ipadx=0, ipady=5, sticky=E+W)
btn_log = Button(window, text="log", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("log("))
btn_log.grid(row=2, column=0, ipadx=0, ipady=5, sticky=E+W)
btn_ln = Button(window, text="ln", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("ln("))
btn_ln.grid(row=2, column=1, ipadx=0, ipady=5, sticky=E+W)
btn_deg = Button(window, text="deg", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("deg("))
btn_deg.grid(row=2, column=2, ipadx=0, ipady=5, sticky=E+W)
btn_rad = Button(window, text="rad", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("rad("))
btn_rad.grid(row=2, column=3, ipadx=0, ipady=5, sticky=E+W)
btn_fac = Button(window, text="x!", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("factorial("))
btn_fac.grid(row=3, column=0, ipadx=0, ipady=5, sticky=E+W)
btn_power = Button(window, text="x^y", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("pow"))
btn_power.grid(row=3, column=1, ipadx=0, ipady=5, sticky=E+W)
btn_rem = Button(window, text="Rem", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("rem"))
btn_rem.grid(row=3, column=2, ipadx=0, ipady=5, sticky=E+W)
btn_pi = Button(window, text="Π", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(3.14159265359))
btn_pi.grid(row=3, column=3, ipadx=0, ipady=5, sticky=E+W)
btn_clear = Button(window, text="C", font=font_value, foreground=keyFontColor, background="gray5", borderwidth=1, relief= SOLID, command=clear)
btn_clear.grid(row=4, column=0, ipadx=0, ipady=5, sticky=E+W,columnspan=2)
btn_backspace = Button(window, text="Del", font=font_value, foreground=keyFontColor, background="gray5", borderwidth=1, relief= SOLID, command=backspace)
btn_backspace.grid(row=4, column=2, ipadx=0, ipady=5, sticky=E+W, columnspan=2)
btn_7 = Button(window, text="7", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(7))
btn_7.grid(row=5, column=0, ipadx=0, ipady=5, sticky=E+W)
btn_8 = Button(window, text="8", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(8))
btn_8.grid(row=5, column=1, ipadx=0, ipady=5, sticky=E+W)
btn_9 = Button(window, text="9", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(9))
btn_9.grid(row=5, column=2, ipadx=0, ipady=5, sticky=E+W)
btn_div = Button(window, text="÷", font=font_value, foreground=keyFontColor, background="gray5", borderwidth=1, relief= SOLID, command=lambda: press("÷"))
btn_div.grid(row=5, column=3, ipadx=0, ipady=5, sticky=E+W)
btn_4 = Button(window, text="4", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(4))
btn_4.grid(row=6, column=0, ipadx=0, ipady=5, sticky=E+W)
btn_5 = Button(window, text="5", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(5))
btn_5.grid(row=6, column=1, ipadx=0, ipady=5, sticky=E+W)
btn_6 = Button(window, text="6", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(6))
btn_6.grid(row=6, column=2, ipadx=0, ipady=5, sticky=E+W)
btn_mul = Button(window, text="x", font=font_value, foreground=keyFontColor, background="gray5", borderwidth=1, relief= SOLID, command=lambda: press("x"))
btn_mul.grid(row=6, column=3, ipadx=0, ipady=5, sticky=E+W)
btn_1 = Button(window, text="1", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(1))
btn_1.grid(row=7, column=0, ipadx=0, ipady=5, sticky=E+W)
btn_2 = Button(window, text="2", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(2))
btn_2.grid(row=7, column=1, ipadx=0, ipady=5, sticky=E+W)
btn_3 = Button(window, text="3", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(3))
btn_3.grid(row=7, column=2, ipadx=0, ipady=5, sticky=E+W)
btn_sub = Button(window, text="-", font=font_value, foreground=keyFontColor, background="gray5", borderwidth=1, relief= SOLID, command=lambda: press("-"))
btn_sub.grid(row=7, column=3, ipadx=0, ipady=5, sticky=E+W)
btn_dot = Button(window, text=".", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press("."))
btn_dot.grid(row=8, column=0, ipadx=0, ipady=5, sticky=E+W)
btn_0 = Button(window, text="0", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(0))
btn_0.grid(row=8, column=1, ipadx=0, ipady=5, sticky=E+W)
btn_e= Button(window, text="e", font=font_value, foreground=keyFontColor, background="gray11", borderwidth=1, relief= SOLID, command=lambda: press(m.e))
btn_e.grid(row=8, column=2, ipadx=0, ipady=5, sticky=E+W)
btn_add = Button(window, text="+", font=font_value, foreground=keyFontColor, background="gray5", borderwidth=1, relief= SOLID, command=lambda: press("+"))
btn_add.grid(row=8, column=3, ipadx=0, ipady=5, sticky=E+W)
btn_equal = Button(window, text="=", font=font_value, foreground="white", background=keyFontColor, borderwidth=1, relief= SOLID, command=equal)
btn_equal.grid(row=9, column=0, ipadx=0, ipady=5, sticky=E+W, columnspan=3)
btn_close= Button(window, text="Close", font=font_value, foreground="white", background="red", borderwidth=1, relief= SOLID, command=close)
btn_close.grid(row=9, column=3, ipadx=0, ipady=5, sticky=E+W)
mainloop()