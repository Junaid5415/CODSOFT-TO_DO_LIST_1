import random
from tkinter import *
import string



def randkey(length):

    char = string.ascii_letters + string.digits + string.punctuation
    pass1  = ''.join(random.choice(char) for i in range(length))
    return pass1

def pass_button_click():
    try:
        pass1_length = int(Len_of_pass.get())
        random_pass1 = randkey(pass1_length)
        Pass_Label.config(text='Pass = ' + str(random_pass1))
    except Exception as E:
        Error_Label.config(text='Please Enter Value:\n ' + str(E),font=('arial',8,'bold'))
def bind_return(event):
    pass_button_click()


root = Tk()
root.geometry('350x200')

root.title('Random Pass Generator')
root.config(bg='black')

root.maxsize(350,200)
root.minsize(350,200)

root.wm_iconbitmap('GRP.ico')

Label(text='Welcome To Password Generator',bg='black',fg='white',font=('arial',11,'bold')).place(x=50,y=0)


label_input = Label(root,bg='black' ,text='Enter The Length Of Password: ',fg='white',font=('arial',9,'bold'))
label_input.place(x= 5, y= 30)

Len_of_pass = Entry(bg='WHITE',fg='black',font=('arial',10,'bold'))
Len_of_pass.place(x=190,y=30)

Pass_Label = Label(text="Pass = ",bg='black',fg='white',font=('arial',12,'bold'))
Pass_Label.place(x=10,y=130)

Error_Label = Label(bg='black',fg='white',font=('arial',8,'bold'))
Error_Label.place(x= 65,y=160)

Gen_button = Button(width=14,height=1,text="Generate Pass",font=('arial',10,'bold'),command=pass_button_click)
Gen_button.place(x=190,y=70 )
root.bind('<Return>',bind_return)

root.mainloop()
