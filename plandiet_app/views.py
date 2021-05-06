from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from .models import Exercise, CustomUser, Category, Diet, Plan
from .forms import LoginForm, RegistrationForm, DietModelForm, PlanForm, MacroCalculatorForm


class ExerciseView(View):
    def get(self, request, id):
        exercise = Exercise.objects.get(pk=id)
        return render(request, 'exercise.html', {'exercise': exercise})


class ExerciseListView(View):
    def get(self, request):
        exercises = Exercise.objects.all()
        paginator = Paginator(exercises, 18)
        page = request.GET.get('page', 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        return render(request, 'exerciselist.html', {'exercises': exercises, 'pages': pages})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/index')
            else:
                return render(request, 'login.html', {'form': form, 'error': "User can't be found"})


class LogoutView(View):
    def get(self, request):
        logout(request)
        # return redirect(request.META['HTTP_REFERER'])
        return redirect(reverse('index'))


class RegistrationFormView(FormView):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            CustomUser.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                age=form.cleaned_data['age'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                sex=form.cleaned_data['sex']
                )
            return redirect('/login')
        return render(request, 'registration.html', {'form': form})


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categorylist.html', {'categories': categories})


class CategoryView(View):
    def get(self, request, id):
        category = Category.objects.get(pk=id)
        return render(request, 'category.html', {'category': category})


class DietListView(View):
    def get(self, request):
        diets = Diet.objects.all()
        paginator = Paginator(diets, 10)
        page = request.GET.get('page', 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return render(request, 'diets/dietlist.html', {'diets': diets, 'pages': pages})


class DietView(View):
    def get(self, request, pk):
        diet = Diet.objects.get(pk=pk)

        return render(request, 'diets/diet.html', {'diet': diet})


class DietCreateView(CreateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.add_diet'
    form_class = DietModelForm
    template_name = 'diets/diet_create.html'

    def get_success_url(self):
        return reverse("diet", kwargs={'pk': self.object.pk})


class DietUpdateView(UpdateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.change_diet'
    form_class = DietModelForm
    template_name = 'diets/diet_update.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Diet, pk=id_)


class DietDeleteView(DeleteView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.delete_diet'
    template_name = 'diets/diet_delete.html'
    success_url = '/diet_list'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Diet, pk=id_)


class PlanListView(View):
    def get(self, request):
        plans = Plan.objects.all()
        paginator = Paginator(plans, 5)
        page = request.GET.get('page', 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return render(request, 'plans/planlist.html', {'plans': plans, 'pages': pages})


class PlanView(View):
    def get(self, request, pk):
        plan = Plan.objects.get(pk=pk)
        return render(request, 'plans/plan.html', {'plan': plan})


class PlanCreateView(CreateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.add_plan'
    form_class = PlanForm
    template_name = 'plans/plan_create.html'

    def get_success_url(self):
        return reverse("plan", kwargs={'pk': self.object.pk})


class PlanUpdateView(UpdateView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.change_plan'
    form_class = PlanForm
    template_name = 'plans/plan_update.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Plan, pk=id_)


class PlanDeleteView(DeleteView):
    # PermissionRequiredMixin,
    # permission_required = 'plandiet_app.delete_plan'
    template_name = 'plans/plan_delete.html'
    success_url = '/plan_list'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Plan, pk=id_)


def bmr_calc(sex, weight, height, age):
    weight = float(weight)
    height = float(height)
    age = float(age)
    if sex == 'male':
        bmr = (9.99 * weight) + (6.25 * height) - (4.92 * age) + 5
        return round(bmr)
    elif sex == 'female':
        bmr = (9.99 * weight) + (6.25 * height) - (4.92 * age) - 161
        return round(bmr)


def cpm_calc(goal, bmr, activity):
    bmr = float(bmr)
    activity = float(activity)
    if goal == 'reduce':
        cpm = bmr * activity
        cpm -= (0.1 * cpm)
        return round(cpm)
    elif goal == 'maintain':
        cpm = bmr * activity
        return round(cpm)
    else:
        cpm = bmr * activity
        cpm += (0.1 * cpm)
        return round(cpm)


class MacroCalculatorView(View):
    def get(self, request):
        try:
            current_user = request.user
            form = MacroCalculatorForm(initial={
                'age': current_user.age,
                'height': current_user.height,
                'weight': current_user.weight,
                'sex': current_user.sex,
                })
            return render(request, 'macrocalculator.html', {'form': form})
        except:
            form = MacroCalculatorForm()
            return render(request, 'macrocalculator.html', {'form': form})

    def post(self, request):
        form = MacroCalculatorForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            sex = form.cleaned_data['sex']
            activity = form.cleaned_data['activity']
            goal = form.cleaned_data['goal']

            bmr = bmr_calc(sex, weight, height, age)
            cpm = cpm_calc(goal, bmr, activity)

        return render(request, 'macrocalculator.html', {'form': form, 'bmr': bmr, 'cpm': cpm})


class ProfileView(View):
    def get(self, request):
        if CustomUser.is_authenticated:
            current_user = request.user
            return render(request, 'profile.html', {'current_user': current_user})
        return render(request, 'profile.html')
