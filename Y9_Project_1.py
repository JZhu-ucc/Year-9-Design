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
	a = var.get()
	if a == "Sig Figs":
		print("")
		x = entIn1.get() #still a string
		tlist = list(x)
		print(tlist)
		#find the first zero in the list
		#write with a for loop
		loc = -1 #no zero
		##Backwarsd through list
		for i in range(len(tlist) - 1, -1, -1):
			if tlist[i] == "0":
				loc = i
				break #exits loop

		if varCheck.get() == 1:
					text1 = " You entered " + str(entIn1.get()) + ". Your result was" + str(loc) + " ."
					os.system("say \""+text1+"\"")

		print(loc)
	else:
		try:
			print("Submit pressed")
			x = int(entIn1.get())
			answers.append(x)
			print(x*1000)
			x2 = x*1000
			
		except:
			print("Please input an integer")

	print(answers)
	if varCheck.get() == 1:
					text2 = "You entered "+str(entIn1.get)+ " the result is "+ str(x2)
					os.system("say \""+text2+"\"")

answers = []
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




