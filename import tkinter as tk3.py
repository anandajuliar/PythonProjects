import tkinter as tk

root = tk.Tk()

var = tk.StringVar()
label = tk.Message(root, textvariable=var, relief=tk.RAISED)

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
