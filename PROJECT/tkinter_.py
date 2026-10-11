from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email =="agamsaxena59@gmail.com" and password =="1234":
        messagebox.showinfo("User info","Login Succesfully")
    else:
        messagebox.showwarning("ERROR","Login Failed")

    
    

root  = Tk() # Root is object of Tk class
root.title("GUI LOGIN ") # Title of the window
root.iconbitmap("C:\\Users\\Agam\\OneDrive\\Desktop\\AI\\PROJECT\\Tkinter AI Portrait Icon.ico") # Icon of the window
root.geometry("600x500") # Size of the window
root.configure(bg="#2874F0") # Background color of the window
# Image of the window
img_resized = Image.open("C:\\Users\\Agam\\OneDrive\\Desktop\\AI\\PROJECT\\download (1).jpg") # Image of the window
img_resized = img_resized.resize((100, 100),) # Resize the image
img = ImageTk.PhotoImage(img_resized) # Image of the window

img_label = Label(root, image=img) # Label is used to display the image
img_label.pack(pady=40) # Pack is used to display the label

# flipkart text label
text_Label = Label(root, text="Flipkart",fg="White",bg="#2874F0")
text_Label.pack(pady=10) # Pack is used to display the label
text_Label.config(font=("Verdana", 24)) # Font of the label


# Login Form
# email segment
email_label = Label(root, text="Email",fg="White",bg="#2874F0") # Label is used to display the text
email_label.pack(pady=10,padx=10) # Pack is used to display the label
email_label.config(font=("Verdana", 12)) # Font of the label

# Email Input

email_input = Entry(root,width=30)
email_input.pack(ipady=6,pady=(1,14))

# email segment
password_label = Label(root, text="Password",fg="White",bg="#2874F0") # Label is used to display the text
password_label.pack(pady=10,padx=10) # Pack is used to display the label
password_label.config(font=("Verdana", 12)) # Font of the label

# Email Input

password_input = Entry(root,width=30)
password_input.pack(ipady=6,pady=(1,14))

# login

login_btn = Button(root,text="Login Here",fg="White",bg="#2874F0",command=handle_login)
login_btn.pack(pady=5)
login_btn.config(font=('verdana',10))






root.mainloop() # It is the method of Tk class which is used to run the application and wait for events. It is an infinite loop that keeps the application running until the user closes it. 


