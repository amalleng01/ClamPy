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
interface.resizable(0,0)
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
label_white_color=Label(interface, image=white_color, cursor="hand2")
label_white_color.pack()
label_white_color.place(x=785, y=25)
label_white_color.bind("<Button-1>", change_theme)

# Purpule color image and label
purpule_color=ImageTk.PhotoImage(file="img/color-morado.png")
label_purpule_color=Label(interface, image=purpule_color, cursor="hand2")
label_purpule_color.pack()
label_purpule_color.place(x=800, y=25)
label_purpule_color.bind("<Button-1>", change_theme)

# Black color image and label
black_color=ImageTk.PhotoImage(file="img/color-negro.png")
label_black_color=Label(interface, image=black_color, cursor="hand2")
label_black_color.pack()
label_black_color.place(x=815, y=25)
label_black_color.bind("<Button-1>", change_theme)
#----------------------------------------------------------------------------#

# Top line
top_line = Canvas(interface,
    width=850,
    height=1.5,
    bg="white"
    )
top_line.pack()
top_line.create_line(0, 0, 200, 200, fill="white")
top_line.place(x=0, y=70)
#---------------------------------------------------------------------#

# Scan buttons
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

# Adblock
# Install adblock function
def install_adblock():
    interface.withdraw()
    interface_adblock=Toplevel()

    # Editing interface_adblock
    interface_adblock.title("Install adblock")
    interface_adblock.config(background="#2A0A1B")
    interface_adblock.geometry("850x600")

    # Logo
    logo_interface_adblock = ImageTk.PhotoImage(file="img/logo.png")
    label_logo_interface_adblock = Label(interface_adblock,
        image=logo_interface_adblock,
        background="#2A0A1B",)
    label_logo_interface_adblock.pack()
    label_logo_interface_adblock.place(x=3, y=3)

    # Logo Name
    logo_interface_name = Label(interface_adblock,
    text="ClamTK",
    foreground="#FF0000",
    font="Helveltica 20",
    background="#2A0A1B",
    )
    logo_interface_name.pack()
    logo_interface_name.place(x=78, y=15)

    # Main menu
    # Main menu function
    def return_main_menu():
        interface_adblock.destroy()
        interface.deiconify()

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
