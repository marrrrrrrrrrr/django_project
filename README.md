# 👜 TIMELESS – E-commerce Web App (Django)

### A minimal e-commerce platform for browsing and purchasing fashion accessories.

---

## 📌 Description

**TIMELESS** is a simple yet functional e-commerce web application built using the Django framework. The project demonstrates user authentication, category-based product listings, cart functionality, and a basic checkout flow.

All user-facing forms (such as registration and login) include server-side input validations to ensure data integrity and prevent incorrect or incomplete submissions.

The application allows customers to:
- Browse items by category.
- Add products to a shopping cart.
- Register and log into an account with validation.
- View and manage their cart.
- Search for products.

---

## 🧰 Languages & Frameworks

- **Python 3**
- **Django**
- **HTML / CSS**
- **SQLite**

---

## 📸 App Walkthrough

### 🏠 Home Page – Browse Products by Category
![Home Page](https://imgur.com/vusv2fx.png)

---

### 🔐 Login Page – Secure Access for Returning Users
![Login Page](https://i.imgur.com/nZB4HDE.png)

---

### 📝 Registration Page – Sign Up for a New Account
![Registration Page](https://i.imgur.com/w7jICu4.png)

---

## 🛒 Features

- 🗂 Product categories  
- 🔍 Product search bar  
- 🧾 Cart with item count and pricing  
- 🔑 Authentication system  
- ✅ **Form input validation for login, registration, and checkout**  
- 📋 Simple and clean UI  
- 🛠 Admin backend via Django admin panel

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/marrrrrrrrrrr/django_project.git

cd django_project

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
