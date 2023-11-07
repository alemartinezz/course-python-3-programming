---
author: No author.
tags:
  - knowledge
  - comp-sci
  - projects
  - Python 3 Programming Specialization - Coursera
  - Python3Programming_PillowImageManipulation
description: No description.
---
import PIL
from PIL import Image, ImageDraw

# read image and convert to RGB
image = Image.open("readonly/msi_recruitment.gif").convert('RGB')

# create a list with the resulting images
images = []


for i in (0.1, 0.5, 0.9):
        
    # divide the bands (red, green, blue).
    red, green, blue = image.split()
    
    # Map this band through a single value (intensity: 0.1, 0.5, 0.9).
    red = red.point(lambda x: x * i)
    
    # Merge the result and the other bands into a single image.
    merged = Image.merge('RGB', (red, green, blue))
    
    # Create a new image with the given mode and size.
    result = Image.new('RGB', (merged.width, 50))
    
    # Draw the resulting image.
    result_image = ImageDraw.Draw(result)
    
    # Add the required text
    fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 50)
    result_image.text((10, 10), 'channel 0 intensity {}'.format(i), font = fnt, fill = merged.getpixel((0, 100)))
    
    # Create a "sheet" containing the new image with the proper height and width.
    sheet = PIL.Image.new(merged.mode, (merged.width, merged.height + result.height))
    sheet.paste(result, (0, merged.height))
    sheet.paste(merged, (0, 0))
    
    # Append the new image to the 'images' list.
    images.append(sheet)


for i in (0.1, 0.5, 0.9):
    red, green, blue = image.split()
    green = green.point(lambda x: x * i)
    
    merged = Image.merge('RGB', (red, green, blue))
    result = Image.new('RGB', (merged.width, 50))
    result_image = ImageDraw.Draw(result)
    
    fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 50)
    result_image.text((10, 10), 'channel 1 intensity {}'.format(i), font = fnt, fill = merged.getpixel((0, 100)))
    
    sheet = PIL.Image.new(merged.mode, (merged.width, merged.height + result.height))
    sheet.paste(result, (0, merged.height))
    sheet.paste(merged, (0, 0))
    
    images.append(sheet)


for i in (0.1, 0.5, 0.9):
    red, green, blue = image.split()
    blue = blue.point(lambda x: x * i)
    
    merged = Image.merge('RGB', (red, green, blue))
    result = Image.new('RGB', (merged.width, 50))
    result_image = ImageDraw.Draw(result)
    
    fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 50)
    result_image.text((10, 10), 'channel 2 intensity {}'.format(i), font = fnt, fill = merged.getpixel((0, 100)))
    
    sheet = PIL.Image.new(merged.mode, (merged.width, merged.height + result.height))
    sheet.paste(result, (0, merged.height))
    sheet.paste(merged, (0, 0))
    
    images.append(sheet)


# create a contact sheet for displaying the 'images' list.
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)