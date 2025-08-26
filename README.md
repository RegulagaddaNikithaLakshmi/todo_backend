**📝 Todo Backend API**


**Project Overview**

Todo Backend API is a RESTful backend service built with Django and Django REST Framework.
It allows users to create, read, update, and delete todos efficiently, providing a scalable task management solution. ✅

**✨ Key Features:**

🆕 Create new todos

📖 Retrieve all or specific todos

✏️ Update existing todos

❌ Delete todos

⚡ Fast, lightweight, and ready for production deployment

🛠️ Technology Stack

🐍 Python 3.x

🌐 Django 5.2.4

🔧 Django REST Framework 3.16.0

💾 SQLite (can be swapped with PostgreSQL/MySQL)

🚀 Gunicorn (for production deployment)

**🚀 Installation & Setup:**

1. Clone the repository
  git clone https://github.com/RegulagaddaNikithaLakshmi/todo_backend.git
  cd todo_backend

2. Create a virtual environment

   python -m venv venv

# Windows

venv\Scripts\activate

# Linux/Mac

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Apply database migrations
 
python manage.py migrate

Run the development server

python manage.py runserver

**📄 API Endpoints**:

Method	Endpoint	Description

GET	/todos/	📖 Retrieve all todos

POST	/todos/	🆕 Create a new todo

GET	/todos/{id}/	📖 Retrieve a specific todo

PUT	/todos/{id}/	✏️ Update a todo

DELETE	/todos/{id}/	❌ Delete a todo


**🚀 Deployment**

Use Gunicorn for production deployment:

gunicorn todoproject.wsgi


⚠️ Note: Replace todoproject with your actual Django project folder name containing settings.py and wsgi.py.



**📄 License**

This project is licensed under the MIT License. See the LICENSE file for details. 
