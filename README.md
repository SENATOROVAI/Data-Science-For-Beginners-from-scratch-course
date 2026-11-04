# Data Science For Beginners: курс с нуля

[![CI](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Практический курс по Data Science для начинающих: git, Python, GitHub и
работа с открытым кодом. Домашние задания оформляются как pull request в
этот репозиторий.

## Задания

| Задание | Issue | Файлы | Статус |
| --- | --- | --- | --- |
| Open Source: тест и анализ проекта | [intro-cs#8](https://github.com/SENATOROVAI/intro-cs/issues/8) | `docs/github/quiz.ipynb`, `docs/github/quiz.py`, `docs/github/opensource.ipynb`, `docs/github/opensource.py` | Готово |

## Быстрый старт

```bash
git clone https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course.git
cd Data-Science-For-Beginners-from-scratch-course
python -m venv .venv
source .venv/bin/activate
pip install pre-commit
pre-commit install
```

## Структура репозитория

```text
.
├── .github/      # шаблон pull request, workflow pre-commit
├── docs/
│   ├── git/      # материалы по git
│   └── github/   # тест и анализ open source проекта
├── projects/     # практические проекты
├── scripts/      # вспомогательные скрипты
└── tests/        # тесты
```

## Стандарты кода

Проверки запускает [pre-commit](https://pre-commit.com/): форматирование
(black, isort), линтеры (flake8, pylint, mypy, pydocstyle), проверка
орфографии (codespell) и синхронизация `.ipynb` с `.py` (jupytext).
Запуск вручную: `pre-commit run --all-files`. Максимальная длина строки
— 79 символов, сообщения коммитов — по
[Conventional Commits](https://www.conventionalcommits.org/ru/).

## Участие в проекте

Правила описаны в [CONTRIBUTING.md](CONTRIBUTING.md), нормы общения — в
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), сообщения об уязвимостях — в
[SECURITY.md](SECURITY.md). Ветка называется `task/<номер-issue>-<кратко>`,
в описании pull request указывается `Closes <ссылка на issue>`. Список
участников и благодарности: [AUTHORS.md](AUTHORS.md), история изменений:
[CHANGELOG.md](CHANGELOG.md).

## Лицензия

[MIT](LICENSE)
