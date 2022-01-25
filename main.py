from tkinter import *
from menu_functions import MenuManager



root = Tk()
root.title("WaterMaker Adder")

menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)

menu_manager = MenuManager(root)


# add menu items to the File menu
file_menu.add_command(label="Open", command=menu_manager.open_image_file)
file_menu.add_command(label="Save As", command=menu_manager.save_as_file)
file_menu.add_command(label="Edit Watermark", command=menu_manager.get_user_text)

# add Exit menu option
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)



if __name__ == "__main__":
    root.mainloop() 

