#!/usr/bin/python3
from tkinter import *
import requests
from threading import Thread
from termcolor import colored

root = Tk()
root.configure(bg='black',cursor="spider")
root.title("<<Racer>>")

root.geometry("600x700")
w = StringVar(root)
Label(root,text="[ URL ]",fg='lime',bg='black').pack(pady=10)
Entry(root,textvariable=w,width=100,borderwidth=2,bg='black',fg='lime',highlightthickness=2, highlightbackground="red", highlightcolor="lime").pack()

para = StringVar()
Label(root,text="[ PARAMETER SETTING ]",fg='lime',bg='black').pack(pady=10)
Entry(root,textvariable=para,fg='lime',bg='black',width=100,borderwidth=2,  highlightthickness=2, highlightbackground="red", highlightcolor="lime").pack()
Label(root,text="[ HEADER SETTING ]",fg='lime',bg='black').pack(pady=10)

f1 = Frame(root)
f1.pack()

value1 = StringVar()
Entry(f1,textvariable=value1,fg='lime',bg='black',width=29,borderwidth=2,highlightthickness=2, highlightbackground="red", highlightcolor="lime").pack(side=LEFT)
value2 = StringVar()
Entry(f1,textvariable=value2,fg='lime',bg='black',width=70,borderwidth=2,highlightthickness=2, highlightbackground="red", highlightcolor="lime").pack(side=LEFT)

f2 = Frame(root)
f2.pack()
value3 = StringVar()
Entry(f2,textvariable=value3,fg='lime',bg='black',width=29,borderwidth=2,highlightthickness=2, highlightbackground="red", highlightcolor="lime").pack(side=LEFT)
value4 = StringVar()
Entry(f2,textvariable=value4,fg='lime',bg='black',width=70,borderwidth=2,highlightthickness=2, highlightbackground="red", highlightcolor="lime").pack(side=LEFT)

w1 = StringVar(root)
Label(root,text="[ THREAD ]",fg='lime',bg='black').pack(pady=10)
entry = Entry(root,textvariable=w1,width=10,borderwidth=5,bg='black',fg='red',highlightthickness=2, highlightbackground="white", highlightcolor="red")
entry.pack() 

def head():
 inp1 = w.get()
 inp2 = w1.get() 
 inp3 = para.get()
 v1 = value1.get()
 v2 = value2.get()
 v3 = value3.get()
 v4 = value4.get()
 if v1 == '':
  headers = {"User-Agent":"Browser/5.0"}
 else:
  if v3 == '':
   headers = {v1:v2}
  else:
   headers = {v1:v2,v3:v4}
  
 def kk(i):
  print(colored('| Thread |-|> ','red'),i+1)
  ab = requests.head(inp1,data=inp3,headers=headers)
  textarea.insert(END,f"{ab.status_code}/")
 for i in range(0,int(inp2)):
  t = Thread(target=kk,args=(i,))
  t.start()
 
def get():
 inp1 = w.get()
 inp2 = w1.get()
 inp3 = para.get()
 v1 = value1.get()
 v2 = value2.get()
 v3 = value3.get()
 v4 = value4.get()
 if v1 == '':
  headers = {"User-Agent":"Browser/5.0"}
 else:
  if v3 == '':
   headers = {v1:v2}
  else:
   headers = {v1:v2,v3:v4}
   
 def kk(i):
  print(colored('| Thread |-|> ','red'),i+1)
  ab = requests.get(inp1,data=inp3,headers=headers)
  textarea.insert(END,f"{ab.status_code}/")
 for i in range(0,int(inp2)):
  t = Thread(target=kk,args=(i,))
  t.start()
     

