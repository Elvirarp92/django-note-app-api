# Django Note App API

A RESTful API for CRUD operations on a DB for a note-making app. (WIP)

## Getting started

### Requisites

* Python

* A package manager such as [pipenv](https://pipenv.pypa.io/en/latest/)

Installation instructions provided below will be for, specifically, pipenv. By default, the CORS middleware is coded to expect requests from `http://localhost:3000`

### Installation

From the root directory of this project:

`$ pipenv install -r requirements.txt`

### Running on local (development)

```shell
$ pipenv shell
$ python noteapprestapi/manage.py runserver
```

By default, this will launch the development server in `http://127.0.0.1:8000/`

## API Endpoints

| **Method** | **Route**  | **Description**                                                                              |
| ---------- | ---------- | -------------------------------------------------------------------------------------------- |
| GET        | /notes     | Retrieves all Note objects                                                                   |
| GET        | /notes/:id | Retrieves an specific Note                                                                   |
| POST       | /notes     | Creates a new Note                                                                           |
| PUT        | /notes/:id | Modifies a Note - being a PUT request, it requires all fields on the object to be sent.      |
| PATCH      | /notes/:id | Modifies a Note - being a PATCH request, it only requires the fields that are to be modified |
| DELETE     | /notes/:id | Deletes a specific Note                                                                      |

| **Method** | **Route**  | **Description**                                                                               |
| ---------- | ---------- | --------------------------------------------------------------------------------------------- |
| GET        | /users     | Retrieves all User objects                                                                    |
| GET        | /users/:id | Retrieves an specific User                                                                    |
| POST       | /users     | Creates a new User                                                                            |
| PUT        | /users/:id | Modifies an User - being a PUT request, it requires all fields on the object to be sent.      |
| PATCH      | /user/:id  | Modifies an User - being a PATCH request, it only requires the fields that are to be modified |
| DELETE     | /users/:id | Deletes a specific User                                                                       |

| **Method** | **Route** | **Description**                                                                             |
| ---------- | --------- | ------------------------------------------------------------------------------------------- |
| GET        | /tags     | Retrieves all Tag objects                                                                   |
| GET        | /tags/:id | Retrieves an specific Tag                                                                   |
| POST       | /tags     | Creates a new Tag                                                                           |
| PUT        | /tags/:id | Modifies a Tag - being a PUT request, it requires all fields on the object to be sent.      |
| PATCH      | /tags/:id | Modifies a Tag - being a PATCH request, it only requires the fields that are to be modified |
| DELETE     | /tags/:id | Deletes a specific Tag                                                                      |

## Roadmap

* Correct serializers
* File upload handling
* Handling cross references in note creation
* Filter functions: by tags, by type, by user

## Built with

* [Django](https://www.djangoproject.com/)

* [Django REST Framework](https://www.django-rest-framework.org/)

## Authors

* [Ira Ramírez](mailto:elvirarp92@gmail.com)
