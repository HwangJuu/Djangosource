from django import forms
from .models import Photo

# ModelForm 상속받아 fields 에 정의한 값을 받는
# 폼 클래스 작성
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo

        fields = ("title", "author", "image", "description", "price")
