# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 09:13:46 2022

@author: Fierce Bird//Ziyah Virani
"""

from tkinter import*
from tkinter import Label
from tkinter import Button
import random

root = Tk()
root.title("COLOR RANDOMIZER GAME")
root.geometry("500x600")
root.configure(bg="AntiqueWhite1")

label_score = Label(root,text = "Score : 0",font=("Bookman Old Style",30,"bold"),bg="AntiqueWhite1",fg="navy")
label_score.place(relx=0.015,rely=0.05 ,anchor =W)

label_name=Label(root,font=("Arial Black",45,"bold"),bg="AntiqueWhite1")
label_name.place(relx=0.5,rely=0.35,anchor=CENTER)

input_value =Entry(root,bg="light cyan",font=("Times New Roman",20,"bold"))
input_value.place(relx = 0.5,rely = 0.6,anchor=CENTER)

class game():
   def __init__(self):
        self.__score = 0
        
   def Updated_Score(self):
        self.text=["Red","Blue","Green","Orange","White","Black","Yellow","Purple","Brown","Gray","Pink","Olive","Maroon","Violet"]
        self.color=["red","blue","hot pink","green","orange","black","yellow","purple","brown","gray","olive","violet","maroon"]
        self.rando_no_for_text = random.randint(0,13) 
        self.rando_no_for_cor = random.randint(0, 12)
        label_name["text"]=self.text[self.rando_no_for_text]
        label_name["fg"]=self.color[self.rando_no_for_cor]

   def __update_score(self,input_value):
        if (input_value == self.color[self.rando_no_for_cor]):
            self.__score = self.__score + random.randint(0,10)
            label_score["text"] = "Score : " + str(self.__score)
            
   def GetUserName(self,input_value):
        self.__update_score(input_value)

obj_1 = game()

def GetInput():
    value = input_value.get()
    obj_1.GetUserName(value)
    obj_1.Updated_Score()
    input_value.delete(0,END)
            
            
btn_check = Button(root, text = " Check ",command = GetInput,bg="red",font=("Times New Roman",25,"bold"))
btn_check.place(relx = 0.35 , rely = 0.7,anchor =CENTER)        
        
btn_start = Button(root, text = "  Start ",command = obj_1.Updated_Score,bg="green",font=("Times New Roman",25,"bold"))
btn_start.place(relx = 0.65 , rely = 0.7,anchor =CENTER)

root.mainloop()

        


	  
	             
        		
            

	  
	  



    
    
    
    
    
    
    
    
