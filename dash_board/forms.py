from django import forms

from .models import MissionaryBasicModel

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
