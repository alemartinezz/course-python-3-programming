---
author: No author.
tags:
  - knowledge
  - comp-sci
  - projects
  - Python 3 Programming Specialization - Coursera
  - Python3Programming_FinalProject
description: No description.
---
import math
import zipfile
from PIL import Image, ImageOps, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np


# loading the face detection classifier
face_cascade = cv.CascadeClassifier(
    'readonly/haarcascade_frontalface_default.xml')
images = {}


# iterate through the zip file and save all the binarized versions to images
with zipfile.ZipFile('readonly/images.zip', 'r') as archive:
    for entry in archive.infolist():
        with archive.open(entry) as file:
            img = Image.open(file).convert('RGB')
            images[entry.filename] = {'pil_img': img}


# parse all images text
for img_name in images.keys():
    text = pytesseract.image_to_string(images[img_name]['pil_img'])
    images[img_name]['text'] = text


# find the bounding boxes for all the faces from every page and extract them
for img_name in images.keys():
    open_cv_image = np.array(images[img_name]['pil_img'])
    img_g = cv.cvtColor(open_cv_image, cv.COLOR_BGR2GRAY)
    faces_bounding_boxes = face_cascade.detectMultiScale(img_g, 1.3, 5)
    images[img_name]['faces'] = []
    for x, y, w, h in faces_bounding_boxes:
        face = images[img_name]['pil_img'].crop((x, y, x + w, y + h))
        images[img_name]['faces'].append(face)


# create thumbnails
for img_name in images.keys():
    for face in images[img_name]['faces']:
        face.thumbnail((100, 100), Image.ANTIALIAS)


# search the keyword in every page's text and return the faces
def search(keyword):
    for img_name in images:
        if (keyword in images[img_name]['text']):
            if(len(images[img_name]['faces']) != 0):
                print("Result found in file {}".format(img_name))
                h = math.ceil(len(images[img_name]['faces']) / 5)
                contact_sheet = Image.new('RGB', (500, 100 * h))
                xc = 0
                yc = 0

                for img in images[img_name]['faces']:
                    contact_sheet.paste(img, (xc, yc))
                    if xc + 100 == contact_sheet.width:
                        xc = 0
                        yc += 100
                    else:
                        xc += 100

                return display(contact_sheet)

            else:
                return "Result found in file {} \nBut there were no faces in that file".format(img_name)search("Christopher")search("Mark")

search('Christopher')
search('Mark')
search('pizza')