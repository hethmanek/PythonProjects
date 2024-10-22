import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="password")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Hospital_Management_System")
mycursor.execute("USE Hospital_Management_System")
mycursor.execute("CREATE TABLE IF NOT EXISTS doctor(id varchar(10) primary key, name varchar(50), shift varchar(50))")
mycursor.execute("CREATE TABLE IF NOT EXISTS patient(name varchar(50), address varchar(50), age varchar(50), disease varchar(50))")
mycursor.execute("CREATE TABLE IF NOT EXISTS staff(id varchar(10) primary key, name varchar(50), designation varchar(50))")

from tkinter import *

def doctor():
    def changer():
        v1=e1.get()
        v2=e2.get()
        v3=e3.get()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        sql=("INSERT INTO doctor(id, name, shift) VALUES(%s,%s,%s)")
        val=(v1,v2,v3)
        mycursor.execute(sql,val)
        mydb.commit()
        Label(d,text="Details Have Been Submitted!!",bg="light blue").grid(row=6,column=6)
        
    def retrieve():
        mycursor.execute("SELECT * FROM doctor")
        myresult = mycursor.fetchall()
        print("------Doctor------")
        for x in myresult:
            print(x)
            
    d=Tk()
    d.title("DOCTORS")
    d.configure(bg="light blue")
    
    Label(d,text="ID:",bg="light blue",font=("Times New Roman","20")).grid(row=0)
    Label(d,text="NAME:",bg="light blue",font=("Times New Roman","20")).grid(row=1)
    Label(d,text="SHIFT:",bg="light blue",font=("Times New Roman","20")).grid(row=2)

    e1=Entry(d,font=("Times New Roman","20"))
    e1.grid(row=0,column=1)

    e2=Entry(d,font=("Times New Roman","20"))
    e2.grid(row=1,column=1)

    e3=Entry(d,font=("Times New Roman","20"))
    e3.grid(row=2,column=1)

    b1=Button(d,text="Submit",command=changer)
    b1.grid(row=5,column=5)

    b2=Button(d,text="Retrieve",command=retrieve)
    b2.grid(row=50,column=50)
    
    d.mainloop()

def patient():
    def changer():
        v1=e1.get()
        v2=e2.get()
        v3=e3.get()
        v4=e4.get()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        sql=("INSERT INTO patient(name,address,age,disease) VALUES(%s,%s,%s,%s)")
        val=(v1,v2,v3,v4)
        mycursor.execute(sql,val)
        mydb.commit()
        Label(p,text="Details Have Been Submitted!!",bg="light blue").grid(row=6,column=6)
        
    def retrieve():
        mycursor.execute("SELECT * FROM patient")
        myresult = mycursor.fetchall()
        print("------Patient------")
        for x in myresult:
            print(x)
        
    
    p=Tk()
    p.title("PATIENTS")
    p.configure(bg="light blue")
    
    Label(p,text="NAME:",bg="light blue",font=("Times New Roman","20")).grid(row=0)
    Label(p,text="ADDRESS:",bg="light blue",font=("Times New Roman","20")).grid(row=1)
    Label(p,text="AGE:",bg="light blue",font=("Times New Roman","20")).grid(row=2)
    Label(p,text="DISEASE:",bg="light blue",font=("Times New Roman","20")).grid(row=3)

    e1=Entry(p,font=("Times New Roman","20"))
    e1.grid(row=0,column=1)

    e2=Entry(p,font=("Times New Roman","20"))
    e2.grid(row=1,column=1)

    e3=Entry(p,font=("Times New Roman","20"))
    e3.grid(row=2,column=1)

    e4=Entry(p,font=("Times New Roman","20"))
    e4.grid(row=3,column=1)

    b1=Button(p,text="Submit",command=changer)
    b1.grid(row=5,column=5)

    b2=Button(p,text="Retrieve",command=retrieve)
    b2.grid(row=50,column=50)
    
    p.mainloop()

def staff():
    def changer():
        v1=e1.get()
        v2=e2.get()
        v3=e3.get()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        sql=("INSERT INTO staff(id,name,designation) VALUES(%s,%s,%s)")
        val=(v1,v2,v3)
        mycursor.execute(sql,val)
        mydb.commit()
        Label(s,text="Details Have Been Submitted!!",bg="light blue").grid(row=6,column=6)
    def retrieve():
        mycursor.execute("SELECT * FROM staff")
        myresult = mycursor.fetchall()
        print("------Staff------")
        for x in myresult:
            print(x)
        
    
    s=Tk()
    s.title("STAFF")
    s.configure(bg="light blue")
    Label(s,text="ID:",bg="light blue",font=("Times New Roman","20")).grid(row=0)
    Label(s,text="NAME:",bg="light blue",font=("Times New Roman","20")).grid(row=1)
    Label(s,text="DESIGNATION:",bg="light blue",font=("Times New Roman","20")).grid(row=2)

    e1=Entry(s,font=("Times New Roman","20"))
    e1.grid(row=0,column=1)

    e2=Entry(s,font=("Times New Roman","20"))
    e2.grid(row=1,column=1)

    e3=Entry(s,font=("Times New Roman","20"))
    e3.grid(row=2,column=1)

    b1=Button(s,text="Submit",command=changer)
    b1.grid(row=5,column=5)

    b2=Button(s,text="Retrieve",command=retrieve)
    b2.grid(row=50,column=50)
    
    s.mainloop()

m=Tk()
m.title("HOSPITAL MANAGEMENT SYSTEM")
Label(m, text="-----Dhanvantari Hospital-----",font=("Times New Roman","50"),bg="light blue", fg="red").grid(row=0,column=10)
m.configure(bg="light blue")
radio=StringVar()
Radiobutton(m,text="Doctors", padx=20, variable=radio, value="Doctors", bg="light blue",font=("Times New Roman","20"),command=doctor).grid(row=40,column=10)
Radiobutton(m,text="Patients", padx=20, variable=radio, value="Patients", bg="light blue",font=("Times New Roman","20"),command=patient).grid(row=41,column=10)
Radiobutton(m,text="Staff", padx=20, variable=radio, value="Staff", bg="light blue",font=("Times New Roman","20"),command=staff).grid(row=42,column=10)
m.mainloop()