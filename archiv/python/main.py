from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import messagebox

import os
import signal
import subprocess

################################################################################
# Methods
################################################################################

def browse_button():
    filename = filedialog.askdirectory() + '/'
    return filename


def choose_cloud_folder():
    global cloudFolder
    cloudFolder.set(browse_button())
    print()


def choose_usb_folder():
    global usbFolder
    usbFolder.set(browse_button())

def check_vars():
    if len(txt_cloudFolder.get()) <= 1:
        messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie den Pfad zum You In The Cloud Ordner an.')
        return False

    if bool_usbFolder.get() == 1:
        if len(txt_usbFolder.get()) <= 1:
            messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie den Pfad zum USB Stick an.')
            return False

    if bool_qrCode.get() == 1:
        if len(txt_qrCode.get()) <= 0:
            messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie eine URL an, auf die der QR Code zeigen soll.')
            return False
        else:
            subprocess.Popen("qrencode -o %sqrcode.png -s 10 %s"
                % (txt_cloudFolder.get(), txt_qrCode.get()), shell=True)

    if bool_zeit.get() == 1:
        if len(txt_zeit.get()) != 20:
            messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie das aktuelle Datum und die Uhrzeit im vorgegebenen Format an.')
            return False
        else:
            subprocess.Popen("sudo date -s %s" % (txt_zeit.get()), shell=True)

    return True



def startScript():
    # print('Start')

    if check_vars():
        if bool_usbFolder.get() == 1:
            p = subprocess.Popen("./start.sh %s %s"
                % (txt_cloudFolder.get(),
                txt_usbFolder.get()), shell=True)
        else:
            p = subprocess.Popen("./start.sh %s"
                % (txt_cloudFolder.get()), shell=True)

        global process
        process = p

        btn_start.destroy()
        global btn_end
        btn_end = ttk.Button(window,text='Beenden', command=stopScript)
        btn_end.grid(row=13, column=2, sticky=E)

    # print('End')


def stopScript():
    if 'process' in globals():
        process.kill()

        btn_end.destroy()
        global btn_start
        btn_start = ttk.Button(window,text='Starten', command=startScript)
        btn_start.grid(row=13, column=2, sticky=E)

#def clicked():
#     subprocess.call("./start.sh", shell=True)
#
# btn = Button(window,text='Click here', command=clicked)
#
# btn.grid(column=0,row=0)


# messagebox.showinfo('Message title', 'Message content')
# res = messagebox.askquestion('Message title','Message content')
# res = messagebox.askyesno('Message title','Message content')
# res = messagebox.askyesnocancel('Message title','Message content')
# res = messagebox.askokcancel('Message title','Message content')
# res = messagebox.askretrycancel('Message title','Message content')

################################################################################
# Main
################################################################################

### Window
window = Tk()
window.title("Fotobox 2.0")
window.geometry('410x360')


### Style
ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")


### Cloud Folder
lbl_cloudFolder = Label(master=window,text="Cloud Folder *")
lbl_cloudFolder.grid(row=0, column=1, sticky=W)

cloudFolder = StringVar()
txt_cloudFolder = Entry(master=window,width=30,textvariable=cloudFolder,state='disabled')
txt_cloudFolder.grid(row=1, column=1)

btn_cloudFolder = ttk.Button(text="...", command=choose_cloud_folder)
btn_cloudFolder.grid(row=1, column=2)

###
lbl_empty = Label(master=window,text="")
lbl_empty.grid(row=2, column=0)

### USB Folder
bool_usbFolder = IntVar()
chb_usbFolder = Checkbutton(master=window, variable=bool_usbFolder)
chb_usbFolder.grid(row=3, column=0)

lbl_usbFolder = Label(master=window,text="USB Folder")
lbl_usbFolder.grid(row=3, column=1, sticky=W)

usbFolder = StringVar()
txt_usbFolder = Entry(master=window,width=30,textvariable=usbFolder,state='disabled')
txt_usbFolder.grid(row=4, column=1)

btn_usbFolder = ttk.Button(text="...", command=choose_usb_folder)
btn_usbFolder.grid(row=4, column=2)

###
lbl_empty = Label(master=window,text="")
lbl_empty.grid(row=5, column=0)


### QR Code
bool_qrCode = IntVar()
chb_qrCode = Checkbutton(master=window, variable=bool_qrCode)
chb_qrCode.grid(row=6, column=0)

lbl_qrCode = Label(master=window,text="QR Code")
lbl_qrCode.grid(row=6, column=1, sticky=W)

txt_qrCode = Entry(window,width=30)
txt_qrCode.grid(row=7, column=1)

###
lbl_empty = Label(master=window,text="")
lbl_empty.grid(row=8, column=0)

### Zeit
bool_zeit = IntVar()
chb_zeit = Checkbutton(master=window, variable=bool_zeit)
chb_zeit.grid(row=9, column=0, sticky=W)

lbl_zeitBool = Label(master=window,text="Datum/Uhrzeit einstellen?")
lbl_zeitBool.grid(row=9, column=1, sticky=W)


lbl_zeit = Label(master=window,text="Datum/Uhrzeit (02 FEB 2019 22:22:22)")
lbl_zeit.grid(row=10, column=1, sticky=W)

txt_zeit = Entry(master=window,width=30)
txt_zeit.grid(row=11, column=1)


###
lbl_empty = Label(master=window,text="")
lbl_empty.grid(row=12, column=0)

### Start
global btn_start
btn_start = ttk.Button(window,text='Starten', command=startScript)
btn_start.grid(row=13, column=2, sticky=E)

window.mainloop()
