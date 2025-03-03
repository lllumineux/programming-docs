from abc import ABC, abstractmethod


# Интерфейс компонента
class Notification(ABC):
    @abstractmethod
    def send(self, msg: dict):
        pass


# Конкретный компонент
class EmailNotification(Notification):
    def send(self, msg: dict):
        print(f'Sending email: {msg["text"]}')


# Интерфейс декоратора
class NotificationDecorator(Notification, ABC):
    def __init__(self, source: Notification):
        self._wrappee = source


# Конкретный декоратор #1
class LoggingDecorator(NotificationDecorator):
    def send(self, msg: dict):
        print(f'Logging: Preparing to send message: {msg}')
        self._wrappee.send(msg['text'])
        print(f'Logging: Message sent: {msg}')


# Конкретный декоратор #2
class PermissionDecorator(NotificationDecorator):
    def __init__(self, source: Notification, role: str):
        super().__init__(source)
        self._role = role

    def send(self, msg: dict):
        if msg['role'] == self._role:
            self._wrappee.send(msg)
        else:
            raise PermissionError(f'Access denied: User is not {self._role}')


# Клиентский код
class Application:
    def main(self):
        notif = EmailNotification()
        logging_notif = LoggingDecorator(notif)
        perm_notif = PermissionDecorator(logging_notif, role='admin')
        perm_notif.send({'text': 'Test message.', 'role': 'admin'})
