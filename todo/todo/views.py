from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# todo 전체조회
def todo_list(request):
    # 문자열 보여주기
    # return HttpResponse("Todo 앱")
    #  전체 내용가져오기
    # Todo.objects.all()

    # 전체 내용이 아닌 complte가 False 인 레코드 가져오기
    # 가져온 내용을 todos에 담기
    todos = Todo.objects.filter(complete=False)

    # 특정 html 파일 보여주기
    # 키값은  임의로 주기
    return render(request, "todo/todo_list.html", {"todos": todos})


# todo 상세조회
def todo_detail(request, pk):
    # pk에 해당하는 레코드 가져오기
    todo = Todo.objects.get(id=pk)
    return render(request, "todo/todo_detail.html", {"todo": todo})


# todo 등록
def todo_register(request):
    """
    # http://127.0.0.1:8000/todo/new 경로로
    #  Get 요청, Post 요청  한번씩 들어오게 되어있음
    """
    if request.method == "POST":
        # 입력값 받아오기
        form = TodoForm(request.POST)  # POST
        if form.is_valid():  # 간단한 유효성 검사. 비어있는 값 있는지 확인
            todo = form.save(commit=False)  # 저장은 하되 DB에 반영은 바로 하지 말기
            todo.save()  # 데이터 베이스에 저장.
            # 입력 성공 시 상세보기로(별칭사용)
            # id 값 같이 보내기
            return redirect("todo_detail", pk=todo.id)

        pass
    else:  # Get
        # todo 입력 가능한 form 보여주기
        form = TodoForm()  # 비어있음

    return render(request, "todo/todo_register.html", {"form": form})


# todo 수정
def todo_edit(request, pk):
    # pk 조회해서 todo에 담기
    todo = Todo.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():  # 간단한 유효성 검사. 비어있는 값 있는지 확인
            todo = form.save(commit=False)  # 저장은 하되 DB에 반영은 바로 하지 말기
            todo.save()  # 데이터 베이스에 저장.
            # 수정 성공 시 목록에서 보여주기
            return redirect("todo_list")
    else:  # Get방식
        # 조회한 todo 보여주기
        # instance= : 조회한 결과를 todo로 보낸다
        form = TodoForm(instance=todo)

    # 조회한 결과가 담긴 form 전송.
    return render(request, "todo/todo_register.html", {"form": form})


# todo done
def todo_done(request, pk):
    # pk에 해당하는 todo를 가져온 후
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    # 변경하여 save()
    todo.save()
    return redirect("todo_list")


# 완료된 ToDo 목록 보여주기
def done_list(request):
    # complete가 Ture 인 데이터 가져오기
    dones = Todo.objects.filter(complete=True)

    return render(request, "todo/done_list.html", {"dones": dones})
