from tkinter import *
from file_menu import FileMenu
from edit_menu import EditMenu


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("WaterMark Adder")
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        self.file_menu = FileMenu(self, menu_bar)
        self.edit_menu = EditMenu(self, menu_bar)
        


if __name__ == "__main__":
    app = App()
    app.mainloop()

