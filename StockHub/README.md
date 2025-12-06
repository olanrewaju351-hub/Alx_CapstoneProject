# StockHub - Basic Django Setup
This repository contains the StockHub starter Django project for the ALX capstone.

# StockHub – Inventory Management API

**Author:** KAZEEM OLANREWAJU ALIMI
**Project:** Capstone
**Subject:** Inventory Management API

---

## Overview

StockHub – Inventory Management API Documentation

StockHub is a Django-based Inventory Management API designed to manage users, inventory, purchases, and sales. It uses Django REST Framework (DRF) to provide secure, token-based authentication and RESTful API endpoints.

This project simulates a real-world inventory management system for companies to efficiently track inventory, manage purchases, and record sales.


1. Project Idea

The idea behind StockHub is to build a well-structured Inventory Management API that allows organizations to manage their stock records, monitor purchases, track sales, and maintain accurate inventory balance.
The system will streamline how users issue stock, record supplies, track clients/vendors, and maintain real-time inventory visibility.

The API will serve as a backend for any inventory system—web, mobile, or desktop—and will include authentication to ensure secure access.

2. Project Features
User Authentication & Authorization

Admin and Staff user roles

Login/logout and token-based authentication

Restriction of access to sensitive data

Inventory Management

Add, update, delete, and view inventory records

Maintain stock balance

Record item issuance and stock movements

Header + Item Body structure for each transaction

Purchase Management

Record new purchases

Track vendor information

Update stock balance on supply

CRUD operations on purchase entries

Sales Management

Capture sales transactions

Track client details

Deduct quantity sold from stock

CRUD operations on sales entries

Reporting (Optional / Extra Feature)

Summary of total items in stock

Total purchases and sales

Low-stock alerts

API-Ready Backend

Will expose REST API endpoints

JSON responses

Proper validation and error handling

3. API & Technology Stack
Backend Framework

Django

Django REST Framework (DRF)

Database

PostgreSQL / SQLite (for development)

Authentication

DRF Token Authentication or JWT (Optional)

Hosting (Optional)

Render, Railway, or DigitalOcean


---

## Features Implemented

* **User Management**

  * Register, login, and manage users
  * Token-based authentication (DRF)

* **API Endpoints**

  * Users CRUD operations
  * Authentication endpoints

* **Project Structure**

  * Modular Django apps for scalability: `accounts`, `inventory`, `purchase`, `sales`
  * Python virtual environment for project isolation

---

## Technologies Used

* Python 3.x
* Django 4.x
* Django REST Framework
* SQLite (development)
* Git & GitHub

---

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YourUsername/Alx_CapstoneProject.git
   cd Alx_CapstoneProject
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access API:**
   Open your browser or Postman at: `http://127.0.0.1:8000/api/`

---

## API Endpoints (Examples)

* **User Registration:**
  `POST /api/auth/register/`

  ```json
  {
    "username": "kazeem",
    "password": "securepassword",
    "company": "StockHub Ltd",
    "role": "Admin",
    "year": 2025
  }
  ```

* **User Login:**
  `POST /api/auth/login/`

  ```json
  {
    "username": "kazeem",
    "password": "securepassword"
  }
  ```

* **User List (Authenticated):**
  `GET /api/users/`

---

## Challenges Faced

* Initial server errors were resolved through debugging and AI guidance.
* Learning Git staging and commits posed some difficulties, which were overcome with practice.

---

## Next Steps

* Implement Inventory App
* Implement Purchase App
* Implement Sales App
* Expand API endpoints for inventory, purchases, and sales

---

## License

This project is for educational purposes and can be freely used and modified.

---

## Contact

* GitHub: https://github.com/olanrewaju351-hub
