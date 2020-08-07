# Logs System
[![Build Status](https://travis-ci.org/carlos-moreno/logs-system.svg?branch=master)](https://travis-ci.org/carlos-moreno/logs-system)
[![Updates](https://pyup.io/repos/github/carlos-moreno/logs-system/shield.svg)](https://pyup.io/repos/github/carlos-moreno/logs-system/)
[![Maintainability](https://api.codeclimate.com/v1/badges/020de6a6f7c5eb37638c/maintainability)](https://codeclimate.com/github/carlos-moreno/logs-system/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/020de6a6f7c5eb37638c/test_coverage)](https://codeclimate.com/github/carlos-moreno/logs-system/test_coverage)

Log system developed as a final challenge during the acceleration of 
[Codenation](https://www.codenation.dev/) in partnership with [Stone](https://www.stone.com.br/).

The system was developed as a proposal to be an API to centralize the receipt of logs and, thus, 
improve the management of information about possible problems in the applications where the logs come from.

## Tools used in the project

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html#)
* [Swagger UI](https://swagger.io/)
* [Code Climate](https://codeclimate.com/)
* [Travis-CI](https://travis-ci.org/)
* [Heroku](https://www.heroku.com/)
* among other tools


## How to execute the project?

1. Clone the repository
2. Access the application directory
3. Create a virtualenv with Python 3.6+
4. Activate virtualenv
5. Install the dependencies
6. Configure the instance with .env
7. Run migrate 
8. Run the tests
9. Create a superuser
10. Start django

```console
git clone https://github.com/carlos-moreno/logs-system.git
cd logs-system
python -m venv .logs-system
source .logs-system/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py migrate
python manage.py test
python manage.py createsuperuser
python manage.py runserver
```

### System Url's
```
|----------------------------------------------------|
| Description           | URLS                       |
|----------------------------------------------------|
| Documentation         | /                          |
| List Users            | /api/v1/users/             |
| Create User           | /api/v1/users/             |
| Get user specific     | /api/v1/users/{id}/        |
| Update User           | /api/v1/users/{id}/        |
| Delete User           | /api/v1/users/{id}/        |
| List Agents           | /api/v1/agents/            |
| Create Agent          | /api/v1/agents/            |
| Get Agent specific    | /api/v1/agents/{id}/       |
| Update Agent          | /api/v1/agents/{id}/       |
| Delete Agent          | /api/v1/agents/{id}/       |
| List Events           | /api/v1/events/            |
| Create Event          | /api/v1/events/            |
| Get Event specific    | /api/v1/events/{id}/       |
| Update Event          | /api/v1/events/{id}/       |
| Delete Event          | /api/v1/events/{id}/       |
| Get token             | /api/v1/get_token/         |
| Refresh token         | /api/v1/refresh_token/     |
|----------------------------------------------------|
```

### EndPoints and Verbs API
```
|--------------------------------------------|
| Endpoints               | Verbs            |
|--------------------------------------------|
| /api/v1/users/          | GET, POST        |
| /api/v1/users/{id}/     | GET, PUT, DELETE |
| /api/v1/agents/         | GET, POST        |
| /api/v1/agents/{id}/    | GET, PUT, DELETE |
| /api/v1/events/         | GET, POST        |
| /api/v1/events/{id}/    | GET, PUT, DELETE |
| /api/v1/get_token/      | POST             |
| /api/v1/refresh_token/  | POST             |
|--------------------------------------------|
```

## Query examples

- List all users
```console
GET >> http://localhost:8000/api/v1/users/
```
- Create a new user
```console
body example
{
    "first_name": "Fulano",
    "last_name": "de Tal",
    "email": "fulano@xpto.com",
    "password": "fulano123"
}
POST >> http://localhost:8000/api/v1/users/
```
- Get user token
```console
body example
{
    "email": "fulano@xpto.com",
    "password": "fulano123"
}
POST >> http://localhost:8000/api/v1/get_token/
```
- List agents filtering by status
```console
GET >> http://localhost:8000/api/v1/agents/?status=true
```
- List events filtering by level
```console
GET >> http://localhost:8000/api/v1/events/?level=CRITICAL
```
- List events sorted by level
```console
GET >> http://localhost:8000/api/v1/events/?ordering=level
```

### Tip:

If desired, the postgres database can be used in a docker container. To do this, simply set 
the DATABASE_URL variable pointing to the data in the docker-compose file and run the 
docker-compose.yml file as follows:
```console
docker-compose -f docker-compose.yml up -d
```
