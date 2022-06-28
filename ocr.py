import cv2
import pytesseract
from difflib import SequenceMatcher

import tft_assets

# needed to add tesseract to path
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

# resize image
def resize_img(img, scale):
    return cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

# converting image into gray scale image
def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply blur to image to remove noise
def blur_image(img):
    return cv2.medianBlur(img,3)

# threshold image
def threshold(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# displaying an image
def show_image(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)

# now feeding image to tesseract to extract text
def run_OCR(im, coord, whitelist) -> str:
    # extract a ROI (Region of Interest) from the input image using input coordinates
    roi = im[coord[1]:coord[3], coord[0]:coord[2]]

    # skip image if size does not match. Should never happen if image is 1920x1080
    if roi.shape[0] == 0 or roi.shape[1] == 0:
        return ""

    img = resize_img(roi, scale = 2)
    img = get_grayscale(img)
    #img = threshold(img)
    return pytesseract.image_to_string(img, config = f'--oem 3 --psm 7 -c tessedit_char_whitelist= {whitelist}')

# match input name to champions if similar enough
def find_similar_string(input) -> str:
    for champ in tft_assets.champions:
        if SequenceMatcher(a=input,b=champ).ratio() >= 0.7:
            return champ
    return ""