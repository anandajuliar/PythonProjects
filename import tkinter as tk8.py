import tkinter as tk
from tkinter import messagebox
top = tk.Tk()
CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
C1 = tk.Checkbutton(top, text="Music", variable=CheckVar1,
onvalue=1, offvalue=0, height=5, width=20)
C2 = tk.Checkbutton(top, text="Video", variable=CheckVar2,
onvalue=1, offvalue=0, height=5, width=20)
C1.pack()
C2.pack()
top.mainloop()
