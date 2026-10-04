# Contributing

Thanks for your interest in improving this boilerplate. This project is built in the open, and contributions of all sizes are welcome, from typo fixes to new features.

## Have something you want to work on?

**Open an issue first.** That applies to anything beyond a small fix, including items already on the [roadmap](docs/roadmap.md). A quick discussion up front avoids duplicated work and makes sure the change fits the direction of the project.

When opening an issue, please share:

- **What** you'd like to add, change, or fix
- **Why** it would be useful
- **How** you think it could work (a rough idea is fine)

Not every suggestion will end up in the boilerplate. The goal is to keep the project useful, maintainable, and focused.

## Finding something to work on

- Browse the open issues.
- Look for labels like `good first issue` and `help wanted`.
- Check the [roadmap](docs/roadmap.md) for planned features, then comment on the related issue to say you'd like to take it.

## Workflow

```text
Find or open an issue
        │
        ▼
Discuss the approach
        │
        ▼
Fork the repository
        │
        ▼
Create a branch
        │
        ▼
Make changes + write tests
        │
        ▼
Run checks
        │
        ▼
Open a pull request
```

### 1. Fork and clone

```bash
git clone <your-fork-url>
cd sassiwa-django-api-boilerplate
```

### 2. Set up your environment

Follow the Quick Start in the [README](README.md), then install the pre-commit hooks:

```bash
pre-commit install
```

### 3. Create a branch

```bash
git checkout -b your-branch-name
```

Use a short, descriptive name, for example `feature/jwt-auth` or `fix/user-manager-email`.

### 4. Make your changes

- Keep changes focused. One pull request should do one thing.
- Add or update tests for any behaviour you change.
- Update the docs if your change affects setup, configuration, or structure.

### 5. Run the checks

```bash
pytest
pre-commit run --all-files
```

Both must pass before you open a pull request.

### 6. Open a pull request

- Link the issue it relates to (for example, `Closes #12`).
- Describe what changed and why.
- Note anything you'd like reviewers to look at closely.

## Code style

Formatting and linting are handled by [Ruff](https://docs.astral.sh/ruff/) through pre-commit. If the hooks pass, your formatting is fine.

## Questions

If you're unsure about anything, open an issue and ask. Questions are welcome.
