import os.path
import pathlib
import time
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

extension = ['*']
states = []
filepath = ""
paths = []


# root window
root = tk.Tk()
root.title('Replace')
# root.geometry('400x300')
root.resizable(0, 0)
# windows only (remove the minimize/maximize button)
root.attributes('-toolwindow', True)

# layout on the root window
root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=1)

# cvar = tk.IntVar()
#
# Find a way to log dictionary for every checkbox created with its name so you can
# .get() the Checkbox value to see if it is on or off
# then if it is on take those value and add them to another list for pathlib to iterate thro
# to move/convert/delete files
#
#
def Checkbox():

    # fail safe for blank entries in list, removes blank entries
    while '' in extension:
        extension.remove('')

    Col = 1
    ROW = 4
    for i in extension:
        cvar = tk.IntVar()
        cvar.set(0)
        if Col == 4:
            ttk.Checkbutton(option, text=i, variable=cvar).grid(column=Col, row=ROW, sticky=tk.W)
            states.append(cvar)
            ROW += 1
            Col = 1
        else:
            ttk.Checkbutton(option, text=i, variable=cvar).grid(column=Col, row=ROW, sticky=tk.W)
            Col += 1
            states.append(cvar)

def Move():
    selected = []
    for var in states:
        text = []
        if var.get():
            # print(var.get(), var)
            text.append(str(var))
            # print(text)
            for i in text:
                # print(i[6:])
                name = extension[int(i[6:])]
                selected.append(name)
    print(selected)
    for p in selected:
        # work around for creating file directories, wont work unless i have the exact names and extra folder
        # directories for each file

        # input = source.get()
        # print("{}{}{}".format((input), ("YESS"), (p)))
        print(p)





def Get_Directory_Source():
    # Clears any items listed previously in checkbox variables, (refreshes the checkbox options)
    for items in option.winfo_children():
        items.destroy()
    extension.clear()

    filepath = filedialog.askdirectory()
    source.delete(0, 3000)
    source.insert(1, filepath)
    for ext in pathlib.Path(filepath).rglob('*'):
        head, tail = os.path.split(ext)
        name, ext = os.path.splitext(tail)
        if ext not in extension:
            extension.append(ext)
    Checkbox()


def Get_Directory_Destination():
    filepath = filedialog.askdirectory()
    destination.delete(0, 3000)
    destination.insert(1, filepath)

#Create Left side Frame box

frame = ttk.Frame(root)
frame.grid(column=0, row=0)


# grid layout for the input frame
frame.columnconfigure(0, weight=1)
frame.columnconfigure(0, weight=3)

# Source Folder Button
ttk.Button(frame, text='Source Folder :', command=Get_Directory_Source).grid(column=0, row=0, sticky=tk.W)
# TextBox
source = ttk.Entry(frame, width=30)
source.grid(column=1, row=0, sticky=tk.W)

# Destination Folder Button
ttk.Button(frame, text='Destination Folder :', command=Get_Directory_Destination).grid(column=0, row=1, sticky=tk.W)
# TextBox
destination = ttk.Entry(frame, width=30)
destination.grid(column=1, row=1, sticky=tk.W)

# Ignore Button
ttk.Label(frame, text='Ignore :').grid(column=0, row=2, sticky=tk.W)
# TextBox
Ignore = ttk.Entry(frame, width=30)
Ignore.grid(column=1, row=2, sticky=tk.W)


for widget in frame.winfo_children():
    widget.grid(padx=0, pady=5)

# Create right side frame box

frame2 = ttk.Frame(root)
frame2.grid(column=1, row=0)

frame2.columnconfigure(0, weight=1)

ttk.Button(frame2, text='Move', command=Move).grid(column=0, row=0)
ttk.Button(frame2, text='Delete').grid(column=0, row=1)
ttk.Button(frame2, text='Convert').grid(column=0, row=2)
ttk.Button(frame2, text='Cancel', command=exit).grid(column=0, row=3)

for widget in frame2.winfo_children():
    widget.grid(padx=0, pady=2)

ttk.Label(frame, text='Available Extensions : ').grid(column=0, row=4, sticky=tk.W)
option = ttk.Frame(frame)
option.grid(columnspan=2, row=5, sticky=tk.W)

root.mainloop()