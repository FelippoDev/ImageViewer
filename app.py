from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

img_list = [ImageTk.PhotoImage(Image.open('testphoto.jpg')), ImageTk.PhotoImage(Image.open('testphoto2.jpg')),
            ImageTk.PhotoImage(Image.open('testphoto3.jpg')), ImageTk.PhotoImage(Image.open('testphoto4.jpg'))
            ]
n = 0
my_label = Label(image=img_list[n])
my_label.pack()


def forward():
    global n
    global my_label
    if len(img_list) - 1 == n:
        n += 0
    else:
        n += 1

    my_label.pack_forget()
    my_label = Label(image=img_list[n])
    my_label.pack()


def back():
    global n
    global my_label
    if n == 0:
        n += 0
    elif n > 0:
        n -= 1

    my_label.pack_forget()
    my_label = Label(image=img_list[n])
    my_label.pack()


btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_forward = Button(root, text=">>", command=forward)
btn_back = Button(root, text="<<", command=back)

btn_forward.pack()
btn_back.pack()
btn_quit.pack()

root.mainloop()
