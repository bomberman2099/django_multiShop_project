# django_multiShop_project

A full-stack e-commerce platform built with Django, focusing on a clean architecture, modular backend design, and smooth frontend experience.

---

## 🚀 Overview

`django_multiShop_project` is an e-commerce application developed using Django. It covers features such as product management, shopping cart, order processing, user authentication, and backend APIs. The primary focus is on robust backend logic, clean design, and maintainability.

---

## 🧰 Technologies & Tools

- **Backend & APIs:** Python, Django, Django REST Framework  
- **Database:** PostgreSQL / MySQL  
- **Frontend (basic):** HTML, CSS, JavaScript  
- **DevOps / Tools:** Docker, Git, GitHub Actions (CI/CD)  
- **Authentication & Security:** JWT, Role-based access control  
- **Other:** Swagger / OpenAPI (if used), request validation, clean architecture  

---

## ✅ Features

- Product management: CRUD operations for products, categories, images  
- Shopping cart: Add/remove items, quantity management  
- Order processing: Checkout, order history, status updates  
- User system: Signup, login, role-based permissions (admin vs customer)  
- Backend APIs: RESTful endpoints for frontend consumption  
- Security: Token-based authentication (JWT) and permission checks  
- Modular code structure: separation of concerns between models, views, serializers  
- Docker setup: easy local development and deployment (if Docker files included)  


````markdown
## 🛠 Installation & Running Locally

1. Clone the repository:  
   ```bash
   git clone https://github.com/bomberman2099/django_multiShop_project.git
   cd django_multiShop_project
````

2. Create & activate a virtual environment (recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure database settings in `settings.py` for **MySQL** or **PostgreSQL**. Update your username, password, and database name accordingly.

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

> If Docker is set up in this project, you can alternatively run:
>
> ```bash
> docker-compose up
> ```
>
> This will build the containers and start the application automatically.

```


