# -*- coding: utf-8 -*-
"""extract text from image.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18TLI8u5C6mGSazT7_6ZrQCqHbBqYvvYo
"""

!pip install pytesseract pillow
!apt-get install tesseract-ocr

import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (in Google Colab)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

#Function that extracts text from image
def extract_text_from_image(image_path):
  with Image.open(image_path)as img:
    text = pytesseract.image_to_string(img)
    return text

#Function that saves the extracted text into a txt file
def save_to_file(text,output):
  with open(output, "w") as file:
    file.write(text)

#Enter the image path, and use the function to extract the image text to string
path=input("Please enter the path for the image:")
image_path = str(path)
text = extract_text_from_image(image_path)
print("\n\nExtracted text:\n")
print(text)

#give the output file a name, and call the save_to_file function with the corresponding parameters
output_file="text_from_image_transcribed.txt"
save_to_file(text,output_file)

