class StorageClient:
    def __init__(self, storage_type: str):
        self.storage_type = storage_type

    async def send_to_storage(self, aggregated_results):
        """
        Здесь необходимо реализовать функцию отправки агрегированных результатов
        в зависимости от типа хранилища.
        """
        pass

