#!/usr/bin/env python
#-*- coding: utf-8 -*-

# © Juan Miguel Segura Fernandez and Alejandro Mallen Gomez
# This is Free Software. License GNU GPLv3

from Tkinter import *
from PIL import Image, ImageTk
import webbrowser

# Interface and title interface
#--------------------------------------------#
interface = Tk()
interface.title("ClamTK")
interface.geometry("850x600")
interface.config(background="#2A0A1B")
title = Label(interface,
    text="ClamTK",
    foreground="#FF0000",
    font="Helveltica 20",
    background="#2A0A1B",)
title.pack()
title.place(x=78, y=15)
#----------------------------------------------#

# Top logo and text
#----------------------------------------------#
logo = ImageTk.PhotoImage(file="img/logo.png")
logo_image = Label(interface,
    image=logo,
    background="#2A0A1B",)
logo_image.pack()
logo_image.place(x=3, y=3)
#---------------------------------------------#

# Left top menu
#---------------------------------------------#

# Web Page
# Web page function
def open_web_page(event):
    webbrowser.open_new("https://www.clamav.net")

# Web page link top label
label_web = Label(interface,
    text="Web Page",
    foreground="white",
    font="Helvetica 12 italic",
    cursor="hand2",
    background="#2A0A1B",
    )
label_web.pack()
label_web.place(x=450, y=20)
# Calls web page function in the label
label_web.bind("<Button-1>", open_web_page)

# Github
# Github function
def open_git_hub(event):
    webbrowser.open_new("https://github.com/Cisco-Talos/clamav-devel")

# Github link top label
label_git_hub = Label(interface,
    text="GitHub",
    background="#2A0A1B",
    foreground="white",
    cursor="hand2",
    font="Helvetica 12 italic",
    )
label_git_hub.pack()
label_git_hub.place(x=550, y=20)
# Calls open_git_hub function in the label
label_git_hub.bind("<Button-1>", open_git_hub)

# Support
# Support link function and Support interface
def open_support(event):
    interface_support = Tk()
    interface_support.pack()

# Support link top label
label_support = Label(interface,
    text="Support",
    background="#2A0A1B",
    foreground="white",
    cursor="hand2",
    font="Helvetica 12 italic",
)

label_support.pack()
label_support.place(x=630, y=20)
label_support.bind("<Button-1>", open_support)

# Themes
# Theme function changes dark or light
def change_theme(event):
    color=textvariable.get()
    print color

#--------------------------------------------#
# Label theme
label_theme=Label(interface,
    text="Theme:",
    background="#2A0A1B",
    foreground="white",
    cursor="hand2",
    font="Helvetica 12 italic"
    )
label_theme.pack()
label_theme.place(x=710, y=20)

# Label of colors
# ----------------
v=StringVar()
# White color image and label
white_color=ImageTk.PhotoImage(file="img/color-blanco.png")
label_white_color=Label(interface, image=white_color, cursor="hand2", textvariable=v("white"))
label_white_color.pack()
label_white_color.place(x=785, y=25)
label_white_color.bind("<Button-1>", change_theme)

# Purpule color image and label
purpule_color=ImageTk.PhotoImage(file="img/color-morado.png")
label_purpule_color=Label(interface, image=purpule_color, cursor="hand2", textvariable="purpule")
label_purpule_color.pack()
label_purpule_color.place(x=800, y=25)
label_purpule_color.bind("<Button-1>", change_theme)

# Black color image and label
black_color=ImageTk.PhotoImage(file="img/color-negro.png")
label_black_color=Label(interface, image=black_color, cursor="hand2", textvariable="black")
label_black_color.pack()
label_black_color.place(x=815, y=25)
label_black_color.bind("<Button-1>", change_theme)


interface.mainloop()
