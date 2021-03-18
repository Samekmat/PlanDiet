import pytest

from plandiet_app.models import Exercise, CustomUser, Category, Diet, Plan
from django.test import Client


@pytest.fixture
def client():
    return Client()


#  Include your db into testing

# @pytest.fixture(scope='session')
# def django_db_setup():
#     settings.DATABASES['default'] = {}


@pytest.fixture
def exercise():
    return Exercise.objects.create(name='testowe', description='opis jakis', difficulty='beginner')


# @pytest.fixture
# def exercises_db():
#     return Exercise.objects.all()


@pytest.fixture
def exercises_fake_db():
    for _ in range(1, 10):
        exercise = Exercise.objects.create(
            name=f'exercise{_}',
            description=f'description{_}',
            difficulty='beginner',
        )
    return Exercise.objects.all()

@pytest.fixture
def register():
    return CustomUser.objects.create(username='test', password=123, sex='male')


@pytest.fixture
def categories():
    for _ in range(5):
        category = Category.objects.create(
            name=f'category{_}',
            description=f'desc{_}',
        )
    return Category.objects.all()


@pytest.fixture
def category():
    return Category.objects.create(name='nowa', description='opis nowej kategori')


# @pytest.fixture
# def diets_db():
#     return Diet.objects.all()


@pytest.fixture
def diets_fake_db():
    for _ in range(1, 10):
        diet = Diet.objects.create(
            name=f'diet{_}',
            description=f'desc{_}',
            caloric_demand=10,
            carbs_demand=10,
            fat_demand=10,
            protein_demand=10,
        )
    return Diet.objects.all()


@pytest.fixture
def diet():
    return Diet.objects.create(
        name='test for diet',
        carbs_demand=12,
        caloric_demand=12,
        fat_demand=12,
        protein_demand=12,
        description='opsi',
    )


@pytest.fixture
def diet_data():
    return {
        'name': 'dobra',
        'carbs_demand': 260,
        'caloric_demand': 2700,
        'fat_demand': 70,
        'protein_demand': 150,
        'description': 'dobra dieta',
    }


@pytest.fixture
def plans_fake_db():
    for _ in range(1, 10):
        plan = Plan.objects.create(name=f'plan{_}')
    return Plan.objects.all()


@pytest.fixture
def plan():
    return Plan.objects.create(name=f'plan',)


@pytest.fixture
def plan_data():
    return {
        'name': 'planik',
    }


@pytest.fixture
def user():
    user = CustomUser.objects.create_user(username='normal', email='normal@email.com', password='normal')
    return user


@pytest.fixture
def user_data():
    return {'username': 'normal', 'email': 'normal@gmail.com', 'password1': 'normal', 'password2': 'normal'}