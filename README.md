# Data Science For Beginners — решения заданий

[![CI](https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Форк курса
[SENATOROVAI/Data-Science-For-Beginners-from-scratch-course](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course)
с решениями заданий из [SENATOROVAI/intro-cs](https://github.com/SENATOROVAI/intro-cs).
Каналы курса: https://t.me/RuslanSenatorov, https://t.me/SENATOROVAI

## Задания

| Задание | Issue | Файлы | Статус |
|---|---|---|---|
| Первый вклад в Open Source | [intro-cs#8](https://github.com/SENATOROVAI/intro-cs/issues/8) | [`docs/github/quiz`](docs/github/quiz.ipynb), [`docs/github/opensource`](docs/github/opensource.ipynb) | На ревью |

Вклад в open source по заданию #8 (проект
[catboost/catboost](https://github.com/catboost/catboost)):

- issue [catboost/catboost#3239](https://github.com/catboost/catboost/issues/3239);
- первое улучшение, исправления PEP8:
  [catboost/catboost#3240](https://github.com/catboost/catboost/pull/3240);
- второе улучшение, опечатки в документации:
  [catboost/catboost#3241](https://github.com/catboost/catboost/pull/3241);
- гарантированный вклад:
  [firstcontributions/first-contributions#127656](https://github.com/firstcontributions/first-contributions/pull/127656).

## Быстрый старт

```bash
git clone https://github.com/nysib/Data-Science-For-Beginners-from-scratch-course.git
cd Data-Science-For-Beginners-from-scratch-course
python -m venv .venv
source .venv/bin/activate
pip install pre-commit jupytext
pre-commit install
pre-commit run --all-files
```

## Структура репозитория

```text
.
├── .github/          # шаблоны issue и pull request, workflow pre-commit
├── docs/
│   ├── git/          # материалы по Git
│   └── github/       # задание intro-cs#8: тест по GitHub и анализ проекта
│       └── images/   # скриншоты к ответам
├── projects/
│   └── supervised_learning/
│       └── linear_regression/
├── scripts/          # служебные скрипты репозитория
└── tests/
    └── quiz/
```

## Стандарты кода

- Каждый ноутбук `.ipynb` хранится в паре с файлом `.py`, их синхронизирует
  [jupytext](https://jupytext.readthedocs.io/).
- Перед коммитом запускаются хуки из `.pre-commit-config.yaml`: black, isort,
  flake8, mypy, pylint, pydocstyle, codespell и другие. В CI те же хуки
  запускаются на каждый push и pull request.
- Коммиты оформляются по
  [Conventional Commits](https://www.conventionalcommits.org/ru/v1.0.0/),
  один коммит — один файл или пара `.ipynb` + `.py`.
- Одна ветка — одно задание — один issue.

## Участие в проекте

Порядок работы описан в [CONTRIBUTING.md](CONTRIBUTING.md), правила общения —
в [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), сообщения об уязвимостях — в
[SECURITY.md](SECURITY.md). Авторы и благодарности — в
[AUTHORS.md](AUTHORS.md), история изменений — в [CHANGELOG.md](CHANGELOG.md).

## Лицензия

Проект распространяется под лицензией MIT, см. [LICENSE](LICENSE).
