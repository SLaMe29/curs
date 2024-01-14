
### Инструменты разработки

**Стек:**

- Python >= 3.9
- Django == 3.2.4
- sqlite3

##### 3) Создать виртуальное окружение

    python -m venv venv

##### 4) Активировать виртуальное окружение

Linux

    source venv/bin/activate

Windows

    ./venv/Scripts/activate

##### 5) Устанавливить зависимости

    pip install -r req.txt

##### 6) Выполнить команду для выполнения миграций

    python manage.py migrate

##### 8) Создать суперпользователя

    python manage.py createsuperuser

##### 9) Запустить сервер

    python manage.py runserver

##### 10) Ссылки

- Сайт <http://127.0.0.1:8000/>

- Админ панель <http://127.0.0.1:8000/admin>
