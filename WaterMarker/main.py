from tkinter import filedialog
from functools import partial
from PIL import ImageDraw, ImageTk
from PIL import Image as pilim
from tkinter import *

BG_A = '#cee5d0'
BG_B = '#f3f0d7'
FG_A = '#d8b384'
FG_B = '#5e454b'


window = Tk()
window.title("Watermarker")
window.config(padx=20, pady=20, bg=BG_A)

image_url_A = StringVar()
image_url_B = StringVar()
water_text = StringVar()
image_A = PhotoImage(file=image_url_A.get())
image_B = PhotoImage(file=image_url_B.get())
image_C = PhotoImage(file=image_url_A.get())


def browseFiles(image_url):
    filename = filedialog.askopenfilename(initialdir='C:/Desktop', title='Select an Image')
    image_url.set(filename)


def change_image_A():
    global image_A
    with pilim.open(image_url_A.get()) as im:
        resized_im = im.resize((100, 100))
        image_A = ImageTk.PhotoImage(resized_im)
    canvas_1.itemconfig(container_1, image=image_A)


def change_image_B():
    global image_B
    with pilim.open(image_url_B.get()) as im:
        resized_im = im.resize((100, 100))
        image_B = ImageTk.PhotoImage(resized_im)
    canvas_2.itemconfig(container_2, image=image_B)


def submit_image_C():
    global image_C
    with pilim.open(image_url_A.get()) as imA:
        with pilim.open(image_url_B.get()) as imB:
            resized_im = imB.resize((50, 50))
            imA.paste(resized_im)
            image_C = ImageTk.PhotoImage(imA)
            text_version = ImageDraw.Draw(imA)
            text_version.text((50,50), water_text.get())
            imA.save('new_image.png')
            image_C = ImageTk.PhotoImage(imA.resize((200,200)))

    canvas_3.itemconfig(container_3, image=image_C)


title_label = Label(text="Watermarking Machine", fg=FG_B, bg=BG_B)
canvas_1 = Canvas(width=100, height=100, bg=BG_B)
canvas_2 = Canvas(width=100, height=100, bg=BG_B)
canvas_3 = Canvas(width=200, height=200, bg=BG_B)
url_A = Entry(window, textvariable=image_url_A)
url_B = Entry(window, textvariable=image_url_B)
water_entry = Entry(window, textvariable=water_text)
search_A = Button(text='...', command=partial(browseFiles, image_url_A))
search_B = Button(text='...', command=partial(browseFiles, image_url_B))
submit_A = Button(text='Submit', command=change_image_A)
submit_B = Button(text='Submit', command=change_image_B)
submit_C = Button(text='Submit', command=submit_image_C)

container_1 = canvas_1.create_image(50, 50, image=image_A)
container_2 = canvas_2.create_image(50, 50, image=image_B)
container_3 = canvas_3.create_image(100, 100,image=image_C)

title_label.grid(column=1, row=0, padx=10, pady=5)
canvas_1.grid(column=0, row=1, rowspan=6)
canvas_2.grid(column=0, row=7, rowspan=6)
canvas_3.grid(column=1, row=1, rowspan=12)
url_A.grid(column=2, row=1)
url_B.grid(column=2, row=2)
water_entry.grid(column=2, row=3)
search_A.grid(column=3, row=1)
search_B.grid(column=3, row=2)
submit_A.grid(column=4, row=1)
submit_B.grid(column=4, row=2)
submit_C.grid(column=2, row=12, columnspan=3)


window.mainloop()
