from django import forms

from .models import Image, Category

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =['name', 'image_file', 'category', 'description', 'shoot_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['name',]