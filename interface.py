#!/usr/bin/env python
#-*- coding: utf-8 -*-

# © Juan Miguel Segura Fernandez and Alejandro Mallen Gomez
# This is Free Software. License GNU GPLv3.

from Tkinter import *
from PIL import Image, ImageTk
import webbrowser

# Interface and title interface
interface = Tk()
interface.title("ClamPy")
interface.config(background="#2A0A1B")
interface.resizable(0,0)

# Interface in the middle of the screeen
windowWidth = interface.winfo_reqwidth()
windowHeight = interface.winfo_reqheight()
positionRight = int(interface.winfo_screenwidth()/2 - windowWidth)
positionDown = int(interface.winfo_screenheight()/2 - windowHeight)
interface.geometry("850x600+%s+%s"%(positionRight,positionDown))

title = Label(interface,
    text="ClamPy",
    foreground="#FF0000",
    font="Helveltica 20",
    background="#2A0A1B",)
title.pack()
title.place(x=78, y=15)

# Top logo and text
#----------------------------------------------#
logo = ImageTk.PhotoImage(file="img/logo.png")
logo_image = Label(interface,
    image=logo,
    background="#2A0A1B",)
logo_image.pack()
logo_image.place(x=3, y=3)

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
label_github = Label(interface,
    text="GitHub",
    background="#2A0A1B",
    foreground="white",
    cursor="hand2",
    font="Helvetica 12 italic",
    )
label_github.pack()
label_github.place(x=550, y=20)
# Calls open_git_hub function in the label
label_github.bind("<Button-1>", open_git_hub)

# ---------------------------------------
#          Support
# Support link function and Support interface
def open_support(event):
    interface.destroy()
    # Support interface
    interface_support = Tk()
    interface_support.title("ClamPy")
    interface_support.config(bg="#2A0A1B")
    interface_support.resizable(0,0)

    # Interface in the middle of the screeen
    windowWidth = interface_support.winfo_reqwidth()
    windowHeight = interface_support.winfo_reqheight()
    positionRight = int(interface_support.winfo_screenwidth()/2 - windowWidth)
    positionDown = int(interface_support.winfo_screenheight()/2 - windowHeight/2)
    interface_support.geometry("850x400+%s+%s"%(positionRight,positionDown))


    # Image and label logo interface
    logo_interface_support=ImageTk.PhotoImage(file="img/logo.png")
    label_logo_interface_support=Label(interface_support, image=logo_interface_support, bg="#2A0A1B")
    label_logo_interface_support.pack()
    label_logo_interface_support.place(x=3, y=3)

    # Label license
    license_interface_support=Label(interface_support, text="License", bg="#2A0A1B", fg="#FF0000", font="Helveltica 15 italic", cursor="hand2"    )
    license_interface_support.pack()
    license_interface_support.place(x=100, y=25)

    # Label program
    program_interface_support=Label(interface_support, text="Program", bg="#2A0A1B", fg="#FF0000", font="Helveltica 15 italic", cursor="hand2"    )
    program_interface_support.pack()
    program_interface_support.place(x=200, y=25)

    # Label contact
    contact_interface_support=Label(interface_support, text="Contact", bg="#2A0A1B", fg="#FF0000", font="Helveltica 15 italic", cursor="hand2"    )
    contact_interface_support.pack()
    contact_interface_support.place(x=300, y=25)


    interface_support.mainloop()

# Finish support
# ------------------------------------------

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
def theme_white(event):
    # Change interface, label, and buttons colors
    interface.config(bg="#d6d6c2")
    logo_image.config(bg="#d6d6c2")
    title.config(bg="#d6d6c2")
    label_web.config(bg="#d6d6c2", fg="black")
    label_github.config(bg="#d6d6c2", fg="black")
    label_support.config(bg="#d6d6c2", fg="black")
    label_theme.config(bg="#d6d6c2", fg="black")

def theme_purpule(event):
    # Change interface, label, and buttons colors
    interface.config(bg="#2A0A1B")
    logo_image.config(bg="#2A0A1B")
    title.config(bg="#2A0A1B")
    label_web.config(bg="#2A0A1B", fg="white")
    label_github.config(bg="#2A0A1B", fg="white")
    label_support.config(bg="#2A0A1B", fg="white")
    label_theme.config(bg="#2A0A1B", fg="white")

def theme_black(event):
    # Change interface, label, and buttons colors
    interface.config(bg="#262626")
    logo_image.config(bg="#262626")
    title.config(bg="#262626")
    label_web.config(bg="#262626", fg="white")
    label_github.config(bg="#262626", fg="white")
    label_support.config(bg="#262626", fg="white")
    label_theme.config(bg="#262626", fg="white")

# Label theme
label_theme=Label(interface,
    text="Theme:",
    background="#2A0A1B",
    foreground="white",
    font="Helvetica 12 italic"
    )
label_theme.pack()
label_theme.place(x=710, y=20)

# Label of colors
# ----------------

# White color canvas
canvas_white = Canvas(interface, bg="#d6d6c2", highlightbackground="white", height=10, width=10, cursor="hand2")
canvas_white.pack()
canvas_white.place(x=780, y=30)
canvas_white.bind("<Button-1>", theme_white)

# Purpule color canvas
canvas_purpule = Canvas(interface, bg="#2A0A1B", highlightbackground="white",height=10, width=10, cursor="hand2")
canvas_purpule.pack()
canvas_purpule.place(x=795, y=30)
canvas_purpule.bind("<Button-1>", theme_purpule)

# Black color canvas
canvas_black = Canvas(interface, bg="#262626", highlightbackground="white",height=10, width=10, cursor="hand2")
canvas_black.pack()
canvas_black.place(x=810, y=30)
canvas_black.bind("<Button-1>", theme_black)


interface.mainloop()
