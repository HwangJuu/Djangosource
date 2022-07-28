from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from ..models import Comment, Question, Answer
from ..forms import CommentForm  # 모델에 담겨 있는 폼
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# 질문에 대한 답변 등록
@login_required(login_url="common:login")
def comment_create_question(request, question_id):

    # 질문 가져오기 - models.py에서 질문 정로를 question에서 담아서 옴
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            # 추가 작업 (forms.py에서 안한 작업)
            comment.author = request.user  # 로그인 사용자
            comment.create_date = timezone.now()  # 현재 시간 날짜
            comment.question = question
            comment.save()
            # return redirect("board:detail", question_id=question_id)

            # 앵커가 들어온 후
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", question_id=question_id), comment.id
                )
            )

    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


# 질문 답변 수정
@login_required(login_url="common:login")
def comment_modify_question(request, comment_id):

    commnet = get_object_or_404(Comment, pk=comment_id)

    # 작성자와 같은지 확인
    if request.user != commnet.author:
        messages.error(request, "댓글을 수정할 권한이 없습니다.")
        return redirect("board:detail", question_id=commnet.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=commnet)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            # return redirect("voard:detail", question_id=comment.question.id)

            # 앵커가 들어온 후
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", question_id=comment.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm(instance=commnet)

    return render(request, "board/comment_form.html", {"form": form})


# 답변 삭제
@login_required(login_url="common:login")
def comment_delete_question(request, comment_id):
    # 삭제할 데이터 찾기
    commnet = get_object_or_404(Comment, pk=comment_id)

    # 작성자와 같은지 확인
    if request.user != commnet.author:
        messages.error(request, "댓글을 삭제할 권한이 없습니다.")
        return redirect("board:detail", question_id=commnet.question.id)

    commnet.delete()

    # 내용보기로 들어가기
    return redirect("board:detail", question_id=commnet.question.id)


# 댓글에 대한 답변 등록
@login_required(login_url="common:login")
def comment_create_answer(request, answer_id):

    # 질문 가져오기 - models.py에서 질문 정로를 question에서 담아서 옴
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            # 추가 작업 (forms.py에서 안한 작업)
            comment.author = request.user  # 로그인 사용자
            comment.create_date = timezone.now()  # 현재 시간 날짜
            comment.answer = answer
            comment.save()

            # 앵커가 들어온 후
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", comment.answer.question.id), comment.id
                )
            )

    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


# 댓글 답변 수정
@login_required(login_url="common:login")
def comment_modify_answer(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    # 작성자와 같은지 확인
    if request.user != comment.author:
        messages.error(request, "댓글을 수정할 권한이 없습니다.")
        return redirect("board:detail", question_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()

            # 앵커가 들어온 후
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", question_id=comment.answer.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


# 댓글 답변 삭제
@login_required(login_url="common:login")
def comment_delete_answer(request, comment_id):
    # 삭제할 데이터 찾기
    comment = get_object_or_404(Comment, pk=comment_id)

    # 작성자와 같은지 확인
    if request.user != comment.author:
        messages.error(request, "댓글을 삭제할 권한이 없습니다.")
        return redirect("board:detail", question_id=comment.answer.question.id)

    # 댓글 삭제 명령어
    comment.delete()

    # 내용보기로 들어가기
    return redirect("board:detail", question_id=comment.answer.question.id)
