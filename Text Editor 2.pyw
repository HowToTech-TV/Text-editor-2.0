import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from time import strftime
from PIL import Image
import tkinter.messagebox as meg
import subprocess
import tkinter.font as font
from tkinter import ttk
import webbrowser

loading = tk.Tk()
loading.title("Loading ...")
loading.iconbitmap("23.ico")
loading.geometry("400x400")
loading.resizable(False, False)
loading.config(bg="white")
label = tk.Label(loading, text="Text Editor 2.0", fg="black", bg="white", font=("Segoe UI Bold", 30)).pack()
imagename = "loaading.gif"
info = Image.open(imagename)
frame = info.n_frames
im = [tk.PhotoImage(file=imagename, format=f"gif -index {i}") for i in range(frame)]
imagelabel = tk.Label(loading, bg="white", image="")
imagelabel.pack()
count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]
    imagelabel.configure(image=im2)
    count += 1
    if count == frame:
        count = 0
    anim = loading.after(50, lambda: animation(count))


animation(count)
labele = tk.Label(loading, text="Initializing Interface...", fg="black", bg="white").pack()
labelf = tk.Label(loading, text="2021 HowToTech Systems.", fg="black", bg="white").pack()


def main():
    loading.destroy()
    root = Tk()
    root.title("Text Editor")
    root.config(bg="white")
    root.iconbitmap("23.ico")

    text = Text(root, height=35, width=138)
    text.grid(row=1, column=0)
    scr1 = Scrollbar(command=text.yview, orient=VERTICAL)
    scr1.grid(row=1, column=1, sticky="ns")
    text.config(yscrollcommand=scr1.set)
    fn = StringVar()
    font = Menubutton(root, text="Font")
    font.grid(row=2, column=0)
    font.menu = Menu(font, tearoff=0)
    font["menu"] = font.menu
    Helvetica = IntVar()

    roboto = IntVar()
    Courier = IntVar()

    def FontHelvetica():
        text.config(font="Helvetica")

    def FontCourier():
        text.config(font="Courier")

    def FontRoboto():
        text.config(font="Roboto")

    font.menu.add_checkbutton(label="Courier", variable=Courier,
                              command=FontCourier)
    font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
                              command=FontHelvetica)
    font.menu.add_checkbutton(label="Roboto", variable=roboto,
                              command=FontRoboto)

    def saveas():
        t = text.get("1.0", "end-1c")

        savelocation = fd.asksaveasfilename(defaultextension="txt",
                                            filetypes=[("Notepad Files", "*.txt"), ("HTML", "*.html"),
                                                       ("All Files", "*.*")])

        file1 = open(savelocation, "w+")

        file1.write(t)

        file1.close()
        root.title("Text Editor - {}".format(savelocation))
        fn.set(savelocation)

    def openas():
        openoccasion = fd.askopenfilename(defaultextension="txt",
                                          filetypes=[("Notepad Files", "*.txt"), ("HTML", "*.html"),
                                                     ("All Files", "*.*")])

        t = open(openoccasion, "r")
        txt = t.read()
        text.insert(1.0, txt)

        root.title("Text Editor - {}".format(openoccasion))
        fn.set(openoccasion)

    def FontHelvetica():
        text.config(font="Helvetica")

    def FontCourier():
        text.config(font="Courier")

    def FontRoboto():
        text.config(font="Times New Roman")

    def exit():
        root.destroy()

    def about():
        base3 = Tk()
        base3.title("About")
        base3.geometry("500x300")
        base3.config(bg="white")
        base3.iconbitmap("23.ico")
        ft2 = "Calibri", "26"
        Label(base3, font=ft2, text="Notepad", bg = "white").pack()
        Label(base3, text="Version 2.0", bg="white").pack()
        Label(base3, text="Copyright 2021 HowToTech Systems, All Rights Reserved", bg="white").pack()
        Label(base3, text="A Simple tool for opening text files on All Devices, written in python.", bg="white").pack()
        def repo():
            webbrowser.open("https://github.com/HowToTech-TV/Text-editor-2.0/")

        Button(base3, text="View Repo Online", command=repo).pack()
        base3.mainloop()

    def extension():
        base5 = Tk()
        base5.title("Extensions")
        base5.iconbitmap("23.ico")
        base5.geometry("400x400")
        counts = 0
        label = Label(base5, text="Extensions", font=("Segoe UI Bold", 30)).pack()
        label2 = Label(base5, text="Installed Extensions: 0")
        label2.pack()
        label3 = Label(base5, text="Avaliable Extensions for version 2.0: Total (1)").pack()
        label4 = Label(base5, text="Clock in Text editor", font=("Segoe UI Bold", 20)).pack()
        label5 = Label(base5, text="extension size: 0.00MB, version: 1.0.0").pack()
        label6 = Label(base5, text="").pack()
        label7 = Label(base5, text="Description:").pack()
        label8 = Label(base5, text="A small digital clock for your text editor.").pack()

        def apply():
            appl.config(text="Applied!")
            appl["state"] = "disabled"
            openex["state"] = "normal"
            label2.config(text="Installed Extensions: {}".format(count))

        def ope():
            time = Tk()
            time.title("Clock for text editor 2.0")
            time.geometry("200x50")
            time.resizable(False, False)
            time.config(bg="black")
            timelabel = Label(time, bg="black", fg="white", font=("Segoe UI Bold", "30"))
            timelabel.pack()

            def update():
                text = strftime("%H:%M:%S")
                timelabel.config(text=text)
                timelabel.after(80, update)

            update()
            time.mainloop()

        appl = Button(base5, text="Apply", command=apply)
        appl.pack()
        openex = Button(base5, text="Open", command=ope)
        openex.pack()
        openex["state"] = "disabled"
        def submit():
            webbrowser.open("https://drive.google.com/drive/folders/1FIdUA25rh174FT2sUw0xg8L7pOWH0yP4xR_HXLgdXQEM4ajX2rtmBHppak6eujmmJCNDMWoQ?usp=sharing")
        Button(base5, text = "Submit an Extension", command = submit).pack()

        base5.mainloop()

    def settings():
        base6 = Tk()
        base6.geometry("200x200")
        base6.title("Settings")
        base6.iconbitmap("23.ico")
        base6.config(bg="white")
        Label(base6, text="Settings", font=("Roboto Bold", 20), bg="white").pack()
        Label(base6, text="Font", font=("Roboto Bold", 15), bg="white").pack()

        font = Menubutton(base6, text="Font")
        font.pack()
        font.menu = Menu(font, tearoff=0)
        font["menu"] = font.menu
        Helvetica = IntVar()

        roboto = IntVar()
        Courier = IntVar()

        def FontHelvetica():
            text.config(font="Helvetica")

        def FontCourier():
            text.config(font="Courier")

        def FontRoboto():
            text.config(font="Roboto")

        font.menu.add_checkbutton(label="Courier", variable=Courier,
                                  command=FontCourier)
        font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
                                  command=FontHelvetica)
        font.menu.add_checkbutton(label="Roboto", variable=roboto,
                                  command=FontRoboto)

        base6.mainloop()

    def run():
        if ".py" not in fn.get():
            meg.showerror("Error", "Couldn't Run file because not a Python File.")
        else:
            import os
            os.system(f"python {fn.get()}")

    menu = Menu(root)
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)

    filemenu.add_command(label="Open", command=openas)
    filemenu.add_command(label="Save As...", command=saveas)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit)
    winmenu = Menu(menu, tearoff=0)
    menu.add_cascade(menu=winmenu, label="Window")
    winmenu.add_command(label="{Root Window}")
    configmenu = Menu(menu, tearoff=0)
    menu.add_cascade(menu=configmenu, label="Configure")
    configmenu.add_command(label="Extensions", command=extension)
    configmenu.add_command(label="Run File", command=run)
    configmenu.add_separator()
    configmenu.add_command(label="Settings", command=settings)
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(menu=helpmenu, label="Help")

    helpmenu.add_command(label="About Notepad", command=about)
    root.config(menu=menu)

    root.mainloop()


loading.after(10000, main)

loading.mainloop()
