from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomUser, SEX, Diet, Plan, ACTIVITY, GOAL


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginForm(forms.Form):
    login = forms.CharField(label='Your login')
    password = forms.CharField(label='Your password', widget=forms.PasswordInput)


def username_unique(username):
    if CustomUser.objects.filter(username=username).exists():
        raise ValidationError('That login already exists')


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Login', validators=[username_unique, ])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First_name', required=False)
    last_name = forms.CharField(label='Last_name', required=False)
    email = forms.EmailField(label='Email', required=False)
    age = forms.IntegerField(label='Age', required=False)
    height = forms.IntegerField(label='Height', required=False)
    weight = forms.FloatField(label='Weight', required=False)
    sex = forms.ChoiceField(label='Sex', choices=SEX, required=False)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Passwords are not the same')


class DietModelForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = '__all__'


class PlanForm(forms.ModelForm):
    # exercises = forms.ModelMultipleChoiceField(queryset=Exercise.objects.all(), label='Exercise list', widget=CheckboxSelectMultiple())

    class Meta:
        model = Plan
        fields = ['name', 'diet', 'exercises']


class MacroCalculatorForm(forms.Form):
    age = forms.IntegerField(label='Age')
    height = forms.IntegerField(label='Height')
    weight = forms.FloatField(label='Weight')
    sex = forms.ChoiceField(label='Sex', choices=SEX)
    activity = forms.ChoiceField(label='Activity', choices=ACTIVITY)
    goal = forms.ChoiceField(label='Goal', choices=GOAL)
