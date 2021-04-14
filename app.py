from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

img_list = [ImageTk.PhotoImage(Image.open('testphoto.jpg')), ImageTk.PhotoImage(Image.open('testphoto2.jpg')),
            ImageTk.PhotoImage(Image.open('testphoto3.jpg')), ImageTk.PhotoImage(Image.open('testphoto4.jpg'))
            ]
n = 0
my_label = Label(image=img_list[n])
my_label.grid(row=0, column=0, columnspan=3)


def forward():
    global n
    global my_label
    if len(img_list) - 1 == n:
        n += 0
    else:
        n += 1

    my_label.grid_forget()
    my_label = Label(image=img_list[n])
    my_label.grid(row=0, column=0, columnspan=3)


def back():
    global n
    global my_label
    if n == 0:
        n += 0
    elif n > 0:
        n -= 1

    my_label.grid_forget()
    my_label = Label(image=img_list[n])
    my_label.grid(row=0, column=0, columnspan=3)


btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_forward = Button(root, text=">>", command=forward)
btn_back = Button(root, text="<<", command=back)

btn_forward.grid(row=1, column=2)
btn_back.grid(row=1, column=0)
btn_quit.grid(row=1, column=1)

root.mainloop()
