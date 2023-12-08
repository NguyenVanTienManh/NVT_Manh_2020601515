from tkinter import filedialog

import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Hàm xử lý sự kiện khi nút "Chọn ảnh" được nhấn
def open_image():
    global input_image
    file_path = filedialog.askopenfilename()
    if file_path:
        input_image = cv2.imread(file_path)
        update_image(input_image)

# Hàm xử lý sự kiện khi nút "Làm mịn ảnh" được nhấn
def smooth_image():
    global input_image
    if input_image is not None:
        sigma = 1.5  # Độ lệch chuẩn cố định
        output_image = cv2.GaussianBlur(input_image, (5, 5),sigma)
        update_image(output_image)

# Hàm cập nhật hiển thị ảnh trên giao diện
def update_image(image, image_label=None):
    if image is not None:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image

win = Tk()
win.title("Lam min anh")
win.geometry('500x500')
win.attributes('-topmost',True)

but1 = Button(win, text= "Chon anh", command=open_image)
but1.place(x=50,y=70)

but2 = Button(win, text="Lam min anh",command=smooth_image)
but2.place(x=50,y=90)

win.mainloop()