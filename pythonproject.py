from tkinter import *
import random
from tkinter import messagebox 
entries={}

i=0
def input1(a,b,c,e1,e2,e3):
    entries.update({a:[b,c]})
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
def search(root,item,WW):
    if entries.has_key(item):
        a=entries.get(item)
        showinfo('YOUR DEAILS','Name is '+item+'\nMobile No. :'+a[0]+'\nAddress is :'+a[1])
    else:
        showerror('SORRY','Record not Found')
    WW.delete(0,END)

def mainl():
    root=Tk()
    root.title('PHONE BOOK')
    
    Label(root,text='Register your record here:-',width='25',font='Algerian 17 bold',foreground='brown',relief='sunken',bg='wheat').grid(row=0,column=0)

    Label(root,text='ENTER YOUR NAME',width='20',font='Algerian 15 bold',height='1',foreground='dark blue',relief='sunken',bg='tan').grid(row=1,column=0)

    e1=Entry(root,bg='cyan',width='25',bd=6,font='Arial 14 bold')
    e1.grid(row=2,column=0)

    Label(root,text='ENTER YOUR MOBILE NO',width='22',font='Algerian 15 bold',height='1',foreground='dark blue',relief='sunken',bg='tan').grid(row=3,column=0)

    e2=Entry(root,bg='aquamarine1',width='25',bd=6,font='Arial 14 bold')
    e2.grid(row=4,column=0)

    Label(root,text='ENTER YOUR ADDRESS ',width='20',font='Algerian 15 bold',height='1',foreground='dark blue',relief='sunken',bg='tan').grid(row=5,column=0)

    e3=Entry(root,bg='skyblue',width='25',bd=6,font='Arial 14 bold')
    e3.grid(row=6,column=0)

    Button(root,text='SIGN UP',bg='tan',font='Algerian 15 bold',foreground='brown',command=lambda:input1(e1.get(),e2.get(),e3.get(),e1,e2,e3),bd=6).grid(row=7,column=0)

    Label(root,text='Search your record here:-',width='25',font='Algerian 17 bold',foreground='brown',relief='sunken',bg='wheat').grid(row=2,column=1)    
    s=Entry(root,bg='aquamarine1',width='25',bd=6,font='Arial 14 bold')
    s.grid(row=4,column=1)

    Button(root,text='CHECK',bg='tan',font='Algerian 15 bold',foreground='brown',bd=6,command=lambda:search(root,s.get(),s)).grid(row=5,column=1)
    root.mainloop()
def start():
    u=Tk()
    Label(u,text='project by\n\n\n Name:  Sudhir Tewari\n\nEnr No:  151423\n\nMob No:  8400899179\n\nEmail id:  ersudhirtiwari800@gmail.com',font='Algerian 18 italic',foreground='black',bd=4).pack()
    Button(u,command=lambda:maino(u),text='Start Project',bd=5,bg='tan',font='Algerian 18 bold',foreground='blue').pack()
    u.mainloop()
def maino(o):
    o.destroy()
    mainl()
start()
