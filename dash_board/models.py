from django.db import models

# Create your models here.

# DB Column [ author (auth) // level (int:1~4) // homelocation (string)]
class AdminModel(models.Model):
   author = models.ForeignKey('auth.User')
   level = models.PositiveSmallIntegerField()
   home_location = models.TextField()

   def publish_admin(self):
      self.save()

   # 표현식 : (hslee@gmail.com)4coordcouncil1
   def __str__(self):
      return '('+self.author.username+')'+str(self.level)+'-'+self.home_location

class MissionaryBasicModel(models.Model):
   # not null string / ex : 2016-01-01
   releaseDate = models.DateField()
   # not null string / ex : 홍길동
   name = models.TextField()
   # null string / ex ??
   areaServingIn = models.TextField(null=True, blank=True)
   # null string / ex ??
   missionServingIn = models.TextField(null=True, blank=True)

   # not null string / case sesitive
   # Lv 1 ward branch
   homeWardBranch = models.TextField()
   # Lv 2 stake mission
   homeStakeMiss = models.TextField()
   # Lv 3 area
   homeArea = models.TextField()
   # Lv 4 country
   homeCountry = models.TextField()
   # Lv 5 coord council
   coordCouncil = models.TextField()

   def create_new_persion(self):
      self.save()

   # 표현식 : branch1-홍길동(primary key)
   def __str__(self):
      return self.homeWardBranch+'-'+self.name+'('+str(self.id)+')'

class MissionaryAdaptationModel(models.Model):
   # 0:no 1:yes
   ldsJobsReg = models.PositiveSmallIntegerField(default = 0)
   # 0:no 1:yes
   completedMyPath = models.PositiveSmallIntegerField(default = 0)
   selfRelianceGroup = models.TextField(default = '')
   education = models.TextField(default = '')
   lengthEducation = models.PositiveSmallIntegerField(default = 0)
   educationCompletion = models.DateField(default = '1900-01-01')
   # 0:partTime 1:fullTime
   employment = models.PositiveSmallIntegerField(default = 0)
   # 0:education 1:employment 2:business
   newStart = models.PositiveSmallIntegerField(default = 0)
   # 0:single 1:married
   maritalStatus = models.PositiveSmallIntegerField(default = 0)
   # 0:active 1:less active 2:address unknown
   churchActivity = models.PositiveSmallIntegerField(default = 0)
   # 0:inarea 1:outsideofared
   placeResidence = models.PositiveSmallIntegerField(default = 0)
   sixMonthPlan = models.TextField(null=True, blank=True)
   # 0 ~ 5: module1~6 6:completed
   contMissionProgress = models.PositiveSmallIntegerField(default = 0)
   comments = models.TextField(default = 'comment here ~')

   def create_new_persion(self):
      self.save()

   # 표현식 : (primary key)
   def __str__(self):
      return '('+str(self.id)+')'
