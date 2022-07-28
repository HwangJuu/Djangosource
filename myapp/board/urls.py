from django.urls import path
from .views import base_views, answer_views, comment_views, question_views, vote_views

# 네임스페이스 지정
app_name = "board"

urlpatterns = [
    path("", base_views.index, name="index"),
    # 상세보기
    path("<int:question_id>", base_views.detail, name="detail"),
    # 질문 등록
    # /board/question/create/ question_create
    path("question/create", question_views.question_create, name="question_create"),
    # 질문 수정
    # /board/question/modify/305
    path(
        "question/modify/<int:question_id>",
        question_views.question_modify,
        name="question_modify",
    ),
    # 질문 삭제
    # /board/question/delete/305
    path(
        "question/delete/<int:question_id>",
        question_views.question_delete,
        name="question_delete",
    ),
    # 답변 등록
    # /board/answer/create/1
    path(
        "answer/create<int:question_id>",
        answer_views.answer_create,
        name="answer_create",
    ),
    # 답변 수정
    # /board/answer/modify/1 answer.id : 값을 받을 변수 answer_id
    path(
        "answer/modify/<int:answer_id>",
        answer_views.answer_modify,
        name="answer_modify",
    ),
    # 답변 삭제
    # /board/answer/delete/1 answer.id : 값을 받을 변수 answer_id
    path(
        "answer/delete/<int:answer_id>",
        answer_views.answer_delete,
        name="answer_delete",
    ),
    # 질문 댓글 작성
    # /board/comment/create/question_id
    path(
        "comment/create/<int:question_id>",
        comment_views.comment_create_question,
        name="comment_create_question",
    ),
    # 질문 댓글 수정
    path(
        "comment/modify/<int:comment_id>",
        comment_views.comment_modify_question,
        name="comment_modify_question",
    ),
    # 질문 댓글 삭제
    path(
        "comment/delete/<int:comment_id>",
        comment_views.comment_delete_question,
        name="comment_delete_question",
    ),
    # 답변 댓글 작성
    # /board/comment/create/answer_id
    path(
        "comment/create/answer/<int:answer_id>",
        comment_views.comment_create_answer,
        name="comment_create_answer",
    ),
    # 답변 댓글 수정
    path(
        "comment/modify/answer/<int:comment_id>",
        comment_views.comment_modify_answer,
        name="comment_modify_answer",
    ),
    # 답변 댓글 삭제
    path(
        "comment/delete/answer/<int:comment_id>",
        comment_views.comment_delete_answer,
        name="comment_delete_answer",
    ),
    # 질문 추천 수
    path(
        "vote/queestion/<int:question_id>",
        vote_views.vote_question,
        name="vote_question",
    ),
    # 답변 추천 수
    path("vote/answer/<int:answer_id>", vote_views.vote_answer, name="vote_answer"),
]
