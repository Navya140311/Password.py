from tkinter import*
import random

root=Tk()
root.title("Password Generator")
root.geometry("500x500")

label_password=Label(root)

label_guessed_password=Label(root)
input_1= Entry(root)
array_3d=[[[1,2,3,4,5,6],["King","Queen"],["&","$","@","#","!","~",";",":"]]]

def new_password():
    value= input_1.get()
    random_no_1=random.randint(0,5)
    random_no_2=random.randint(0,1)
    random_no_3=random.randint(0,7)
    
    letter_1=str(array_3d[0][0][random_no_1])
    letter_2=str(array_3d[0][1][random_no_2])
    letter_3=str(array_3d[0][2][random_no_3])
    
    label_password["text"]="Your new password is : " + letter_1 + "" +letter_2 + ""+ letter_3 + "\n Note never share or tell anyone your password in any case"
    label_guessed_password["text"]="Guessed Password :" + str(value)
    


input_1.place(relx=0.5,rely=0.2, anchor=CENTER)
label_guessed_password.place(relx=0.5,rely=0.3,anchor=CENTER)

btn1 = Button(root, text=" Generate password!  ", command = new_password)
btn1.place(relx= 0.5, rely = 0.5, anchor= CENTER )

label_password.place(relx=0.5, rely = 0.8, anchor= CENTER)
root.mainloop()