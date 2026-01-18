Employee Management System (Django)

A simple and efficient Employee Management System built using the Django framework. This application provides core functionality to manage employee records, including adding, updating, deleting, and filtering employees. The project is designed to demonstrate Django fundamentals and CRUD operations in a clean and structured way.

📌 About the Project

Managing employee information manually can be time-consuming and error-prone. This web-based system offers a centralized solution to store and manage employee data efficiently. It uses Django’s powerful ORM and follows the MVT (Model-View-Template) architecture.

This project is ideal for:

Beginners learning Django

Academic or college submissions

Portfolio and GitHub projects

✨ Features

Add new employee records

Update existing employee details

Delete employee records

Filter employees based on criteria

Simple and user-friendly interface

Database-backed application using Django ORM

🛠️ Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

Database: SQLite

Version Control: Git, GitHub

📂 Project Structure
employee_management_system/
│
├── employee_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
└── README.md

⚙️ Installation & Setup
Prerequisites

Python 3.x

pip

Git

Steps to Run the Project

Clone the repository

git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install Django

pip install django


Apply migrations

python manage.py makemigrations
python manage.py migrate


Run the server

python manage.py runserver


Open the application

http://127.0.0.1:8000/
