from tkinter import *

#create a global variable to store value
calculation = ""

#function to show text
def add_to_calc(para):
    global calculation
    calculation +=str(para)
    text_ent.delete(1.0,'end')
    text_ent.insert(1.0,calculation)

#funtion to do calculations
def evalute_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_ent.delete(1.0,'end')
        text_ent.insert(2.0,calculation)
    except:
        clear_field()
        text_ent.insert(1.0,'Error')

def clear_field():
    global calculation
    calculation = ''
    text_ent.delete(1.0,'end')

def one_back():
    global calculation
    calculation = ''
    text_ent.delete(1.0)

#creating root
root = Tk()
root.geometry('350x500')
root.maxsize(350,500)
root.minsize(350,500)
root.title('Calculator')
root.wm_iconbitmap('Calculate.ico')

can = Canvas(root,width=350,height=500,bg='#E6E6FA').pack()

#initializing frame
mf = Frame(root,bg='#515151',highlightcolor='blue',width=310,height=70,highlightthickness=1)
mf.place(x= 20,y=15)

#initializing label
Label1 =Label(font=("Arial",14,'bold'),height=2,width=24)
Label1.pack(padx= 10,pady= 25)

#initializing entry box
# mynum = IntVar
text_ent = Text(can,width=13,height=1,fg='#1E1E1E',font=("Arial",30,'bold'))
text_ent.place(x= 30,y=23)

#initializing button 9
btn9 = Button(text='9',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(9))
btn9.place(x= 160,y=230)

#initializing button 8
btn8 = Button(text='8',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(8))
btn8.place(x= 90,y=230)

#initializing button 7
btn7 = Button(text='7',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(7))
btn7.place(x= 20,y=230)

#initializing button 6
btn6= Button(text='6',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(6))
btn6.place(x= 160,y=290)

#initializing button 5
btn5 = Button(text='5',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(5))
btn5.place(x= 90,y=290)

#initializing button 4
btn4 = Button(text='4',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(4))
btn4.place(x= 20,y=290)

#initializing button 3
btn3 = Button(text='3',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(3))
btn3.place(x= 160,y=350)

#initializing button 2
btn2 = Button(text='2',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(2))
btn2.place(x= 90,y=350)

#initializing button 1
btn1 = Button(text='1',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(1))
btn1.place(x= 20,y=350)

#initializing button 0
btn0 = Button(text='0',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(0))
btn0.place(x= 90,y=410)

#initializing button 'C'
btnC = Button(text='C',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=clear_field)
btnC.place(x= 20,y=410)

#initializing button '.'
btndot = Button(text='.',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc('.'))
btndot.place(x= 160,y=410)

#initializing button equal
btneql = Button(text='=',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=evalute_calculation)
btneql.place(x= 250,y=410)

#initializing button plus
btnplus = Button(text='+',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc('+'))
btnplus.place(x= 250,y=350)

#initializing button multiply
btnmul = Button(text='x',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc('*'))
btnmul.place(x= 250,y=290)

#initializing buttin subtraction
btnsub = Button(text='-',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc('-'))
btnsub.place(x= 250,y=230)

#initializing button division
btndiv = Button(text='/',width=8,height=3,bg="#515151",fg='#FFFFFF',command=lambda :add_to_calc('/'))
btndiv.place(x= 250,y = 170)

#initializing button back
btnback = Button(text='Back',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=one_back)
btnback.place(x= 160,y = 170)

#initializing button ')'
btnRpara = Button(text=')',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc(')'))
btnRpara.place(x= 90,y=170)

#initializing button '('
btnLpara = Button(text='(',width=8,height=3,bg="#515151",fg= "#FFFFFF",command=lambda :add_to_calc('('))
btnLpara.place(x= 20,y=170)

root.mainloop()
