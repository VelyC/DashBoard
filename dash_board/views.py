from django.shortcuts import render
from django.shortcuts import redirect

# for Sign up
from django.contrib.auth.models import User
# for Sig in
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def main(request):
   return render(request, 'dash_board/main.html', {})

def login_page(request):
   logout(request)
   if request.method == "POST":
      form = request.POST
      user = authenticate(username=form['email'], password=form['password'])
      if user is not None:
         if user.is_active:
            # authenticated
            login(request, user)
            return redirect('dash_board.views.main')
         else:
            # uid and pwd is valied but account has been disalbed
            return render(request, 'dash_board/login.html', {'meesage':'Account has been disabled'})
      else:
         # Check the id and pwd
         return render(request, 'dash_board/login.html', {'message':'Please check ID or Password'})
   else:
      # intenal errror
      return render(request, 'dash_board/login.html', {'message':''})

def new_user(request):
   if request.method == "POST":
      form = request.POST
      try:
         user = User.objects.create_user(form['email'], form['email'], form['password'])
         user.last_name = form['name']
         user.save()
      except:
         return render(request, 'dash_board/signup.html', {'message':'Email이 이미 사용 중입니다.'})
      else:
         return redirect('dash_board.views.login_page')
   else:
      return render(request, 'dash_board/signup.html', {'message':''})
