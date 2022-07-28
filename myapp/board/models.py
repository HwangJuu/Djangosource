from django.db import models
from django.contrib.auth.models import User

# 질문 모델(create table Question ~~~ )
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    # 작성자 추가
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_question"
    )
    create_date = models.DateTimeField()
    # 수정된 날짜 보여주기
    # black=True : form.is_valid()를 통한 폼 검사시 값이 없어도 됨
    modify_date = models.DateTimeField(null=True, blank=True)

    # 추천수
    # ManyToManyField : 다대다
    voter = models.ManyToManyField(User, related_name="vote_question")

    # 조회수
    view_cnt = models.BigIntegerField(default=0)

    # Question 모델에서 author, voter 필드가 모두 User 모델 참조 ==> join 참조
    # User.question_set.all or User.question_set.count  같은 명령을 통해 User 모델을 통해서
    # Question 데이터에 접근할 때 author 필드를 기준으로 할지, voter 필드를 기준으로 할지 지정

    # 객체가 반환될 때 원본 구조말고 글자로 반환
    def __str__(self) -> str:
        return self.subject + " " + self.content


class QuestionCount(models.Model):
    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.ip


# 답변 모델(create table Answer ~~~ )
class Answer(models.Model):
    # Answer 테이블과 Question 테이블의 외래키 제약 조건
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()

    # 작성자 추가
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_answer"
    )
    create_date = models.DateTimeField()
    # 수정된 날짜 보여주기
    # black=True : form.is_valid()를 통한 폼 검사시 값이 없어도 됨
    modify_date = models.DateTimeField(null=True, blank=True)

    # 추천수 : 다대다
    voter = models.ManyToManyField(User, related_name="vote_answer")

    def __str__(self) -> str:
        return self.content


# 댓글 모델
class Comment(models.Model):
    # 댓글 작성자 - user 테이블 정보 사용 외래키
    # (테이블, 정보)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 댓글 내용 => 입력받기
    content = models.TextField()

    # 댓글 작성 날짜
    create_date = models.DateTimeField()

    # 수정 날짜
    modify_date = models.DateTimeField(null=True, blank=True)

    # 질문 정보
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE
    )
    # 답글 정보
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
