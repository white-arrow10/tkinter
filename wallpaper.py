from tkinter import *
from PIL import ImageTk,Image
import os #to navigate through files and directories 

def change():
    global counter
    img_label.config(image = img_array[counter%len(img_array)])
    counter +=1

counter = 1
root = Tk()
root.title('Wallpaper Viewer')

root.geometry('250x400')
root.configure(background = 'black')

files = os.listdir("wallpapers")
#for i in files: print (i)
img_array = []
for file in files:
    img = Image.open(os.path.join('wallpapers',file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image = img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(root,text = "Next",bg = 'white',fg = 'black',width = 28,height = 2,command = change)
next_btn.pack()


root.mainloop()
