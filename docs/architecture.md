# Architecture

This document explains how the project is organised and where it's heading.

## Overview

The project separates global configuration from application-specific business logic.

```text
                    Django/DRF Boilerplate
                              │
               ┌──────────────┴──────────────┐
               │                             │
            config/                        apps/
               │                             │
      Project configuration            Application logic
               │                             │
      ┌────────┼────────┐                  users/
      │        │        │
   base.py   dev.py   prod.py
```

## `config/`

Project-wide configuration:

- Django settings (see [configuration.md](configuration.md))
- Root URL configuration
- ASGI and WSGI entry points

## `apps/`

The Django applications and their business logic. The boilerplate starts with a single `users` app containing the custom user model, its manager, serializers, views, and tests.

Add more apps as your project needs them:

```text
apps/
├── users/
├── payments/
├── orders/
└── products/
```

Each app should keep its own models, serializers, views, URLs, and tests.

### Adding a new app

```bash
mkdir apps/products
python manage.py startapp products apps/products
```

Then add it to `INSTALLED_APPS` in `config/settings/base.py`. Make sure the app's `name` in `apps.py` is `apps.products`.

## Why this structure?

- **Settings are layered**, so development and production never share risky defaults like `DEBUG=True`.
- **Apps live under `apps/`**, which keeps the project root uncluttered as the number of apps grows.
- **Configuration is separate from logic**, so changing how the project is deployed doesn't touch business code.

## Target structure

This is the structure the project is working towards. Items not yet in the repository (Docker files, CI workflow, top-level `tests/`) are tracked in the [roadmap](roadmap.md) and in GitHub issues.

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
├── docker/
│   └── ...
│
├── docs/
│
├── tests/
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── pyproject.toml
├── pytest.ini
├── README.md
└── requirements.txt
```

This target may change as the project develops and better approaches are found. If you have thoughts on it, open an issue.
