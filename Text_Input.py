import tkinter as tk

def submit():
	print("Submit pressed.")
	



root = tk.Tk() 
root.title("A text box")

labr = tk.Label(root, text="Here it is:")
labr.pack()
entr = tk.Entry(root)
entr.pack()

root.mainloop()