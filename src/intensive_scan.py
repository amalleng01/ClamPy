#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import os, commands, time
from tkSimpleDialog import askstring

# Create a inteface
interface=Tk()
interface.title("Intensive Scan")
interface.config(background="#2A0A1B")
interface.resizable(0,0)

# Interface in the middle of the screeen
windowWidth = interface.winfo_reqwidth()
windowHeight = interface.winfo_reqheight()
positionRight = int(interface.winfo_screenwidth()/2 - windowWidth)
positionDown = int(interface.winfo_screenheight()/2 - windowHeight)
interface.geometry("850x600+%s+%s"%(positionRight,positionDown))

# Label title
title = Label(interface,
    text="ClamPy",
    foreground="#FF0000",
    font="Helveltica 20",
    background="#2A0A1B",)
title.pack()
title.place(x=78, y=15)

# Top logo and text
logo = ImageTk.PhotoImage(file="img/logo.png")
logo_image = Label(interface,
    image=logo,
    background="#2A0A1B",)
logo_image.pack()
logo_image.place(x=3, y=3)


# Top line
top_line = Canvas(interface,
    width=850,
    height=1.5,
    bg="white"
    )
top_line.pack()
top_line.create_line(0, 0, 200, 200, fill="white")
top_line.place(x=0, y=70)

# Function to go to the menu file ( main.py ).
def return_main_menu():
    interface.destroy()
    from subprocess import call
    call(["python", "main.py"])

# Image an button for back to menu
go_back = ImageTk.PhotoImage(file="img/go-back.png")
main_menu_interface_adblock = Button(interface,
image=go_back,
cursor="hand2",
background="#2A0A1B",
activebackground="#2A0A1B",
command=return_main_menu,
highlightbackground="#2A0A1B"
)
main_menu_interface_adblock.pack()
main_menu_interface_adblock.place(x=780, y=15)


# -----------------------------------
# Function for start scan
def start_scan():
    button_start.destroy()
    # Enter a root password and this, save in a variable
    root_password=askstring("Root", "Enter root password:")
    passwd_correct=commands.getoutput("echo "+root_password+" | sudo -S sudo -s")

    # Label refresh database...
    label_refresh_database=Label(interface, text="Refreshing database...", font="Helvetica 14", bg="#2A0A1B", fg="white")
    label_refresh_database.pack()
    label_refresh_database.place(x=10, y=100)
    # Commands to refresh database
    os.system("sudo systemctl stop clamav-freshclam.service")
    freshclam=os.popen("sudo freshclam").read()
    canvas = Canvas(interface, width=820, height=420, bg="black")
    canvas.pack()
    canvas.create_text(7,7, text=freshclam, fill="white", anchor=NW)
    canvas.place(x=10, y=150)
    os.system("sudo systemctl start clamav-freshclam.service")
    canvas.create_text(7,150, text="Start scan...", fill="green", font="Helvetica 14", anchor=NW)
    # Subprocess
    # time.sleep(5)
    # starting_scan=commands.getoutput("sudo clamscan -r /")
    # canvas.create_text(7,170, text=starting_scan_output, fill="white", font="Helvetica 13", anchor=NW)


# -----------------------------------
# Button start
button_start=Button(interface, text="Start scan", command=start_scan, cursor="hand2", width=15, height=3, font="Helvetica 20 italic bold", fg="white", bg="#890000", activebackground="#890000", activeforeground="black")
button_start.pack()
button_start.place(x=280, y=225)

interface.mainloop()
