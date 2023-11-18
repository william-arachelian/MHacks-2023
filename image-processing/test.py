import cv2
import pytesseract
from paddleocr import PaddleOCR
# import pandas as pd

#reader = easyocr.Reader(['en'], gpu = True) # this needs to run only once to load the model into memory
img_cv = cv2.imread("IMG_7505.jpg")
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)


ocr = PaddleOCR(use_angle_cls=True)
result = ocr.ocr(img_cv)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)