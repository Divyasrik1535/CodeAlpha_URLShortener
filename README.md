# CodeAlpha URL Shortener

A URL Shortener API built using Django and Django REST Framework.

## Features

* Shorten long URLs
* Generate unique short codes
* Store URLs in SQLite database
* Redirect short URLs to original URLs
* List all shortened URLs

## Installation

```bash
git clone <repository-url>
cd urlshortener
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

### Create Short URL

POST `/api/shorten/`

Request:

```json
{
  "original_url": "https://www.google.com"
}
```

### List URLs

GET `/api/urls/`

### Redirect

GET `/s/<short_code>/`

Example:

`http://127.0.0.1:8000/s/axtQIe/`
