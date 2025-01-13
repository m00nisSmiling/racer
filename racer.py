#!/usr/bin/python3
from tkinter import *
import requests
from threading import Thread
from termcolor import colored

root = Tk()
root.configure(bg='black')
root.geometry("600x700")
root.title("<<Racer>>")
w = StringVar(root)
Label(root,text="[ R3QU35T R4C3R ]",font=("Arial", 20,"bold"),fg='#2832C2',bg='black').pack(pady=10)
Label(root,text="[ URL ]",fg='white',bg='black').pack(pady=10)
Entry(root,textvariable=w,width=100,borderwidth=2,bg='#03C04A',fg='blue',highlightthickness=2, highlightbackground="white", highlightcolor="blue").pack()

para = StringVar()
Label(root,text="[ PARAMETER SETTING ]",fg='white',bg='black').pack(pady=10)
Entry(root,textvariable=para,fg='red',bg='#99EDC3',width=100,borderwidth=2,  highlightthickness=2, highlightbackground="white", highlightcolor="yellow").pack()

Label(root,text="[ HEADER SETTING ]",fg='white',bg='black').pack(pady=10)

f1 = Frame(root)
f1.pack()

value1 = StringVar()
Entry(f1,textvariable=value1,fg='white',bg='#234F1E',width=29,borderwidth=2,highlightthickness=2, highlightbackground="white", highlightcolor="black").pack(side=LEFT)
value2 = StringVar()
Entry(f1,textvariable=value2,fg='white',bg='#234F1E',width=70,borderwidth=2,highlightthickness=2, highlightbackground="white", highlightcolor="black").pack(side=LEFT)

f2 = Frame(root)
f2.pack()

value3 = StringVar()
Entry(f2,textvariable=value3,fg='white',bg='#234F1E',width=29,borderwidth=2,highlightthickness=2, highlightbackground="white", highlightcolor="black").pack(side=LEFT)
value4 = StringVar()
Entry(f2,textvariable=value4,fg='white',bg='#234F1E',width=70,borderwidth=2,highlightthickness=2, highlightbackground="white", highlightcolor="black").pack(side=LEFT)
 
w1 = StringVar(root)
Label(root,text="[ THREAD ]",fg='white',bg='black').pack(pady=10)
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

  
f = Frame(root,bg='blue')
f.pack()

Button(f,text='HEAD',fg='white',bg='red',command=head,width=10,borderwidth=2,relief="flat",activebackground="lime").pack(pady=10,side=LEFT)
Button(f,text='GET',fg='white',bg='red',command=get,width=10,borderwidth=2,relief="flat",activebackground="lime").pack(pady=10,side=LEFT)
Button(f,text='POST',fg='white',bg='red',command=post,width=10,borderwidth=2,relief="flat",activebackground="yellow").pack(side=LEFT)
Button(f,text='PUT',fg='white',bg='red',command=put,width=10,borderwidth=2,relief="flat",activebackground="yellow").pack(side=LEFT)
Button(f,text='PATCH',fg='white',bg='red',command=patch,width=10,borderwidth=2,relief="flat",activebackground="yellow").pack(side=LEFT)
Button(f,text='DELETE',fg='white',bg='red',command=delete,width=10,borderwidth=2,relief="flat",activebackground="white",activeforeground="red").pack(side=LEFT)

Label(root,text="[ RESPONSE STATUS CODES ]",fg='white',bg='black').pack(pady=10)
textarea = Text(root,fg='lime',bg='black',width=100,height=20,borderwidth=5,highlightthickness=2, highlightbackground="white", highlightcolor="lime")
textarea.pack()

root.mainloop()
