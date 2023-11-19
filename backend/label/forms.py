from django import forms

from .models import Label

class labelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = [
            'calories',
            'total_fat',
            'trans_fat',
            'sat_fat', 
            'carbs', 
            'sugar', 
            'fiber', 
            'cholesterol',
            'sodium',
            'protein'
        ]