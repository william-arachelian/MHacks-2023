from django.shortcuts import render

from .models import Label

from .forms import labelForm
# Create your views here.


def label_detail_view(request):
    obj = Label.objects.get(id = 1)
    context = {
        "calories": obj.calories,
        "total_fat": obj.total_fat,
        "trans_fat": obj.trans_fat,
        "sat_fat": obj.sat_fat,
        "carbs": obj.carbs,
        "sugar": obj.sugar,
        "fiber": obj.fiber,
        "cholesterol": obj.cholesterol,
        "sodium": obj.sodium,
        "protein": obj.protein
    }
    return render(request, "label/detail.html", context)