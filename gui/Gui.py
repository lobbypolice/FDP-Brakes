from tkinter import *

class Application(Frame):
    def __init__(self, root):

        menuSeparator = Frame(height=2, bd=1, relief=SUNKEN)
        menuSeparator.pack(side=TOP,fill=X, padx=1, pady=1)
        
        Frame.__init__(self, root)
        self.pack(fill = BOTH, expand = True)

        self.root = root

        self.root.geometry("600x400")
        self.root.resizable(0, 1)

        statusBar = StatusBar(root)
        statusBar.pack(side = BOTTOM,fill = X)

        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        self.fileMenu = Menu(menubar, tearoff = 0)
        self.fileMenu.add_command(label = "Import", command = self.onImport)
        menubar.add_cascade(label = "File", menu = self.fileMenu)


        leftFrame = Frame(self)
        leftFrame.pack(side = LEFT, fill=Y, padx=10, pady=20)

        leftFrameSeparator = Frame(self,width=2, bd=1, relief=SUNKEN)
        leftFrameSeparator.pack(side=LEFT,fill=Y, pady = 15)

        leftFrame2 = Frame(self)
        leftFrame2.pack(side = LEFT, padx=10, pady=20)

        
        textEntry1 = Entry(leftFrame)
        textEntry1.pack()
        
    def onImport(self):
        pass

    def statusBarUpdate(self, event=None):
        pass

    



class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd = 1, relief = SUNKEN, anchor = "w")
        self.label.pack(fill=X)
    def set(self, format0, *args):
        self.label.config(text = format0 % args)
        self.label.update_idletasks()
    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

class MenuBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        

def main():
   root = Tk()
   Application(root)
   root.mainloop()

if __name__ == '__main__':
   main()
