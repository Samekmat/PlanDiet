from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

DIFFICULTIES = (
    ('begnner', "Beginner"),
    ('intermediate', "Intermediate"),
    ('advanced', "Advanced"),
)


CATEGORIES = (
    ('endurance', "Endurance"),
    ('strength', "Strength"),
    ('flexibility', "Flexibility"),
    ('balance', "Balance"),
)


SEX = (
    ('female', "female"),
    ('male', "male"),
)

ACTIVITY = (
    ('1.2', 'zero activity'),
    ('1.4', 'sedentary with max 2 training days per week'),
    ('1.6', 'sedentary but intermediate 3-4 trainings per week'),
    ('1.8', 'active work with 3-4 trainings per week'),
    ('2.0', 'daily trainings with high intesivity'),
)

GOAL = (
    ('reduce', 'reduce'),
    ('maintain', 'maintain'),
    ('bulk', 'bulk')
)


class Category(models.Model):
    name = models.CharField(choices=CATEGORIES, max_length=60)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class MuscleGroup(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class SportType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=124)
    description = models.TextField()
    difficulty = models.CharField(choices=DIFFICULTIES, max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    muscles = models.ManyToManyField(MuscleGroup)
    type = models.ManyToManyField(SportType)

    def __str__(self):
        return self.name


class Diet(models.Model):
    name = models.CharField(max_length=124)
    caloric_demand = models.IntegerField()
    carbs_demand = models.IntegerField()
    protein_demand = models.IntegerField()
    fat_demand = models.IntegerField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('diet', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=60)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, null=True, default=None)
    exercises = models.ManyToManyField(Exercise, default=None)

    def get_absolute_url(self):
        return reverse('plan', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = models.CharField(max_length=24, unique=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    sex = models.CharField(choices=SEX, max_length=6)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, null=True)
