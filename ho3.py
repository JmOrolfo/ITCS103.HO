import tkinter as cal

window = cal.Tk()

window.title("Simple Calculator")

def addi():
    val1 = entry1.get()
    val2 = entry2.get()
    val1 = eval(val1)
    val2 = eval(val2)
    total = val1 + val2 
    label ['text'] = (f"The Sum of {val1} and {val2} is {total}")

def subtract():
    val1 = entry1.get()
    val2 = entry2.get()
    val1 = eval(val1)
    val2 = eval(val2)
    total = val1 - val2 
    label ['text'] = (f"The diffirence of {val1} and {val2} is {total}")

def divide():
    val1 = entry1.get()
    val2 = entry2.get()
    val1 = eval(val1)
    val2 = eval(val2)
    total = val1 / val2 
    label ['text'] = (f"The quotient {val1} and {val2} is {total}")

def multiply():
    val1 = entry1.get()
    val2 = entry2.get()
    val1 = eval(val1)
    val2 = eval(val2)
    total = val1 * val2 
    label ['text'] = (f"The product of {val1} and {val2} is {total}")

window.config( cursor = "cross")

label = cal.Label(window, text = "Simple Calculator", font = ("courier", 12, "bold"))
label.grid(column = 0, row = 0, columnspan = 2,pady = 5)

label1 = cal.Label(window, text = "Enter 1st Number:", font = ("poppins", 10))
label1.grid(column = 0, row = 1,pady = 5)

entry1 = cal.Entry(window)
entry1.grid(column = 1, row = 1)

label2 = cal.Label(window, text = "Enter 2nd Number:", font = ("poppins", 10))
label2.grid(column = 0, row = 2,pady = 5)

entry2 = cal.Entry(window)
entry2.grid(column = 1, row = 2)

add = cal.Button(window, text = "Addition", command = addi, font = ("poppins", 10), relief = "groove")
add.grid(column = 0, row = 3,pady = 5)

sub = cal.Button(window, text = "Subtraction", command = subtract, font = ("poppins", 10), relief = "groove")
sub.grid(column = 0, row = 4,pady = 5)

div = cal.Button(window, text = "Divition", command = divide, font = ("poppins", 10), relief = "groove")
div.grid(column = 1, row = 3,pady = 5)

mul = cal.Button(window, text = "Multiplication", command = multiply, font = ("poppins", 10), relief = "groove")
mul.grid(column = 1, row = 4,pady = 5)



window.mainloop()