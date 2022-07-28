from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from ..models import Question
from ..forms import QuestionForm  # 모델에 담겨 있는 폼
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# 질문 등록
# 질문 등록 전에 로그인 확인 여부
@login_required(login_url="common:login")
def question_create(request):

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 임시저장
            question.create_date = timezone.now()

            # 작성자 추가(현재 로그인 사용자 : request.user)
            question.author = request.user

            question.save()

            return redirect("board:index")
    else:  # get 방식 비어있는 폼
        form = QuestionForm()

    return render(request, "board/question_form.html", {"form": form})


@login_required(login_url="common:login")
#  질문수정(원본 내용을 보여준 후 수정)
def question_modify(request, question_id):
    # question_id 값에 맞는 질문 찾아오기
    question = get_object_or_404(Question, pk=question_id)

    # 작성자와 같은지 확인
    if request.user != question.author:
        messages.error(request, "수정할 권한이 없습니다.")
        return redirect("board:detail", question_id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        # user 정보,
        question = form.save(commit=False)
        question.author = request.user
        question.modify_date = timezone.now()
        question.save()
        return redirect("board:detail", question_id=question_id)

    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_form.html", {"form": form})


# 질문 삭제
# 질문 삭제 전에 로그인 확인 여부
@login_required(login_url="common:login")
def question_delete(request, question_id):

    # question_id에 맞는 질문 찾아오기
    question = get_object_or_404(Question, pk=question_id)

    # 작성자와 같은지 확인
    if request.user != question.author:
        messages.error(request, "삭제할 권한이 없습니다.")
        return redirect("board:detail", question_id=question_id)

    # 삭제
    question.delete()
    return redirect("index")
