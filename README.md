# Data Science For Beginners

[![CI](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Курс и практические материалы для изучения Data Science с нуля: Python, Git
и GitHub, математика и машинное обучение. Сайт курса:
[SenatorovAI.com](https://SenatorovAI.com).

## Задания

| Задание | Issue | Файлы | Статус |
| --- | --- | --- | --- |
| Контрибьютинг в Open Source | [intro-cs#8](https://github.com/SENATOROVAI/intro-cs/issues/8) | [docs/github/quiz.ipynb](docs/github/quiz.ipynb), [docs/github/opensource.ipynb](docs/github/opensource.ipynb) | На ревью |

## Быстрый старт

```bash
git clone https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course.git
cd Data-Science-For-Beginners-from-scratch-course
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install pre-commit jupytext
pre-commit install
```

## Структура репозитория

```text
.
├── .github/
│   └── workflows/          # CI: проверка pre-commit
├── docs/
│   ├── git/                # задания по Git
│   └── github/             # задания по GitHub и open source
├── projects/
│   └── supervised_learning/
│       └── linear_regression/
├── scripts/                # служебные скрипты
├── tests/
│   └── quiz/
├── AUTHORS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

## Стандарты кода

- Каждому ноутбуку `.ipynb` соответствует парный файл `.py` (jupytext).
- Код и ноутбуки проверяются хуками pre-commit: black, isort, flake8, pylint,
  mypy, pydocstyle, codespell. Запуск вручную: `pre-commit run --all-files`.
- Стиль кода — PEP 8, у каждого модуля есть docstring.
- Сообщения коммитов — по [Conventional Commits](https://www.conventionalcommits.org/ru/v1.0.0/),
  один коммит — один файл (или пара `.ipynb` + `.py`).
- Ветки называются `task/<номер-issue>-<кратко>`.

## Участие в проекте

Порядок отправки изменений описан в [CONTRIBUTING.md](CONTRIBUTING.md), правила
общения — в [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). О найденных уязвимостях
сообщайте по правилам из [SECURITY.md](SECURITY.md). Авторы и благодарности
участникам — в [AUTHORS.md](AUTHORS.md), история изменений — в
[CHANGELOG.md](CHANGELOG.md).

## Лицензия

Проект распространяется по лицензии MIT, текст — в файле [LICENSE](LICENSE).
