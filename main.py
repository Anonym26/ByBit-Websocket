import logging
import time
from bybit_handler import BybitPublic, BybitPrivate
from logger import setup_logger
from dotenv import load_dotenv
import os

"""
Модуль запускает работу с WebSocket API Bybit, подписываясь на потоки публичных и приватных данных.
Используются классы из модуля bybit_handler для подключения к публичным и приватным каналам.
Логирование осуществляется через модуль logger. API-ключи загружаются из файла .env.
Основной цикл программы поддерживает подключение и подписки на данные в реальном времени.
"""

# Настройка логирование
setup_logger()

# Загрузка API-ключей из файла .env
load_dotenv()
BYBIT_API_KEY_TEST = os.getenv("BYBIT_API_KEY_TEST")
BYBIT_API_SECRET_TEST = os.getenv("BYBIT_API_SECRET_TEST")

# Создание экземпляров классов для публичного и приватного подключения
public_ws = BybitPublic()
private_ws = BybitPrivate(api_key=BYBIT_API_KEY_TEST, api_secret=BYBIT_API_SECRET_TEST)

# Подписка на поток ордербука
# public_ws.subscribe_orderbook("BTCUSDT", public_ws.handle_orderbook)

# Подписка на поток данных о позиции
private_ws.subscribe_position(private_ws.handle_position)

# Подписка на поток данных о кошельке
private_ws.subscribe_wallet(private_ws.handle_message)

if __name__ == "__main__":
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Работа программы завершена вручную.")
