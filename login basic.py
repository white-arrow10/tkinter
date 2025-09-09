from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mb # used to give message window

def handle_login():
    name = name_input.get()
    role = role_input.get()
    if name == 'Preet' and role == 'Bowling All-Rounder':
        mb.showinfo("Welcome Sir")
    else:
        mb.showerror ('Not Valid')
        

root = Tk() #root is a variable of Tk class
root.title("Login Form")
root.iconbitmap("IMG.jpg")
#root.minsize(400,400) #similarly maxsize() also works
#geometry used to fix the size
root.geometry ('350x500') 
root.configure(background = 'blue') # hexcode can be used as well

img = Image.open('IMG.jpg')
resized_img = img.resize((150,150))
img = ImageTk.PhotoImage(resized_img) #to add image

#label used to print both text and images on window
#label needs to be expicitly set on window by geometry manager like interior designer
#pack is the geometry manager here
img_label = Label(root,image=img) 
img_label.pack(pady = (10,10))#shifts below pad-y attribute upar neeche thi 10 chodine
text_label = Label(root,text = 'IIT-BHU Cricket',fg = 'white',bg='blue')
text_label.config(font=('garamond',22))
text_label.pack()

name_label = Label(root,text ='Enter Name ',fg = 'white',bg='blue')
name_label.config(font =('verdana',12))
name_label.pack(pady = (20,5))
name_input = Entry(root,width = 50)
#pady = adds space outside the widget vertically.

#ipady = adds space inside the widget vertically.
name_input.pack(ipady = 6,pady=(1,15))

role_label = Label(root,text ='Enter Role',fg = 'white',bg='blue')
role_label.config(font =('verdana',12))
role_label.pack(pady = (20,5))
role_input = Entry(root,width = 50)
role_input.pack(ipady = 6,pady=(1,15))

#command attribute used to add functionality in button in which you can give a fn's name
#note command accepts reference to function not a function call
#no need for parenthesis
login_btn = Button(root,text='Login Here',fg = 'white',bg='blue', width =20,height = 2, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font =('verdana',10))

root.mainloop() # it keeps gui consistently on main window
