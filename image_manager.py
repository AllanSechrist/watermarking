from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk

WIDTH = 1260
HEIGHT = 840


class ImageManager():
    def __init__(self, root):
        self.canvas = Canvas(root, width = WIDTH, height = HEIGHT)  
        self.canvas.pack()
        self.canvas.bind('<B1-Motion>', self.move_watermark)
        self.image_to_save = None
        self.watermark_text = "Allan's WaterMarker"
        self.watermark_pos = None
        self.base_image = None
        self.overlay = None


    def move_watermark(self, event):
        self.update_watermark_overlay(x=event.x, y=event.y)


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


    def create_and_display_watermarked_image(self, file_name):
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
            
        resize = (image_width, image_height)
        image_resize = my_image.resize(size=resize)
        # image_resize = my_image.thumbnail([self.canvas.winfo_width(), self.canvas.winfo_height()], Image.ANTIALIAS)
        self.base_image = image_resize.convert("RGBA")
            
        self.update_watermark_overlay(x=self.base_image.width-100, y=self.base_image.height-50)

        my_image.close()  
  