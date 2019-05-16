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
    interface.withdraw()
    # Support interface
    interface_support = Toplevel()
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

    # Go to main menu function
    def return_main_menu():
        interface_support.destroy()
        interface.deiconify()

    # Image an button for back to menu
    go_back = ImageTk.PhotoImage(file="img/go-back.png")
    main_menu_interface_support = Button(interface_support,
    image=go_back,
    # foreground="#2A0A1B",
    cursor="hand2",
    background="#2A0A1B",
    highlightbackground="#2A0A1B",
    command=return_main_menu
    )
    main_menu_interface_support.pack()
    main_menu_interface_support.place(x=780, y=15)



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



# Top line
top_line = Canvas(interface,
    width=850,
    height=1.5,
    bg="white"
    )
top_line.pack()
top_line.create_line(0, 0, 200, 200, fill="white")
top_line.place(x=0, y=70)

# Scan buttons
# --------------------
# Intensive scan button
intensive_scan_button = Button(interface,
    text="Intensive Scan",
    fg="White",
    bg="Red",
    width="15",
    height="6",
    cursor="hand2",
    font="Helvetica"
    )
intensive_scan_button.pack()
intensive_scan_button.place(x=10, y=150)

# Fast scan button
fast_scan_button = Button(interface,
    text="Fast Scan",
    fg="White",
    bg="Red",
    width="15",
    height="6",
    cursor="hand2",
    font="Helvetica"
    )
fast_scan_button.pack()
fast_scan_button.place(x=180, y=150)

# Specific scan button
specific_scan_button = Button(interface,
    text="Specific Scan",
    fg="White",
    bg="Red",
    width="15",
    height="6",
    cursor="hand2",
    font="Helvetica"
    )
specific_scan_button.pack()
specific_scan_button.place(x=350, y=150)

# ---------------------------------------------------
#                   Adblock
# Install adblock function
def install_adblock():
    interface.withdraw()
    interface_adblock=Toplevel()

    # Editing interface_adblock
    interface_adblock.title("Install adblock")
    interface_adblock.config(background="#2A0A1B")

    # Interface in the middle of the screeen
    windowWidth = interface_adblock.winfo_reqwidth()
    windowHeight = interface_adblock.winfo_reqheight()
    positionRight = int(interface_adblock.winfo_screenwidth()/2 - windowWidth)
    positionDown = int(interface_adblock.winfo_screenheight()/2 - windowHeight)
    interface_adblock.geometry("850x400+%s+%s"%(positionRight,positionDown))

    # Logo
    logo_interface_adblock = ImageTk.PhotoImage(file="img/logo.png")
    label_logo_interface_adblock = Label(interface_adblock, image=logo_interface_adblock, background="#2A0A1B")
    label_logo_interface_adblock.pack()
    label_logo_interface_adblock.place(x=3, y=3)

    # Logo Name
    logo_interface_name = Label(interface_adblock,
    text="ClamPy",
    foreground="#FF0000",
    font="Helveltica 20",
    background="#2A0A1B",
    )
    logo_interface_name.pack()
    logo_interface_name.place(x=78, y=15)

    # Go to main menu function
    def return_main_menu():
        interface_adblock.destroy()
        interface.deiconify()

    # Image an button for back to menu
    go_back = ImageTk.PhotoImage(file="img/go-back.png")
    main_menu_interface_adblock = Button(interface_adblock,
    image=go_back,
    # foreground="#2A0A1B",
    cursor="hand2",
    background="#2A0A1B",
    highlightbackground="#2A0A1B",
    command=return_main_menu
    )
    main_menu_interface_adblock.pack()
    main_menu_interface_adblock.place(x=780, y=15)

    interface_adblock.mainloop()

#  Finish adblock
# -------------------------------------------------

# Ablock button
adblock_image = ImageTk.PhotoImage(file="img/adblock.png")
adblock_button = Button(interface,
    image=adblock_image,
    fg="White",
    bg="Red",
    width="150",
    height="151.5",
    cursor="hand2",
    command=install_adblock
    )
adblock_button.pack()
adblock_button.place(x=520, y=150)


interface.mainloop()
