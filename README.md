# Bee Garden Backend API
An API that handles storage and delivery of Blog or News articles and User managment.

## Features

- Multiple article types supported: e.g. news, howto, article, blog
- Password hashing
- Auth tokens for user CRUD routes
- Email verification system.

## Future Features

- Admin pages beyond basic Django Admin.
- Abilitiy to send newsletter through Admin Pages.
- HTML based email template.
- Additional routes for raw data for use in vizualization. 

## Technology Used

- Written in Python
- DjangoREST Framework
- Postgres SQL
- PyJWT

## Routes

### GET /articles/:type
Calls all articles of the type where visible: true. Returns: '[{id: int, title: str, content: str, type: str, thumbnail: str, description: str, and visible: bool}, ...]'

### GET /article/get/:id
Calls up the indivual article called by id.
Returns: '{id: int, title: str, content: str, type: str, thumbnail: str, description: str, and visible: bool}'

### PUT /login/
Requires '{email: str, password: str}' form data. 
Validates user exists and that password is correct then returns user. 
Returns: '{id: int, email: str, zipcode: int, gardenarea: int, newsletter: bool, token: str, verified: bool, created: date}'

### POST /create/

Requires '{email: str, password: str, newsleter: bool, gardenarea: int, zipcode: int}'. 
Creates new user, after validating e-mail is not already registered. 
Returns: '{id: int, email: str, zipcode: int, gardenarea: int, newsletter: bool, token: str, verified: bool, created: date}'

### POST, DELETE /update/
Requires: {object: str, email: str, zipcode: int, gardenarea: int, newsletter: int, password: str, new: variable, token: str}.
Deletes or Updates user info as defined by 'object'--must match key from user info above. New data for defined object is passed by 'new' key.
Returns: '{id: int, email: str, zipcode: int, gardenarea: int, newsletter: bool, token: str, verified: bool, created: date}'

### GET /garden/:id
Calls publicly available garden data by garden id for data viz or factoids.
Returns: '{created: date, zipcode: int, gardenarea: int, gardencount_local: int, gardencount_total: int, totalsqft_local: int, totalsqft_total: int, avgsqft_local: int, avgsqft_total: int}

## Installation
Download all packages.

Install dependencies with:
'pip install requirements.txt'

Migrate database with:
'python manage.py makemigrations'
'python manage.py migrate'

Run:
'python manage.py runserver'



