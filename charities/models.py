from django.db import models
from accounts.models import User

class Benefactor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    experience = models.SmallIntegerField(default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
         return self.user.first_name

class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Task(models.Model):
    GENDER_CHOICES = (
        ("m", "Male"),
        ("f", "Female"),
    )
    STATE_CHOICES = (
        ("p", "Pending"),
        ("w", "Waiting"),
        ("a", "Assigned"),
        ("d", "Done"),
    )

    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default="p")
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title