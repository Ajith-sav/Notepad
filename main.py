from argparse import FileType
from ast import main
from cgitb import text
from sys import getprofile
# install tkinter from pypi
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfilename
#import os
import os
from xml.etree.ElementTree import Comment

#declare root variable
root = Tk()
root.title('Notpad')  # set title bar name
root.geometry('600x500') # set size of the window

def newfile(): # create the new file 
    global file
    root.title("untitled - Notepade")
    entry.delete(1.0, END)

def openfile(): # open the file
    global file
    file = askopenfilename(defaultextension= ".txt", filetypes=[("Text Documents", "*.txt")])
    if (file == " "):
        file = None

    else:
        root.title(os.path.basename(file) + "-Notedap")   
        f = open(file, "r")
        entry.delete('1.0', tkinter.END)
        entry.insert(1.0, f.read())
        f.close()

def savefile(): # save the file .txt format
    global file
    file = asksaveasfilename(defaultextension= ".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])   
    if (file == " "):
        file = None       

    else:
        root.title(os.path.basename(file) + "-Notedap")
        f = open(file, "w")    
        f.write(entry.get(1.0, END))
        f.close()
       
def exitfile(): # exit the window
    root.destroy()            

def cut(): 
    entry.event_generate(("<<Cut>>"))

def copy():
    entry.event_generate(("<<Copy>>"))

def paste():
    entry.event_generate(("<<Paste>>"))   

def helpa():
    messagebox.showinfo("Ajith", "vist my github...") 

def About():
    messagebox.showinfo("About us", "This notepad is create using python \n -By Mr.A corporation")       

# set scrollbar 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# create the working area with bg color
entry = Text(root, yscrollcommand = scrollbar.set,font=("Arial", 15), bg="#808080") 
entry.pack(padx=10, pady=5, expand=TRUE, fill=BOTH)
scrollbar.config( command= entry.yview)

#create the menu bar
menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar, tearoff=0) # create the menu button list
file.add_command(label="New", command=newfile)
file.add_command(label="Open", command=openfile)
file.add_command(label="Save", command=savefile)
file.add_separator()
file.add_command(label="Exit", command=exitfile)
menubar.add_cascade(label="File", menu=file)

#create the edit button
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Cut", command=cut)
edit.add_command(label="Copy", command=copy)
edit.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=edit)

help = Menu(menubar, tearoff=0) #create the help button
help.add_command(label="Report", command=helpa)
menubar.add_cascade(label="Help", menu=help)

about = Menu(menubar, tearoff=0) #about button
about.add_command(label="detail...", command=About)
menubar.add_cascade(label="About", menu=about)

mainloop()

if __name__=="__main__":
   main()