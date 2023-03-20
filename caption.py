
import sys
from transformers import pipeline

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

PATH = str(sys.argv[1])

print(PATH)

# we want to pass each image to image_to_text, and save the output to a list, then rename the images to the generated text

import os
import shutil

generated_file_names = []
    
for i in os.listdir(PATH):
    test = image_to_text(PATH + i)
    
    # replace the spaces with underscores
    text = test[0]['generated_text']
    
    text = text.replace(' ', '_')
    # rename the file
    os.rename(PATH + i, PATH + text + '.jpg')
    


