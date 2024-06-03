# Aggregator
Сервис для отправки данных во внешнее хранилище.

#№ Описание проекта
Сервис выполняет следующие функции:
- Забирает события из шины данных VaBus
- Отправляет свои метрики в шину данных VaBus
- Группирует события по названию и временному инетрвалу и агрегирует по заданной функции
- Агрегированные события отправляются в хранилище (kafka или postgres)

## Структура проекта
```
/aggregator
    /app
        __init__.py
        aggregator.py
        metrics.py
        storage.py
        vabus.py
        main.py
    /tests
        __init__.py
        test_aggregator.py
        test_metrics.py
        test_storage.py
        test_vabus.py
    Dockerfile
    pyproject.toml
    README.md
```
