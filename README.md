# ImageViewer
Simple image app viewer written in Python using Tkinter


In the GIF below we have a demonstration of the app being executed




![Image_Viewer](https://user-images.githubusercontent.com/65267252/114647207-14faec80-9cb3-11eb-80c6-3b17c86967b9.gif)

The following code shows all the images that are going to be used in the app are being stored in the list `img_list`, using the module `PIL` to open the images. After that we use the function `Label` to put the images in the GUI.



```python
img_list = [ImageTk.PhotoImage(Image.open('testphoto.jpg')), ImageTk.PhotoImage(Image.open('testphoto2.jpg')),
            ImageTk.PhotoImage(Image.open('testphoto3.jpg')), ImageTk.PhotoImage(Image.open('testphoto4.jpg'))
            ]
n = 0
my_label = Label(image=img_list[n])
my_label.grid(row=0, column=0, columnspan=3)
```



In the code below we are defining the layout of the buttons that will appear in the app.




```python
btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_forward = Button(root, text=">>", command=forward)
btn_back = Button(root, text="<<", command=back)

btn_forward.grid(row=1, column=2)
btn_back.grid(row=1, column=0)
btn_quit.grid(row=1, column=1, pady=10)

status = Label(root, text=f"Image {n+1} of {len(img_list)}", relief=SUNKEN, bd=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

```


The function forward is the function that will be called has the command when the button `btn_forward` is clicked. In this function, we define how the button when is being clicked will react, if the `n` (that is the variable which tells in what index of the list we are on, in other words, says in what image is being shown) is equal to the length of the list `img_list` then when the button is clicked the `n` variable will receive 0 so it will not change to the next photo cause is already in the last photo to be shown. Now, if the length is not equal to `n` so we can pass it to the next photo.
```python
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
```

In the `back` function we have the same principles as the `forward` function but with the difference that if `n` is equal to 0 it means that we are in the first photo so we won't be able to go back and if it's not, the value stored in `n`  will be subtracted by -1 so it will be able to go to the previous image.

```python
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
```


## Contributors
@[FelippoDev](https://github.com/FelippoDev)
