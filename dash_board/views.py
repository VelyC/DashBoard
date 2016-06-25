from django.shortcuts import render
from django.shortcuts import redirect

# for Sign up
from django.contrib.auth.models import User
# for Sig in
from django.contrib.auth import authenticate, logout
# Create your views here.

def main(request):
    return render(request, 'dash_board/main.html', {})

def login_page(request):
    return render(request, 'dash_board/login.html', {})

def signup_page(request):
    return render(request, 'dash_board/signup.html', {})

def login(request):
    logout(request)
    if request.method == "POST":
        form = request.POST
        # if form.is_vaild():
        user = authenticate(username=form['username'], password=form['password'])
        if user is not None:
            if user.is_active:
                # authenticated
                return main(request)
            else:
                # uid and pwd is valied but account has been disalbed
                return redirect('dash_board.views.login_page')
        else:
            # Check the id and pwd
            return redirect('dash_board.views.login_page')
        # else:
        #     # Input id and pwd correctly
        #     return login_page(request)
    else:
        # intenal errror
        return redirect('dash_board.views.login_page')

def new_user(request):
    if request.method == "POST":
        form = request.POST
        if form.is_vaild():
            # 이 부분ㅇ서 오류처리가 필요함.
            # ID not available
            user = User.objects.create_user(request.username, request.email, request.password)
            user.last_name = request.name
            return login_page(request)
    else:
        return login_page(request)
