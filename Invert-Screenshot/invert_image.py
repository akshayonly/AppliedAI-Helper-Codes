import os
import shutil
from PIL import Image, ImageOps
from datetime import date

# Directory to store both inverted and original screenshots
main_directory_path = "/home/akshaysonly/Pictures/Lecture-Screenshots"

# Place where screenshots are located
os.chdir("/home/akshaysonly/Pictures/")

# Getting the current date
today = date.today()
# Directory name which store inverted screenshot images with date of taken
# e.g Inverted-Screenshot-day-month-year
inverted_dir = "Inverted-Screenshot-"+str(today.day)+"-"+str(today.month)+"-"+str(today.year)

# Directory name which store original screenshot images
original_dir = "Original-Screenshot-"+str(today.day)+"-"+str(today.month)+"-"+str(today.year)


# Creating Directory to store inverted images
inverted_dir_path = os.path.join(main_directory_path, inverted_dir) 
  
try: 
    os.makedirs(inverted_dir_path, exist_ok = True) 
    print(f"'{inverted_dir_path}'- directory for inverted images created.") 
except OSError as error: 
    print(f"{inverted_dir_path} can not be created.\n") 

# Creating Directory to store original screenshot images
original_dir_path = os.path.join(main_directory_path, original_dir) 

try: 
    os.makedirs(original_dir_path, exist_ok = True) 
    print(f"'{original_dir_path}'- directory for original images created.\n")
except OSError as error: 
    print(f"{original_dir_path} can not be created.\n")    
    
# Iterating over directory contain 
image_count = 0 
for file in os.listdir():
    file_name, file_extension = os.path.splitext(file)
    # Selecting only images with '.png' extension
    # And "screen" name in them.
    if "screen" in (file_name).lower() and file_extension.lower() == '.png':
        image_count+=1
        print(f"Image {image_count}: {file}")
        # Opening & Converting .png
        img = Image.open(file).convert('RGB')
        # Inverting image object
        img_invert = ImageOps.invert(img)
        # Path To Save Inverted Image
        save_path = inverted_dir_path + "/" + "invert-" + file
        # Saving Image
        img_invert.save(save_path)
        # Move a file from the directory 
        source = os.getcwd() + '/' + file
        shutil.move(source, original_dir_path)

print(f"\nTotal Image Converted:{image_count}")     