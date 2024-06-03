# Aggregator
Сервис для отправки данных во внешнее хранилище.

## Описание проекта
Сервис выполняет следующие функции:
- Забирает события из шины данных VaBus
- Отправляет свои метрики в шину данных VaBus
- Группирует события по названию и временному инетрвалу и агрегирует по заданной функции
- Агрегированные события отправляются в хранилище (`kafka` или `postgres`)

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

### Установка зависимостей
#### Используя `pip` и `setuptools`
```bash
pip install .
```

## Запуск
### Локально
Для запуска сервиса локально, выполните:
```bash
python src/aggregator/main.py
```

### С использованием Docker
Для запуска сервиса в Docker-контейнере, выполните следующие шаги:

1. **Сборка Docker-образа:**
   ```bash
   docker build -t aggregator .
   ```

2. **Запуск Docker-контейнера:**
   ```bash
   docker run -d -p 8000:8000 aggregator
   ```

## Тестирование
### Запуск тестов
Для запуска тестов используйте:
```bash
pytest
```

## Конфигурация
Сервис использует переменные окружения для конфигурации:
- `VABUS_URL`: URL шины данных VaBus
- `STORAGE_TYPE`: Тип хранилища для агрегированных данных (`kafka` или `postgres`)
- `AGGREGATION_INTERVAL`: Интервал времени для агрегации событий в секундах (по умолчанию 60 секунд)
### Пример конфигурации и запуска сервиса:
```bash
export VABUS_URL=http://localhost:8000
export STORAGE_TYPE=postgres
export AGGREGATION_INTERVAL=60

python src/aggregator/main.py
```

## Автор
Павел Орлов https://github.com/pavelorlovyeah

## Лицензия
MIT
