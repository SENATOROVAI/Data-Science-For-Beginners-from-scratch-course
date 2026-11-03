
# Data Science For Beginners

[![Python](https://img.shields.io/badge/Python-3-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<!-- Добавить бейдж CI для реально существующего workflow -->

Практические материалы по Python, математике, анализу данных и машинному обучению.

## Задания

| Тема | Материалы |
| --- | --- |
| GitHub и Open Source | [Задания](docs/github/) |

## Быстрый старт

```bash
git clone https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course.git
cd Data-Science-For-Beginners-from-scratch-course
python -m venv .venv
source .venv/bin/activate
python -m pip install pre-commit
pre-commit install
```

## Структура репозитория

```text
.
├── .github/
├── docs/
│   └── github/
│       ├── images/
│       ├── opensource.ipynb
│       ├── opensource.py
│       ├── quiz.ipynb
│       └── quiz.py
├── projects/
├── scripts/
├── tests/
├── AUTHORS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

## Стандарты кода

- Соблюдайте PEP 8 для Python.
- Используйте Conventional Commits.
- Запускайте pre-commit перед отправкой изменений.
- Синхронизируйте файлы .py и .ipynb.
- Не добавляйте секреты и временные файлы.

## Участие в проекте

Порядок внесения изменений описан в [CONTRIBUTING.md](CONTRIBUTING.md).

Правила поведения приведены в [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Информация об авторах находится в [AUTHORS.md](AUTHORS.md).

## Лицензия

Проект распространяется на условиях [MIT License](LICENSE).