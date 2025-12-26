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



# StockHub API Documentation

## Overview

StockHub is an Inventory Management REST API built with Django and Django REST Framework (DRF). This documentation covers authentication and user management functionalities, including user registration, login, token-based authentication, and profile access.

Base URL (Development):


http://127.0.0.1:8000/


All API responses are in JSON format.


## Authentication

StockHub uses **Django REST Framework Token Authentication**.

* A token is generated when a user registers or logs in successfully.
* The token must be included in the `Authorization` header for protected endpoints.

### Authorization Header Format


Authorization: Token <your_token_here>


## User Roles

Users can have one of the following roles:

* **Admin** – Full access to system data and management features.
* **Staff** – Limited access based on permissions.

Role-based permissions can be extended as the application grows.


## API Endpoints

### 1. User Registration

**Endpoint:**

POST /api/accounts/register/

**Description:**
Registers a new user and returns an authentication token.

**Request Body:**

```json
{
  "username": "john_doe",
  "password": "StrongPassword123",
  "company": "StockHub Ltd",
  "year": 2025,
  "role": "staff"
}

**Success Response (201 Created):**

json
{
  "message": "User registered successfully",
  "token": "abc123xyz..."
}


**Error Response (400 Bad Request):**

json
{
  "username": ["This field is required."]
}


### 2. User Login

**Endpoint:**

POST /api/accounts/login/

**Description:**
Authenticates a user and returns an authentication token.

**Request Body:**

json
{
  "username": "john_doe",
  "password": "StrongPassword123"
}


**Success Response (200 OK):**

json
{
  "message": "Login successful",
  "token": "abc123xyz..."
}

**Error Response (400 Bad Request):**

json
{
  "non_field_errors": ["Invalid username or password"]
}

### 3. User Profile (Protected)

**Endpoint:**

GET /api/accounts/profile/


**Description:**
Retrieves the profile of the currently authenticated user.

**Headers Required:**


Authorization: Token <your_token_here>


**Success Response (200 OK):**

json
{
  "username": "john_doe",
  "company": "StockHub Ltd",
  "year": 2025,
  "role": "staff"
}


**Error Response (401 Unauthorized):**

json
{
  "detail": "Authentication credentials were not provided."
}



## Authentication Flow Summary

1. User registers via `/register/` → receives token.
2. User logs in via `/login/` → receives token.
3. Token is included in headers for protected requests.
4. Protected endpoints validate token before granting access.


## HTTP Status Codes Used

| Status Code | Meaning                                 |
| ----------- | --------------------------------------- |
| 200         | OK – Request successful                 |
| 201         | Created – Resource successfully created |
| 400         | Bad Request – Validation or input error |
| 401         | Unauthorized – Missing or invalid token |
| 403         | Forbidden – Insufficient permissions    |


## Security Notes

* Passwords are securely hashed using Django’s authentication system.
* Tokens should be kept secret and transmitted only over HTTPS in production.
* Token authentication is suitable for mobile apps and frontend frameworks.


## Future Enhancements

* Inventory, Purchase, and Sales CRUD APIs
* Role-based permissions (Admin vs Staff)
* JWT authentication option
* API versioning
* Swagger/OpenAPI documentation


## Conclusion

This documentation provides a clear guide for integrating and testing StockHub’s authentication and user management APIs. It serves as a foundation for extending the system with inventory and transactional features.

| Method | Endpoint              | Purpose                                    |
| ------ | --------------------- | ------------------------------------------ |
| POST   | `/api/auth/login/`    | Login user and return authentication token |
| POST   | `/api/token/`         | Obtain JWT access & refresh tokens         |
| POST   | `/api/token/refresh/` | Refresh JWT access token                   |
| GET    | `/logout/`            | Logout the currently logged-in user        |

| GET    | `/api/accounts/`          | List all users (admin use)      |
| POST   | `/api/accounts/register/` | Register a new user             |
| GET    | `/api/accounts/profile/`  | Retrieve logged-in user profile |
| PUT    | `/api/accounts/profile/`  | Update user profile             |
| PATCH  | `/api/accounts/profile/`  | Partially update user profile   |





# StockHub – Inventory Management API

## Overview

StockHub is a Django REST Framework–based Inventory Management API designed to help organizations manage stock records efficiently. This project demonstrates core Django concepts including models, migrations, authentication, and CRUD operations using Django ORM and RESTful APIs.

This README focuses on the **Stock module**, which represents inventory records consisting of header and body fields.


## Features

* Token-based authentication (Django REST Framework)
* Role-based users (Admin & Staff)
* Stock inventory management
* Full CRUD operations via API and Django shell
* Clean, modular Django app structure


## Technology Stack

* Python 3
* Django
* Django REST Framework
* SQLite (development database)


## Authentication

This API uses **DRF Token Authentication**.

### How Authentication Works

1. User registers or logs in
2. A token is generated
3. Token must be included in request headers:

Authorization: Token <your_token_here>

## Stock Model

### Header Fields

* `date`
* `remark`
* `currency`
* `project`

### Body Fields

* `item_code`
* `item_description`
* `warehouse`
* `quantity_issued`
* `stock_balance`
* `price`
* `remarks`


## API Endpoints

| Method | Endpoint                     | Purpose                            |
| ------ | ---------------------------- | ---------------------------------- |
| GET    | `/api/inventory/stocks/`      | Retrieve all inventory items       |
| POST   | `/api/inventory/stocks/`      | Create a new inventory record      |
| GET    | `/api/inventory/stocks/{id}/` | Retrieve a single inventory item   |
| PUT    | `/api/inventory/stocks/{id}/` | Update an inventory item           |
| PATCH  | `/api/inventory/stocks/{id}/` | Partially update an inventory item |
| DELETE | `/api/inventory/stocks/{id}/` | Delete an inventory item           |

| GET    | `/api/inventory/stock/?item_code=` | Search inventory by item code |
| GET    | `/api/inventory/stock/?warehouse=` | Filter inventory by warehouse |
| GET    | `/api/inventory/stock/?project=`   | Filter inventory by project   |


> 🔐 All endpoints require authentication.


## CRUD Operations via Django Shell

CRUD operations are demonstrated and documented using the Django shell.

### Documentation Files

* `create.md` – Stock creation
* `retrieve.md` – Stock retrieval
* `update.md` – Stock update
* `delete.md` – Stock deletion
* `CRUD_operations.md` – Combined documentation

Each file contains:

* Django shell command used
* Expected output as comments


## Project Structure

StockHub/
├── inventory/
│   ├── models.py
│   ├── migrations/
│   └── apps.py
├── StockHub/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md

## Future Enhancements

* Purchase module
* Sales module
* Inventory reports
* Swagger / OpenAPI documentation
* PostgreSQL database


## Conclusion

This project demonstrates a solid understanding of Django fundamentals, RESTful API design, authentication, and database operations using Django ORM. It is suitable for academic submission and real-world extension.




# StockHub – Inventory Management API


## Purchase & Sales API Documentation

### Overview

The Purchase and Sales modules manage incoming and outgoing stock transactions within the StockHub Inventory Management System. These modules are designed following RESTful principles and support full CRUD operations.

All endpoints are protected using token-based authentication.


## Authentication

**Method:** Token Authentication (Django REST Framework)

**Header Format:**

```
Authorization: Token <your_token>
```


## Purchase API

### Purchase Model Fields

**Header Fields**

* date
* client_name
* client_code
* client_address
* project_name
* warehouse

**Body Fields**

* item_id
* item_code
* item_description
* quantity_purchased
* remarks

### Purchase Endpoints
| Method | Endpoint                        | Purpose                       |
| ------ | ------------------------------- | ----------------------------- |
| GET    | `/api/purchases/purchase/`      | Retrieve all purchase records |
| POST   | `/api/purchases/purchase/`      | Create a new purchase record  |
| GET    | `/api/purchases/purchase/{id}/` | Retrieve a single purchase    |
| PUT    | `/api/purchases/purchase/{id}/` | Update a purchase record      |
| PATCH  | `/api/purchases/purchase/{id}/` | Partially update a purchase   |
| DELETE | `/api/purchases/purchase/{id}/` | Delete a purchase record      |



## Sales API

### Sales Model Fields

**Header Fields**

* date
* client_name
* client_code
* client_address
* project_name
* warehouse

**Body Fields**

* item_id
* item_code
* item_description
* quantity_sold
* remarks

### Sales Endpoints

| Method | Endpoint                 | Purpose                         |
| ------ | ------------------------ | ------------------------------- |
| GET    | `/api/sales/sales/`      | Retrieve all sales records      |
| POST   | `/api/sales/sales/`      | Create a new sales record       |
| GET    | `/api/sales/sales/{id}/` | Retrieve a single sale          |
| PUT    | `/api/sales/sales/{id}/` | Update a sales record           |
| PATCH  | `/api/sales/sales/{id}/` | Partially update a sales record |
| DELETE | `/api/sales/sales/{id}/` | Delete a sales record           |


## Status Codes

* 200 OK – Successful request
* 201 Created – Resource created successfully
* 400 Bad Request – Validation error
* 401 Unauthorized – Authentication required
* 404 Not Found – Resource not found

## Security Notes

* All write operations require authentication
* Input validation is enforced via serializers
* Sensitive operations are restricted to authorized users


## Conclusion

The Purchase and Sales APIs provide a structured and secure way to manage inventory transactions. They integrate seamlessly with the Stock module and are designed for future scalability, reporting, and analytics.
