from django.contrib import admin
from .models import Question

# admin 페이지에서 Question 모델 관리 할 수 있도록 등록
admin.site.register(Question)
