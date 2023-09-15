# Сервис "Конвертер валют" (тестовое задание)

API-сервис быстрого перевода одной валюты в другую  

Данные берутся с внешнего сервиса [https://exchangerate.host], документация [https://exchangerate.host/#/docs]

## Как установить

Python 3 должен быть установлен.

* Скачать проект (git clone)
* Создать виртуальное окружение.

```bash
python -m venv venv
```

* Установить зависимости.

```bash
pip install -r requirements.txt
```

## Запуск проекта

```bash
uvicorn main:app
```

### Доступные endpoints

GET /api/rates

GET /api/symbols

Подробная информация в документации [OpenAPI]('http://127.0.0.1:8000/docs') или [Redoc]('http://127.0.0.1:8000/redoc')

## Запуск проекта в контейнере

```bash
docker compose build
docker compose up
```

тестовый сервис можно посмотреть на [kruser.site]('https://kruser.site')

Примеры запросов:

```bash
- документация API
http://127.0.0.1:8000/docs

- альтернативная документация
http://127.0.0.1:8000/redoc

- доступные символы валют
http://127.0.0.1:8000/api/symbols

- по умолчанию конвертация USD -> RUB value=1
http://127.0.0.1:8000/api/rates

- по умолчанию value=1
http://127.0.0.1:8000/api/rates?&from=EUR&to=RUB

http://127.0.0.1:8000/api/rates?&from=EUR&to=RUB&value=100
```

## Цель проекта

Выполнение тестового задания на вакансию Python-разработчик