def post():
 inp1 = w.get()
 inp2 = w1.get()
 inp3 = para.get()
 v1 = value1.get()
 v2 = value2.get()
 v3 = value3.get() 
 v4 = value4.get()
 if v1 == '':
  headers = {"User-Agent":"Browser/5.0"}
 else:
  if v3 == '':
   headers = {v1:v2}
  else:
   headers = {v1:v2,v3:v4}
 def kk(i):
  print(colored('| Thread |-|> ','red'),i+1)
  ab = requests.post(inp1,data=inp3,headers=headers)
  textarea.insert(END,f"{ab.status_code}/")
 for i in range(0,int(inp2)):
  t = Thread(target=kk,args=(i,))
  t.start()
 
def put():
 inp1 = w.get()
 inp2 = w1.get()
 inp3 = para.get()
 v1 = value1.get()
 v2 = value2.get()
 v3 = value3.get()
 v4 = value4.get()
 if v1 == '':
  headers = {"User-Agent":"Browser/5.0"}
 else:
  if v3 == '':
   headers = {v1:v2}
  else:
   headers = {v1:v2,v3:v4}
 def kk(i):
  print(colored('| Thread |-|> ','red'),i+1)
  ab = requests.put(inp1,data=inp3,headers=headers)
  textarea.insert(END,f"{ab.status_code}/")
 for i in range(0,int(inp2)):
  t = Thread(target=kk,args=(i,))
  t.start()
 
def patch():
 inp1 = w.get()
 inp2 = w1.get()
 inp3 = para.get()
 v1 = value1.get()
 v2 = value2.get()
 v3 = value3.get()
 v4 = value4.get()
 if v1 == '':
  headers = {"User-Agent":"Browser/5.0"}
 else:
  if v3 == '':
   headers = {v1:v2}
  else:
   headers = {v1:v2,v3:v4}
 def kk(i):
  print(colored('| Thread |-|> ','red'),i+1)
  ab = requests.patch(inp1,data=inp3,headers=headers)
  textarea.insert(END,f"{ab.status_code}/")
 for i in range(0,int(inp2)):
  t = Thread(target=kk,args=(i,))
  t.start() 

def delete():
 inp1 = w.get()
 inp2 = w1.get()
 inp3 = para.get()
 v1 = value1.get()
 v2 = value2.get()
 v3 = value3.get()
 v4 = value4.get()
 if v1 == '':
  headers = {"User-Agent":"Browser/5.0"}
 else:
  if v3 == '':
   headers = {v1:v2}
  else:
   headers = {v1:v2,v3:v4}
 def kk(i):
  print(colored('| Thread |-|> ','red'),i+1)
  ab = requests.delete(inp1,data=inp3,headers=headers)
  textarea.insert(END,f"{ab.status_code}/")
 for i in range(0,int(inp2)):
  t = Thread(target=kk,args=(i,))
  t.start() 
  
f = Frame(root,bg='black')
f.pack() 

Button(f,text='HEAD',fg='white',bg='black',command=head,width=10,borderwidth=2,relief="flat",activebackground="lime",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(pady=10,side=LEFT)
Button(f,text='GET',fg='white',bg='black',command=get,width=10,borderwidth=2,relief="flat",activebackground="lime",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(pady=10,side=LEFT)
Button(f,text='POST',fg='white',bg='black',command=post,width=10,borderwidth=2,relief="flat",activebackground="yellow",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT)
Button(f,text='PUT',fg='white',bg='black',command=put,width=10,borderwidth=2,relief="flat",activebackground="yellow",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT)
Button(f,text='PATCH',fg='white',bg='black',command=patch,width=10,borderwidth=2,relief="flat",activebackground="yellow",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT)
Button(f,text='DELETE',fg='white',bg='black',command=delete,width=10,borderwidth=2,relief="flat",activebackground="white",activeforeground="red",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT) 

Label(root,text="[ RESPONSE STATUS CODES ]",fg='lime',bg='black').pack(pady=10)
textarea = Text(root,fg='lime',bg='black',width=100,height=20,borderwidth=5,highlightthickness=2, highlightbackground="lime", highlightcolor="lime")
textarea.pack() 

root.mainloop()

