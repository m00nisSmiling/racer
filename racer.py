#!/usr/bin/python3
from tkinter import *
import requests
from threading import Thread
from termcolor import colored
import sys
from bs4 import BeautifulSoup

root = Tk()
r1 = Frame(root,bg='black')
r1.pack(side=LEFT)
root.configure(bg='black',cursor="spider")
root.title("<<Racer>>")

root.geometry("600x700")
w = StringVar(root)
Label(r1,text="[ URL ]",fg='lime',bg='black').pack(pady=10)
Entry(r1,insertbackground='red',textvariable=w,width=100,borderwidth=2,bg='black',fg='lime',highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack()

# Headers Settings
Label(r1,text="[ HEADER SETTING ]",fg='lime',bg='black').pack(pady=10)
f1 = Frame(r1)
f1.pack()
value1 = StringVar()
Entry(f1,insertbackground='red',textvariable=value1,fg='lime',bg='black',width=29,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)
value2 = StringVar()
Entry(f1,insertbackground='red',textvariable=value2,fg='lime',bg='black',width=70,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)
f2 = Frame(r1)
f2.pack()
value3 = StringVar()
Entry(f2,insertbackground='red',textvariable=value3,fg='lime',bg='black',width=29,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)
value4 = StringVar()
Entry(f2,insertbackground='red',textvariable=value4,fg='lime',bg='black',width=70,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)
f3 = Frame(r1)
f3.pack()
value5 = StringVar()
Entry(f3,insertbackground='red',textvariable=value5,fg='lime',bg='black',width=29,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)
value6 = StringVar()
Entry(f3,insertbackground='red',textvariable=value6,fg='lime',bg='black',width=70,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)
f4 = Frame(r1)
f4.pack()
value7 = StringVar()
Entry(f4,insertbackground='red',textvariable=value7,fg='lime',bg='black',width=29,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)
value8 = StringVar()
Entry(f4,insertbackground='red',textvariable=value8,fg='lime',bg='black',width=70,borderwidth=2,highlightthickness=2, highlightbackground="blue", highlightcolor="lime").pack(side=LEFT)



# Cli url append
try:
 a1 = sys.argv[1]
 a2 = sys.argv[2]
except IndexError:
 pass
else:
 if a1 == '-u':
  w.set(a2)
 else:
  pass

# Main Method Function
def met(x):
 method = x
 inp1 = w.get()
 inp2 = w1.get()
 inp3 = para.get(0.0,END)
 v1 = value1.get()
 v2 = value2.get()
 v3 = value3.get()
 v4 = value4.get()
 v5 = value5.get()
 v6 = value6.get()
 v7 = value7.get()
 v8 = value8.get()
 if v1 == '':
  headers = {"User-Agent":"Browser/5.0"}
 else:
  if v3 == '':
   headers = {v1:v2}
  else:
   if v5 == '':
    headers = {v1:v2,v3:v4}
   else:
    if v7 == '':
     headers = {v1:v2,v3:v4,v5:v6}
    else:
     headers = {v1:v2,v3:v4,v5:v6,v7:v8}
 if method == 'head':
  soup = requests.head(inp1,data=inp3,headers=headers).text
  response1.delete(0.0,END)
  response1.insert(0.0,soup)
 elif method == 'get':
  soup = requests.get(inp1,data=inp3,headers=headers).text
  response1.delete(0.0,END)
  response1.insert(0.0,soup)
 elif method == 'post':
  soup = requests.post(inp1,data=inp3,headers=headers).text
  response1.delete(0.0,END)
  response1.insert(0.0,soup)
 elif method == 'put':
  soup = requests.put(inp1,data=inp3,headers=headers).text
  response1.delete(0.0,END)
  response1.insert(0.0,soup)
 elif method == 'patch':
  soup = requests.patch(inp1,data=inp3,headers=headers).text
  response1.delete(0.0,END)
  response1.insert(0.0,soup)
 elif method == 'delete':
  soup = requests.delete(inp1,data=inp3,headers=headers).text
  response1.delete(0.0,END)
  response1.insert(0.0,soup)
     
 def kk(i):
  print(colored('| Thread |-|> ','red'),i+1)
  if method == 'head':
   ab = requests.head(inp1,data=inp3,headers=headers)
  elif method == 'get':
   ab = requests.get(inp1,data=inp3,headers=headers)
  elif method == 'post':
   ab = requests.post(inp1,data=inp3,headers=headers)
  elif method == 'put':
   ab = requests.put(inp1,data=inp3,headers=headers)
  elif method == 'patch':
   ab = requests.patch(inp1,data=inp3,headers=headers)
  elif method == 'delete':
   ab = requests.patch(inp1,data=inp3,headers=headers)
  
 for i in range(0,int(inp2)):
  t = Thread(target=kk,args=(i,))
  t.start()
     
# Head request
def head():
 met('head')
 
# Get request
def get():
 met('get')
 
# Post request
def post():
 met('post')
 
# Put request
def put():
 met('put')

# Patch request 
def patch():
 met('patch')

# Delete request
def delete():
 met('delete')

# Data settings
Label(r1,text="[ DATA ]",fg='lime',bg='black').pack(pady=10)
para = Text(r1,insertbackground='red',fg='lime',bg='black',width=100,height=8,borderwidth=5,highlightthickness=2, highlightbackground="lime", highlightcolor="lime")
para.pack()

r2 = Frame(root,bg='white')
r2.pack(padx=15,side=LEFT)

# Response widget
response1 = Text(r2,insertbackground='red',fg='white',bg='black',width=80,height=40,borderwidth=5,highlightthickness=2, highlightbackground="red", highlightcolor="red")
response1.pack()

# Thread count
w1 = StringVar(root)
Label(r1,text="[ THREAD ]",fg='lime',bg='black').pack(pady=10)
entry = Entry(r1,insertbackground='red',textvariable=w1,width=10,borderwidth=5,bg='black',fg='red',highlightthickness=2, highlightbackground="white", highlightcolor="red")
entry.pack() 

f = Frame(r1,bg='black')
f.pack() 
# GUI buttons
Button(f,text='HEAD',fg='white',bg='black',command=head,width=10,borderwidth=2,relief="flat",activebackground="lime",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(pady=10,side=LEFT)
Button(f,text='GET',fg='white',bg='black',command=get,width=10,borderwidth=2,relief="flat",activebackground="lime",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(pady=10,side=LEFT)
Button(f,text='POST',fg='white',bg='black',command=post,width=10,borderwidth=2,relief="flat",activebackground="yellow",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT)
Button(f,text='PUT',fg='white',bg='black',command=put,width=10,borderwidth=2,relief="flat",activebackground="yellow",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT)
Button(f,text='PATCH',fg='white',bg='black',command=patch,width=10,borderwidth=2,relief="flat",activebackground="yellow",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT)
Button(f,text='DELETE',fg='white',bg='black',command=delete,width=10,borderwidth=2,relief="flat",activebackground="white",activeforeground="red",highlightthickness=2, highlightbackground="lime",font='Verdana 10 bold').pack(side=LEFT) 
root.mainloop()
