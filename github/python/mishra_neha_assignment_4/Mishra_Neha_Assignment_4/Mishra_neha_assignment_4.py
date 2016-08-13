

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os

filename = ''


########################newfile#################
def newfile(event=None):
    global filename
    root.title("New File")
    filename = None
    textPad.delete(1.0, END)


############openfile############
def openfile(event=None):
    global filename

    fileobject = askopenfile(defaultextension='.txt')
    if fileobject == None:
        filename = None
    else:
        filename = fileobject.name
        root.title('File: ' + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()


#################save#################
def save(event=None):
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()

###############saveas#####################

def saveas(event=None):
    f = asksaveasfile(initialfile='newfile.txt', defaultextension='.txt')
    global filename
    try:
        filename = f.name
        ofile = open(filename, 'w')
        message = textPad.get(1.0, END)
        ofile.write(message)
        ofile.close()
        root.title('File: ' + os.path.basename(filename))
    except:
        pass

################ copy ################################
def copy(event=None):
    textPad.event_generate('<<Copy>>')

################ cut ##########################
def cut(event=None):
    textPad.event_generate('<<Cut>>')


################ paste ##########################
def paste(event=None):
    textPad.event_generate('<<Paste>>')

################ redo ##########################
def redo(event=None):
    textPad.event_generate('<<Redo>>')

################ undo ##########################
def undo(event=None):
    textPad.event_generate('<<Undo>>')

################ selectall ##########################
def selectall(event=None):
    textPad.tag_add('sel', '1.0', END)

################ author ##########################
def author():
    showinfo("Author", "Created by Neha Mishra")

################ copyright##########################
def copyright():
    showinfo("Copyright", "Used by students")





root = Tk()
root.title('Notepad Project by Neha')
root.geometry("500x500+100+100")


menubar = Menu(root)
root.config(menu=menubar,bg='light blue')

root.bind('<Control-n>', newfile)
root.bind('<Control-o>', openfile)
root.bind('<Control-s>', save)
root.bind('<Control-Shift-s>', saveas)

root.bind('<Control-z>', undo)
root.bind('<Control-y>', redo)

root.bind('<Control-x>', cut)
root.bind('<Control-x>', copy)
root.bind('<Control-v>', paste)


root.bind('<Control-a>', selectall)

#####################Creating File menu bar##########
file = Menu(menubar)
file.add_command(label='New', accelerator='Ctrl + N', command=newfile)
file.add_command(label='Open', accelerator='Ctrl + O', command=openfile)
file.add_command(label='Save', accelerator='Ctrl + S', command=save)
file.add_command(label='Save as', accelerator='Ctrl +Shift + S', command=saveas)
menubar.add_cascade(label='File', menu=file)

#####################Creating Edit menu bar##########
edit = Menu(menubar)
edit.add_command(label='Undo', accelerator='Ctrl + Z', command=undo)
edit.add_command(label='Redo', accelerator='Ctrl + Y', command=redo)
edit.add_separator()
edit.add_command(label='Cut', accelerator='Ctrl + X', command=cut)
edit.add_command(label='Copy', accelerator='Ctrl + C', command=copy)
edit.add_command(label='Paste', accelerator='Ctrl + V', command=paste)
edit.add_separator()

edit.add_command(label='Select all', accelerator='Ctrl + A', command=selectall)
menubar.add_cascade(label='Edit', menu=edit)

 #####################Creating help menu bar##########
help = Menu(menubar)
help.add_command(label='Author', command=author)
help.add_command(label='Copyright', command=copyright)
menubar.add_cascade(label='Help', menu=help)


#########################line label##################
label = Label(root, width=2, bg='white')
label.pack(side=LEFT, fill=Y)

 ################Textpad#########
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

######################status bar to display version###########
statusbar = Label(root, text='Notepad v1.0',bg='light blue')
statusbar.pack(side=BOTTOM)

###################Scroll bar####
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)



###########calling main function ############
root.mainloop()
