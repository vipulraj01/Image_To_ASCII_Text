# Deserialize from PIL import image
from PIL import Image

# Open walterwhite .jpg image
Image.open(r"walterwhite.jpg")

# Import pywhatkit.
import pywhatkit

# convert walterwhite .jpg to ascii art
pywhatkit.image_to_ascii_art(r"walterwhite.jpg","walterwhite")

# Read walterwhite. txt file
read_file= open("walterwhite.txt","r")

# Print the contents of a file to stdout
print(read_file.read())
