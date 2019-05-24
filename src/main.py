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
    webbrowser.open_new("https://github.com/amalleng01/ClamPy")

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

    # Top line
    top_line = Canvas(interface_support, width=850, height=1.5, bg="white")
    top_line.pack()
    top_line.place(x=0, y=90)

    # ______________________________________
    # Support License
    # Underline support
    underline_support = Canvas(interface_support, width=75, height=1, bg="white")
    underline_support.pack()

    # All label into license
    label_clampy_interface_support=Label(interface_support, text="ClamPy", font="Helvetica 13", bg="#2A0A1B", fg="#FF0000")
    label_clampy_interface_support.pack()
    label_copyright=Label(interface_support, bg="#2A0A1B", fg="white", font="Helvetica 11 italic", text="Copyright © 2019 Juan Miguel Segura Fernandez and Alejandro Mallén Gómez.")
    label_copyright.pack()
    label_all_licese=Label(interface_support, bg="#2A0A1B", fg="white", font="Helvetica 11", justify=LEFT, text="This program is free software: you can redistribute it and/or modify.\nIt under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the\nLicense, or at your option, any later version.\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY\nwithout even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU \nGeneral Public License for more details. You should have received a copy of the GNU General Public License along with this\nprogram.")
    label_all_licese.pack()
    # This function open de browser and go to page web license gnu
    def goto_pageweb_license(event):
        webbrowser.open_new_tab("https://www.gnu.org/licenses/gpl-3.0.en.html")
    # Label for see license ( go to license page web )
    label_see_license=Label(interface_support, text="If not, see <http://www.gnu.org/licenses/>", bg="#2A0A1B", fg="white", font="Helvetica 11 underline", cursor="hand2")
    label_see_license.pack()
    label_see_license.bind("<Button-1>", goto_pageweb_license)

    # Function for support_license
    def support_license(event):
        # Hide all label of program
        label_que_es_program.place_forget()
        label_que_es_explicacon_program.place_forget()
        label_porque_antivirus_program.place_forget()
        label_porque_antivirus_explicacion_program.place_forget()
        label_imagen_open_source.place_forget()
        label_imagen_clamav.place_forget()
        # Hide all labels of contact
        label_nosotros_contact.place_forget()
        label_nosotros_explicacion_contact.place_forget()
        label_contactar_connosotros_contact.place_forget()
        label_contactar_connosotros_explicacion.place_forget()
        label_imagen_gitlab_contact_juanmi.place_forget()
        label_imagen_gitlab_contact_alejandro.place_forget()
        # Position of elements in the license
        underline_support.place(x=100,y=55)
        label_clampy_interface_support.place(x=5, y=105)
        label_copyright.place(x=5, y=130)
        label_all_licese.place(x=6, y=160)
        label_see_license.place(x=5, y=285)

    # Label license
    license_interface_support=Label(interface_support, text="License", bg="#2A0A1B", fg="#FF0000", font="Helveltica 15 italic", cursor="hand2")
    license_interface_support.pack()
    license_interface_support.place(x=100, y=25)
    license_interface_support.bind("<Button-1>", support_license)

    # Hide all labels and buttons with grid
    label_clampy_interface_support.place_forget()
    label_copyright.place_forget()
    label_all_licese.place_forget()
    label_see_license.place_forget()
    # ______________________________________

    # ----------------------------
    # Support Program
    # ----------------------------
    # Labels in part or support
    label_que_es_program=Label(interface_support, text="Que es ClamPy?", font="Helvetica 12 italic", bg="#2A0A1B", fg="white")
    label_que_es_program.pack()
    label_que_es_explicacon_program=Label(interface_support, font="Helvetica 11", bg="#2A0A1B", fg="white", justify=LEFT, text="- ClamPy es una interfaz para el antivirus Clamav. Tanto el propio antivirus, como la interfaz ClamPy, son completamente\n  Open Source y se puede contrtibuir con estos. ",)
    label_que_es_explicacon_program.pack()
    label_porque_antivirus_program=Label(interface_support, text="Por qué un antivirus?", font="Helvetica 12 italic", bg="#2A0A1B", fg="white")
    label_porque_antivirus_program.pack()
    label_porque_antivirus_explicacion_program=Label(interface_support, font="Helvetica 11", bg="#2A0A1B", fg="white", justify=LEFT, text="- Hemos decidido en cuntribuir creando una interfaz para el antivirus Open Source Clamav, porque creemos\n  que es necesario que exista un antivirus completamente libre y gratis.")
    label_porque_antivirus_explicacion_program.pack()
    imagen_open_source=ImageTk.PhotoImage(file="img/opensource.png")
    label_imagen_open_source=Label(interface_support, image=imagen_open_source, bg="#2A0A1B")
    label_imagen_open_source.pack()
    imagen_clamav=ImageTk.PhotoImage(file="img/clamav_support_program.png")
    label_imagen_clamav=Label(interface_support, image=imagen_clamav, bg="#2A0A1B")
    label_imagen_clamav.pack()

    # Function for support_program
    def support_program(event):
        # Hide all labels of license
        label_copyright.place_forget()
        label_all_licese.place_forget()
        label_see_license.place_forget()
        # Hide all labels of contact
        label_nosotros_contact.place_forget()
        label_nosotros_explicacion_contact.place_forget()
        label_contactar_connosotros_contact.place_forget()
        label_contactar_connosotros_explicacion.place_forget()
        label_imagen_gitlab_contact_juanmi.place_forget()
        label_imagen_gitlab_contact_alejandro.place_forget()
        # Position of elements in the program
        underline_support.place(x=200, y=55)
        label_que_es_program.place(x=5, y=130)
        label_que_es_explicacon_program.place(x=5, y=155)
        label_porque_antivirus_program.place(x=5, y=210)
        label_porque_antivirus_explicacion_program.place(x=5, y=235)
        label_imagen_open_source.place(x=690, y=280)
        label_imagen_clamav.place(x=480, y=270)

    # Label program
    program_interface_support=Label(interface_support, text="Program", bg="#2A0A1B", fg="#FF0000", font="Helveltica 15 italic", cursor="hand2"    )
    program_interface_support.pack()
    program_interface_support.place(x=200, y=25)
    program_interface_support.bind("<Button-1>", support_program )

    # Hide all labels and buttons
    label_que_es_program.forget()
    label_que_es_explicacon_program.forget()
    label_porque_antivirus_program.forget()
    label_porque_antivirus_explicacion_program.forget()
    label_imagen_open_source.forget()
    label_imagen_clamav.forget()
    # ----------------------------------

    # _________________________________
    # Support Contact
    # _________________________________
    # All label into contact
    label_nosotros_contact=Label(interface_support, text="Sobre nosotros:", font="Helvetica 12 italic", bg="#2A0A1B", fg="white")
    label_nosotros_contact.pack()
    label_nosotros_explicacion_contact=Label(interface_support, font="Helvetica 11", bg="#2A0A1B", justify=LEFT, fg="white", text=" - Somos Juan Miguel Segura Fernandez y Alejandro Mallén Gomez, dos alumnos de SMX ( Sistemas Microinformáticos y\n   Redes ) de Grado Medio. Nos gusta programar y nos gusta el software libre, por ello hemos decidido iniciar este pequeño\n   proyecto.")
    label_nosotros_explicacion_contact.pack()
    label_contactar_connosotros_contact=Label(interface_support, text="Contacto:", font="Helvetica 12 italic", bg="#2A0A1B", fg="white")
    label_contactar_connosotros_contact.pack()
    label_contactar_connosotros_explicacion=Label(interface_support, font="Helvetica 11", bg="#2A0A1B", fg="white", justify=LEFT, text=" - Correo de Juanmi: jusefer2@hotmail.es.\n - Correo de Alejandro: alejandromallengomez@gmail.com")
    label_contactar_connosotros_explicacion.pack()
    imagen_gitlab_contact=ImageTk.PhotoImage(file="img/gitlab.png")
    # Funcion for open gitlab juanmi in browser
    def open_gitlab_juanmi(event):
        webbrowser.open_new("https://gitlab.com/jmseguraf01")
    # Label, image and buttons of gitlab juanmi and alejandro
    label_imagen_gitlab_contact_juanmi=Label(interface_support, image=imagen_gitlab_contact, bg="#2A0A1B", cursor="hand2", compound="top", text="Juanmi", fg="white", font="Helvetica 11 italic")
    label_imagen_gitlab_contact_juanmi.pack()
    label_imagen_gitlab_contact_juanmi.bind("<Button-1>", open_gitlab_juanmi)
    # Funcion for open gitlab alejandro in browser
    def open_gitlab_alejandro(event):
        webbrowser.open_new("https://gitlab.com/amalleng01")
    label_imagen_gitlab_contact_alejandro=Label(interface_support, image=imagen_gitlab_contact, bg="#2A0A1B", cursor="hand2", compound="top", text="Alejandro", fg="white", font="Helvetica 11 italic")
    label_imagen_gitlab_contact_alejandro.pack()
    label_imagen_gitlab_contact_alejandro.bind("<Button-1>", open_gitlab_alejandro)

    # Function of support contact
    def support_contact(event):
        # Hide all elements of license
        label_copyright.place_forget()
        label_all_licese.place_forget()
        label_see_license.place_forget()
        # Hide all elements support
        label_que_es_program.place_forget()
        label_que_es_explicacon_program.place_forget()
        label_porque_antivirus_program.place_forget()
        label_porque_antivirus_explicacion_program.place_forget()
        label_imagen_open_source.place_forget()
        label_imagen_clamav.place_forget()
        # Position of elements in the contact
        underline_support.place(x=300, y=55)
        label_nosotros_contact.place(x=5, y=130)
        label_nosotros_explicacion_contact.place(x=5, y=155)
        label_contactar_connosotros_contact.place(x=5, y=230)
        label_contactar_connosotros_explicacion.place(x=5, y=255)
        label_imagen_gitlab_contact_juanmi.place(x=50, y=310)
        label_imagen_gitlab_contact_alejandro.place(x=150, y=310)

    # Label contact
    contact_interface_support=Label(interface_support, text="Contact", bg="#2A0A1B", fg="#FF0000", font="Helveltica 15 italic", cursor="hand2"    )
    contact_interface_support.pack()
    contact_interface_support.place(x=300, y=25)
    contact_interface_support.bind("<Button-1>", support_contact)
    # Hide all label in contact
    label_nosotros_contact.forget()
    label_nosotros_explicacion_contact.forget()
    label_contactar_connosotros_contact.forget()
    label_contactar_connosotros_explicacion.forget()
    label_imagen_gitlab_contact_juanmi.forget()
    label_imagen_gitlab_contact_alejandro.forget()
    # _________________________________

    # Go to main menu function
    def return_main_menu():
        interface_support.destroy()
        interface.deiconify()

    # Image an button for back to menu
    go_back = ImageTk.PhotoImage(file="img/go-back.png")
    main_menu_interface_support = Button(interface_support, image=go_back, cursor="hand2", background="#2A0A1B", highlightbackground="#2A0A1B", activebackground="#2A0A1B", command=return_main_menu)
    main_menu_interface_support.pack()
    main_menu_interface_support.place(x=780, y=15)

    # Calling a function for the open support interface
    support_license(event)
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
    intensive_scan_title.config(bg="#d6d6c2", fg="black")
    fast_scan_title.config(bg="#d6d6c2", fg="black")
    specific_scan_title.config(bg="#d6d6c2", fg="black")
    adblock_title.config(bg="#d6d6c2", fg="black")
    quarantine_title.config(bg="#d6d6c2", fg="black")

