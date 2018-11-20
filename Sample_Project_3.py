##hello world
import tkinter as tk
root = tk.Tk() 


labUN = tk.Label(root, text = "Username") 
labUN.pack ()
entUN = tk.Entry(root)
entUN.pack(padx = 10)
labPassword = tk.Label (root, text = "password")
labPassword.pack()
entPassword = tk.Entry(root, show = "*") 
entPassword.pack() 
binSubmit = tk.Button(root, text = "Submit")
binSubmit.pack() 
##Everything_Does_Nothing
root.mainloop() 
