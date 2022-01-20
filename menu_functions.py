from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


class MenuManager(object):
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.image_to_save = None

    def open_image_file(self):
        global img
        file_name = filedialog.askopenfilename(initialdir="/", title="Select a file",filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))

        if file_name:
            self.root.title(f'{file_name} - Watermark Adder')
            my_image = Image.open(file_name)
            
            try:
                if my_image.width > 1260:
                    my_image.width = 1260

                if my_image.height > 840:
                    my_image.height = 840
            except AttributeError:
                pass

            # my_resize = (my_image.width // 4, my_image.height // 4)
            my_resize = (my_image.width, my_image.height)
            image_resize = my_image.resize(size=my_resize)
        
            image_resize = image_resize.convert("RGBA") 

            # make a blank image for the text, initialized to transparent text color
            overlay = Image.new("RGBA", image_resize.size, (255, 255, 255, 0))

            # get a font
            font = ImageFont.truetype("arial.ttf", 15)

            watermark = ImageDraw.Draw(overlay)
            watermark.text((image_resize.width - 100, image_resize.height - 50), "Hello World", font=font, fill=(255,255,255,128))

            img_with_watermark = Image.alpha_composite(image_resize, overlay)
            self.image_to_save = img_with_watermark

            img = ImageTk.PhotoImage(image = img_with_watermark)
            self.canvas.create_image(20, 20, anchor=NW, image=img) 
            

            my_image.close()   

    def save_as_file(self):
        files = [("PNG File", "*.png")]
        image_file = filedialog.asksaveasfilename(initialdir = "C:\\Users\\Allan\\Projects\\pycourse\\watermarking",filetypes=files, defaultextension=files)

        if image_file:
            self.root.title(f'{image_file} - Watermark Adder')

            # save the file
            self.image_to_save.save(image_file)

