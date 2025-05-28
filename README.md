# Bank Webhook Service

## Описание

Django-сервис, обрабатывающий webhook-и от банка:

- сохраняет уникальные платежи
- обновляет баланс организации по ИНН
- предотвращает дублирование операций
- предоставляет API для просмотра баланса

## Запуск

```
docker-compose up
```

## Миграции

```
docker exec -it django-web-1 sh
```

стартовые уже есть(опционально):

```
python manage.py makemigrations
```

применить миграции:

```
python manage.py migrate
```

## API-документация (Swagger & ReDoc)

В проекте используется drf-yasg для автогенерации документации API.

Swagger UI
📎 http://localhost:8000/swagger/

ReDoc UI
📎 http://localhost:8000/redoc/