def theme_purpule(event):
    # Change interface, label, and buttons colors
    interface.config(bg="#2A0A1B")
    logo_image.config(bg="#2A0A1B")
    title.config(bg="#2A0A1B")
    label_web.config(bg="#2A0A1B", fg="white")
    label_github.config(bg="#2A0A1B", fg="white")
    label_support.config(bg="#2A0A1B", fg="white")
    label_theme.config(bg="#2A0A1B", fg="white")
    intensive_scan_title.config(bg="#2A0A1B", fg="white")
    fast_scan_title.config(bg="#2A0A1B", fg="white")
    specific_scan_title.config(bg="#2A0A1B", fg="white")
    adblock_title.config(bg="#2A0A1B", fg="white")
    quarantine_title.config(bg="#2A0A1B", fg="white")

def theme_black(event):
    # Change interface, label, and buttons colors
    interface.config(bg="#262626")
    logo_image.config(bg="#262626")
    title.config(bg="#262626")
    label_web.config(bg="#262626", fg="white")
    label_github.config(bg="#262626", fg="white")
    label_support.config(bg="#262626", fg="white")
    label_theme.config(bg="#262626", fg="white")
    intensive_scan_title.config(bg="#262626", fg="white")
    fast_scan_title.config(bg="#262626", fg="white")
    specific_scan_title.config(bg="#262626", fg="white")
    adblock_title.config(bg="#262626", fg="white")
    quarantine_title.config(bg="#262626", fg="white")

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
# Funciton of intensive scan
def intensive_scan():
    # Destroy interface and call an other file when execute this functon
    interface.destroy()
    from subprocess import call
    call(["python", "intensive_scan.py"])

