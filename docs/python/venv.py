"""Answers to the venv and conda quiz."""

# 1. Что делает команда python -m venv venv?
# - создает виртуальное окружение: папку venv в проекте с отдельным
#   интерпретатором Python и собственным набором пакетов
#
# 1.1 Что делает каждая команда в списке ниже?
# - pip list # выводит в терминал список пакетов, установленных в
#   текущем окружении
# - pip freeze > requirements.txt # экспортирует пакеты и их версии из
#   текущей venv в файл requirements.txt
# - pip install -r requirements.txt # устанавливает пакеты из
#   requirements.txt в активное окружение (venv или глобальный python)
#
# 2. Что делает каждая команда в списке ниже?
# - conda env list # выводит список conda-окружений (имена и пути),
#   а не список пакетов; пакеты показывает conda list
# - conda create -n env_name python=3.5 # создание нового окружения env_name и
#   установка в него python 3.5
# - conda env update -n env_name -f file.yml # обновление окружения по yml
#   файлу
# - conda activate env_name # активация окружения env_name
# - conda deactivate # выход из окружения conda
# - conda clean -a # очистка кэша conda и освобождение места на диске
#
# 3. вставьте скрин вашего терминала, где вы активировали сначала venv, потом
#    conda, назовите окружение "SENATOROV"
#
# ![Активация окружений](images/activate_venv_conda.png)
#
# 4. Как установить необходимые пакеты внутрь виртуального окружения для
#    conda/venv?
# - conda env update -f environment.yml
# - pip install -r requirements.txt
#
# 5. Что делают эти команды?
# pip freeze > requirements.txt # экспортирует все пакеты текущей venv
#   и их версии в файл requirements.txt пакетным менеджером pip
#
# conda env export > environment.yml # экспортирует все пакеты текущего
#   окружения Conda и их версии в файл environment.yml
#
# 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также
#     файлы зависимостей requirements.txt и environment.yml, файлы должны
#     содержать зависимости
#
# ![VENV](images/venv_screen.png)
#
# 6. Что делают эти команды?
# pip install -r requirements.txt # устанавливает пакеты из файла
#   requirements.txt в текущий venv при помощи pip.
#
# conda env create -f environment.yml # создает новое окружение (имя
#   берётся из поля name в environment.yml) и устанавливает в него
#   пакеты, перечисленные в environment.yml.
#
# 7. Что делают эти команды?
# pip list # выводит список библиотек, установленных pip в текущем окружении
# pip show # показывает сведения о конкретной библиотеке
# conda list # показывает все пакеты в Conda-окружении, установленные
#   через conda, а также установленные через pip.
#
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата
#    сайнинисты используют conda?
#
# - по умолчанию пакетов больше в conda. DS используют conda, ибо в ней
#   предустановлены основные библиотеки для исследований, такие как
#   numpy, pandas и 20+ др.
#
#
# 9. вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS
#    Code/cursor
# ![Interpreter](images/conda-interpreter.png)
#
# 10. добавьте в .gitignore папку SENATOROV
# ![gitignore-dir](images/adding-gitignore.png)
#
# 11. Зачем нужно виртуально окружение?
# - это изолированная среда Python, которая позволяет каждому проекту
#   использовать свою версию Python и свой набор библиотек без влияния
#   на глобальную систему и другие проекты.
#
# 12. С этого момента надо работать в виртуальном окружении conda, ты
#     научился(-ась) выгружать зависимости и работать с окружением?
# ДА!
#
# Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только
# conda
# - Анигилировал
