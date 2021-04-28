import string
from tkinter import *
import main
from tkinter import messagebox

# Define try and if for user input values

def get_data():

    fm = False
    lm = False
    dlnm = False
    sm = False

    first = str(e1.get())
    if len(first) == 0:
        first_message = "Invalid Input, Please Enter your First Name"
    else:
        first_message = "\n First Name: " + first
        fm = True

    last = str(e2.get())
    if len(last) == 0:
        last_message = "Invalid Input, Please Enter your Last Name"
    else:
        last_message = "\n Last Name: " + last
        lm = True
    
    dln = str(e4.get())
    if len(dln) == 0:
        dln_message = "Invalid Input, Please Enter your Driver's License Number"
    else:
        dln_message = "\n DLN: " + dln
        dlnm = True

    state = str(e4.get())
    if len(state) == 0:
        state_message= "Invalid Input, Please Enter Your State According to Your Driver's License"
    else:
        state_message = "\n State: " + state
        sm = True
    
    if fm == True and lm == True and dlnm == True and sm == True:
        return True
    else:
        return False


def clear_data():
    output.delete(0.0, END)
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    list1.delete(0, "end")

# Window creation

window = Tk()

# Define 4 labels

l1 = Label(window, text="First Name")
l1.grid(row=0, column=0)
l2 = Label(window, text="Last Name")
l2.grid(row=0, column=2)
l3 = Label(window, text="License #")
l3.grid(row=1, column=0)
l4 = Label(window, text="State")
l4.grid(row=1, column=2)

# Define Entries

fName = StringVar()
e1 = Entry(window, textvariable=fName, bg="light blue")
e1.grid(row=0, column=1)
lName = StringVar()
e2 = Entry(window, textvariable=lName, bg="light blue")
e2.grid(row=0, column=3)
dln = StringVar()
e3 = Entry(window, textvariable=dln, bg="light blue")
e3.grid(row=1, column=1)
state_text = StringVar()
e4 = Entry(window, textvariable=state_text, bg="light blue")
e4.grid(row=1, column=3)

# Define Buttons if text has been filled
def show_validation_buttons(is_get_data_true):
    if is_get_data_true:
        b1 = Button(window, text="Validate", width=12, bg="Light Green", command=lambda: messagebox.showinfo("Is it valid?",
            e1.get() + ' ' + main.check_is_valid(main.get_state_abbr(e4.get()), e3.get())))
        b1.grid(row=2, column=3, sticky=W)
        b2 = Button(window, text="Clear", width=12, bg="Red", command=clear_data)
        b2.grid(row=3, column=3, sticky=W)

b0 = Button(window, text='Start', width=12, bg="Light Green", command=lambda:show_validation_buttons(get_data()))
b0.grid(row=4, column=3, sticky=W)
window.mainloop()