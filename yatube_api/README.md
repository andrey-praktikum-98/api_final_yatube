# Api_yatube
Api для просмотра/создание/редактирование постов, групп
Поддержка авторизации с возможностью редактирование записей и для анонимов просмотр записей
# Установка
Для установки Api_yatube, требуется:
1. клонировать репозиторий командой 
```git clone git@github.com:andrey-praktikum-98/api_yatube.git```
5. установить виртуальное окружение
`python3 -m venv venv`
Подробная инструкция: [Документация env](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments).
6. Активировать виртуальное окружение
`source venv/Scripts/activate`
7. Установка пакетов из requirements.txt
`python -m pip install -r requirements.txt`
Подробная инструкция: [Документация freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/#examples).
8. Загрузить пакеты в файл requirements.txt
`python -m pip freeze > requirements.txt`
9. Обновить миграции 
`python manage.py makemigrations`
`python manage.py migrate`
9. запустить проект ```python manage.py runserver```
# Примеры запросов и ответов
# Запрос на создание записи (POST)
``` http://127.0.0.1:8000/api/v1/posts/  ```
# Body
``` 
{
    "title": "Пост отредактированный 2",
    "author": "leo",
    "text":"новое описание 332"
} 
```
# Ответ
```
{
    "id": 3,
    "author": "admin",
    "group": null,
    "text": "новое описание 332",
    "pub_date": "2022-06-21T17:37:14.065330Z",
    "image": null
}
```
# Автор
Автор проекта: andrey-praktikum-98
