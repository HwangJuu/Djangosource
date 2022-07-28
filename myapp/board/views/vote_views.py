from django.shortcuts import get_object_or_404, redirect
from ..models import Question, Answer
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# 질문 추천 등록
@login_required(login_url="common:login")
def vote_question(request, question_id):
    pass
    # question_id 해당하는 question 가져오기
    question = get_object_or_404(Question, pk=question_id)
    # 자신의 글은 추천 불가 로그인 사용자 == 질문작성자
    if request.user == question.author:
        messages.orror(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        # question.voter + 1
        question.voter.add(request.user)
    return redirect("board:detail", question_id=question_id)


# 답변 추천 등록
@login_required(login_url="common:login")
def vote_answer(request, answer_id):
    pass
    # question_id 해당하는 question 가져오기
    answer = get_object_or_404(Answer, pk=answer_id)
    # 자신의 글은 추천 불가 로그인 사용자 == 질문작성자
    if request.user == answer.author:
        messages.orror(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        # answer.voter + 1
        answer.voter.add(request.user)
    return redirect("board:detail", question_id=answer.question.id)
