#weight in kg
#height in cm

#will need to get from backend
weight = 0.0
height = 0.0
age = 0
sex = ""


sex = sex.lower()

#BEE = Basal Energy Expenditure (Calories)
min_calories = 0.0
if sex == "male":
    min_calories = 66.5 + 13.8 * weight + 5.0 * height - 6.8 * age
else:
    min_calories = 655.1 + 9.6 * weight + 1.9 * height - 4.7 * age

#protein range
min_protein_range = []
min_protein_range[0] = weight * .8
min_protein_range[1] = weight

#fat
fat = min_calories * .3

#carbs range
min_carbs_range = []
min_carbs_range[0] = min_calories * .45
min_carbs_range[1] = min_calories * .65

