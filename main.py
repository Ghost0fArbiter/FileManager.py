import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('File Manager')
root.iconbitmap('Icon.PNG')
root.config(bg="#808080")
 = Frame(root)


# Layout of application

# Source UI
sourceBtn = Button(root, text="Source Directory: ")
sourceLabel = Label(root, text="Available Extensions: ")
sourceList = Listbox(root, selectmode="multiple")
sourceDir = Text(root, height=1, width=8, state='disabled')


# Mapping to screen
sourceLabel.grid(row=3, column=0)
sourceLabel.config(bg="#808080")
sourceLabel.rowconfigure(0)
sourceList.grid(row=3, column=0, padx=15)
sourceList.rowconfigure(1)
sourceBtn.grid(row=1, column=0, sticky="w")
sourceDir.grid(row=2, column=0, sticky="we")

# Destination UI
destBtn = Button(root, text="Dest Directory")
destLabel = Label(root, text="Options:  ", bg="#808080")
destList = Listbox(root, selectmode="multiple")

# Mapping to screen
# destLabel.grid(row=2, column=1)
# destLabel.config(bg="#808080")
# destList.grid(row=3, column=1, padx=15)
# destBtn.grid(row=1, column=1)




# List Variables
src = []
options = ['Move', 'Delete', 'Convert']
optionExtra = "Ignore: "



for each_item in range(len(src)):
    sourceExt.insert(END, src[each_item])

    # coloring alternative lines of listbox
    sourceExt.itemconfig(each_item,
                    bg="yellow" if each_item % 2 == 0 else "cyan")

root.mainloop()