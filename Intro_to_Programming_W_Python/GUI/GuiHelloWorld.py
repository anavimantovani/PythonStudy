
import tkinter


class MyGui:


    def __init__(self):

        self.main_window = tkinter.Tk()


        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        self.label1.pack()


        self.label2 = tkinter.Label(self.main_window, text='Goodbye.')
        self.label2.pack()

        tkinter.mainloop()

myGui = MyGui()
