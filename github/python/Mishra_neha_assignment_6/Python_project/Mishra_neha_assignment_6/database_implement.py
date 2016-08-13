

import sqlite3
import importfile


################################Some functions are defined in this class #########################
class AddressBook(object):

    def __init__(self,bookName = 'default'):

        self.connection = sqlite3.connect('AddressBook.db')
        self.bookName = bookName

    def __del__(self):
        self.connection.close()

#####################Add contact ##################################################################
    def addContact(self, first_nm='', last_nm='',address1='',address2='',city='',state='',zip='',phone=''):

        cur = self.connection.cursor()
        cur.execute('INSERT INTO contacts(first_nm,last_nm,address1,address2,city,state,zip,phone,bookName) '
                    'VALUES(?,?,?,?,?,?,?,?,?)', (first_nm, last_nm, address1, address2, city, state, zip,phone,self.bookName))
        self.connection.commit()

###########################View all contact#############################################################

    def viewContacts(self,contactId ='',last_nm ='',zip =''):
        cur = self.connection.cursor()
        if contactId == '' and last_nm =='' and zip=='':
            cur.execute('SELECT * FROM contacts WHERE bookName = ?',(self.bookName,))
        elif last_nm == '' and zip != '':
            cur.execute('SELECT * FROM contacts WHERE zip = ? AND bookName = ?', (zip,self.bookName))
        elif last_nm != '' and zip == '':
            cur.execute('SELECT * FROM contacts WHERE bookName = ? AND last_nm = ?', (self.bookName,last_nm))
        elif last_nm != '' and zip != '':
            cur.execute('SELECT * FROM contacts WHERE bookName = ? AND last_nm = ? AND zip = ?', (self.bookName,last_nm,zip))
        else:
            cur.execute('SELECT * FROM contacts WHERE contact_id = ? AND bookName = ?', (contactId,self.bookName))

        return cur.fetchall()

###########################Export to create csv file #######################################################
    def exportContacts(self):
        cur = self.connection.cursor()
        cur.execute('SELECT first_nm, last_nm, address1, address2, city, state, zip, phone FROM contacts WHERE bookName = ?', (self.bookName,))
        result_set = cur.fetchall()
        print result_set
        importfile.createBasicCSV(dataList=result_set)





#########################sorting by first name ###########################################
    def sortByFirst(self):

        cur = self.connection.cursor()

        cur.execute('SELECT * FROM contacts WHERE bookName = ? ORDER BY  first_nm DESC', (self.bookName,))

        return cur.fetchall()

    #########################sorting by last name ###########################################
    def sortByLast(self):

        cur = self.connection.cursor()

        cur.execute('SELECT * FROM contacts WHERE bookName = ? ORDER BY  last_nm  DESC', (self.bookName,))

        return cur.fetchall()



        #########################sorting by Address1  ###########################################

    def sortByAddress(self):

        cur = self.connection.cursor()

        cur.execute('SELECT * FROM contacts WHERE bookName = ? ORDER BY  address1  DESC', (self.bookName,))

        return cur.fetchall()

    #########################sorting by first name ###########################################
    def sortByZip(self):

        cur = self.connection.cursor()

        cur.execute('SELECT * FROM contacts WHERE bookName = ? ORDER BY zip DESC',(self.bookName,))

        return cur.fetchall()

    #########################sorting by State ###########################################
    def sortByState(self):

        cur = self.connection.cursor()

        cur.execute('SELECT * FROM contacts WHERE bookName = ? ORDER BY state DESC', (self.bookName,))

        return cur.fetchall()

    #########################sorting by Phone ####################################################
    def sortByPhone(self):

        cur = self.connection.cursor()

        cur.execute('SELECT * FROM contacts WHERE bookName = ? ORDER BY phone DESC', (self.bookName,))

        return cur.fetchall()

    #########################sorting by City ###################################################
    def sortByCity(self):

        cur = self.connection.cursor()

        cur.execute('SELECT * FROM contacts WHERE bookName = ? ORDER BY city DESC',(self.bookName,))

        return cur.fetchall()

    #########################Edit details ###########################################
    def edit(self, contact_id, first_nm, last_nm, address1, address2, city, state, zip,phone):
        cur = self.connection.cursor()
        cur.execute('UPDATE contacts SET first_nm = ?, last_nm = ?, address1 = ?, address2 = ?,'
                    'city = ?, state = ?, zip = ?, phone =? WHERE contact_id = ?',
                    (first_nm, last_nm, address1, address2, city, state, zip, phone, contact_id))
        self.connection.commit()

    #########################delete by contact id ###########################################
    def delete(self,contact_id):
        cur = self.connection.cursor()
        cur.execute('DELETE FROM contacts WHERE contact_id = ?',(contact_id,))
        self.connection.commit()

    #########################deleteall records  ###########################################
    def deleteAll(self,bookName):
        cur = self.connection.cursor()
        cur.execute('DELETE FROM contacts WHERE bookName = ?',(bookName,))
        self.connection.commit()

    #########################Getting book names  ###########################################
    def getBookNames(self):
        cur = self.connection.cursor()

        cur.execute('SELECT bookName FROM contacts GROUP BY bookName')

        return cur.fetchall()




