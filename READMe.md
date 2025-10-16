# Blog Application Using Django
## Description

A simple blog application built with Django that supports creating, editing and listing posts, user authentication, and comments.

## How to run

1. Prerequisites
    - Python 3.8+ and pip
    - virtualenv (optional but recommended)

2. Setup
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    pip install -r requirements.txt 

    ```
3. Clone the project 

    ```bash
    git clone https://github.com/Kushan2k/social-media-app-using-django-python.git && cd <project_folder>
    ```

3. Database and static files
    ```bash
    python manage.py makemigrations
    python manage.py migrate 
    ```

4. Create admin user (optional)
    ```bash
    python manage.py createsuperuser
    ```

5. Run development server
    ```bash
    python manage.py runserver
    ```
    Open http://127.0.0.1:8000/ in a browser.

Notes: For production, configure allowed hosts, a production-ready database, and a WSGI/ASGI server.

## Currently in DEvelopment