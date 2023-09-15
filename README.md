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

## Цель проекта

Выполнение тестового задания на вакансию Python-разработчик
