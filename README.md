# 🍲 ShareMyDish - Django Recipe Sharing Platform

A full-featured web application for food enthusiasts to **share, discover, and manage recipes** with ease. Built using Django, this platform offers secure login/logout functionality, post creation and editing, and community-driven recipe discovery. Hosted live at [https://django-sharemydish.onrender.com](https://django-sharemydish.onrender.com/).

---

## 🌮 Features

### 🔐 Authentication

* User registration, login, and logout
* Session management with CSRF protection

### 📃 Recipe Management

* Create, edit, and delete your own dishes
* View detailed recipe posts from other users
* Responsive form validation using Django Forms

### 📄 CRUD Functionality

* **C**reate: Add new recipes with a title, description, and ingredients
* **R**ead: Browse all shared recipes
* **U**pdate: Edit your existing posts
* **D**elete: Remove recipes you no longer want to share

### 💡 UI & Templates

* Clean template-based views with modular HTML using Django's template inheritance system
* Feedback messages for every action (e.g., post created, updated, deleted)

---

## 🏆 Live Demo

📍 [https://django-sharemydish.onrender.com](https://django-sharemydish.onrender.com)

---

## 🌐 Technologies Used

| Purpose             | Stack                       |
| ------------------- | --------------------------- |
| Web Framework       | Django (Python)             |
| Frontend Templating | Django Templates + HTML/CSS |
| Database            | SQLite3 (Default Django DB) |
| Hosting             | Render                      |
| Version Control     | Git + GitHub                |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sharemydish.git
cd sharemydish
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Migrations & Start Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the app locally.

---

## 🔍 Project Structure

```
sharemydish/
├── dish/
│   ├── migrations/
│   ├── templates/dish/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/  # user auth
├── sharemydish/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── db.sqlite3
├── requirements.txt
└── Procfile
```

---

## 🚧 Future Improvements

* Add image upload for dishes
* Commenting system on recipes
* Search and filter functionality
* User profiles and saved recipes

---



## 👨‍💼 Author

Developed by [@vedantmpatil](https://github.com/vedantmpatil)

---

Happy Cooking ☕️ and Happy Coding 🚀!
