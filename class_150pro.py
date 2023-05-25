# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:19:37 2023

@author: kanis
"""

from tkinter import *
import random

root=Tk()
root.title("Coountry and its capital's tour")
root.geometry("400x400")

enter_name = Entry(root)
enter_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)

enter_name1 = Entry(root)
enter_name1.place(relx = 0.5, rely = 0.3, anchor = CENTER)

country_list = Label(root)
capital_list = Label(root)
random_number = Label(root)
lucky_country = Label(root)
lucky_capital = Label(root)

list1 = []
list2 = []
def addcountry():
    country_name = enter_name.get()
    list1.append(country_name)
    country_list["text"] = "Your Country list is : " + str(list1)

def addcapital():
    capital_name = enter_name.get()
    list2.append(capital_name)
    capital_list["text"] = "Your Capital list is : " + str(list2)
    
    
def random_number1():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number["text"] = str(random_no)
    generated_random_number = list1[random_no]
    lucky_country["text"] = "Your lucky country is : " + str(generated_random_number)
 
def random_number2():
    length = len(list2)
    random_no = random.randint(0, length-1)
    random_number["text"] = str(random_no)
    generated_random_number = list2[random_no]
    lucky_capital["text"] = "Your lucky capital is : " + str(generated_random_number)

       
btn = Button(root, text = "Add to the country list", command =  addcountry)
btn.place(relx = 0.5, rely = 0.25, anchor = CENTER)

btn2 = Button(root, text = "Add to the capital list : ", command = addcapital)
btn2.place(relx = 0.5, rely = 0.35, anchor = CENTER)

country_list.place(relx = 0.5, rely = 0.9, anchor = CENTER)
capital_list.place(relx = 0.5, rely = 0.10, anchor = CENTER)

btn1 = Button(root, text = "Who is your lucky country?  ", command = random_number1)
btn1.place(relx = 0.3, rely = 0.5)

btn3 = Button(root, text="Who is your lucky capital?  ", command =  random_number2)
btn3.place(relx = 0.6, rely = 0.5)

random_number.place(relx = 0.5, rely = 0.6, anchor = CENTER)
lucky_country.place(relx = 0.5, rely = 0.7, anchor = CENTER)
lucky_capital.place(relx = 0.5, rely = 0.8, anchor = CENTER)
     
root.mainloop()