# Configuration

This document covers environment variables and how settings are organised.
Note some details are subject to change as the project is still in development.

## Settings layout

```text
config/settings/
├── base.py
├── development.py
└── production.py
```

Both `development.py` and `production.py` inherit from `base.py`:

```text
development.py          production.py
       │                      │
       ▼                      ▼
              base.py
```

### `base.py`

Settings shared across all environments:

- Installed apps and middleware
- Database configuration
- Django REST Framework configuration
- Custom user model
- Static files
- Internationalization

### `development.py`

Settings for local development:

- `DEBUG = True`
- Local allowed hosts
- Development email backend
- Development-only tools

### `production.py`

Settings for deployment:

- `DEBUG = False`
- Production allowed hosts
- Security settings
- Production email and database configuration

## Choosing a settings module

Django picks the settings module from the `DJANGO_SETTINGS_MODULE` environment variable. Make sure it points at the module you want, for example:

```bash
export DJANGO_SETTINGS_MODULE=config.settings.development
```

Check `manage.py`, `config/asgi.py`, `config/wsgi.py`, and `pytest.ini` to see which default each one uses, and adjust them if you want a different default.

## Environment variables

Environment-specific values live in a `.env` file. `.env.example` is committed as a template so developers know which variables are required. **Never commit `.env`.**

Create yours from the template:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### Variables

| Variable | Description | Example |
| --- | --- | --- |
| `POSTGRES_DB` | Database name. | `your_database` |
| `POSTGRES_USER` | Database user. | `your_user` |
| `POSTGRES_PASSWORD` | Database password. | `your_password` |
| `POSTGRES_HOST` | Database host. | `localhost` |
| `POSTGRES_PORT` | Database port. | `5432` |

### Example `.env`

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

## Adding a new variable

1. Add it to `.env.example` with a safe placeholder value.
2. Read it in the relevant settings file.
3. Add it to the table above.
