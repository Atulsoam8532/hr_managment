from django.db import models
from django.contrib.auth.models import User

job=[
    ('Hr','HR'),
    ('manager','Manager'),
    ('Employees','employe')
]
class Profiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_hr = models.BooleanField(default=False)
    is_employe = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    apply_for = models.CharField(max_length=50)
    HR = models.CharField(max_length=10,default='nothing')
    manager = models.CharField(max_length=10,default='nothing')
    allocated_proj = models.CharField(max_length=50,default='nothing')

class eplo_project(models.Model):
    employes = models.ManyToManyField(User, related_name='us')
    pro_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    RM = models.ForeignKey(User,on_delete=models.CASCADE)
    employe_score = models.CharField(max_length=10)
    added_by = models.CharField(max_length=20,default="nothing")

    def __str__(self):
        return self.pro_name


class Hr_employe(models.Model):
    empolye = models.ForeignKey(User,on_delete=models.CASCADE)
    manager = models.ForeignKey(User,on_delete=models.CASCADE,related_name='manager')

class manager_employe(models.Model):
    employe = models.ForeignKey(User,on_delete=models.CASCADE)


class leave_manag(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    days = models.CharField(max_length=2)
    hr_approved = models.BooleanField(default=False)
    hr_reject = models.BooleanField(default=False)
    manager_approve = models.BooleanField(default=False)
    manager_reject = models.BooleanField(default=False)



    
    





# Create your models here.
