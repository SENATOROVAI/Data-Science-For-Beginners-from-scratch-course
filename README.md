# Data Science For Beginners

[![Python](https://img.shields.io/badge/Python-3-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml)

Практические материалы по Python, математике, анализу данных и машинному обучению.

## Задания

| Задание | Issue | Файлы | Статус |
| --- | --- | --- | --- |
| GitHub и Open Source | [intro-cs#8](https://github.com/SENATOROVAI/intro-cs/issues/8) | [Материалы](docs/github/) | Выполнено, на ревью |

## Быстрый старт

```bash
git clone https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course.git
cd Data-Science-For-Beginners-from-scratch-course
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pre-commit
pre-commit install
```

## Структура репозитория

```text
.
├── .github/
│   └── workflows/
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

- Соблюдайте PEP 8 при написании кода на Python.
- Используйте Conventional Commits для сообщений коммитов.
- Проверяйте изменения с помощью `pre-commit`.
- Поддерживайте согласованность ответов в `.py` и `.ipynb`.
- Не добавляйте секреты, кэши и временные файлы.

## Участие в проекте

- [CONTRIBUTING.md](CONTRIBUTING.md) — как предлагать изменения.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — правила поведения.
- [SECURITY.md](SECURITY.md) — сообщения об уязвимостях.
- [AUTHORS.md](AUTHORS.md) — авторы и участники.
- [CHANGELOG.md](CHANGELOG.md) — история изменений.

## Лицензия

Проект распространяется на условиях [MIT License](LICENSE).
История изменений приведена в [CHANGELOG.md](CHANGELOG.md),
а правила раскрытия уязвимостей — в [SECURITY.md](SECURITY.md).
