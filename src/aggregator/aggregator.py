import asyncio
from collections import defaultdict

from vabus import Event

class Aggregator:
    def __init__(self, aggregation_interval: int):
        self.aggregation_interval = aggregation_interval
        self.events = defaultdict(list)
        self.aggregated_results = None

    async def add_event(self, event: Event):
        self.events[event.name].append(event)

    async def aggregate_events(self):
        await asyncio.sleep(self.aggregation_interval)
        self.aggregated_results = self._aggregate(self.events)
        self.events.clear()

    def _aggregate(self, events: dict):
        """
        Здесь должна быть реализована функция группировки событий по имени и
        агрегации по (sum, avg, min, max).
        Результат функции- агрегированные данные, которые необходимо отправить в хранилище.
        """
        pass

