# 장고 방식 : config 안의 urls.py를 통해 request 처리
# 앱 별로 나누어서 request를 관리
# config 안의 urls.py 참고

from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/todo 로 요청이 들어오면
    # 어느 view를 보여줄 것인지 : views.todo_list
    # name : url 하드코딩 부분의 축소
    path("", views.todo_list, name="todo_list"),
    # todo 하나 조회
    # http://127.0.0.1:8000/todo/1 : 아이디 값
    path("<int:pk>/", views.todo_detail, name="todo_detail"),
    # todo 새글 작성
    # http://127.0.0.1:8000/todo/new
    path("new/", views.todo_register, name="todo_register"),
    # todo 수정
    # http://127.0.0.1:8000/todo/1/edit 수정하기 버튼
    path("<int:pk>/edit", views.todo_edit, name="todo_edit"),
    # todo 완료
    # http://127.0.0.1:8000/todo/1/done 완료 버튼 클릭
    path("<int:pk>/done", views.todo_done, name="todo_done"),
    # 완료된 리스트 보여주기
    # http://127.0.0.1:8000/todo/done 완료한 ToDo목록 버튼 클릭
    path("done/", views.done_list, name="done_list"),
]
