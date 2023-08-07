Описание проекта:
Блог шеф-повара с рецептами

Инструменты разработки
Стек:

Питон >= 3.9
Джанго == 4.2.4

sqlite3
Разработка
1) Поставить звездочку)
2) Клонировать репозиторий
git clone https://github.com/DJWOMS/cook_blog.git
3) Создать окружающее окружение
cd cook_blog

python -m venv venv
4) Активировать окружающее окружение
линукс

source venv/bin/activate
Окна

./venv/Scripts/activate
5) Установить зависимости:
pip install -r req.txt
6) Выполнить команду для выполнения комиссии
python manage.py migrate
8) Создать суперпользователя
python manage.py createsuperuser
9) Запустить сервер
python manage.py runserver