# Intensive scan button
intensive_scan_title = Label(interface,
    text="Intensive scan",
    font="Helvetica 12",
    bg="#2A0A1B",
    fg="White"
    )
intensive_scan_title.pack()
intensive_scan_title.place(x=38, y=290)

img_intensive_img = ImageTk.PhotoImage(file="img/intensive.png")
intensive_scan_button = Button(interface,
    image=img_intensive_img,
    activebackground="#2A0A1B",
    fg="white",
    bg="#2A0A1B",
    width="150",
    height="150",
    cursor="hand2",
    font="Helvetica",
    command=intensive_scan
    )

intensive_scan_button.pack()
intensive_scan_button.place(x=10, y=135)

# Fast scan button
fast_scan_title = Label(interface,
    text="Fast scan",
    font="Helvetica 12",
    bg="#2A0A1B",
    fg="White"
    )
fast_scan_title.pack()
fast_scan_title.place(x=228, y=290)

fast_img = ImageTk.PhotoImage(file="img/fast.png")
fast_scan_button = Button(interface,
    image=fast_img,
    activebackground="#2A0A1B",
    fg="white",
    bg="#2A0A1B",
    width="150",
    height="150",
    cursor="hand2",
    )
fast_scan_button.pack()
fast_scan_button.place(x=180, y=135)

