from tkinter import *
from math import sin, cos, tan, log, log10, sqrt, radians

# Function to handle button clicks
def click(event):
    global scvalue
    text = event.widget.cget("text")  
    print(text)  

    if text == "=":
        try:
            expression = scvalue.get()  
            expression = expression.replace('sin', 'sin(radians')
            expression = expression.replace('cos', 'cos(radians')
            expression = expression.replace('tan', 'tan(radians')
        
            result = eval(expression, {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, "log": log, "log10": log10, "sqrt": sqrt, "radians": radians})
            scvalue.set(result)  
            screen.update()
        except ZeroDivisionError:
            scvalue.set("Error")  
            screen.update()
        except "tan(90" in expression:
            scvalue.set("Error: tan(90) is undefined")
            screen.update()
        except (SyntaxError, NameError):
            scvalue.set("Error") 
            screen.update()

    elif text == "C":
        scvalue.set("")  
        screen.update()
    
    elif text == "Del":
        current_text = scvalue.get()
        scvalue.set(current_text[:-1])  
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)  
        screen.update()

# Handles unary operations like sin, cos, square root, and others by converting the input to a float and performing the appropriate calculation.
def calculate_unary(operation):
    try:
        value = float(scvalue.get())  
        result = None
        if operation == "1/x":
            scvalue.set(1 / value) 
        elif operation == "x^2":
            scvalue.set(value ** 2) 
        elif operation == "√x":
            scvalue.set(sqrt(value))  
        elif operation == "log":
            scvalue.set(log10(value))  
        elif operation == "ln":
            scvalue.set(log(value))  
        elif operation == "sin":
            scvalue.set(sin(radians(value)))  
        elif operation == "cos":
            scvalue.set(cos(radians(value)))  
        elif operation == "tan":
            scvalue.set(tan(radians(value)))  
        if result is not None:
            scvalue.set(result)  
    except Exception as e:
        scvalue.set("Error")  
    screen.update()

cal_root = Tk()
cal_root.geometry("650x900")  
cal_root.title("Calculator by Rajee")  

cal_root.minsize(600, 725)

text_label = Label(text='CALCULATOR', padx=10, pady=5, font='Courier 30 bold')
text_label.pack()

# Create a variable for displaying the screen value
scvalue = StringVar()
scvalue.set("")
screen = Entry(cal_root, textvar=scvalue, font="Courier 40 bold")  # Display screen
screen.pack(fill=X, ipadx=30, pady=20, padx=30)

# Button layout (rows and columns)
buttons = [
    ['1', '2', '3', '+', 'C', '1/x'],
    ['4', '5', '6', '-', 'x^2', '√x'],
    ['7', '8', '9', '*', 'log', 'ln'],
    ['0', '.', '%', '/', 'sin', 'cos'],
    ['(', ')', '=', 'tan', 'Del']
]

# Create buttons  and bind it with function
for row in buttons:
    frame = Frame(cal_root, bg="grey")  
    for text in row:
        button = Button(frame, text=text, padx=15, pady=15, font="Courier 14 bold", width=3, height=1)
        button.pack(side=LEFT, padx=18, pady=12)  
        
        button.bind("<Button-1>", click if text not in ['1/x', 'x^2', '√x', 'log', 'ln', 'sin', 'cos', 'tan'] else lambda e, t=text: calculate_unary(t))
    frame.pack()

cal_root.mainloop()
