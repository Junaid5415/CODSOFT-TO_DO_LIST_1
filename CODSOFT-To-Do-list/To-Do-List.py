from tkinter import * # import tkinter library for GUI

tasks = [] # Create A global list to store task in it

class start: # I Used OOPS concept here and learned somethings new

    def __init__(self,root): # Initialize all these property

        global tasks # by using global I can access the global object \ variable

        self.root = root
        self.root.config(bg='lightblue')
        self.root.geometry('450x350')
        self.root.title('To-Do-List')
        self.root.iconbitmap('brain.ico')
        self.root.minsize(450,350)
        self.root.maxsize(450,350)

        self.txtbox = Text(self.root,height=12,width=35,font=('aerial',11,'bold'))
        self.txtbox.place(x= 10, y=25)

        self.ent = Entry(root,width=53,font=('aerial',11,'bold'))
        self.ent.place(x=10,y=290)

        self.lbl1 = Label(text="Enter Your Task Here 🡓 ",bg='lightblue',foreground='black',font=('aerial',13,'bold'))
        self.lbl1.place(x= 10,y= 260)

        self.lbl2 = Label(text="⦚ COMMANDS ⦚", bg='lightblue',fg='black',font=('aerial',12,'bold'))
        self.lbl2.place(x=320,y=10)

        self.btnadd = Button(root,height=2,width=14,text="ADD TASK",command=self.Add_Tasks,bg="white",fg='black',
                             font=('aerial',9,'bold'))
        self.btnadd.place(x=325,y=45)

        self.btnshow = Button(root,height=2,width=14,text="SHOW TASK",command=self.Show_Tasks,bg="white",fg='black',
                              font=('aerial',9,'bold'))
        self.btnshow.place(x=325,y=95)

        self.btncomp = Button(root,height=2,width=14,text="COMPLETE TASK",command=self.Comp_Task,bg="white",fg='black',
                              font=('aerial',9,'bold'))
        self.btncomp.place(x=325,y=145)

        self.btnquit = Button(root,height=2,width=14,text="QUIT",command=root.quit,bg="white",fg='black',
                              font=('aerial',9,'bold'))
        self.btnquit.place(x=325,y=195)

        self.root.bind('<Escape>',self.Quit) # Bind the 'Escape' key quit the root

        self.ent.bind('<Return>', self.Enter_press) # Bind the 'Enter' key to add task

    def Quit(self,event): # Method to quit the root using "Escape" key
        self.root.quit()

    def Enter_press(self,event): # Method to add tasks using "Enter" key
        self.Add_Tasks()

    def Add_Tasks(self): # Method to add task in the global variable

        task = self.ent.get() # It will get the value of self.ent object

        if task: # If is greater than 0 then this code block is executed
            tasks.append(task)
            self.txtbox.delete('1.0',"end")
            self.txtbox.insert(END,f'Task Added : {task}\n')
            self.ent.delete(0,'end')
        else:
            self.txtbox.insert('end',"Please Enter A Task!\n")
            self.txtbox.delete('end')

    def Show_Tasks(self): # This method is used to show the all the task

        self.txtbox.delete('1.0', END)
        if not tasks: # if there is no task in tasks textbox will print "No Task!"
            self.txtbox.insert(END, "No Task!\n")
        else: # if there is task in tasks, this code block will execute
            for i, task in enumerate(tasks, 1):
                self.txtbox.insert(END, f"{i}. {task}\n")

    def Comp_Task(self): # This method is used to mark a task as completed

        self.Show_Tasks() # when Comp_Tas() is execute it will first execute the Show_Task method.

        self.txtbox.delete('1.0','end')
        try: # Try and Exception code block
            tasks_ind = int(self.ent.get())-1

            if 0 <= tasks_ind < len(tasks):
                '''if "tasks_ind" is greater or equal 0 and 
                    lesser than the length of tasks the below code will execute'''

                Completed_Task = tasks.pop(tasks_ind)
                ''' Whatever the value we enter in entry box will be pop and given 
                    to Completed_Task only when Comp_Task is called'''

                self.ent.delete(0, "end")
                # self.Show_Tasks()
                self.txtbox.insert(END,f"Task '{Completed_Task}' Is Marked As Completed.\n")
                self.txtbox.insert('end',f'{tasks}\n')
            else:
                self.txtbox.insert(END,"Invalid Task Number!\n")

        except ValueError: # if ValueError found it will be handled by exception handler

            self.txtbox.insert(END,"Invalid Input, Please Enter Valid Task Number!\n")
            self.txtbox.insert('end',f'{tasks}')



root = Tk() # main window
app = start(root) # creates a instance of the start class
root.mainloop()


