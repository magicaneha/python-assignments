


from guitest import *



###############Calling main ###################
def main():
    root = Tk()
    root.minsize(width=1100, height=500)
    app = Contactbook(root, 'large_book')


    root.mainloop()

if __name__ == '__main__':

    main()