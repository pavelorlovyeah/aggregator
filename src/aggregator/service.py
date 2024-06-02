import asyncio
from loguru import logger

from aggregator import Aggregator
from metrics import Metrics
from storage import StorageClient
from vabus import VaBus

class Service:
    def __init__(self, vabus_url: str, storage_type: str, aggregation_interval: int):
        self.vabus = VaBus(vabus_url)
        self.storage_client = StorageClient(storage_type)
        self.aggregator = Aggregator(aggregation_interval)
        self.metric = Metrics()

    async def run(self):
        async with self.vabus:
            while True:
                try:
                    # Получение события
                    event = await self.vabus.get_event()
                    # Добавление события в список
                    await self.aggregator.add_event(event)
                    # Агрегация событий и результат агрегации
                    await self.aggregator.aggregate_events()
                    aggregated_results = self.aggregator.aggregated_results
                    # Отправка агрегированных результатов в хранилище
                    await self.storage_client.send_to_storage(aggregated_results)
                    # Метрика для отправки в сервис
                    metric = self.metric.metric_calculation()
                    # Отправление метрики в сервис
                    await self.vabus.send_metric(metric)
                except Exception as e:
                    # Логгирование ошибки
                    logger.exception(e)
                finally:
                    await asyncio.sleep(1)
