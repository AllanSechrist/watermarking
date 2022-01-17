from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont


root = Tk()  
canvas = Canvas(root, width = 1260, height = 840)  
canvas.pack()

my_image = Image.open("open.jpg")
image_resize = my_image.resize(size=(my_image.width // 4, my_image.height // 4))
image_resize = image_resize.convert("RGBA")

# make a blank image for the text, initialized to transparent text color
overlay = Image.new("RGBA", image_resize.size, (255, 255, 255, 0))

# get a font
font = ImageFont.truetype("arial.ttf", 15)

watermark = ImageDraw.Draw(overlay)
watermark.text((image_resize.width - 100, image_resize.height - 50), "Hello World", font=font, fill=(255,255,255,128))

img_with_watermark = Image.alpha_composite(image_resize, overlay)

img = ImageTk.PhotoImage(image = img_with_watermark)
 
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop() 