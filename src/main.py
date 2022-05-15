import tkinter
import shutil
import os
import subprocess
import webbrowser
from os import *
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
win=Tk()
win.title("BolSuite")
win.geometry('1000x600')

#Variables
username = os.getlogin()
dvsdir_tpl = ("/media/", os.getlogin(), "/")
dvsdir = "".join(dvsdir_tpl)
udir_tpl = ("/home/", os.getlogin(), "/")
udir = "".join(udir_tpl)
bakat_tpl = ("/home/", os.getlogin(), "/BolBackup/")
bakat = "".join(bakat_tpl)

#Asks for Device Path
dvcdir = fd.askdirectory(initialdir=dvsdir,title="Select your device")
um_tpl = ("umount ", dvcdir)
um = "".join(um_tpl)

#Generates device paths
devmus_tpl = (dvcdir, "/Music/Bol/")
devmus = "".join(devmus_tpl)
devimg_tpl = (dvcdir, "/Images/Bol/")
devimg = "".join(devimg_tpl)
devmp4_tpl = (dvcdir, "/Videos/Bol/")
devmp4 = "".join(devmp4_tpl)

#Zeroes out user paths
musdir = udir
imgdir = udir
mp4dir = udir

#Preloads assets and defs
photo = PhotoImage(file = r"res/fl.png")
synthesis = PhotoImage(file = r"res/mus.png")
imgsync = PhotoImage(file = r"res/img.png")
vidsync = PhotoImage(file = r"res/vid.png")
backup = PhotoImage(file = r"res/bcp.png")

def fm():
     global oppth
     oppth = fd.askopenfilename(initialdir=dvsdir)
     subprocess.call(["xdg-open", oppth])

def help():
     webbrowser.open_new_tab("https://labs-ht.ml/symbolian/docs/sym3")

def chgdr():
     global dvcdir
     dvcdir = fd.askdirectory(initialdir=dvsdir,title="Select your device's root directory")

def umt():
     um_tpl = ("umount ", dvcdir)
     um = "".join(um_tpl)
     os.system(um)
     exit()

#Sync defs
def smu():
     global musdir
     musdir = fd.askdirectory(initialdir=musdir,title="Select the folder containing your music, click Cancel to desync")
     shutil.rmtree(devmus, ignore_errors=True, onerror=None)
     shutil.copytree(musdir, devmus)
     tkinter.messagebox.showinfo("BolSuite","Sync complete!")

def sim():
     global imgdir
     imgdir = fd.askdirectory(initialdir=imgdir,title="Select the folder containing your images, click Cancel to desync")
     shutil.rmtree(devimg, ignore_errors=True, onerror=None)
     shutil.copytree(imgdir, devimg)
     tkinter.messagebox.showinfo("BolSuite","Sync complete!")

def smp():
     global mp4dir
     mp4dir = fd.askdirectory(initialdir=mp4dir,title="Select the folder containing your videos, click Cancel to desync")
     shutil.rmtree(devmp4, ignore_errors=True, onerror=None)
     shutil.copytree(mp4dir, devmp4)
     tkinter.messagebox.showinfo("BolSuite","Sync complete!")

def bcp():
     answer = askyesno(title='Bol Backup', message='Are you sure you want to perform a backup? This process can take several minutes, so please DO NOT close BolSuite until a popup appears. You can only backup one device at a time.')
     if answer:
          shutil.rmtree(bakat, ignore_errors=True, onerror=None)
          shutil.copytree(dvcdir, bakat)
          tkinter.messagebox.showinfo("Bol Backup","Backup complete! saved at /home/user/BolBackup")

#Main UI
btn=Button(win, text = "Manage files", width = 300, height = 500 , image = photo, compound=TOP, command=fm)
btn.place(x=650,y=30)

btn=Button(win, text = "Sync music", width = 200, height = 200 , image = synthesis, compound=TOP, command=smu)
btn.place(x=40,y=30)

btn=Button(win, text = "Sync images", width = 200, height = 200 , image = imgsync, compound=TOP, command=sim)
btn.place(x=350,y=30)

btn=Button(win, text = "Sync videos", width = 200, height = 200 , image = vidsync, compound=TOP, command=smp)
btn.place(x=40,y=328)

btn=Button(win, text = "Backup", width = 200, height = 200 , image = backup, compound=TOP, command=bcp)
btn.place(x=350,y=328)

mn = Menu(win) 
win.config(menu=mn)

file_menu = Menu(mn)
mn.add_cascade(label='Device', menu=file_menu) 
file_menu.add_command(label='Change selected device', command=chgdr)  
file_menu.add_command(label='Unmount', command=umt)

help_menu = Menu(mn) 
mn.add_cascade(label='Help', menu=help_menu) 
help_menu.add_command(label='SymbolianDocs: Symbian^3', command=help)

win.mainloop()
