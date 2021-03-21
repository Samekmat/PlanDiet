import pytest

from django import urls
from django.urls import reverse

from django.contrib.auth import get_user_model
from .models import Diet, CustomUser


@pytest.mark.django_db
def test_render_views(client):
    temp_url = reverse('exercise-list')
    resp = client.get(temp_url)
    assert resp.status_code == 200


# @pytest.mark.django_db
# def test_exercise_list_db(client):
#     response = client.get('/exercise_list/')
#     assert response.status_code == 200
#     assert response.content != ''
#     assert Exercise.objects.count() == 60


@pytest.mark.django_db
def test_exercise_list_fake_db(client, exercises_fake_db):
    exercises = exercises_fake_db
    resp = client.get(reverse('exercise-list'))
    assert resp.status_code == 200
    for exercise in exercises:
        assert exercise in resp.context['exercises']
    assert len(exercises.all()) == 9


@pytest.mark.django_db(transaction=True)
def test_exercise_id(client, exercise):
    response = client.get(f'/exercise/{exercise.id}/')
    assert response.status_code == 200
    assert exercise.name == 'testowe'
    assert exercise.description == 'opis jakis'
    assert exercise.difficulty == 'beginner'


@pytest.mark.django_db
def test_exercise_fake(exercises_fake_db):
    exercises = exercises_fake_db
    assert exercises[0].name == 'exercise1'
    assert exercises[0].description == 'description1'
    assert exercises[1].name == 'exercise2'
    assert exercises[4].name == 'exercise5'


@pytest.mark.django_db
def test_categories(client, categories):
    response = client.get('/categories/')
    assert response.status_code == 200
    assert response.content != ''
    for category in categories:
        assert category in response.context['categories']
    assert len(categories.all()) == 5


@pytest.mark.django_db
def test_category(client, category):
    response = client.get(f'/category/{category.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_diet_list_fake_db(client, diets_fake_db):
    diets = diets_fake_db
    resp = client.get(reverse('diet-list'))
    assert resp.status_code == 200
    assert diets.count() == 9


@pytest.mark.django_db
def test_diet(client, diet):
    response = client.get(f'/diet/{diet.id}/')
    assert response.status_code == 200
    assert response.content != ''
    assert diet.name == 'test for diet'
    assert diet.fat_demand == 12
    assert diet.description == 'opsi'
    assert diet.carbs_demand == 12
    assert diet.protein_demand == 12
    assert diet.caloric_demand == 12


@pytest.mark.django_db
def test_diet_add(client, diet_data):
    response = client.post('/diet/add/', diet_data)
    assert response.status_code == 302
    # if we're redirected that means we created new diet and we are now on diet/id page


@pytest.mark.django_db
def test_diet_update(client, diets_fake_db):
    diet = diets_fake_db.first()
    response = client.get(f'/diet/update/{diet.id}/')
    assert response.status_code == 302
    assert diet.name == 'diet1'
    assert diet.description == 'desc1'
    assert diet.caloric_demand == 10
    assert diet.carbs_demand == 10
    assert diet.protein_demand == 10
    assert diet.fat_demand == 10
    diet.name = 'dietupdate'
    diet.description = 'descupdate'
    diet.caloric_demand = 15
    assert diet.name == 'dietupdate'
    assert diet.description == 'descupdate'
    assert diet.caloric_demand == 15
    assert diet.fat_demand == 10


@pytest.mark.django_db
def test_diet_delete(client, diets_fake_db):
    diet = diets_fake_db.first()
    response = client.get(f'/diet/delete/{diet.id}/')
    assert response.status_code == 302
    assert Diet.objects.all().count() == 9
    Diet.objects.filter(id=1).delete()
    assert Diet.objects.all().count() == 8


@pytest.mark.django_db
def test_custom_user_create():
    assert CustomUser.objects.count() == 0
    CustomUser.objects.create_user(
                                    username='Johnnie',
                                    first_name='John',
                                    last_name='Doe',
                                    age=30,
                                    height=178,
                                    weight=75,
                                    sex='male',
                                   )
    assert CustomUser.objects.count() == 1


@pytest.mark.django_db
def test_plan_list_fake_db(client, plans_fake_db):
    plans = plans_fake_db
    resp = client.get(reverse('plan-list'))
    assert resp.status_code == 200
    assert plans.count() == 9


@pytest.mark.django_db
def test_plan(client, plan):
    response = client.get(f'/plan/{plan.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_plan_add(client, plan_data):
    response = client.post('/plan/add/', plan_data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_plan_update(client, plans_fake_db):
    plan = plans_fake_db.first()
    response = client.get(f'/plan/update/{plan.id}/')
    assert response.status_code == 302
    assert plan.name == 'plan1'
    plan.name = 'plankupdate'
    assert plan.name == 'plankupdate'


@pytest.mark.django_db
def test_diet_delete(client, plans_fake_db):
    plan = plans_fake_db.first()
    response = client.get(f'/plan/delete/{plan.id}/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_index_view(client):
    response = client.get('/index/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login(client, user):
    resp_get = client.get(reverse('login'))
    assert resp_get.status_code == 200
    resp_post = client.post(reverse('login'), {'login': user.username, 'password': 'normal'})
    assert resp_post.status_code == 302
    resp_post2 = client.post(reverse('login'), {'login': user.username, 'password': 'superuser'})
    assert resp_post2.status_code == 200
    assert resp_post2.context['error'] == "User can't be found"
    resp_post3 = client.post(reverse('login'), {'login': 'admin', 'password': 'normal'})
    assert resp_post3.status_code == 200
    assert resp_post3.context['error'] == "User can't be found"


@pytest.mark.django_db
def test_logout(client, user):
    client.login(username=user.username, password='normal')
    resp = client.get(reverse('logout'))
    assert resp.status_code == 302


@pytest.mark.django_db
def test_register(client, user_data):
    resp_get = client.get(reverse('register'))
    assert resp_get.status_code == 200
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    register_url = urls.reverse('register')
    resp_post = client.post(register_url, user_data)
    assert user_model.objects.count() == 1
    assert resp_post.status_code == 302


@pytest.mark.django_db
def test_macro_calc(client):
    resp = client.get(reverse('macro-calc'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_profile(client):
    response = client.get(reverse('profile'))
    assert response.status_code == 200
