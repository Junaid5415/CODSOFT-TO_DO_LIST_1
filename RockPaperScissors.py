from tkinter import *
import random

schema = {
    'Rock': {'Rock':1,'Paper':0,'Scissor':2},
    'Paper':{'Rock':2,'Paper':1,'Scissor':0},
    'Scissor':{'Rock':0,'Paper':2,'Scissor':1}
}


comp_score = 0
player_score = 0

def outcome_of_game(arg):
    global comp_score
    global player_score
    outcome = ["Rock","Paper","Scissor"]
    rand_num = random.randint(0,2)
    comp_choice = outcome[rand_num]
    result = schema[arg][comp_choice]

    player_chc_label.config( fg='#8B2500',text='Player Choice :' +str(arg),font=('Arial',10,'bold'))
    comp_chc_label.config(fg='blue',text='Computer Choice :'+str(comp_choice))

    if result == 2:
        player_score += 2
        player_score_label.config(fg='#8B2500',text='Player Score :' +str(player_score))
        comp_chc_label.config(bg="#698B69",text="Computer's Choice :" + str(comp_choice))
        outcome_label.config(fg='yellow',text="Outcome :\nPlayer Won")
    elif result == 1:
        player_score += 1
        player_score_label.config(fg='#8B2500',text='Player Score :' + str(player_score))
        comp_chc_label.config(bg="#698B69", text="Computer's Choice :" + str(comp_choice))
        outcome_label.config(fg='yellow',text="Outcome :\nDraw")
    elif result == 0:
        comp_score += 2
        comp_score_label.config(text='Computer Score :' + str(comp_score))
        outcome_label.config(fg='yellow',text="Outcome :\nComputer Won")


root = Tk()

root.geometry('450x400')

root.maxsize(450,400)
root.minsize(450,400)

root.title("Rock-Paper-Scissors")
root.wm_iconbitmap('rock-paper-scissors.ico')

mf = Frame(root,bg='#698B69',width=450,height=400)
mf.pack()
mf.propagate(0)


# Labels
lbl1 = Label(mf,bg='#698B69',width=35,height=1,text="Welcome To The Game",font=('Arial',10,'italic','bold'))
lbl1.place(x=75,y=20)
lblsel = Label(mf,bg='#698B69',width=35,height=1,text="Please Select Rock, Paper Or Scissor ",
               font=('Arial',10,'italic','bold'))
lblsel.place(x=80,y=45)

player_score_label = Label(root,fg='#8B2500',bg='#698B69',text='Player Score: ' + str(player_score),
                           font=('Arial',10,'bold'))
player_score_label.place(x=15, y=80)

comp_score_label = Label(root,fg='blue',bg='#698B69',text='Computer Score :' + str(player_score),
                         font=('Arial',10,'bold'))
comp_score_label.place(x=270, y=80)


player_chc_label = Label(root,bg='#698B69',fg='#8B2500',text='Player Choice :',font=('Arial',10,'bold'))
player_chc_label.place(x=15, y=115)


comp_chc_label = Label(root,bg='#698B69',fg='blue',text="Computer Choice :",font=('Arial',10,'bold'))
comp_chc_label.place(x=270, y=115)

outcome_label = Label(root,bg='#698B69',fg='yellow',text='Outcome',font=('Arial',10,'bold'))
outcome_label.place(x=180,y=150)


#Buttons
btnRock = Button(mf,text='Rock',height=2,width=10,bg= "#FCFCFC",fg='black',borderwidth=5,
                 font=('Arial',11,'italic','bold'),command=lambda :outcome_of_game('Rock'))
btnRock.place(x=20,y=250)

btnPaper = Button(mf,text='Paper',height=2,width=10,bg= "#FCFCFC",fg='black',borderwidth=5,
                  font=('Arial',11,'italic','bold'),command=lambda :outcome_of_game('Paper'))
btnPaper.place(x=160,y=250)

btnScissor = Button(mf,text='Scissor',height=2,width=10,bg= "#FCFCFC",fg='black',borderwidth=5,
                    font=('Arial',11,'italic','bold'),command=lambda :outcome_of_game('Scissor'))
btnScissor.place(x=300,y=250)

btnquit = Button(mf,text="Quit",height=2,width=8,bg= "#CD3700",fg='black',borderwidth=5,
                 font=('Arial',11,'italic','bold'),command=root.quit)
btnquit.place(x=170,y=310)

root.mainloop()