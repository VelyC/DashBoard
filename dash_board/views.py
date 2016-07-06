from django.shortcuts import render

##########################################################################
# User inports..
##########################################################################
# for redirect
from django.shortcuts import redirect
# for Sign up
from django.contrib.auth.models import User
# for Sig in
from django.contrib.auth import authenticate, logout, login
# for Admin
from .models import AdminModel, MissionaryBasicModel, MissionaryAdaptationModel
# using model forms..
from .forms import MissionaryBasicModelForm, MissionaryAdaptationModelForm

# Create your views here.

# Data statistics and visualization sections.

# 미작동. 개발중...
def missionary_modify(request, pk):
    post = get_object_or_404(MissionaryAdaptationModel, pk=pk)

    if request.method == "POST":
        form = MissionaryAdaptationModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('dash_board.views.missionary_spread')
    else:
        form = MissionaryAdaptationModelForm()
    return render(request, 'dash_board/missionary_modify.html', {'modalForm':form})

##########################################################################
# Home Page..
##########################################################################
def missionary_overview(request):
   return render(request, 'dash_board/overview.html', {})

##########################################################################
# Modify 메뉴를 눌렀을 때 현재 로그인 된 관리자의 레벨과 지역에 맞는
# 선교사들을 전부 table에 뿌려준다.
##########################################################################
def missionary_spread(request):
   try:
      # request의 ForeignKey 를 가져와서 필터를 입혀 객체를 가져온다.
      # 어차피 ForeignKey는 고유하므로 하나만 저장.
      admin = AdminModel.objects.filter(author=request.user)[0]
   except Exception as e:
      # 이 상황은 오류가 없으면 일어나지 않을 것이다.
      admin = AdminModel()

   # 레벨과 지역을 저장.
   lv = admin.level
   hl = admin.home_location

   # 레벨에 따라서 서로다른 data base column을 검색해야 하므로 코드 분기.
   if lv == 1:
      mBasic = MissionaryBasicModel.objects.filter(homeWardBranch=hl).order_by('id')
   elif lv == 2:
      mBasic = MissionaryBasicModel.objects.filter(homeStakeMiss=hl).order_by('id')
   elif lv == 3:
      mBasic = MissionaryBasicModel.objects.filter(homeArea=hl).order_by('id')
   elif lv == 4:
      mBasic = MissionaryBasicModel.objects.filter(homeCountry=hl).order_by('id')
   else:
      mBasic = MissionaryBasicModel.objects.filter(coordCouncil=hl).order_by('id')

   return render(request, 'dash_board/missionary_modify.html', {'mBasics':mBasic})

##########################################################################
# Model 객체에 정보를 저장한 후 save - db에 저장
##########################################################################
def missionary_add(request):
   if request.method == "POST":
      # html form 정보를 Modle 객체에 저장.
      form = MissionaryBasicModelForm(request.POST)
      if form.is_valid():
         # Basic Model 에 상응하는 빈 Adaptation Model 객체도 같이 생성하여 save
         nullAdapt = MissionaryAdaptationModel()
         nullAdapt.save()
         form.save()
         return redirect('dash_board.views.missionary_overview')
   else:
      form = MissionaryBasicModelForm()
   return render(request, 'dash_board/missionary_add.html', {'form':form})



# Authentication System.
##########################################################################
# form에 적힌 정보대로 authenticate가 되면
# user 변수에 User 객체가 저장될 것이다.
# 저장되면 세션에 login 하고 overview로 redirect.
##########################################################################
def signin(request):
   if request.method == "POST":
      form = request.POST
      user = authenticate(username=form['signinEmail'], password=form['signinPassword'])
      if user is not None:
         if user.is_active:
            # authenticated
            login(request, user)
            return redirect('dash_board.views.missionary_overview')
         else:
            # uid and pwd is valied but account has been disalbed
            return render(request, 'dash_board/overview.html', {'meesage':'Account has been disabled'})
      else:
         # Check the id and pwd
         return render(request, 'dash_board/overview.html', {'message':'Please check ID or Password'})
   else:
      # intenal errror
      return render(request, 'dash_board/overview.html', {'message':''})

##########################################################################
# 세션에서 authentication 정보를 지운 후 맨 처음 페이지로 redirect
##########################################################################
def signout(request):
   logout(request)
   return redirect('dash_board.views.signin')

##########################################################################
# create user 기본 메소드를 사용하여 유저 정보를 db에 저장한다.
# 유저 정보가 이미 있으면 unique 에러(???) 를 내므로 try-except 문을 사용하여
# 에러가 나면 email이 이미 사용 중이라는 메세지를 페이지에 보내준다.
##########################################################################
def signup(request):
   if request.method == "POST":
      form = request.POST
      try:
         user = User.objects.create_user(form['email'], form['email'], form['password'])
         user.last_name = form['name']
         admin = AdminModel()
         admin.author = user
         admin.level = int(form['level'])
         admin.home_location = form['home_location']
         admin.publish_admin()
         user.save()
      except:
         return render(request, 'dash_board/signup.html', {'message':'Email이 이미 사용 중입니다.'})
      else:
         return redirect('dash_board.views.signin')
   else:
      return render(request, 'dash_board/signup.html', {'message':''})
