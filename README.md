# Django/DRF Boilerplate

A reusable Django and Django REST Framework boilerplate designed to provide a clean, consistent foundation for building APIs.

The goal is to handle the repetitive project setup so you can focus on building the actual features and business logic of your application.

## Features

* Django
* Django REST Framework
* Custom User Model
* Email-based authentication foundation
* PostgreSQL
* Environment-based configuration
* Separate development and production settings
* Docker and Docker Compose
* Pytest testing setup
* Pre-commit hooks
* Code quality checks
* GitHub Actions CI
* Structured project layout
* `.env.example` configuration template

## Project Structure

```text
django-boilerplate/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── apps/
│   └── users/
│       ├── migrations/
│       │   └── __init__.py
│       │
│       ├── tests/
│       │   ├── __init__.py
│       │   └── test_models.py
│       │
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
│
├── config/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   │
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
│
├── tests/
│   └── __init__.py
│
├── docker/
│   └── ...
│
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Architecture

The project separates global configuration from application-specific business logic.

```text
                    Django/DRF Boilerplate
                             │
              ┌──────────────┴──────────────┐
              │                             │
           config/                        apps/
              │                             │
      Project configuration          Application logic
              │                             │
      ┌───────┼────────┐                  users/
      │       │        │
   base.py  dev.py  prod.py
```

### `config/`

Contains project-wide configuration such as:

* Django settings
* URL configuration
* ASGI configuration
* WSGI configuration

### `apps/`

Contains the actual Django applications and business logic.

The boilerplate starts with a `users` application. Additional applications can be added depending on the project.

For example:

```text
apps/
├── users/
├── payments/
├── orders/
└── products/
```

## Settings

The settings are separated into three layers:

```text
config/settings/
├── base.py
├── development.py
└── production.py
```

### `base.py`

Contains settings shared across environments.

Examples:

* Installed applications
* Middleware
* Database configuration
* Django REST Framework configuration
* Custom user model
* Static files
* Internationalization

### `development.py`

Contains settings specific to local development.

Examples:

* `DEBUG=True`
* Local hosts
* Development email backend
* Development-specific tools

### `production.py`

Contains settings specific to deployment.

Examples:

* `DEBUG=False`
* Production hosts
* Security settings
* Production email configuration
* Production-specific configuration

Both environment-specific files inherit from `base.py`.

```text
development.py
       │
       ▼
    base.py

production.py
       │
       ▼
    base.py
```

## Environment Variables

Create a `.env` file using `.env.example` as a template.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

POSTGRES_DB=your_database
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

ALLOWED_HOSTS=localhost,127.0.0.1
```

Do not commit your `.env` file to version control.

The `.env.example` file should be committed so other developers know which environment variables are required.

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd django-boilerplate
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Update the values in `.env`.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Running with Docker

Build and start the services:

```bash
docker compose up --build
```

To run the containers in the background:

```bash
docker compose up -d
```

Stop the services:

```bash
docker compose down
```

The Docker setup is intended to provide a consistent development environment for Django and PostgreSQL.

## Testing

Tests are written using `pytest` and `pytest-django`.

Run the test suite:

```bash
pytest
```

Run a specific test file:

```bash
pytest apps/users/tests/test_models.py
```

The test suite should cover important application behavior and help prevent regressions as the project grows.

## Pre-commit

Pre-commit runs automated checks before code is committed.

Install the hooks:

```bash
pre-commit install
```

Run all checks manually:

```bash
pre-commit run --all-files
```

The configured checks are intended to help maintain:

* Consistent formatting
* Clean imports
* Code quality
* Consistent project standards

## Continuous Integration

GitHub Actions is used for continuous integration.

The CI workflow runs automated checks when changes are pushed to GitHub or submitted through a pull request.

The general workflow is:

```text
Push / Pull Request
        │
        ▼
GitHub Actions
        │
        ├── Install dependencies
        ├── Run code-quality checks
        └── Run tests
                │
                ▼
             Result
```

A failing check should be resolved before merging the changes.

## Adding a New Application

Create new Django applications inside the `apps/` directory.

For example:

```bash
python manage.py startapp products apps/products
```

Your structure would become:

```text
apps/
├── users/
└── products/
```

Then add the application to `INSTALLED_APPS`.

For larger projects, each application should contain its own models, serializers, views, URLs, and tests.

## Development Workflow

A typical development workflow looks like:

```text
Create feature
      │
      ▼
Write code
      │
      ▼
Write tests
      │
      ▼
Run pytest
      │
      ▼
Run pre-commit
      │
      ▼
Commit changes
      │
      ▼
Push to GitHub
      │
      ▼
GitHub Actions
      │
      ▼
Tests + quality checks
```

## Philosophy

This boilerplate is intentionally kept simple.

The goal is not to include every possible Django package or architecture pattern.

Instead, it provides a solid foundation containing the common pieces needed when starting a Django/DRF API.

Project-specific functionality should be added only when the application actually needs it.

## Future Improvements

Potential additions for future versions include:

* JWT authentication
* Redis
* Celery
* API documentation
* Caching configuration
* Rate limiting
* Email services
* Object storage
* Production deployment configuration
* More comprehensive integration tests

These features are intentionally not part of the initial foundation.

## Contributing

Contributions, suggestions, and improvements are welcome.

If you find a bug or have an idea for improving the boilerplate, open an issue or submit a pull request.

## License

This project is open source and available under the terms of the license included in this repository.
