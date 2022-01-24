from textwrap import fill
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import time

WIDTH = 1260
HEIGHT = 840

class MenuManager(object):
    def __init__(self, root):
        self.root = root
        canvas = Canvas(root, width = WIDTH, height = HEIGHT)  
        canvas.pack()
        self.canvas = canvas
        self.canvas.bind('<B1-Motion>', self.move_watermark)
        self.image_to_save = None
        self.watermark_text = "Allan's WaterMarker"
        self.watermark_pos = None
        self.base_image = None
        self.overlay = None

    def open_image_file(self):
        global img
        file_name = filedialog.askopenfilename(initialdir="/", title="Select a file",filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))

        if file_name:
            self.root.title(f'{file_name} - Watermark Adder')
            my_image = Image.open(file_name)
            
            image_width = my_image.width
            image_height = my_image.height

            try:
                if my_image.width > self.canvas.winfo_width(): # get width of the canvas
                    image_width = self.canvas.winfo_width() # set image width to that of the canvas

                if my_image.height > self.canvas.winfo_height(): # get the height of the canvas
                    image_height = self.canvas.winfo_height() # set image height to that of the canvas
            except AttributeError:
                pass

            # my_resize = (my_image.width // 4, my_image.height // 4)
            resize = (image_width, image_height)
            image_resize = my_image.resize(size=resize)
            image_resize = image_resize.convert("RGBA")
            self.base_image = image_resize 
            # image_resize = my_image.thumbnail([self.canvas.winfo_width(), self.canvas.winfo_height()], Image.ANTIALIAS)

            self.update_watermark_overlay(x=self.base_image.width-100, y=self.base_image.height-50)
            my_image.close()   


    def move_watermark(self, event):
        self.update_watermark_overlay(x=event.x, y=event.y)


    def save_as_file(self):
        files = [("PNG File", "*.png")]
        image_file = filedialog.asksaveasfilename(initialdir = "C:\\Users\\Allan\\Projects\\pycourse\\watermarking",filetypes=files, defaultextension=files)

        if image_file:
            self.root.title(f'{image_file} - Watermark Adder')

            # save the file
            self.image_to_save.save(image_file)


    def get_user_text(self):
        window = Toplevel(self.root)
        window.geometry("500x250")
        window.title("Text Watermark")

        label=Label(window, text="Please enter your text into the box", font=("Courier 15 bold"))
        label.pack(pady=40)

        entry= Entry(window, width= 20)
        entry.focus_set()
        entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        
        def set_text(): # sets new watermark
            # NOT FUNCTIONING AS INTEDED/DOES NOT IMMEDIATLY UPDATE THE WATERMARK ON SCREEN
            if not self.base_image:
                self.watermark_text = entry.get()
                label.configure(text="Your Watermark has been saved!")
                window.destroy()
            else:
                self.watermark_text = entry.get()
                
                # self.overlay = Image.new("RGBA", self.base_image.size, (255, 255, 255, 0))

                # # get a font
                # font = ImageFont.truetype("arial.ttf", 15)

                # self.watermark_pos = ImageDraw.Draw(self.overlay)
                # self.watermark_pos.text((self.base_image.width - 100, self.base_image.height - 50), f'{self.watermark_text}', font=font, fill=(255,255,255,128), anchor="mb")


                # img_with_watermark = Image.alpha_composite(self.base_image, self.overlay)
                # self.image_to_save = img_with_watermark # store the image to save it.

                # img = ImageTk.PhotoImage(image = img_with_watermark)
                # self.canvas.create_image(20, 20, anchor=NW, image=img) 

                window.destroy()

        Button(window, text= "Ok",width= 20, command=set_text).pack(pady=40)


    def update_watermark_overlay(self, x=0, y=0):
        global img
        text_pos = (x, y)
        self.overlay = Image.new("RGBA", self.base_image.size, (255, 255, 255, 0))
        # get a font
        font = ImageFont.truetype("arial.ttf", 15)
        self.watermark_pos = ImageDraw.Draw(self.overlay)
        self.watermark_pos.text(text_pos, f'{self.watermark_text}', font=font, fill=(255,255,255,128), anchor="mb")
        img_with_watermark = Image.alpha_composite(self.base_image, self.overlay)
        self.image_to_save = img_with_watermark # store the image to save it.
        img = ImageTk.PhotoImage(image = img_with_watermark)
        self.canvas.create_image(20, 20, anchor=NW, image=img) 