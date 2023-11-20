from django import forms

from .models import User

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'weight',
            'height',
            'age',
            'sex'
        ]
        
# class rawUserForm(forms.Form):
#     weight = forms.IntegerField()
#     height = forms.IntegerField()
#     age = forms.IntegerField()
#     weight = forms.CharField()
#     image = forms.ImageField()