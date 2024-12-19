 

import io
import os
from google.cloud import vision_v1p3beta1 as vision
import cv2

import os
    
# Setup google authen client key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'

# Source path content all images
SOURCE_PATH = "img/"


def recognize_license_plate(img_path):
    img = cv2.imread(img_path)
    # Get image size
    height, width = img.shape[:2]
    # Scale image
    img = cv2.resize(img, (800, int((height * 800) / width)))
    # Show the origin image
    cv2.imshow('Origin image', img)
    # Save the image to temp file
    cv2.imwrite(SOURCE_PATH + "output.jpg", img)
    # Create new img path for google vision
    img_path = SOURCE_PATH + "output.jpg"
    # Create google vision client
    client = vision.ImageAnnotatorClient()
    # Read image file
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    response2 = client.text_detection(image=image)
    texts = response2.text_annotations
    for logo in logos:
        print(logo.description)
        cv2.putText(img, logo.description, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        cv2.imshow('Recognize & Draw', img)  
    i=0
    for text in texts:
        if i==0 :
            i=i+1
            license_plate = text.description
            print(license_plate)
            vertices = [(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices]
            cv2.rectangle(img, (vertices[0][0]-10, vertices[0][1]-10), (vertices[2][0]+10, vertices[2][1]+10), (0, 255, 0), 3)
            cv2.imshow('Recognize & Draw2', img)
            #cv2.waitKey(0)
            
print('---------- Start recognize license palate --------')
path = 'img'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))
            
for f in files:
    print(f)
    path = f
    recognize_license_plate(path)
    
print('---------- End ----------')