# Specific scan button
specific_scan_title = Label(interface,
    text="Specific scan",
    font="Helvetica 12",
    bg="#2A0A1B",
    fg="White"
    )
specific_scan_title.pack()
specific_scan_title.place(x=383, y=290)

specific_img = ImageTk.PhotoImage(file="img/specific.png")
specific_scan_button = Button(interface,
    image=specific_img,
    activebackground="#2A0A1B",
    fg="white",
    bg="#2A0A1B",
    width="150",
    height="150",
    cursor="hand2",
    )
specific_scan_button.pack()
specific_scan_button.place(x=350, y=135)

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
    interface_adblock.geometry("850x600+%s+%s"%(positionRight,positionDown))

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
    cursor="hand2",
    background="#2A0A1B",
    activebackground="#2A0A1B",
    command=return_main_menu,
    highlightbackground="#2A0A1B"
    )
    main_menu_interface_adblock.pack()
    main_menu_interface_adblock.place(x=780, y=15)

    # line
    line_interface_adblock = Canvas(interface_adblock,
    width=850,
    height=1.5,
    bg="white"
    )
    line_interface_adblock.pack()
    line_interface_adblock.create_line(0, 0, 200, 200, fill="white")
    line_interface_adblock.place(x=0, y=70)

    # Label text title
    text_interface_adblock = Label(interface_adblock,
    text="Install Adblock Plus",
    font="Helvetica 20",
    fg="white",
    bg="#2A0A1B"
    )
    text_interface_adblock.pack()
    text_interface_adblock.place(x=310, y=15)

    # Label text select:
    text_interface_adblock_select = Label(interface_adblock,
    text="Select your browser: ",
    font="Helvetica 20",
    fg="white",
    bg="#2A0A1B"
    )
    text_interface_adblock_select.pack()
    text_interface_adblock_select.place(x=15, y=100)


    # Adblock for firefox
    def adblock_link_firefox():
        webbrowser.open_new("https://eyeo.to/adblockplus/firefox_install/")

    firefox_logo = ImageTk.PhotoImage(file="img/firefox-logo.png")
    adblock_firefox = Button(interface_adblock,
    image=firefox_logo,
    width=150,
    height=150,
    command=adblock_link_firefox,
    background="#2A0A1B"
    )

    adblock_firefox.pack()
    adblock_firefox.place(x=15, y=180)

    # Adblock for Chrome
    def adblock_link_chrome():
        webbrowser.open_new("https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb")

    chrome_logo = ImageTk.PhotoImage(file="img/chrome-logo.png")
    adblock_chrome = Button(interface_adblock,
    image=chrome_logo,
    width=150,
    height=150,
    command=adblock_link_chrome,
    background="#2A0A1B"
    )

    adblock_chrome.pack()
    adblock_chrome.place(x=180, y=180)

    # Adblock for Internet Explorer
    def adblock_link_ie():
        webbrowser.open_new("https://eyeo.to/adblockplus/ie_install/")

    ie_logo = ImageTk.PhotoImage(file="img/ie-logo.png")
    adblock_ie = Button(interface_adblock,
    image=ie_logo,
    width=150,
    height=150,
    command=adblock_link_ie,
    background="#2A0A1B"
    )

    adblock_ie.pack()
    adblock_ie.place(x=345, y=180)

    # Adblock Opera
    def adblock_link_op():
        webbrowser.open_new("https://addons.opera.com/en/extensions/details/adblock-plus/")

    op_logo = ImageTk.PhotoImage(file="img/op-logo.png")
    adblock_op = Button(interface_adblock,
    image=op_logo,
    width=150,
    height=150,
    command=adblock_link_op,
    background="#2A0A1B"
    )

    adblock_op.pack()
    adblock_op.place(x=510, y=180)

    # Adblock Safari
    def adblock_link_safari():
        webbrowser.open_new("https://itunes.apple.com/us/app/adblock-plus-for-safari/id1432731683?ls=1&mt=8")

    safari_logo = ImageTk.PhotoImage(file="img/safari-logo.png")
    adblock_safari = Button(interface_adblock,
    image=safari_logo,
    width="150",
    height="150",
    command=adblock_link_safari,
    background="#2A0A1B"
    )

    adblock_safari.pack()
    adblock_safari.place(x=675, y=180)


    interface_adblock.mainloop()



