import tkinter as tk

window = tk.Tk()

window.title("Jay Lord Menk I. Orolfo")

window.geometry("600x600")

window.resizable(False , True)

window.configure(bg = "black")

label = tk.Label(window,text = " Student Profile ", font = ("Georgia", 28, "bold", "underline"), fg = "black", bg = "white", width = 100, height = 6 , anchor = "center" )
label.pack(padx = 10 , pady = 5)

label = tk.Label(window,text = "Name : Jay Lord Menk I. Orolfo ", font = ("Courier New", 14, "bold"), fg = "black", bg = "white", width = 100, height = 0 , anchor = "w" )
label.pack(padx = 10 , pady = 5)

label = tk.Label(window,text = "Age : 20 years old ", font = ("Courier New", 14, "bold"), fg = "black", bg = "white", width = 100, height = 0 , anchor = "w" )
label.pack(padx = 10 , pady = 5)

label = tk.Label(window,text = "Course : BSIT ", font = ("Courier New", 14, "bold"), fg = "black", bg = "white", width = 100, height = 0 , anchor = "w" )
label.pack(padx = 10 , pady = 5)

label = tk.Label(window,text = "Birthdate : August 24, 2005 ", font = ("Courier New", 14, "bold"), fg = "black", bg = "white", width = 100, height = 0 , anchor = "w" )
label.pack(padx = 10 , pady = 5)

label = tk.Label(window,text = " You'll never know unless you try ", font = ("arial", 22, "italic"), fg = "black", bg = "white", width = 100, height = 5 , anchor = "center" )
label.pack(padx = 10 , pady = 5)

window.mainloop()




