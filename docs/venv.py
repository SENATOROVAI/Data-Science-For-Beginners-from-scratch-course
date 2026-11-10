"""Learning log: виртуальное окружение."""

# Что делает python -m venv venv?
# Создаёт папку venv с копией (или ссылкой) на интерпретатор Python,
# собственным site-packages и скриптами активации.
# Активация: source venv/bin/activate (Linux/macOS),
# venv\Scripts\activate (Windows).
# - pip list — список пакетов
# - pip freeze > requirements.txt — сохраняет список пакетов в файл
# - pip install -r requirements.txt — установка пакетов с файла
# - conda env list — список окружений
# - conda create -n env_name python=3.12 — создание вирт окр
# - conda env update -n env_name -f file.yml — обновление пакетов с файла
# - conda activate env_name — активирует вирт окр
# - conda deactivate — деактивация вирт окр
# - conda clean -a — очистка

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# pip install пакет = установка пакета в venv
# conda install пакет = установка в conda

# pip freeze > requirements.txt = загрузить пакеты в файл
# conda env export > environment.yml = тоже самое в конде

# pip install -r = скачать пакеты из файла requirements
# conda env create -f = тоже в конде из environment

# pip list = список пакетов
# pip show = информация о пакете ее версия и тд
# conda list = список пакетов в conda

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# Где по умолчанию больше пакетов, в venv или в conda, и почему DS
# используют conda?
# В новом venv лежит только pip (с Python 3.12 setuptools в venv уже
# не ставится), а numpy и pandas есть в дистрибутиве Anaconda, но не в
# только что созданном conda-окружении. DS любят conda, потому что она
# сама ставит готовые бинарные пакеты, в том числе не-Python библиотеки.

# ![image.png](attachment:image.png)

# Зачем нужно виртуальное окружение?
# Оно изолирует зависимости и версии Python между проектами, поэтому
# нет конфликтов, а результат воспроизводим: окружение можно пересоздать
# из requirements.txt или environment.yml.
