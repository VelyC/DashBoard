from django import forms

from .models import MissionaryBasicModel, MissionaryAdaptationModel
from django.forms.extras import widgets

# create yout own forms.
class MissionaryBasicModelForm(forms.ModelForm):
   class Meta:
      model = MissionaryBasicModel
      fields = '__all__'
      widgets = {
         'releaseDate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'2016-01-01'}),
         'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'홍길동'}),
         'areaServingIn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'염리동'}),
         'missionServingIn': forms.TextInput(attrs={'class':'form-control', 'placeholder':'서울'}),
         'homeWardBranch': forms.TextInput(attrs={'class':'form-control', 'placeholder':'필수 요소 !'}),
         'homeStakeMiss': forms.TextInput(attrs={'class':'form-control', 'placeholder':'필수 요소 !'}),
         'homeArea': forms.TextInput(attrs={'class':'form-control', 'placeholder':'필수 요소 !'}),
         'homeCountry': forms.TextInput(attrs={'class':'form-control', 'placeholder':'필수 요소 !'}),
         'coordCouncil': forms.TextInput(attrs={'class':'form-control', 'placeholder':'필수 요소 !'}),
      }
      labels = {
         'releaseDate': 'Release date ',
         'name': 'Name ',
         'areaServingIn': 'Area serving in ',
         'missionServingIn': 'Mission serving in ',
         'homeWardBranch': 'Home Ward or Branch ',
         'homeStakeMiss': 'Home Stake or Mission ',
         'homeArea': 'Home Area ',
         'homeCountry': 'Home Country ',
         'coordCouncil': 'Home Coord council ',
      }

class MissionaryAdaptationModelForm(forms.ModelForm):

   class Meta:
      # CHOICES
      YN_CHOICES = ((0,'No'),(1,'Yes'))
      EP_CHOICES = ((0,'Part Time'),(1,"Full Time"))
      NS_CHOICES = ((0,'Education'),(1,'Employment'),(2,'Business'))
      MS_CHOICES = ((0,'Single'),(1,'Married'))
      CA_CHOICES = ((0,'Active'),(1,'Less Active'),(2,'Address unkown'))
      PR_CHOICES = ((0,'In area'),(1,'Outside of area'))


      model = MissionaryAdaptationModel
      fields = '__all__'
      widgets = {
         'ldsJobsReg': forms.Select(choices = YN_CHOICES, attrs={'class':"form-control"}),
         'completedMyPath': forms.Select(choices = YN_CHOICES, attrs={'class':"form-control"}),
         'selfRelianceGroup': forms.TextInput(attrs={'class':"form-control"}),
         'education': forms.TextInput(attrs={'class':"form-control"}),
         'lengthEducation': forms.NumberInput(attrs={'class':"form-control"}),
         'educationCompletion': widgets.SelectDateWidget(attrs={'class':"form-control"}),
         'employment': forms.Select(choices = EP_CHOICES, attrs={'class':"form-control"}),
         'newStart': forms.Select(choices = NS_CHOICES, attrs={'class':"form-control"}),
         'maritalStatus': forms.Select(choices = MS_CHOICES, attrs={'class':"form-control"}),
         'churchActivity': forms.Select(choices = CA_CHOICES, attrs={'class':"form-control"}),
         'placeResidence': forms.Select(choices = PR_CHOICES, attrs={'class':"form-control"}),
         'sixMonthPlan': forms.TextInput(attrs={'class':"form-control"}),
         'contMissionProgress': forms.Select(choices = PR_CHOICES, attrs={'class':"form-control"}),
         'comments': forms.Textarea(attrs={'class':"form-control"}),
      }
      labels = {
         'ldsJobsReg': 'ldsjobs.com Registered?'
      }
