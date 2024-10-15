from tkinter import *
from tkinter import ttk
from pymongo import MongoClient
#import messagebox
Client = MongoClient('localhost', 27017)
db=Client['CRUD-testp']
persons=db['persons6']






screen = Tk()

screen.geometry("850x500+400+200")
screen.title("CRUD")
screen.configure(bg="#34b4eb")
screen.resizable(width=False , height=False)




#def

def onclickreg(e):
    if Name.get()=="" or LasName.get()=="" or StdField.get()=="" or Age.get()=="":
        print("please fill all of the boxes")
        #messagebox.showerror("توجه", "تمامی باکس ها را داده وارد کنید")

    else:
        try:
            person = {"name":Name.get(), "lastname":LasName.get(), "field":StdField.get(), "age":int(Age.get())}
            if Exist(person)==False:
                Register(person)
                Load()
                Clearentry()
                print("register was succesfull")
                #messagebox.showinfo("تمام", "ثبت نام با موفقیت انجام شد")
            else:
                print("this person is already registered")
                #messagebox.showinfo("توجه", "این کاربر قبلا ثبت شده است")
        except:
            print("please enter a number inside age box")
            #messagebox.showerror("توجه", "مقدار داخل باکس سن را عددی وارد کنید")


def Register(person):
    persons.insert_one(person)





def ReadData():
    result = persons.find()
    return result

def Exist(person):
    alldata = ReadData()
    for data in alldata:
        if data["name"]==person["name"] and data["lastname"]==person["lastname"] and data["field"]==person["field"] and data["age"]==person["age"]:
            return True
        return False


def Load():
    alldata=ReadData()
    Cleantable()
    for data in alldata:
        InsertDataToTable(data)


def InsertDataToTable(person):

    table.insert('', 'end', values=[person['name'], person['lastname'], person['field'], person['age']])


def Clearentry():
    Name.set("")
    LasName.set("")
    StdField.set("")
    Age.set("")
    txtname.focus_set()


def Cleantable():
    for item in table.get_children():
        table.delete(item)





def onclicksrch():
    dialog = Searchvar.get()
    if dialog=="":
        Load()
    else:
        result = Search(dialog)
        Cleantable()
        for item in result:
            InsertDataToTable(item)



def Search(dialog):
    searchresult = []
    alldata = ReadData()
    for data in alldata:
        if data["name"]==dialog or data["lastname"]==dialog or data["field"]==dialog or data["age"]==dialog:
            searchresult.append(data)
            return searchresult
        




def onclickdlt():
    selected_row = table.selection()
    if selected_row != ():
        Data = table.item(selected_row)["values"]
        person = {"name": Data[0], "lastname": Data[1], "field": Data[2], "age": int(Data[3])}
        Delete(person)
        table.delete(selected_row)


def Delete(person):
    result = FindData(person)
    if result !=False:
        persons.delete_one(person)


def FindData(person):
    alldata = ReadData()
    for data in alldata:
        if data['name']==person['name'] and data['lastname']==person['lastname'] and data['field']==person['field'] and data['age']==person['age']:
            return data
    return False







def Selection(e):
    selected_row = table.selection()
    if selected_row !=():
        data=table.item(selected_row)['values']
        Name.set(data[0])
        LasName.set(data[1])
        StdField.set(data[2])
        Age.set(data[3])


def onClickUpdate():
     selected_row = table.selection()
     if selected_row != ():
        Data = table.item(selected_row)['values']
        OldPerson = {'name': Data[0], 'lastname': Data[1], 'field': Data[2], 'age': int(Data[3])}
        NewPerson={'name':Name.get(),'lastname':LasName.get(),'field':StdField.get(),'age':int(Age.get())}
        Update(OldPerson,NewPerson)
        Cleantable()
        Load()


def Update(OldPerson,NewPerson):
    result=FindData(OldPerson)
    if result!=False:
        newData={'$set':NewPerson}
        persons.update_one(OldPerson,newData)





















#variables

Name = StringVar()
LasName = StringVar()
StdField = StringVar()
Age = StringVar()
Searchvar = StringVar()




#entries

txtname = Entry(screen, bd=4,textvariable=Name,width="18", font=("arial 13 bold"), justify="center")
txtname.place(x=150, y=100)

txtlastname = Entry(screen, bd=4,textvariable=LasName,width="18", font=("arial 13 bold"), justify="center")
txtlastname.place(x=150, y=150)

txtfield = Entry(screen, bd=4,textvariable=StdField,width="18", font=("arial 13 bold"), justify="center")
txtfield.place(x=150, y=200)

txtage = Entry(screen, bd=4,textvariable=Age,width="18", font=("arial 13 bold"), justify="center")
txtage.place(x=150, y=250)

txtsrch = Entry(screen, bd=4,textvariable=Searchvar,width="18", font=("arial 13 bold"), justify="center")
txtsrch.place(x=500, y=50)

















#lables

lblname = Label(screen, text="Name", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lblname.place(x=30, y=100)

lbllastname = Label(screen, text="Last Name", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lbllastname.place(x=30, y=150)

lblfield = Label(screen, text="Field", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lblfield.place(x=30, y=200)

lblage = Label(screen, text="Age", font=("arial 13 bold"), fg="black", bg="#34b4eb")
lblage.place(x=30, y=250)



#buttons

btnreg = Button(screen, text="Register",bd=2, font=("arial 13 bold"), fg="#34b4eb", bg="black")
btnreg.place(x=200, y=300)

btnreg.bind("<Button-1>", onclickreg)




btnsrch= Button(screen, text="Search",bd=2, font=("arial 13 bold"), fg="#34b4eb", bg="black",command=onclicksrch)
btnsrch.place(x=700, y=50)




btndlt= Button(screen, text="Delete",bd=2, font=("arial 13 bold"), fg="black", bg="red",command=onclickdlt)
btndlt.place(x=700, y=330)





btnload = Button(screen, text="Reload",bd=2, font=("arial 13 bold"), fg="#34b4eb", bg="black",command=Load)
btnload.place(x=400, y=330)






btnupd= Button(screen, text="Update",bd=2, font=("arial 13 bold"), fg="black", bg="#03bafc",command=onClickUpdate)
btnupd.place(x=550, y=330)















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


table.bind("<Button-1>",Selection)






screen.mainloop()
