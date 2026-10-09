
# E-Commerce REST API — Django + DRF + PostgreSQL

Scalable REST API for e-commerce with JWT auth, cart & checkout logic.

**Stack:** Python, Django, Django REST Framework, PostgreSQL, SimpleJWT, Swagger

**Features**
- JWT Authentication (login, refresh, register)
- Product CRUD + filtering & search
- Cart management (add/remove, quantity)
- Optimized ORM — select_related / prefetch_related to avoid N+1
- Swagger docs at /api/docs/

**Quick Start**
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
