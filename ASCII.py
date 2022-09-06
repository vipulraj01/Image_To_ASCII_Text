from PIL import Image
Image.open(r"walterwhite.jpg")

import pywhatkit
pywhatkit.image_to_ascii_art(r"walterwhite.jpg","walterwhite")
read_file= open("walterwhite.txt","r")
print(read_file.read())
