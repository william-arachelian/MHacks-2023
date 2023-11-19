from paddleocr import PaddleOCR
import cv2
import numpy as np
import pandas as pd
import nltk
import re
nltk.download('popular')


def split_nutrition_string(nutrition_string):
    # Define a regex pattern to match nutrition name and measurement
    pattern = r'(\D+)(\d+\s*\.*\d*\s*\w+)'

    # Use re.findall to find all matches in the string
    matches = re.findall(pattern, nutrition_string)

    # If there are matches, extract nutrition name and measurement
    if matches:
        nutrition_name, measurement = matches[0]
        return nutrition_name.strip(), measurement.strip()
    else:
        return None


main_nutrition_facts = ["serving size", "fiber", "protein", "total carbohydrate", "total fat", "saturated fat", "trans fat", "cholesterol", "sodium"]

ocr = PaddleOCR(lang='en') # need to run only once to download and load model into memory
img_path = 'thing.jpg'
image = cv2.imread(img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


result = ocr.ocr(gray)

item_res = []
for idx in range(len(result)):
    res = result[idx]
    for counter, line in enumerate(res):
        text = line[1][0].lower()
        if text == "calories":      
            if res[counter - 1][1][0].isdigit():
                item_res.append(("calories", res[counter - 1][1][0]))
            elif res[counter + 1][1][0].isdigit():
                item_res.append(("calories", res[counter + 1][1][0]))
        
        try_split = split_nutrition_string(text)
        if try_split:
            if try_split[0] in main_nutrition_facts:
                item_res.append(try_split)   

series = pd.DataFrame(item_res)



series.to_csv("nutrition_label.txt", sep=',', index=False, encoding='utf-8')

