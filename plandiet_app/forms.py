from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomUser, SEX, Diet, Plan, ACTIVITY, GOAL


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginForm(forms.Form):
    login = forms.CharField(label='Your login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Your password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


def username_unique(username):
    if CustomUser.objects.filter(username=username).exists():
        raise ValidationError('That login already exists')


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Login',
        validators=[username_unique, ],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='First_name',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Last_name',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    age = forms.IntegerField(
        label='Age',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    height = forms.IntegerField(
        label='Height',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    weight = forms.FloatField(
        label='Weight',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    sex = forms.ChoiceField(
        label='Sex',
        choices=SEX,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Passwords are not the same')


class DietModelForm(forms.ModelForm):
    class Meta:
        model = Diet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'caloric_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'carbs_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'protein_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'fat_demand': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PlanForm(forms.ModelForm):
    # exercises = forms.ModelMultipleChoiceField(queryset=Exercise.objects.all(), label='Exercise list', widget=CheckboxSelectMultiple())

    class Meta:
        model = Plan
        fields = ['name', 'diet', 'exercises']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'diet': forms.Select(attrs={'class': 'form-control'}),
            'exercises': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class MacroCalculatorForm(forms.Form):
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.IntegerField(label='Height', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight = forms.FloatField(label='Weight', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sex', choices=SEX, widget=forms.Select(attrs={'class': 'form-control'}))
    activity = forms.ChoiceField(label='Activity', choices=ACTIVITY, widget=forms.Select(attrs={'class': 'form-control'}))
    goal = forms.ChoiceField(label='Goal', choices=GOAL, widget=forms.Select(attrs={'class': 'form-control'}))
