import tkinter as tk

root = tk.Tk()

output = tk.Text(root, background = "black", height = 10, width = 50)
output.config(state = "disable")
## disables writing in it
output.grid(row = 0, column = 0, columnspan = 2)
##columnspan shows how many columns it spans







root.mainloop()