from django.db import models

# 데이터베이스 테이블
# todo 테이블 = title, description, created(목록작성 날짜), complete(todo 완료 여부), important(todo 중요도)


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + " " + self.description
