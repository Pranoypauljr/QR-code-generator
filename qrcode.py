from tkinter import *
import requests
from PIL import ImageTk, Image


root = Tk()
root.title('QR Code Generator')
root.geometry('680x600')
root.iconbitmap('qrcode.ico')


def find_qr():

    for i in root.grid_slaves():
        if type(i) == Label:
            i.destroy()

    try:
        a = link.get()
        b = user_name.get()
        c = file_name.get()

        r = requests.get(
            'https://chart.googleapis.com/chart?cht=qr&chl=' + a + '&chs=200x200')

        file = open("C:/Users/"+b+"/"+c+".jpg", "wb")
        file.write(r.content)
        file.close()

        img = PhotoImage(file="C:/Users/" + b + "/" + c + ".jpg")
        l = Label(image=img)
        l.image = img
        l.grid(row=15, column=0)

    except:
        Label(root, text='Please enter  valid details.',
              fg='red').grid(row=11, column=0)

    # Label(root).grid(row=11, column=0)

    # img = PhotoImage(file="C:/Users/" + b + "/" + c + ".jpg")
    # l = Label(image=img)
    # l.image = img
    # l.grid(row=15, column=0)

    link.delete(0, END)
    user_name.delete(0, END)
    file_name.delete(0, END)


link_label = LabelFrame(root, text='Enter the text', pady=5,
                        relief=FLAT, font=('Helvetica', 10))
link_label.grid(row=0, column=0)

link = Entry(link_label, borderwidth=4, width=50, font=('Helvetica', 18))
link.grid(row=1, column=0)


# Label(root).grid(row=2, column=0)
# Label(root).grid(row=3, column=0)

user_name_label = LabelFrame(root, text='Enter the username of your system.', pady=5,
                             relief=FLAT, font=('Helvetica', 10))
user_name_label.grid(row=4, column=0)


user_name = Entry(user_name_label, borderwidth=4,
                  width=50, font=('Helvetica', 18))
user_name.grid(row=5, column=0)

# Label(root).grid(row=6, column=0)
# Label(root).grid(row=7, column=0)

file_name_label = LabelFrame(root, text='What do you want to save it as?', pady=5,
                             relief=FLAT, font=('Helvetica', 10))
file_name_label.grid(row=8, column=0)

file_name = Entry(file_name_label, borderwidth=4,
                  width=50, font=('Helvetica', 18))
file_name.grid(row=9, column=0)

sub_button = Button(root, text='Submit', width=10,
                    height=2, borderwidth=3, command=find_qr)
sub_button.grid(row=10, column=0)

color_canvas = Canvas(root, width=680, height=700, bg='grey')
color_canvas.grid(row=16, column=0)


root.mainloop()
