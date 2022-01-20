from tkinter import *
from menu_functions import MenuManager
# from PIL import Image, ImageTk
# from tkinter import ttk


# def display_image():
#     global img
#     img_to_display = open_image_file()
#     img = ImageTk.PhotoImage(image = img_to_display)
#     canvas.create_image(20, 20, anchor=NW, image=img) 


root = Tk()

menu_bar = Menu(root)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)

canvas = Canvas(root, width = 1260, height = 840)  
canvas.pack()

menu_manager = MenuManager(root, canvas)



# add menu items to the File menu
file_menu.add_command(label="Open", command=menu_manager.open_image_file)
file_menu.add_command(label="Save As", command=menu_manager.save_as_file)

# add Exit menu option
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menu_bar.add_cascade(label="File", menu=file_menu)


# save_btn = Button(root, text ='Save', width=15, height=2, command = save_file)
# save_btn.pack()

# open_btn = Button(root, text="Open File", width=15, height=2, command=open_image_file).pack()

root.mainloop() 

