from tkinter import *
import tkinter.messagebox as alert
import mysql.connector  as mysql
 
def Create():
    id=id_entry.get()
    FirstName = firstname_entry.get()
    LastName = Lastname_entry.get()
    phone=phone_entry.get()
    age=age_entry.get()

    if(id=="" or FirstName=="" or LastName=="" or phone=="" or age==""):
        alert.showinfo("Prompt","Empty record is not allow in table learning_tb please fill the entry")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="learning_db")
        r=con.cursor()
        r.execute("insert into learning_tb values('" + id + "', '" + FirstName + "', ' " + LastName + "', '" + phone + "', '" + age + "')")
        r.execute("commit")

        id_entry.delete(0, "end")
        firstname_entry.delete(0, "end")
        Lastname_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        age_entry.delete(0, "end")
        alert.showinfo("Prompt", "Record inserted successfully")

def Retrieve():
    if(id_entry.get() ==""):
        alert.showinfo("Prompt", "Id is required to retrieve a row in your table")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="learning_db")
        r=con.cursor()
        r.execute("select * from learning_tb where  id='" + id_entry.get() + "'")
        rows=r.fetchall()
        for row in rows:
            firstname_entry.insert(0, row[1])
            Lastname_entry.insert(0, row[2])
            phone_entry.insert(0, row[3])
            age_entry.insert(0, row[4])
        con.close();
def Update():
    id=id_entry.get()
    FirstName=firstname_entry.get()
    LastName=Lastname_entry.get()
    phone=phone_entry.get()
    age=age_entry.get()
    if(FirstName=="" or LastName=="" or phone=="" or age==""):
        alert.showinfo("Prompt", "Empty record is not allowed, form must be filled")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="learning_db")
        r=con.cursor()
        r.execute("update learning_tb set FirstName='" + FirstName + "', LastName='" + LastName + "', phone='" + phone + "', age='" + age + "' where id='" + id + "'" )
        con.commit()
        con.close()

        id_entry.delete(0, "end")
        firstname_entry.delete(0, "end")
        Lastname_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        age_entry.delete(0, "end")

        alert.showinfo("Prompt","Record updated successfully")
def Del():
    if(id_entry.get()==""):
        alert.showinfo("Prompt", "Sorry Id must be filled")
    else:
        con=mysql.connect(host="localhost", user="root", password="", database="learning_db")
        r=con.cursor()
        r.execute("delete from learning_tb where id='" + id_entry.get() + "'")
        con.commit()
        id_entry.delete(0,"end")
        firstname_entry.delete(0,"end")
        Lastname_entry.delete(0,"end")
        phone_entry.delete(0,"end")
        age_entry.delete(0,"end")

        alert.showinfo("Message", "Deleted completely")


root=Tk()
root.geometry("700x500+250+0")
root.configure(bg="powderblue")
root.title("CRUD APPLICATION ")
id=Label(root, text="Enter ID", font="verdana 14", bg="powderblue")
id.place(x=50,y=30)
id_entry=Entry(root, width=5, font="verdana 14")
id_entry.place(x=150, y=30)

FirstName=Label(root, text="Enter your first name", font="verdana 14", bg="powderblue")
FirstName.place(x=50,y=80)
firstname_entry=Entry(root, width=20, font="verdana 14")
firstname_entry.place(x=280, y=80)

Last_Name=Label(root, text="Enter your last name", font="verdana 14", bg="powderblue")
Last_Name.place(x=50, y=130)
Lastname_entry=Entry(root, width=20, font="verdana 14")
Lastname_entry.place(x=280, y=130)

phone=Label(root, text="Enter Phone Number:", font="verdana 14", bg="powderblue")
phone.place(x=50, y=180)
phone_entry=Entry(root, width=20, font="verdana 14")
phone_entry.place(x=280, y=180)

age=Label(root, text="Enter Age:", font="verdana 14", bg="powderblue")
age.place(x=50, y=230)
age_entry=Entry(root, width=10, font="verdana 14")
age_entry.place(x=280, y=230)


btnCreate=Button(root, text="Create", font="verdana 14", fg="black", command=Create)
btnCreate.place(x=280, y=280)

btnRetrieve=Button(root, text="Retrieve", font="verdana 14", fg="black", command=Retrieve)
btnRetrieve.place(x=360, y=280)

btnUpdate=Button(root, text="Update", font="verdana 14", fg="black", command=Update)
btnUpdate.place(x=458, y=280)

btnDel=Button(root, text="Delete", font="verdana 14", fg="black", command=Del)
btnDel.place(x=545, y=280)

btnClose=Button(root, text="End", font="verdana 11", fg="white", bg="red", command=root.destroy)
btnClose.place(x=650, y=0)

root.mainloop()
