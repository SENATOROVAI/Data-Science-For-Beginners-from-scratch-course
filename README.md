# Data Science For Beginners — решения заданий

[![CI](https://github.com/Dalvedo/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/Dalvedo/Data-Science-For-Beginners-from-scratch-course/actions/workflows/pre-commit.yaml)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Форк курса
[SENATOROVAI/Data-Science-For-Beginners-from-scratch-course](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-course)
с моими решениями заданий из [SENATOROVAI/intro-cs](https://github.com/SENATOROVAI/intro-cs).
Каналы курса: https://t.me/RuslanSenatorov, https://t.me/SENATOROVAI

## Задания

| Задание | Issue | Файлы | Статус |
|---|---|---|---|
| Первый вклад в Open Source | [intro-cs#8](https://github.com/SENATOROVAI/intro-cs/issues/8) | [`docs/github/quiz`](docs/github/quiz.ipynb), [`docs/github/opensource`](docs/github/opensource.ipynb) | На ревью |

Вклад в open source по заданию #8 (проект
[Kaggle/kagglehub](https://github.com/Kaggle/kagglehub)):

- issue [Kaggle/kagglehub#324](https://github.com/Kaggle/kagglehub/issues/324);
- первое улучшение, исправления PEP8:
  [Kaggle/kagglehub#325](https://github.com/Kaggle/kagglehub/pull/325);
- второе улучшение, опечатки в документации:
  [Kaggle/kagglehub#326](https://github.com/Kaggle/kagglehub/pull/326);
- гарантированный вклад:
  [firstcontributions/first-contributions#129176](https://github.com/firstcontributions/first-contributions/pull/129176).

## Быстрый старт

```bash
git clone https://github.com/Dalvedo/Data-Science-For-Beginners-from-scratch-course.git
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
├── projects/
│   └── supervised_learning/
│       └── linear_regression/
├── scripts/          # служебные скрипты репозитория
└── tests/
    └── quiz/         # ответы на квизы
```

Полный список ноутбуков — в [DIRECTORY.md](DIRECTORY.md).

## Стандарты кода

- Каждый ноутбук `.ipynb` хранится в паре с файлом `.py`, их синхронизирует
  [jupytext](https://jupytext.readthedocs.io/).
- Перед коммитом запускаются хуки из `.pre-commit-config.yaml`: Ruff,
  docformatter, codespell, flake8, mypy, pylint и проверка заголовка коммита.
  В CI те же хуки запускаются на каждый push и pull request.
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
