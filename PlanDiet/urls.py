"""DS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from plandiet_app.views import ExerciseView, ExerciseListView, LoginView, RegistrationFormView, Index, LogoutView,\
    CategoryListView, CategoryView, DietView, DietCreateView,\
    DietUpdateView, DietDeleteView, DietListView, PlanListView, PlanView, PlanCreateView, PlanUpdateView,\
    PlanDeleteView, MacroCalculatorView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exercise/<int:id>/', ExerciseView.as_view(), name='exercise'),
    path('exercise_list/', ExerciseListView.as_view(), name='exercise-list'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:id>/', CategoryView.as_view(), name='category'),
    path('diet_list/', DietListView.as_view(), name='diet-list'),
    path('diet/<int:pk>/', DietView.as_view(), name='diet'),
    path('diet/add/', DietCreateView.as_view(), name='diet-add'),
    path('diet/update/<int:pk>/', DietUpdateView.as_view(), name='diet-update'),
    path('diet/delete/<int:pk>/', DietDeleteView.as_view(), name='diet-delete'),
    path('plan_list/', PlanListView.as_view(), name='plan-list'),
    path('plan/<int:pk>/', PlanView.as_view(), name='plan'),
    path('plan/add/', PlanCreateView.as_view(), name='plan-add'),
    path('plan/update/<int:pk>/', PlanUpdateView.as_view(), name='plan-update'),
    path('plan/delete/<int:pk>/', PlanDeleteView.as_view(), name='plan-delete'),
    path('index/', Index.as_view(), name='index'),
    path('', LoginView.as_view(), name='login-main'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationFormView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('macro_calculator/', MacroCalculatorView.as_view(), name='macro-calc'),
]
