# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 09:13:46 2022

@author: Fierce Bird//Ziyah Virani
"""

from tkinter import*
from tkinter import ttk
import random

root = Tk()
root.title("COLOR RANDOMIZER GAME")
root.geometry("500x600")
root.configure(bg="AntiqueWhite1")

label=Label(root,font=("Britannic Bold",25,"bold"),bg="AntiqueWhite1")
label.place(relx=0.5,rely=0.5,anchor=CENTER)

class game():
   def __init__(self):
        self.__score = 0
        
   def Updated_Score(self):
        self.text=["Red","Blue","Green","Orange","White","Black","Yellow","Purple","Brown","Gray","Pink","Olive","Maroon","Violet"]
        self.rando_no_for_text = random.randint(0,13)
        self.color=["red","blue","hot pink","green","orange","white","black","yellow","purple","brown","gray","olive","violet","maroon"] 
        label["text"]=self.text[self.rando_no_for_text]
        label["fg"]=self.color[self.rando_no_for_text]

        
        
        
        
obj_1 = game()

btn_1 = Button(root, text = "Start",command = obj_1.Updated_Score,bg="green")
btn_1.place(relx = 0.7 , rely = 0.6,anchor =CENTER)

root.mainloop()

        


	  
	             
        		
            

	  
	  



    
    
    
    
    
    
    
    
