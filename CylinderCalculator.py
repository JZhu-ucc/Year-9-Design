import tkinter as tk

def submit():
	print("Submit pressed.")
	



root = tk.Tk() 
root.title("Volume of a cylinder")

labr = tk.Label(root, text="Radius")
labr.pack()
entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="Height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit")
btn.pack()

output = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief =tk.GROOVE)
output.pack()



root.mainloop()
