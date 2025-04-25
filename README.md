Django Blog Application
Description
This is a simple yet powerful blog application built using the Django framework. It allows users to create, read, update, and delete blog posts. The application is designed with user authentication, categories, and a responsive interface to provide an engaging blogging experience.

* Features
User authentication (login, registration, and logout)
CRUD functionality for blog posts
Category management for blog posts
User-friendly admin panel
Pagination for blog listings
Search functionality


*Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript (Bootstrap for styling)
Database: SQLite (default, can be switched to PostgreSQL, MySQL, etc.)
Authentication: Django's built-in user authentication system

* Installation
1.Prerequisites
2.Python 3.8 or higher
3.Django 4.0 or higher
4.Virtual environment (optional but recommended)
-python -m venv env
-source env/bin/activate
5.Install dependencies:
-pip install -r requirements.txt
6.Apply migrations:
-python manage.py makemigrations
-python manage.py migrate
7.Create a superuser (for admin panel access):
-python manage.py createsuperuser
8.Run the development server:
-python manage.py runserver
9.A database system (SQLite by default)


*Admin Panel:
Log in at /admin/ with your superuser credentials to manage users, posts, and categories.

*Blog Functionality:

Navigate to the homepage to view the list of blog posts.
Log in to create new posts or edit/delete your own posts.
Use categories to filter posts and search to find specific content.
