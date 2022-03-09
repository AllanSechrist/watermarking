from tkinter import *
from tkinter import filedialog
from image_manager import ImageManager


class EditMenu(Menu):
    def __init__(self, root, menu_bar):
        super().__init__(menu_bar, tearoff=False)
        self.add_command(label="Rotate image 90", command=self.rotate_image_90_degrees)
        self.add_command(label="Horizontal Flip", command=self.flip_image_horizontally)
        self.add_command(label="Vertical Flip", command=self.flip_image_vertically)
        menu_bar.add_cascade(label="Edit", menu=self)


    def rotate_image_90_degrees(self):
        pass


    def flip_image_horizontally(self):
        pass


    def flip_image_vertically(self):
        pass