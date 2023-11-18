import cv2
import pytesseract
import easyocr
# import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#reader = easyocr.Reader(['en'], gpu = True) # this needs to run only once to load the model into memory
img_cv = cv2.imread("thing.png")
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)



thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
# normalize the distance transform such that the distances lie in
# the range [0, 1] and then convert the distance transform back to
# an unsigned 8-bit integer in the range [0, 255]
dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
dist = (dist * 255).astype("uint8")
# threshold the distance transform using Otsu's method
dist = cv2.threshold(dist, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# imS = cv2.resize(dist, (780, 700))                # Resize image

cv2.imshow("Otsu", dist)

# print(pytesseract.image_to_string(gray))

# result = reader.readtext(gray, detail=0, decoder='beamsearch')
# for r in result:
#     print(r)

#df = pd.to_dataframe(result)
    



# cv2.imshow("Image", imS)

cv2.waitKey(0)

# cv2.destroyAllWindows()
