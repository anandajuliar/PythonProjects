import tkinter as tk

def sel():
    selection = "Value = " + str(var.get())
    label.config(text=selection)

root = tk.Tk()
var = tk.DoubleVar()
scale = tk.Scale(root, variable=var)
scale.pack(anchor=tk.CENTER)

button = tk.Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=tk.CENTER)

label = tk.Label(root)
label.pack()
root.mainloop()
