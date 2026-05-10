from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.geometry("650x400")
root.title("denomination calculator")
root.configure (bg="light blue")
upload = Image.open("app_img.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg = "light blue")
label.place(x = 180, y = 20)
label1 = Label(root, text="hey user, welcome to denomination calculator", bg="light blue")
label1.place(relx=0.5, rely=340, anchor=CENTER)

def msg():
    msgBook = messagebox.showinfo("Alert", " Do you want to calculate the denomination count")
    if msgBook == "ok":
        topwin()

    button1 = Button(root, text="Let's get started", command=msg, bg = "red", fg = "yellow")
    button1.place( x = 260, y = 360)
def topwin():
    top = Toplevel()
    top.title("denomination calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    