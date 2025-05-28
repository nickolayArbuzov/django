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

## API

### POST `/api/webhook/bank/`

Пример запроса:

```json
{
  "operation_id": "uuid",
  "amount": 1000,
  "payer_inn": "1234567890",
  "document_number": "PAY-001",
  "document_date": "2024-01-01T00:00:00Z"
}
```
