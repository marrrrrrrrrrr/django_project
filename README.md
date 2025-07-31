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
![Login Page](https://imgur.com/241FIM6.png)

---

### 📝 Registration Page – Sign Up for a New Account
![Registration Page](https://imgur.com/tHvl3Y0.png)

---

### 📂 Categories Page – Filter Items Easily
![Categories Page](https://imgur.com/YRQfypM.png)

---

### 👤 My Profile – View and Manage Your Account
![Profile Page](https://imgur.com/lkmjBmP.png)

---

### 🛒 View Cart – Track Selected Items
![View Cart](https://imgur.com/H7OnyXB.png)

---

### 💳 Checkout Page – Finalize Your Order
![Checkout Page](https://imgur.com/lkmjBmP.png)

---

### 🧾 Order Details Page – View Completed Orders
![Order Details](https://imgur.com/1uultqB.png)

---

## How to Run Locally

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
