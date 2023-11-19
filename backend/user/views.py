from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import User
from label.models import Label
import cv2
import numpy as np
from paddleocr import PaddleOCR
import cv2
import numpy as np
import pandas as pd
import nltk
import re
def label_create_view(request):
    if (request.method == "POST"):
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        image = _grab_image(stream=request.FILES["image"])
        process_image(image)
        cv2.waitKey(0) 
        u = User(weight=weight, height=height, age=age, sex=sex)
        u.save()
    # print(request.GET)
    # print(request.POST)
    
    return render(request, "label/label_create.html")
# Create your views here.
def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)
	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		# if the stream is not None, then the image has been uploaded
		if stream is not None:
			data = stream.read()
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image

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

def process_image(img):
    
    nltk.download('popular')

    main_nutrition_facts = ["serving size", "fiber", "protein", "total carbohydrate", "total fat", "saturated fat", "trans fat", "cholesterol", "sodium"]

    ocr = PaddleOCR(lang='en') # need to run only once to download and load model into memory
    image = img
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
    calories = 0
    total_fat = 0
    trans_fat = 0
    sat_fat = 0
    carbs = 0
    sugar = 0
    fiber = 0
    cholesterol = 0
    sodium = 0
    protein = 0
    pattern = r'([0-9]+)'
    for i in range(len(series)):
        if series.loc[i, 0] == "calories":
            calories = series.loc[i, 1]
        if series.loc[i, 0] == "total fat":
            total_fat = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "trans fat":
            trans_fat = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "sat_fat":
            sat_fat = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "carbs":
            carbs = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "sugar":
            sugar = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "fiber":
            fiber = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "cholesterol":
            cholesterol = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "sodium":
            sodium = re.findall(pattern, series.loc[i, 1])[0]
        if series.loc[i, 0] == "protein":
            protein = re.findall(pattern, series.loc[i, 1])[0]
        # if series.loc[i, 0] == "total sugars":
        #     sugar = re.findall(pattern, series.loc[i, 1])[0]
    l = Label( calories=calories,  total_fat = total_fat, trans_fat = trans_fat, 
               sodium =sodium,  protein = protein, sat_fat = sat_fat,
               carbs = carbs, sugar = sugar, fiber = fiber, cholesterol = cholesterol
              )
    l.save()
    series.to_csv("nutrition_label.txt", sep=',', index=False, encoding='utf-8')

