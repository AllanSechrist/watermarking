# from textwrap import fill
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
from image_manager import ImageManager




class MenuManager(object):
    def __init__(self, root):
        self.root = root
    
        self.image_manager = ImageManager(root)


    def open_image_file(self):
        file_name = filedialog.askopenfilename(initialdir="/", title="Select a file",filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))

        self.image_manager.create_and_display_watermarked_image(file_name)

          
    def save_as_file(self):
        files = [("PNG File", "*.png")]
        image_file = filedialog.asksaveasfilename(initialdir = "C:\\Users\\Allan\\Projects\\pycourse\\watermarking",filetypes=files, defaultextension=files)

        if image_file:
            self.root.title(f'{image_file} - Watermark Adder')

            # save the file
            self.image_manager.image_to_save.save(image_file) 


    def get_user_text(self):
        window = Toplevel(self.root)
        window.geometry("500x250")
        window.title("Text Watermark")

        label=Label(window, text="Please enter your text into the box", font=("arial 15 bold"))
        label.pack(pady=40)

        entry= Entry(window, width= 20)
        entry.focus_set()
        entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        
        def set_text(): # sets new watermark
            self.image_manager.watermark_text = entry.get()
            if not self.image_manager.base_image:
                label.configure(text="Your Watermark has been saved!")
            else:
                self.image_manager.update_watermark_overlay(self.image_manager.base_image.width - 100, self.image_manager.base_image.height - 50)

            window.destroy()

        Button(window, text= "Ok",width= 20, command=set_text).pack(pady=40)


  