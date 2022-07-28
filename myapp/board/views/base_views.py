# index, detail

from django.shortcuts import get_object_or_404, render
from ..models import Question, QuestionCount
from django.core.paginator import Paginator
from django.db.models import Q, Count
from tools.utils import get_client_ip  # ip가져오는 함수 이용

# 질문 리스트 + 페이지 나누기
def index(request):

    # return HttpResponse("Board")

    # question 테이블 내용 조회
    # Question.objects.all()

    # 주소줄에 따라옴
    # 페이지 나누기
    # http://127.0.0.1:8000/board/?page=1
    page = request.GET.get("page", 1)
    # keyword
    keyword = request.GET.get("keyword", "")
    # sort
    sort = request.GET.get("sort", "")

    # 정렬 조건 넣기 전에
    # 날짜 최신 순으로 정렬 한 내용
    # question_list = Question.objects.order_by("-create_date")

    # 정렬 조건 삽입 후
    # 최신 목록
    if sort == "recent":
        question_list = Question.objects.order_by("-create_date")
    # 추천이 많은 목록 순
    # annotate() : voter라는 필드의 개수를 센 후 num_voter라는 임시 필드를 추가해 주는 함수
    elif sort == "recommend":
        question_list = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "-create_date"  # 역순으로 최신날짜
        )
    # 인기순(답변이 많은 순)
    else:
        question_list = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-create_date"  # 역순
        )

    # 조회된 목록을 기준으로 검색 조건을 줘서 필터링
    # Q() : OR 조건으로 데이터를 조회
    # subject__contains(대소문자 구별)
    # subject__icontains(대소문자 구별하지 않음)

    if keyword:
        question_list = question_list.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()  # 중복 제외

    # Paginator 객체 생성(전체 목록, 10) 전체목록에서 10개씩 가져오기
    paginator = Paginator(question_list, 10)

    # 10개씩 나눠준거 가지고 오기
    page_obj = paginator.get_page(page)

    # 페이지 나누기 전
    # return render(request, "board/question_list.html", {"question_list": question_list})

    # 페이지 나누기 후
    # return render(request, "board/question_list.html", {"question_list": page_obj})

    # 검색 기능 추가
    context = {
        "question_list": page_obj,
        "page": page,
        "keyword": keyword,
        "sort": sort,
    }

    return render(request, "board/question_list.html", context)


# 질문 상세 조회
def detail(request, question_id):
    # get : 없는 id를 요청했을 때 웹 페이지에 오류 메세지가 그대로 출력
    # question = Question.objects.get(id=question_id)

    # get_object_or_404 : 오류가 나면 Page not found 로 보여줌
    question = get_object_or_404(Question, id=question_id)

    # 주소줄에 따라옴
    # 페이지 나누기 후 추가
    # http://127.0.0.1:8000/board/?page=1
    page = request.GET.get("page", 1)
    # keyword
    keyword = request.GET.get("keyword", "")
    # sort
    sort = request.GET.get("sort", "")

    ### 조회수 추가
    # 사용자 ip 가져오기(request로 요청된 ip)
    ip = get_client_ip(request)
    # 찾은 ip가 QuestionCount 테이블에 있는지 확인
    # ip와 질문을 만족하는지 확인. 0보다 크다면 동일한게 존재
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:  # 조회수 증가
        # 모델 생성
        qc = QuestionCount(ip=ip, question=question)
        # 저장
        qc.save()
        # question 테이블에 view_cont = view_cnt + 1
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1

        question.save()

    context = {
        "question": question,
        "page": page,
        "keyword": keyword,
        "sort": sort,
    }

    return render(request, "board/question_detail.html", context)
