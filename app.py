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
    global status

    if len(img_list) - 1 == n:
        n += 0
    else:
        n += 1

    my_label.grid_forget()
    my_label = Label(image=img_list[n])
    my_label.grid(row=0, column=0, columnspan=3)

    status.grid_forget()
    status = Label(root, text=f"Image {n+1} of {len(img_list)}", relief=SUNKEN, bd=1)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back():
    global n
    global my_label
    global status

    if n == 0:
        n += 0
    elif n > 0:
        n -= 1

    my_label.grid_forget()
    my_label = Label(image=img_list[n])
    my_label.grid(row=0, column=0, columnspan=3)

    status.grid_forget()
    status = Label(root, text=f"Image {n+1} of {len(img_list)}", relief=SUNKEN, bd=1)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_forward = Button(root, text=">>", command=forward)
btn_back = Button(root, text="<<", command=back)

btn_forward.grid(row=1, column=2)
btn_back.grid(row=1, column=0)
btn_quit.grid(row=1, column=1, pady=10)

status = Label(root, text=f"Image {n+1} of {len(img_list)}", relief=SUNKEN, bd=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
