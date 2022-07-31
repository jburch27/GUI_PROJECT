"""Created 7/26/22
@author: Julian Burch
"""
# A program that lets the user type in the price of the meals they have order and output the subtotal
import tkinter.messagebox
from tkinter import *

window =Tk()

#This is a function that calls all the food options and accumilates a total once pressing the button
        
def calc():
    #These variables of food indicates that the input is allowed in the text boxes
    Fries=en.get()
    McFlurry=en2.get()
    Mcdouble=en3.get()
    Mcnuggets=en4.get()
    #(input validation, it only works if the inputs are the correct price for each item that is presented on the right side and has to be numbers)
    total=(int(Fries)*2) + (int(McFlurry)*5)+ (int(Mcdouble)*4)+ (int(Mcnuggets)*3)
    label6=Label(window,text= total)
    label6.place(x=100, y=360)






#These are the labels of the food along with menu has the main heading

label_1=Label(window, text="ordered")
#Each label shows coordinates on where it is to be placed on the window
label_1.place(x=550, y=70)

label_2=Label(window, text="fries       $2")
label_2.place(x=450,y=180)


label_3=Label(window, text="mcflurry    $5")
label_3.place(x=450,y=210)

label_4=Label(window, text="mcdouble     $4")
label_4.place(x=450,y=150)

    

label_5=Label(window, text="mcnuggets      $3")
label_5.place(x=450,y=230)



label=Label(window, text="You picked")
label.place(x=70, y=70)







label1=Label(window, text="Fries")
label1.place(x=20, y=120)

en=Entry(window)
en.place(x=20, y=150)



# These are the text boxes for each label food item that must be all filled in order for the program to work
label2=Label(window, text="McFlurry")
label2.place(x=250, y=200)
          

en2=Entry(window)
en2.place(x=250, y=230)


label3=Label(window, text="Mcdouble")
label3.place(x=250, y=120)

en3=Entry(window)
en3.place(x=250, y=150)

label4=Label(window, text="Mcnuggets")
label4.place(x=20, y=200)

en4=Entry(window)
en4.place(x=20, y=230)


#This is a call back from the calc function in order to calculate the inputs

b2=Button(window, text='total', width=20, command=calc)
b2.place(x=100,y=300)

#exit button program

button_quit = Button(window, text="exit program",command =window.destroy).pack()


window.mainloop()


win=Tk() #a new name for the second window
win.title('Welcome') #title of the window
win.geometry('500x200') #size of the window
def func():#function of the button
    tkinter.messagebox.showinfo("Greetings","Thank you for your order! Please come back.")
    
btn=Button(win,text="Click", width=10,height=5,command=func)
btn.place(x=200,y=30)
win.mainloop() #running the loop that works as a trigger





        
