from tkinter import *
import tkinter as tk
import gsi,gsi_unom_instruction,gsi_unom_contact
root = Tk()
root.geometry('1920x1080')
root.configure(bg='#8d5524')
root.title("GRADING SNIPPET AND INVESTIGATOR - UNIVERSITY OF MADRAS")
def command():
   x=regno.get(1.0,END).split("\n")
   s=sheet.get()
   f=file.get()
   p=path.get()
   l=link.get()
   d=dob.get(1.0,END).split("\n")
   while("" in x and d):
      x.remove('')
      d.remove('')
      gsi.gsi(x,d,s,f,p,l)
   for a,b in zip(gsi.an,gsi.ab):
         na=a
         re=b
         op_text.insert(INSERT, na+" "+re+"\n")
def inst():
   gsi_unom_instruction.ins()
def contac():
   gsi_unom_contact.cont()
ins_button = tk.Button(root, text="INSTRUCTONS", bg="grey", font=(
    "serif", 12, 'bold'), activebackground="#E2DFD2", command=inst)
ins_button.place(x=10, y=20)
contact_button = Button(root, text="CONTACT",bg="grey", font=(
    "serif", 12, 'bold'), activebackground="#E2DFD2", command=contac)
contact_button.place(x=150, y=19.5)
button = Button(root, text="OK", bg="grey", font=(
    "serif", 12, 'bold'), activebackground="#E2DFD2", command=command)
head = Label(text = "GRADING SNIPPET AND INVESTIGATOR - UNIVERSITY OF MADRAS",font=20,fg="#000").place(x = 430,y = 20)
auth= Label(text = "AUTHOR : DINEESH R").place(x = 1190,y = 20)
regno = Text(root,width=30,height=20)
regno.place(x=40, y=300)
dob = Text(root,width=30,height=20)
dob.place(x=320, y=300)
button.place(x=650, y=650)
link_ = Label(text = "LINK :").place(x = 40,y = 110) 
link = Entry(root)
link.place(x=170, y=110)
sheet_name = Label(text = "SHEET NAME :").place(x = 40,y = 140) 
sheet = Entry(root)
sheet.place(x=170, y=140)
file_name = Label(text = "FILE NAME :").place(x = 40,y = 170)
file = Entry(root)
file.place(x=170, y=170)
path_ = Label(text = "PATH TO LOCATION :").place(x = 40,y = 200)
path = Entry(root)
path.place(x=170, y=200)
reg= Label(text = "REGISTRATION NUMBERS").place(x = 80,y = 250)
dobl= Label(text = "DATE OF BIRTH").place(x = 390,y = 250)
opt= Label(text = "REFERENCE BOX").place(x = 950,y = 250)
op_text = Text(root, height=20, width=70)
op_text.place(x=720,y=300)
root.mainloop()