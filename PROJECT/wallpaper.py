from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_img():
    global counter
    image_lebel.config(image=img_array[counter%len(img_array)])
    counter +=1
    pass

counter = 1
root = Tk()
root.title("Wallpaper APP")
root.geometry("500x500")
root.configure(bg="black")

files =os.listdir("Wallpaper")
img_array = []
for file in files:
    img =Image.open(os.path.join('Wallpaper',file))
    resize_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resize_img))

image_lebel = Label(root,image= img_array[0])
image_lebel.pack(pady=40)

nxt_btn = Button(root ,text="Next",fg="black",bg="white",width=20,height=2,command=rotate_img)
nxt_btn.pack()

root.mainloop()