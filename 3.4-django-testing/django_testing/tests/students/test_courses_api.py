import pytest
# from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from model_bakery import baker


from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_first_course(client, courses_factory):
    # Arrange
    course = courses_factory(_quantity=1)

    # Act
    response = client.get(f'/api/v1/courses/{course[0].id}/')

    # Assert
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == course[0].id
    assert data['name'] == course[0].name

@pytest.mark.django_db
def test_courses(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=100)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    for i, c in enumerate(data):
        assert c['id'] == courses[i].id
        assert c['name'] == courses[i].name

@pytest.mark.django_db
def test_filter_id_courses(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/', {'id': courses[3].id})

    # Assert
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data[0]['id'] == courses[3].id
    assert data[0]['name'] == courses[3].name

@pytest.mark.django_db
def test_filter_name_courses(client, courses_factory):
    # Arrange
    courses = courses_factory(_quantity=10)
    # Act
    response = client.get('/api/v1/courses/', {'name': courses[7].name})

    # Assert
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == courses[7].id
    assert data[0]['name'] == courses[7].name

@pytest.mark.django_db
def test_create_courses(client):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'name': 'Python'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_courses(client, courses_factory):
    courses = courses_factory(_quantity=10)
    new_name = 'Python Django'
    response = client.patch(f'/api/v1/courses/{courses[7].id}/', data={'name': new_name})
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == courses[7].id
    assert data['name'] == new_name

@pytest.mark.django_db
def test_delete_courses(client, courses_factory):
    courses = courses_factory(_quantity=10)
    response = client.delete(f'/api/v1/courses/{courses[3].id}/')
    assert response.status_code == 204
    assert response.data == None

@pytest.mark.parametrize(
["count_st", "expected_status"],
(
    (15, status.HTTP_200_OK),
    (-1, status.HTTP_400_BAD_REQUEST),
    (21, status.HTTP_400_BAD_REQUEST),
)
)

@pytest.mark.django_db
def test_count_st_validation(settings, count_st, expected_status):
    status_code = status.HTTP_400_BAD_REQUEST
    if 0 <= count_st <= settings.MAX_STUDENTS_PER_COURSE:
        status_code = status.HTTP_200_OK
    assert status_code == expected_status


# def test_example():
#     assert False, "Just test example"

