import tkinter as tk
import os as os



##def change_drop (*args) :
##	if option == "Sig figs"
##	var change_dropd == 0
##	else 
##	change_dropd = 1
def change(*args):
	print("running change")
	print(var.get())

def setting():
	print("TEST")
##def anslist():
##	print (x1)

def checkchange():
	print(varCheck.get())

def submit():
	try:
		print("Submit pressed")
		x = int(entIn1.get())
##		answers.append(x1)
		print(x*1000)
		if varCheck.get() == 1:
			text = "You entered "+entIn1.get+ " the result is "+output.get()
			os.system("say "+text)
	except:
		print("Please input an integer")



root = tk.Tk() 



OPTIONS = [
	"Sig Figs",
	"Micrometer conversion to centimeters",
]
var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)
dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1])
dropDownMenu.pack()


varCheck = tk.IntVar(root)
checkAccess = tk.Checkbutton(root,text = "Accessibility", var = varCheck, command = checkchange)
checkAccess.pack()

labIn1 = tk.Label(root, text = "Input the number to operate on") 
labIn1.pack()
entIn1 = tk.Entry(root)
entIn1.pack(padx = 10)
binSubmit = tk.Button(root, text = "Submit", command = submit)
binSubmit.pack() 

 


root.mainloop() 
## savelist
##def SaveasList(): 
##	root.filename = filedialogue.asksaveasfilename(initialdir = "/", title = "Saved Calculations")
##entIn1.get*1000




