from tkinter import messagebox
from tkinter import *
import tkinter as tk
import mysql.connector
class Application:
    def __init__(self):
        pass
    def looking(self,id):
        conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
        cur1 = conn.cursor()
        try:
            val = int(id)  # check input is integer or not
            try:
                cur1.execute("SELECT * FROM filelog WHERE id=" + id)
                result = cur1.fetchone()
                search.set(result)
            except:
                search.set("Database error")
        except:
            search.set("Check input")
    def seeing(self):
        root = Toplevel(window)
        global search
        root.geometry("400x200")
        l1 = tk.Label(root, text='Enter ID to search: ', width=25)
        l1.grid(row=1, column=1)
        t1 = tk.Text(root, height=1, width=4, bg='yellow')
        t1.grid(row=1, column=2)
        b1 = tk.Button(root, text='Show Details', width=15, bg='red', command=lambda: self.looking(t1.get('1.0', END)))
        b1.grid(row=1, column=4)
        search = tk.StringVar()
        l2 = tk.Label(root, textvariable=search, width=30, fg='red')
        l2.grid(row=3, column=1, columnspan=2)
        search.set("")
    def searching(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
        query = "select id from filelog where username =%s and password=%s"
        val = (username1.get(),password.get())
        cur = conn.cursor(prepared=True)
        cur.execute(query, val)
        result = cur.fetchone()
        if result!=None:
            messagebox.showinfo('messsage', 'user already exsist')
        else:
            q1="insert into filelog(username,password) values(?,?)"
            val=(username1.get(),password.get())
            #cur=conn.cursor()
            cur.execute(q1,val)
            conn.commit()
            messagebox.showinfo('messsage', 'added')

    def newuser(self):
        global username1
        global password
        username1=StringVar()
        password=StringVar()
        window2 = Toplevel(window)
        window2.geometry("300x300")
        Label(window2, text="username1").grid(row=2)
        Label(window2, text="password").grid(row=4)
        Label(window2, text="re-enter password").grid(row=6)
        a1= Entry(window2,textvariable=username1)
        a2= Entry(window2,textvariable=password)
        a3=Entry(window2)
        a1.grid(row=2, column=1)
        a2.grid(row=4, column=1)
        a3.grid(row=6,column=1)
        button = Button(window2, text="sign-in",command=self.searching).place(x=100,y=200)
        window2.mainloop()


    def check(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='password',port=3306,db='hcl')
        query="select id from filelog where username =%s and password=%s"
        val=(username.get(),password.get())
        cur=conn.cursor(prepared=True)
        cur.execute(query,val)
        result=cur.fetchone()
        if result !=None:
            messagebox.showinfo('messsage','login success')
        else:
            messagebox.showinfo('message','invalid')
    def login2(self):

        global username
        global password
        global window1
        window1=Toplevel(window)
        window1.geometry("300x300")
        username=StringVar()
        password=StringVar()
        Label(window1,text="username").grid(row=0)
        Entry(window1, textvariable=username)
        Label(window1,text="password").grid(row=1)
        Entry(window1,textvariable=password)
        button = Button(window1, text="login", command=self.check).place(x=100, y=80)
        e1=Entry(window1,textvariable=username)
        e2=Entry(window1,textvariable=password)
        e1.grid(row=0,column=1)
        e2.grid(row=1,column=1)
        window1.mainloop()
    def win1(self):
        global window
        window=Tk()
        window.geometry("300x300")
        menubar=Menu(window)
        window.config(menu=menubar)
        menubar.add_command(label="login",command=self.login2)
        menubar.add_command(label="new user",command=self.newuser)
        menubar.add_command(label="search",command=self.seeing)

        window.mainloop()
ob1=Application()
ob1.win1()