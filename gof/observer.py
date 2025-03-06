from abc import ABC, abstractmethod


# Интерфейс подписчика
class Subscriber(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


# Конкретный подписчик #1
class Logger(Subscriber):
    def update(self, message: dict):
        pass  # ...


# Конкретный подписчик #2
class TelegramNotifier(Subscriber):
    def update(self, message: dict):
        pass  # ...


# Издатель
class Parser:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, data: dict):
        for observer in self._subscribers:
            observer.update(data)

    def parse_text(self, text: str):
        data = {'text': text}
        # ...
        self.notify_subscribers(data)


# Клиентский код
def main():
    parser = Parser()
    
    logger = Logger()
    parser.subscribe(logger)
    notifier = TelegramNotifier()
    parser.subscribe(notifier)
    
    # Объекты logger и notifier получат данные полученные из парсинга через механизм подписки
    parser.parse_text('Тестовый текст.')
    
