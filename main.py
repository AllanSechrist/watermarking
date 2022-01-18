from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont


root = Tk()

def open_image_file():
    global img
    file_name = filedialog.askopenfilename(initialdir="/", title="Select a file",filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))

    if file_name:
        my_image = Image.open(file_name)
        image_resize = my_image.resize(size=(my_image.width // 4, my_image.height // 4))
        image_resize = image_resize.convert("RGBA")

        # make a blank image for the text, initialized to transparent text color
        overlay = Image.new("RGBA", image_resize.size, (255, 255, 255, 0))

        # get a font
        font = ImageFont.truetype("arial.ttf", 15)

        watermark = ImageDraw.Draw(overlay)
        watermark.text((image_resize.width - 100, image_resize.height - 50), "Hello World", font=font, fill=(255,255,255,64))

        img_with_watermark = Image.alpha_composite(image_resize, overlay)
        # img_with_watermark.save("with_watermark.png", "PNG")

        img = ImageTk.PhotoImage(image = img_with_watermark)

        canvas.create_image(20, 20, anchor=NW, image=img) 

    


def save_file():
    files = [("PNG File", "*.png")]
    f = filedialog.asksaveasfile(initialdir = "C:\\Users\\Allan\\Projects\\pycourse\\watermarking",filetypes=files, defaultextension=files)

    if f is None:
        return

canvas = Canvas(root, width = 1260, height = 840)  
canvas.pack()

save_btn = Button(root, text ='Save', width=15, height=2, command = save_file())
save_btn.pack()

my_btn = Button(root, text="Open File", width=15, height=2, command=open_image_file).pack()




root.mainloop() 