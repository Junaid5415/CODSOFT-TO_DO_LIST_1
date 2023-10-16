from tkinter import *

class Contacts:
    def __init__(self,root):
        self.root = root
        self.root.config(bg='black')
        self.root.geometry("400x340")
        self.root.maxsize(400,340)
        self.root.minsize(400,340)
        self.root.wm_iconbitmap('Contact.ico')
        self.root.title("Contacts")

        self.contact = [] # Initialize A Variable To Store Data

        # Initialize the labels and entry box and place them
        self.name = Label(text='Name:',bg='black',fg='white',font=('aerial',10,'italic'))
        self.name.place(x= 10,y=10)

        self.name_ent = Entry(bg='white',fg='black',font=('aerial',10,'italic'))
        self.name_ent.place(x=70,y=10)

        self.num = Label(text='Number:',bg='black',fg='white',font=('aerial',10,'italic'))
        self.num.place(x=10,y= 50)

        self.num_ent = Entry(bg='white',fg='black',font=('aerial',10,'italic'))
        self.num_ent.place(x=70,y=50)

        self.add = Label(text='Address:',bg='black',fg='white',font=('aerial',10,'italic'))
        self.add.place(x= 10,y= 90)

        self.add_ent = Entry(bg='white', fg='black', font=('aerial', 10, 'italic'))
        self.add_ent.place(x=70, y=90)


        self.mail = Label(text='Email:',bg='black',fg='white',font=('aerial',10,'italic'))
        self.mail.place(x= 10, y=130)

        self.mail_ent = Entry(bg='white', fg='black', font=('aerial', 10, 'italic'))
        self.mail_ent.place(x=70, y=130)

        # Initialize a Listbox widget to show the stored data
        self.list_box = Listbox(root,selectmode=SINGLE,height=15,width=28)
        self.list_box.place(x= 220,y=10)

        # Create Buttons
        self.btn_add = Button(text='Add Contact',width=10,height=2,command=self.Add_Con ,font=('aerial', 10, 'italic'))
        self.btn_add.place(x= 10, y =190)

        self.btn_shw = Button(text='View Contacts',width=10,height=2,command=self.View_Con ,font=('aerial', 10, 'italic'))
        self.btn_shw.place(x= 120, y =190)

        self.btn_src= Button(text='Search Contacts', width=12, height=2,command=self.Search_Con,font=('aerial', 10, 'italic'))
        self.btn_src.place(x=10, y=270)

        self.btn_del = Button(text='Delete Contact',width=12,height=2,command=self.Delete_Con,font=('aerial',10,'italic'))
        self.btn_del.place(x= 140,y=270)

        self.btn_upd = Button(text='Update Contact', width=12, height=2,command=self.Update_Con,font=('aerial', 10, 'italic'))
        self.btn_upd.place(x=270, y=270)


    # Create Methods To Bind With Button

    def Add_Con(self): # This Method Add's Contact To The List
        name = self.name_ent.get()
        number = self.num_ent.get()
        email = self.mail_ent.get()
        address = self.add_ent.get()
        con_info = (name, number, email, address)
        self.contact.append(con_info)
        self.Clear_ent()


    def View_Con(self): # This Method Show's All The Stored Contact's In The List
        self.list_box.delete(0,END)
        for con in self.contact:
            name, number, _, _ = con
            self.list_box.insert(END,f"{name},{number}")


    def Search_Con(self): # This Method Searches For The Name In The List
        search = self.name_ent.get()
        self.list_box.delete(0,END)
        for con in self.contact:
            name,number, _, _ = con
            if search in name:
                self.list_box.insert(END, f'{name},{number}')



    def Update_Con(self): # This Method Update's The Conatact List
        select_index = self.list_box.curselection()
        if select_index:
            select_index = int(select_index[0])
            name = self.name_ent.get()
            number = self.num_ent.get()
            mail = self.mail_ent.get()
            address = self.add_ent.get()
            self.contact[select_index] = (name,number,mail,address)
            self.Clear_ent()


    def Delete_Con(self): # This Method Deletes The Contact
        select_index = self.list_box.curselection()
        if select_index:
            select_index = int(select_index[0])
            del self.contact[select_index]
            self.Clear_ent()


    def Clear_ent(self): # It Is Use To Clear All The Entry Box's
        self.name_ent.delete(0,END)
        self.num_ent.delete(0,END)
        self.mail_ent.delete(0,END)
        self.add_ent.delete(0,END)


if __name__ == '__main__': # This Code Will Run In This Module Only
    root = Tk()
    app = Contacts(root)
    root.mainloop()