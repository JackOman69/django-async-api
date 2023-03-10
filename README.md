<h1 align="center">django-async-api</h1>

---
**Тестовое задание на вакансию Back-end Python Developer**

Данное приложение было создано для интегрирования с внешними учетными системами,
которые содержат данные работников спортивных залов.

**Полностью Асинхронное приложение с использованием httpx и drfasyncview**

**Особенности**:
* API Сервис для создания, изменения и удаления различных учетных систем
* /team/get_employees/{id} - Эталонный Асинхронный GET запрос по ID учетной системы для парсинга данных сотрудников
* Администрирование Django для изменения моделей учетных систем
---


---
## Инструментарий проекта:

* `Python 3.10.9`
* `Django 4.1`
* `Django Rest Framework`
* `DRF Writable Nested`
* `drfasyncview`
* `PyYaml`
* `HTTPX`
* `Whitenoise`
* `Uvicorn`
* `Dotenv`
---
## Установка

* В корневой папке проекта - `pip install -r requirements.txt`
* Создание `.env` файла в директории `django_task/` для хранение секретного ключа Django
* Внутри файла `.env` нужно создать переменную `SECRET_KEY = 'ВАШ_ТОКЕН_ПРОЕКТА'` 

---
## Использование

* После создания проекта и администратора запускаем сервер - `uvicorn --reload django_async.asgi:application`
* `/swagger-ui/` - Графическое представление API
* `/admin/` - Админ панель Django
* `/team/get_employees` - GET Запрос на все системы (Доступен - POST)
* `/team/get_employees/<id>` - GET Запрос на одну систему (Доступны - PUT, DELETE)
