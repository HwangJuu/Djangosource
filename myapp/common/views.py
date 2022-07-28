from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

# 회원가입
def signup(request):
    if request.method == "POST":
        # 사용자가 입력한 폼 가져오기
        form = UserForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 유효성 검사를 통과했다면 DB에 바로 저장
            form.save()
            # 로그인 페이지를 보여줄 때
            # return redirect("common:login")

            # 장고에 있는
            # form.cleaned_data.get() : 넘어온 폼에서 화면의 입력 값을 얻기 위한 함수
            #                           유효성을 통과한
            # 로그인에 필요한 아이디와 비밀번호
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")

            # 함수에 다시 넣어주기
            # authenticate() : 사용자아이디와 비밀번호를 담아서 자격증명을 요청하는 함수
            user = authenticate(username=username, password=raw_password)

            if user is not None:
                # login() : 로그인 해주는 함수
                login(request, user)
            return redirect("index")

    else:
        form = UserForm()

    return render(request, "common/signup.html", {"form": form})
