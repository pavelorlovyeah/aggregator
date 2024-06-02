import os
import asyncio

from service import Service

vabus_url = os.getenv("VABUS_URL")
storage_type = os.getenv("STORAGE_TYPE")
aggregation_interval = int(os.getenv("AGGREGATION_INTERVAL", 60))

service = Service(vabus_url, storage_type, aggregation_interval)

if __name__ == "__main__":
    asyncio.run(service.run())
