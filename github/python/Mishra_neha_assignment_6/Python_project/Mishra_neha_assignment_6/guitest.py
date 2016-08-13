

##################import neccessary modules###############################

from Tkinter import *
import tkMessageBox
import ttk
import database_implement
import VALIDATION
import sqlite3
import Queue
import zipfile
from threading import Thread
import urllib2
import webbrowser
import tkFileDialog


class Contactbook(Frame):
    def __init__(self, root, bookName):
        self.root = root
        Frame.__init__(self, self.root)
        self.bookName = bookName
        self.textArchive = Entry(self, width=35)
        self.textArchive.grid(row=0, column=0)
        self.book = database_implement.AddressBook(bookName)

    ############Few double click operations###############
        self.initUI()
        self.tree.bind("<Double-1>", self.OnDoubleClick)


    #################set up window (GUI)##############################
    def initUI(self):
        self.root.title(self.bookName)
        self.root.configure(background='white')
        # entries in address
    ###############Implemented tree for building column ##################################
        self.tree = ttk.Treeview(self.root)
        self.tree['show'] = 'headings'
        self.tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight")
        self.tree.column("one",width=100)
        self.tree.column("two", width=100)
        self.tree.column("three", width=100)
        self.tree.column("four", width=100)
        self.tree.column("five", width=75)
        self.tree.column("six", width=30)
        self.tree.column("seven", width=50)
        self.tree.column("eight", width=50)
        self.tree.heading("one", text="First", command=lambda: self.sort('first_nm'))
        self.tree.heading("two", text="Last", command=lambda: self.sort('last_nm'))
        self.tree.heading("three", text="Address")
        self.tree.heading("four", text="Address 2")
        self.tree.heading("five", text="City", command=lambda: self.sort('city'))
        self.tree.heading("six", text="State", command=lambda: self.sort('state'))
        self.tree.heading("seven", text="Zip", command=lambda: self.sort('zip'))
        self.tree.heading("eight", text="Phone", command=lambda: self.sort('phone'))
        self.tree.grid(row=0, columnspan=4)
    #####################end entries#################################################

    ############################menu bar#############################################
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: self.name_window('new'))
        filemenu.add_command(label="Open", command=lambda: self.name_window('open'))
        filemenu.add_command(label="Export", command=lambda:self.book.exportContacts())

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=lambda: self.quit())

        menubar.add_cascade(label="File", menu=filemenu)


        self.root.config(menu=menubar,background='light blue')
        #################end menu bar################################################


        ###################Building frame###########################################
        frame1 = Frame(self.root, width=400, height=200)

        firstLabel = Label(frame1, text="First Name:")
        firstLabel.grid(row=0, column=0)

        self.firstName = StringVar()
        self.firstEntry = Entry(frame1, textvariable=self.firstName)
        self.firstEntry.grid(row=0, column=1, sticky=(N, W))

        lastLabel = Label(frame1, text="Last Name:")
        lastLabel.grid(row=0, column=2)

        self.lastName = StringVar()
        self.lastEntry = Entry(frame1, textvariable=self.lastName)
        self.lastEntry.grid(row=0, column=3)

        add1Label = Label(frame1, text="Address Line 1:")
        add1Label.grid(row=0, column=4)

        self.address1 = StringVar()
        self.add1Entry = Entry(frame1, textvariable=self.address1)
        self.add1Entry.grid(row=0, column=5)

        add2Label = Label(frame1, text="Address Line 2:")
        add2Label.grid(row=0, column=6)

        self.address2 = StringVar()
        self.add2Entry = Entry(frame1, textvariable=self.address2)
        self.add2Entry.grid(row=0, column=7)

        cityLabel = Label(frame1, text="City:")
        cityLabel.grid(row=1, column=0)

        self.city = StringVar()
        self.cityEntry = Entry(frame1, textvariable=self.city)
        self.cityEntry.grid(row=1, column=1)

        stateLabel = Label(frame1, text="State:")
        stateLabel.grid(row=1, column=2)

        self.state = StringVar()
        self.stateEntry = Entry(frame1, textvariable=self.state)
        self.stateEntry.grid(row=1, column=3)

        zipLabel = Label(frame1, text="Zip:")
        zipLabel.grid(row=1, column=4)

        self.zip = StringVar()
        self.zipEntry = Entry(frame1, textvariable=self.zip)
        self.zipEntry.grid(row=1, column=5)

        phoneLabel = Label(frame1, text="Phone Number:")
        phoneLabel.grid(row=1, column=6)

        self.phone = StringVar()
        self.phoneEntry = Entry(frame1, textvariable=self.phone)
        self.phoneEntry.grid(row=1, column=7)

        saveCon = Button(frame1, text='Add Contact',width = 12, command=lambda: self.saveContact('save'))
        saveCon.grid(row=0, column=8)

        cancelButton = Button(frame1, text='Cancel',width = 12, command=lambda:self.clearBoxes())
        cancelButton.grid(row=2, column=9)

        PopBut = Button(frame1, text='Pop', width=12, command=lambda: self.pop())
        PopBut.grid(row=2, column=8)
        self.editID = ''
        editCon = Button(frame1, text='Edit Contact',width = 12,command=lambda: self.saveContact('edit'))
        editCon.grid(row=0, column=9)

        deleteCon = Button(frame1, text='Delete Contact',width = 12,command=lambda: self.deleteContact())
        deleteCon.grid(row=1, column=9)

        searchBut = Button(frame1, text='Search',width = 12,command=lambda:self.search())
        searchBut.grid(row=1, column=8)

        Zip = Button(frame1, text='Create zip',width = 36,command=lambda:self.loadFileArchive())
        Zip.grid(row=2, column=7)

        Search = Button(frame1, text='Open multple sites to search', width=36, command=lambda: self.startfunction())
        Search.grid(row=2, column=6)



        self.refresh(self.book.viewContacts())
        frame1.pack(fill=None, expand=NO)
        self.tree.pack(expand=YES, fill=BOTH)



    ##########################Building functions ########################################


        ###################opens multiple sites by threading#####################################

    def startfunction(self):
        def get_url(a_queue, a_url):
            a_queue.put(urllib2.urlopen(a_url).read())
            webbrowser.open_new(a_url)

        the_urls = ["http://google.com", "http://yahoo.com", "http://www.bing.com"]

        the_queue = Queue.Queue()
        tkMessageBox.showinfo("info", "opening websites simultaneously ")
        for url in the_urls:
            Thread(target=get_url, args=(the_queue, url)).start()

    #######################Creating zipfile function#####################################
    def loadFileArchive(self):
        fileArchive = tkFileDialog.askopenfilename(filetypes=(("Text File", "*.txt"),
                                                 ("All files", "*.*")))

        if fileArchive:
            try:
                self.textArchive.insert(0, fileArchive)
                loczip = 'abc.zip'
                zip = zipfile.ZipFile(loczip, "w")
                zip.write(fileArchive)
                tkMessageBox.showinfo("info", "zipfile created")
                zip.close()
            except:
                tkMessageBox.showerror("Open Source File", "Failed to read file\n'%s'" % fileArchive)
            return
 ######################pop the first element and display #######################
    def pop(self):
            db = sqlite3.connect('AddressBook.db')
            cu = db.cursor()

            cu.execute("select * from Contacts")
            AllItems = cu.fetchall()

            AllItems.pop((len(AllItems) - 1))
            db.commit()
            cu.close()
            print(AllItems)
            tkMessageBox.showinfo("pop","First Element popped")



   ############################Search the contacts###################################
    def search(self):
        self.refresh(self.book.viewContacts(last_nm=self.lastName.get(),zip=self.zip.get()))
        tkMessageBox.showinfo("info","search on progress")

    #######add contact to book or edit an existing contact. invoked on button click##########
    def saveContact(self,saveOrEdit):

        first = self.firstEntry.get()
        last = self.lastEntry.get()
        add1 = self.add1Entry.get()
        add2 = self.add2Entry.get()
        city = self.cityEntry.get()
        state = self.stateEntry.get()
        zip = self.zipEntry.get()
        phone = self.phoneEntry.get()

        ###########################Applied validation#############################
        valid, errorMsgs = VALIDATION.validated(first=first, last=last, add1=add1, add2=add2, city=city,
                                                        state=state, zip=zip, phone=phone)
        zipVal = VALIDATION.validateZip(zip)

        #############################adds new contact to book########################
        if saveOrEdit == 'save':
            if valid is False:
                tkMessageBox.showwarning("Warning","Please provide a first or last name and one other field")
                return
            elif zipVal is False:
                if tkMessageBox.askokcancel("Warning","Zip code does not match postal standards! Do you want to continue anyway?"):
                    self.book.addContact(first, last, add1, add2, city, state, zip, phone)
                    tkMessageBox.showinfo("info", "Contact saved")
                else:
                    return
            else:
                self.book.addContact(first, last, add1, add2, city, state, zip, phone)
                tkMessageBox.showinfo("info", "Contact saved")

        #########################edits existing contact#########################################
        elif saveOrEdit == 'edit':
            if self.editID == '':
                tkMessageBox.showwarning("Select Contact","Please select a contact to edit or create a new contact!")
                return
            else:
                if valid is False:
                    tkMessageBox.showwarning("Warning","Please provide a first or last name and one other field")
                    return
                elif zipVal is False:
                     if tkMessageBox.askokcancel("Warning","Zip code does not match postal standards! Do you want to continue anyway?"):
                        self.book.edit(self.editID,first,last,add1,add2,city,state,zip,phone)
                        tkMessageBox.showinfo("info", "Contact saved")
                     else:
                        return
                else:
                    self.book.edit(self.editID,first,last,add1,add2,city,state,zip,phone)
                    tkMessageBox.showinfo("info", "Contact updated")

        self.refresh(self.book.viewContacts())
        self.clearBoxes()
        self.editID = ''

    ####################delete contact from database and window########################################
    def deleteContact(self):
        if tkMessageBox.askokcancel("Warning","Are you sure you want to delete contact?"):
            item = self.tree.selection()[0]
            id = self.tree.item(item, "text")
            self.book.delete(id)
            self.refresh(self.book.viewContacts())
            self.clearBoxes()
            tkMessageBox.showinfo("info", "Contact deleted")
        else:
            return

    ###################################clears entry boxes in top frame when we call cancel button ####################################
    def clearBoxes(self):
        self.firstName.set('')
        self.lastName.set('')
        self.address1.set('')
        self.address2.set('')
        self.city.set('')
        self.state.set('')
        self.zip.set('')
        self.phone.set('')
        self.editID =''

        self.refresh(self.book.viewContacts())


    ###########################################Sort entries using dict sorting by first name, last name ,zip,state ,city#################
    def sort(self, sortby):
        if sortby == 'first_nm':
            sorting = self.book.sortByFirst()
            tkMessageBox.showinfo("info", "Dict_sorting by first name")
        elif sortby == 'last_nm':
            sorting = self.book.sortByLast()
            tkMessageBox.showinfo("info", "Dict_sorting by last name")

        elif sortby == 'address1' :
            sorting = self.book.sortByAddress()
            tkMessageBox.showinfo("info", "Dict_sorting by Address")

        elif sortby == 'zip':
            sorting = self.book.sortByZip()
            tkMessageBox.showinfo("info", "Dict_sorting by zip")
        elif sortby == 'state':
            sorting = self.book.sortByState()
            tkMessageBox.showinfo("info", "Dict_sorting by state")
        elif sortby == 'city':
            sorting = self.book.sortByCity()
            tkMessageBox.showinfo("info", "Dict_sorting by city")
        else:
            sorting = self.book.sortByPhone()
            tkMessageBox.showinfo("info", "Dict_sorting by phone")

        self.refresh(sorting)

    #######################replaces all info in table with info in contacts parameter################################
    def refresh(self, contacts):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for contact in contacts:
            self.tree.insert("", 0, text=contact[0], values=(contact[1], contact[2], contact[3], contact[4], contact[5],
                                                             contact[6], contact[7], contact[8]))

    #######################grabs info from row double clicked and puts it in entries in top frame######################
    def OnDoubleClick(self, event):
        item = self.tree.selection()[0]
        self.editID = self.tree.item(item, "text")
        self.firstName.set(self.tree.set(item)['one'])
        self.lastName.set(self.tree.set(item)['two'])
        self.address1.set(self.tree.set(item)['three'])
        self.address2.set(self.tree.set(item)['four'])
        self.city.set(self.tree.set(item)['five'])
        self.state.set(self.tree.set(item)['six'])
        self.zip.set(self.tree.set(item)['seven'])
        self.phone.set(self.tree.set(item)['eight'])
        id = self.tree.item(item, "text")


    ###############creates new address book#############################################
    def create_window(self, bookName=''):
        newWindow = Toplevel(self)
        newWindow.minsize(width=1100, height=500)
        app = Contactbook(newWindow, bookName)
        app.pack()





    #######################pop up window to get name for new window#################################
    def name_window(self,openOrCreate):
        namewin = Toplevel(self.root)
        namewin.minsize(width=500, height=100)
        nameFrame = Frame(namewin, width=200, height=200)

        if openOrCreate == 'open':
            namewin.title('Open Address Book')
            files = Label(nameFrame, text='Existing Address Books:')
            files.grid(row=3, column=0)
            rowNum = 4
            for name in self.book.getBookNames():
                Label(nameFrame,text=name).grid(row=rowNum)
                rowNum += 1
        else:
            namewin.title('Create Address Book')

        label = Label(nameFrame, text='Enter file name below')
        label.grid(row=1, columnspan=2)
        fileName = StringVar()
        nameEntry = Entry(nameFrame, textvariable=fileName)
        nameEntry.grid(row=2, column=0, sticky=(N, W))
        okay = Button(nameFrame, text="Ok", command=lambda: [self.create_window(fileName.get()), namewin.destroy()])
        okay.grid(row=2, column=1)


        nameFrame.pack()


