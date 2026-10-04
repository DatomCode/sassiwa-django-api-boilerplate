# Django/DRF Boilerplate

A reusable Django and Django REST Framework boilerplate that gives you a clean, consistent foundation for building APIs, so you can skip the repetitive setup and get straight to your features.

> 🚧 **Under active development.** The structure and features are evolving. See the [roadmap](docs/roadmap.md) and open issues for what's planned.

## Features

Currently implemented:

- Django and Django REST Framework
- Custom user model with an email-based authentication foundation
- PostgreSQL configuration
- Environment-based configuration with `.env.example`
- Separate development and production settings
- Pytest and pytest-django, with model tests
- Pre-commit hooks
- Ruff for linting and formatting

Planned (not yet implemented): Docker and Docker Compose, GitHub Actions CI, JWT authentication, Redis, Celery, API documentation, caching, rate limiting, and production deployment configuration.

## Quick Start

```bash
# 1. Clone and enter the project
git clone <repository-url>
cd django-boilerplate

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env            # Windows PowerShell: Copy-Item .env.example .env
# then edit .env with your values

# 5. Migrate and run
python manage.py migrate
python manage.py runserver
```

Run the tests:

```bash
pytest
```

Set up pre-commit:

```bash
pre-commit install
pre-commit run --all-files
```

## Project Structure

This is what exists in the repository today:

```text
django-boilerplate/
│
├── apps/
│   └── users/
│       ├── migrations/
│       │   └── __init__.py
│       ├── tests/
│       │   ├── __init__.py
│       │   └── test_models.py
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── manager.py
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
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── manage.py
├── pyproject.toml
├── pytest.ini
├── README.md
└── requirements.txt
```

The structure the project is working towards (Docker, CI, and more) is described in [docs/architecture.md](docs/architecture.md).

## Documentation

Detailed documentation lives in the [`docs/`](docs/) directory:

- [Architecture](docs/architecture.md): how the project is organised, and the target structure
- [Configuration](docs/configuration.md): environment variables and settings
- [Roadmap](docs/roadmap.md): what's done, in progress, and planned

## Contributing

Contributions are welcome. If you want to work on something, whether it's on the roadmap or your own idea, **please open an issue first** so the approach can be discussed before you start.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full process.

## Philosophy

This boilerplate is intentionally simple. It isn't trying to include every Django package or architecture pattern, just a solid, reliable starting point for a Django/DRF API. Project-specific functionality should be added only when it has a clear benefit.

## License

This project is open source and available under the terms of the license included in this repository.