# Ablock button
adblock_title = Label(interface,
    text="Adblock Plus",
    font="Helvetica 12",
    bg="#2A0A1B",
    fg="White"
    )
adblock_title.pack()
adblock_title.place(x=548, y=290)

adblock_image = ImageTk.PhotoImage(file="img/adblock.png")
adblock_button = Button(interface,
    image=adblock_image,
    fg="white",
    bg="#2A0A1B",
    width="150",
    height="151.5",
    cursor="hand2",
    command=install_adblock,
    activebackground="#2A0A1B"
    )
adblock_button.pack()
adblock_button.place(x=520, y=135)

#  Finish adblock
# -------------------------------------------------

# Quarantine button
quarantine_title = Label(interface,
    text="Quarantine",
    font="Helvetica 12",
    bg="#2A0A1B",
    fg="White"
    )
quarantine_title.pack()
quarantine_title.place(x=718, y=290)


quarantine_image = ImageTk.PhotoImage(file="img/quarantine-logo.png")

quarantine_button = Button(interface,
    image=quarantine_image,
    bg="#2A0A1B",
    width="150",
    height="151.5",
    cursor="hand2",
    activebackground="#2A0A1B",
    compound=TOP
    )
quarantine_button.pack()
quarantine_button.place(x=685, y=135)

# You are protected
protected_button = Label(interface,
    text="You are protected",
    fg="White",
    bg="Green",
    width="103",
    height="2",
    )
protected_button.pack()
protected_button.place(x=10, y=85)




interface.mainloop()
