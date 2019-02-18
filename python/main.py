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


def choose_usb_folder():
    global usbFolder
    usbFolder.set(browse_button())

def check_vars():
    if len(txt_cloudFolder.get()) > 0:
        if len(txt_usbFolder.get()) > 0:
            if len(txt_qrCode.get()) > 0:
                if len(txt_zeit.get()) > 0:
                    return True
                else:
                    messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie das aktuelle Datum und die Uhrzeit im vorgegebenen Format an.')
                    return False
            else:
                messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie eine URL an, auf die der QR Code zeigen soll.')
                return False
        else:
            messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie den Pfad zum USB Stick an.')
            return False
    else:
        messagebox.showinfo('Fehlende Eingabe', 'Bitte geben Sie den Pfad zum You In The Cloud Ordner an.')
        return False


def startScript():
    # print('Start')

    if check_vars():
        p = subprocess.Popen("./start.sh -pc %s -pu %s -q %s -t %s"
            % (txt_cloudFolder.get(),
            txt_usbFolder.get(),
            txt_qrCode.get(),
            txt_zeit.get()), shell=True)

        global process
        process = p

        btn_start.destroy()
        btn_end = ttk.Button(window,text='Beenden', command=stopScript)
        btn_end.grid(column=2,row=7, sticky=W)

    # print('End')


def stopScript():
    if 'process' in globals():
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)

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
window.geometry('665x220')


### Style
ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")


### Cloud Folder
lbl_cloudFolder = Label(master=window,text="Cloud Folder")
lbl_cloudFolder.grid(row=0, column=0, sticky=W)

cloudFolder = StringVar()
txt_cloudFolder = Entry(master=window,width=50,textvariable=cloudFolder,state='disabled')
txt_cloudFolder.grid(row=0, column=1)

btn_cloudFolder = ttk.Button(text="...", command=choose_cloud_folder)
btn_cloudFolder.grid(row=0, column=2)


### USB Folder
lbl_usbFolder = Label(master=window,text="USB Folder")
lbl_usbFolder.grid(row=1, column=0, sticky=W)

usbFolder = StringVar()
txt_usbFolder = Entry(master=window,width=50,textvariable=usbFolder,state='disabled')
txt_usbFolder.grid(row=1, column=1)

btn_usbFolder = ttk.Button(text="...", command=choose_usb_folder)
btn_usbFolder.grid(row=1, column=2)


lbl_empty = Label(master=window,text="")
lbl_empty.grid(row=2, column=0)


### QR Code
lbl_qrCode = Label(master=window,text="QR Code")
lbl_qrCode.grid(row=3, column=0, sticky=W)

txt_qrCode = Entry(window,width=50)
txt_qrCode.grid(row=3, column=1)


### Zeit
lbl_zeit = Label(master=window,text="Datum/Uhrzeit")
lbl_zeit.grid(row=4, column=0, sticky=W)

txt_zeit = Entry(master=window,width=50)
txt_zeit.grid(row=4, column=1)

lbl_zeit = Label(master=window,text="02 FEB 2019 22:22:22")
lbl_zeit.grid(row=5, column=1)


lbl_empty = Label(master=window,text="")
lbl_empty.grid(row=6, column=0)

### Start
global btn_start
btn_start = ttk.Button(window,text='Starten', command=startScript)
btn_start.grid(column=1,row=7, sticky=E)

window.mainloop()
