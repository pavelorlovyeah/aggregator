# Aggregator
Сервис для отправки данных во внешнее хранилище.

## Описание проекта
Сервис выполняет следующие функции:
- Забирает события из шины данных VaBus
- Отправляет свои метрики в шину данных VaBus
- Группирует события по названию и временному инетрвалу и агрегирует по заданной функции
- Агрегированные события отправляются в хранилище (kafka или postgres)

## Структура проекта
```
/aggregator
    /src
        /aggregator
            __init__.py
            aggregator.py
            main.py
            metrics.py
            service.py
            storage.py
            vabus.py
        /tests
            test_aggregator.py
            test_metrics.py
            test_storage.py
            test_vabus.py
Dockerfile
pyproject.toml
README.md
```

## Установка

### Клонирование репозитория
```bash
git clone https://github.com/pavelorlovyeah/aggregator.git
cd aggregator
```
