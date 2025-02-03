from pybit.unified_trading import WebSocket
import logging

"""
Модуль содержит классы для работы с WebSocket API Bybit.
BybitPublic - класс для подключения к публичным данным (например, ордербук).
BybitPrivate - класс для подключения к приватным данным (например, данные о позиции).
Логирование действий подключения и подписок выполняется через модуль logging.
"""


class BybitPublic:
    """
    Класс для работы с публичными данными через WebSocket.
    Создаёт подключение к публичному каналу Bybit и предоставляет методы для подписки на потоки данных.
    """

    def __init__(self, testnet=True):
        """
        Инициализация подключения к публичному WebSocket.

        :param testnet: Если True, подключение осуществляется к тестовой сети Bybit (по умолчанию True).
        """
        self.ws = WebSocket(testnet=testnet, channel_type="linear")
        logging.info("Подключение к публичному WebSocket установлено")

    def subscribe_orderbook(self, symbol, callback):
        """
        Подписка на поток ордербука для выбранной торговой пары.

        :param symbol: Символ торговой пары, например "BTCUSDT".
        :param callback: Функция обратного вызова для обработки полученных данных.
        """
        self.ws.orderbook_stream(depth=50, symbol=symbol, callback=callback)
        logging.info(f"Подписка на ордербук {symbol}")

    def handle_orderbook(self, message):
        """
        Обрабатывает данные ордербука, полученные по WebSocket.

        :param message: Сообщение, полученное от WebSocket, содержащее данные ордербука.
        """
        print("Данные ордербука:", message)


class BybitPrivate:
    """
    Класс для работы с приватными данными через WebSocket.
    Создаёт подключение к приватному каналу Bybit для получения данных о позиции, балансе и т.д.
    """

    def __init__(self, api_key, api_secret, testnet=True):
        """
        Инициализация подключения к приватному WebSocket.

        :param api_key: API-ключ для доступа к приватным данным.
        :param api_secret: Секретный ключ для API.
        :param testnet: Если True, подключение осуществляется к тестовой сети Bybit (по умолчанию True).
        """
        self.ws = WebSocket(testnet=testnet, channel_type="private",
                            api_key=api_key, api_secret=api_secret, trace_logging=False)
        logging.info("Подключение к приватному WebSocket установлено")

    def subscribe_position(self, callback):
        """
        Подписка на поток данных о позиции пользователя.

        :param callback: Функция обратного вызова для обработки полученных данных о позиции.
        """
        self.ws.position_stream(callback=callback)
        logging.info("Подписка на поток данных о позиции")

    def handle_position(self, message):
        """
        Обрабатывает данные о позиции, полученные по WebSocket.

        :param message: Сообщение, полученное от WebSocket, содержащее данные о позиции.
        """
        print("Данные о позиции:", message)

    def subscribe_wallet(self, callback):
        """
        Подписка на поток данных о позиции пользователя.

        :param callback: Функция обратного вызова для обработки полученных данных о позиции.
        """
        self.ws.wallet_stream(callback=callback)
        logging.info("Подписка на поток данных о кошельке")

    def handle_message(self, message):
        """
        Обрабатывает данные о кошельке, полученные по WebSocket.

        :param message: Сообщение, полученное от WebSocket, содержащее данные о кошельке.
        """
        print("Данные о кошельке:", message)
