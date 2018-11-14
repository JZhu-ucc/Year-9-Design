import tkinter as tk
root = tk.Tk() 
root.title("This is an output box")

output = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief =tk.GROOVE)
output.pack()
print ("Here it is!")


root.mainloop()