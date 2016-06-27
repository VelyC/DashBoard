from django.db import models

# Create your models here.

class AdminModel(models.Model):
   author = models.ForeignKey('auth.User')
   level = models.PositiveSmallIntegerField({'min_value':1, 'max_value':5})
   home_location = models.TextField()

   def publish_admin(self):
      self.save()

   def __str__(self):
      return '('+self.author.username+')'+str(self.level)+'-'+self.home_location

class MissionaryBasicModel(models.Model):
   releaseDate = models.DateField()
   name = models.TextField()
   areaServingIn = models.TextField(null=True, blank=True)
   missionServingIn = models.TextField(null=True, blank=True)
   # Lv 1
   homeWardBranch = models.TextField()
   # Lv 2
   homeStakeMiss = models.TextField()
   # Lv 3
   homeArea = models.TextField()
   # Lv 4
   homeCountry = models.TextField()
   # Lv 5
   coordCouncil = models.TextField()

   def create_new_persion(self):
      pa = MissionaryAdaptationModel()
      pa.create_new_persion()
      self.save()

   def __str__(self):
      return self.homeWardBranch+'-'+self.name+'('+str(self.id)+')'

class MissionaryAdaptationModel(models.Model):
   # 0:no 1:yes
   ldsJobsReg = models.PositiveSmallIntegerField({'min_value':0, 'max_value':1}, null=True, blank=True)
   # 0:no 1:yes
   completedMyPath = models.PositiveSmallIntegerField({'min_value':0, 'max_value':1}, null=True, blank=True)
   selfRelianceGroup = models.TextField(null=True, blank=True)
   education = models.TextField(null=True, blank=True)
   lengthEducation = models.PositiveSmallIntegerField(null=True, blank=True)
   educationCompletion = models.DateField(null=True, blank=True)
   # 0:partTime 1:fullTime
   employment = models.PositiveSmallIntegerField({'min_value':0, 'max_value':1}, null=True, blank=True)
   # 0:education 1:employment 2:business
   newStart = models.PositiveSmallIntegerField({'min_value':0, 'max_value':2}, null=True, blank=True)
   # 0:single 1:married
   maritalStatus = models.PositiveSmallIntegerField({'min_value':0, 'max_value':1}, null=True, blank=True)
   # 0:active 1:less active 2:address unknown
   curchActivity = models.PositiveSmallIntegerField({'min_value':0, 'max_value':2}, null=True, blank=True)
   # 0:inarea 1:outsideofared
   placeResidence = models.PositiveSmallIntegerField({'min_value':0, 'max_value':1}, null=True, blank=True)
   sixMonthPlan = models.TextField(null=True, blank=True)
   # 0 ~ 5: module1~6 6:completed
   contMissionProgress = models.PositiveSmallIntegerField({'min_value':0, 'max_value':6}, null=True, blank=True)
   comments = models.TextField(null=True, blank=True)

   def create_new_persion(self):
      self.save()

   def __str__(self):
      return '('+str(self.id)+')'
