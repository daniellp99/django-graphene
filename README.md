# Django-Graphene

This project is for learning proposes of the [django-graphene](https://docs.graphene-python.org/projects/django/en/latest/) module features. Using basic queries and mutations

## Features

 - Use poetry for build and manage python env
 - Use a general abstract class Query for global configuration allow you to add easily multiple app schemas
 - Use GraphiQL, in-browser tool for writing, validating, and testing GraphQL queries.
 - Load data from a json file with fixtures
 - Use graphene relay for queries
 - Use create and update mutations
 - ... and much more

## Getting Started

To run this project locally, please follow the steps below:

### Using Poetry

```bash
poetry install
```

### Using pip

#### Create Python Virtual Environment

```bash
python3 -m venv env
```

#### Activate the Environment

On macOS and Linux:

```bash
source env/bin/activate
```
On Windows:

```bash
.\env\Scripts\activate
```

#### Install Requirements

```bash
pip install -r requirements.txt
```

### Setup Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Load Fixtures

On the root of the project:

```bash
python manage.py loaddata ingredients
```

### Run Development Server

On the root of the project:

```bash
python manage.py runserver
```
You should now be able to access the project at http://localhost:8000/graphql.

## License

[MIT](https://choosealicense.com/licenses/mit/)