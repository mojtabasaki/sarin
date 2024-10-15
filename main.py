from tkinter import *
from tkinter import ttk

screen = Tk()

screen.geometry("850x500+400+200")
screen.title("CRUD")
screen.configure(bg="#34b4eb")


#variables

Name = StringVar()
LasName = StringVar()
StdField = StringVar()
Age = StringVar()




#entries

txtname = Entry(screen, bd=4,textvariable=Name,width="18", font=("arial 13 bold"), justify="center")
txtname.place(x=150, y=100)

txtlastname = Entry(screen, bd=4,textvariable=LasName,width="18", font=("arial 13 bold"), justify="center")
txtlastname.place(x=150, y=150)

txtfield = Entry(screen, bd=4,textvariable=StdField,width="18", font=("arial 13 bold"), justify="center")
txtfield.place(x=150, y=200)

txtage = Entry(screen, bd=4,textvariable=Age,width="18", font=("arial 13 bold"), justify="center")
txtage.place(x=150, y=250)



#lables

lblname = Label(screen, text="Name", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lblname.place(x=30, y=100)

lbllastname = Label(screen, text="Last Name", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lbllastname.place(x=30, y=150)

lblfield = Label(screen, text="Field", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lblfield.place(x=30, y=200)

lblage = Label(screen, text="Age", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lblage.place(x=30, y=250)




#table

table = ttk.Treeview(screen,columns=("c1","c2","c3","c4"), show="headings")
table.place(x=400, y=100)


table.column("c1", anchor=CENTER, width=90)
table.heading("c1", text="Name")

table.column("c2", anchor=CENTER, width=130)
table.heading("c2", text="Last Name")

table.column("c3", anchor=CENTER, width=90)
table.heading("c3", text="Field")

table.column("c4", anchor=CENTER, width=90)
table.heading("c4", text="Age")








screen.mainloop()
