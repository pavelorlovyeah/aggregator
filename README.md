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

# Дополнительное задание
## Возможные проблемы в сервисе
1. Проблемы с производительностью (большое количество ивентов).
    -  Решение:
        - Оптимизация методов асинхронного программирования.
        - Кеширование часто заправшиваемых данных.
        - Оптимизация алгоритмов агрегации.
2. Проблемы с надежностью (сбои в работе VaBus, Kafka, PostreSQL).
    -  Решение:
        - Использование повторных попыток и таймаутов.
        - Использование очередей для буферизации событий.
        - Мониторинг и оповещение при обнаружении проблем.
3. Проблемы с целостностью данных (потеря и дублирование событий).
    -  Решение:
        - Использование уникальных идентификаторов для событий и метрик.
        - Ведение логирования всех операций.
        - Использование транзакций при записи в базу данных.
        - Ведение бэкапов.
4. Проблемы с безопасностью.
    -  Решение:
        - Использование шифрования данных при передаче и хранении.
        - Ограничение доступа к сервису с использованием аутентификации и авторизации.

## Потенциальное развитие сервиса
1. Расширение функциональности:
    - Добавление новых функций агрегации и метрик.
2. Интеграция с другими системами:
   - Поддержка работы с другими типами шин данных и хранилищ.
3. Улучшение пользовательского интерфейса:
   - Разработка веб-интерфейса для мониторинга и управления сервисом.
   - Использование дашбордов для визуализации метрик и агрегированных данных.
4. Повышение устойчивости и отказоустойчивости:
   - Использование распределенных систем для хранения и обработки данных.
   - Использование механизмов автоматического восстановления после сбоев.
5. Настроить CI/CD
