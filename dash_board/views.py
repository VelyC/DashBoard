from django.shortcuts import render
from django.shortcuts import redirect

# for Sign up
from django.contrib.auth.models import User
# for Sig in
from django.contrib.auth import authenticate, logout, login
# for Admin
from .models import AdminModel, MissionaryBasicModel, MissionaryAdaptationModel

from .forms import MissionaryBasicModelForm, MissionaryAdaptationModelForm

# Create your views here.

# Data statistics and visualization sections.
def missionary_overview(request):
   return render(request, 'dash_board/overview.html', {})

def missionary_modify(request):
   try:
      admin = AdminModel.objects.filter(author=request.user)[0]
   except Exception as e:
      admin = AdminModel()

   lv = admin.level
   hl = admin.home_location

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

   mAdapt = []
   for b in mBasic:
      mAdapt += MissionaryAdaptationModel.objects.filter(id=b.id)

   message = ''
   if request.method == "POST":
      modalForm = MissionaryAdaptationModelForm(request.POST)
      if modalForm.is_valid():
         modalForm.save()
         message = '저장 되었습니다!'
         return redirect('dash_board.views.missionary_modify')
      else:
         message = '입력을 확인해주세요.'
         return redirect('dash_board.views.missionary_modify')
   else:
      message = ''
      modalForm = MissionaryAdaptationModelForm()

   return render(request, 'dash_board/missionary_modify.html',
                  {'mBasics':mBasic, 'mAdapts':mAdapt,
                   'modalForm':modalForm, 'message':message})

def missionary_add(request):
   if request.method == "POST":
      form = MissionaryBasicModelForm(request.POST)
      if form.is_valid():
         nullAdapt = MissionaryAdaptationModel()
         nullAdapt.save()
         form.save()
         return redirect('dash_board.views.missionary_overview')
   else:
      form = MissionaryBasicModelForm()
   return render(request, 'dash_board/missionary_add.html', {'form':form})



# Authentication System.
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

def signout(request):
   logout(request)
   return redirect('dash_board.views.signin')

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
