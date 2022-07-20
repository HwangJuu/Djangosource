from django.db import models

# Model : 앱의 데이터와 관련된 부분을 다루는 클래스
#         데이터베이스에 저장될 데이터의 타입을 정의하고 설정
#         sql의 DML 관련된 작업
#         테이블 자동 생성

# models.Model 클래스 상속
# models : django 의 데이터베이스와 관련된 내용을 미리 작성해 놓은 도구
#          사용자 정의 모델 작성시 models에서 제공해 주는 모델을 상속받아 작성 가능

# CharField : 문자열 담기(길이제한 필요)
# TextField : 문자열 (길이제한 필요없음)
# IntegerField : 정수
# DateField : 날짜
# DateTimeField : 날짜 + 시간
# FileField : 파일
# ImageField : 이미지 파일
# ForeignKey : 외래키
# OneToOneField : 1대1관계
# ManyToManyField : 다대다 관계


class Photo(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    # 자바의 toString()역할
    def __str__(self) -> str:
        return self.title + " " + self.author + " " + self.image
