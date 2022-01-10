from tkinter import *
import sqlite3
import tkinter.messagebox
from PATDELSU import P_display
from PATDELSU import D_display
from PATDELSU import P_UPDATE
from RooMT import Room_all
from BILLING import BILLING
from employee_reg import emp_screen
from appointment import appo

conn=sqlite3.connect("MDBA.db")
print("DATABASE CONNECTION SUCCESSFUL")

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_gender=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None


#EXIT for MENU
def ex():
    global root1
    root1.destroy()



root = Tk()  
root.geometry("500x400")
    
labelframe1 = LabelFrame(root, text="MENU",font='Times 16 bold italic',fg='grey',width=200)  
labelframe1.pack(fill="both", expand="yes")
toplabel = Label(labelframe1)  
toplabel.grid(padx=10)   
b1 = Button(labelframe1,text="1.PATIENT REGISTRATION",bg='Blue',width = 25, height = 2,font='Times 10 bold italic',fg='white')
b1.grid(pady=5)
b2 = Button(labelframe1, text="2.ROOM ALLOCATION",bg='Blue',fg='white',width = 25, height = 2,font='Times 10 bold italic')
b2.grid(pady=5)
b3 = Button(labelframe1, text="3.EMPLOYEE REGISTRATION",bg='Blue',fg='white',width = 25, height = 2,font='Times 10 bold italic')
b3.grid(pady=5)
b4 = Button(labelframe1, text="4.BOOK APPOINTMENT",bg='Blue',fg='white',width = 25, height = 2,font='Times 10 bold italic')
b4.grid(pady=5)
b5 = Button(labelframe1, text="5.PATIENT BILL",bg='Blue',fg='white',width = 25, height =2,font='Times 10 bold italic')
b5.grid(pady=5)
b6 = Button(labelframe1, text="6.EXIT",bg='Blue',fg='white',width = 25, height = 2,font='Times 10 bold italic')
b6.grid(pady=5)


labelframe2 = LabelFrame(root, text = "Changes You want!!")  
labelframe2.pack(fill="both", expand = "yes")  

bottomlabel = Label(labelframe2)  
bottomlabel.pack()  


p=None

#exit from patient form
def EXO():
    rootp.destroy()

#function for patient form help
def nothing():
    print("CONTACT DATABASE HEAD :921 ")

def nothing1():
    print("MADE BY Tejas")

#PATIENT FORM
back=None
SEARCH=None
DELETE=None
UPDATE=None




   

