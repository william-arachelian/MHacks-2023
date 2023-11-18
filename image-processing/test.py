from paddleocr import PaddleOCR,draw_ocr
import cv2
import numpy as np
ocr = PaddleOCR(lang='en') # need to run only once to download and load model into memory
img_path = 'IMG_7505.jpg'
image = cv2.imread(img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


result = ocr.ocr(gray)

for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line[1][0])
