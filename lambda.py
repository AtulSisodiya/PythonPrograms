#add =lambda a,b:a+b
#print(add(3,10))
import tkinter as tk
root=tk.TK()
frame= tk.Frame(root)
frame.pack()
button=tk.Button(frame,
                 text="hi there", 
		 fg="black",
		 command= lambda: print("hello"))
button.pack(side=tk.LEFT)
root.mainloop()
