from abc import ABC, abstractmethod


# Интерфейс реализации
class MessageFormatter(ABC):
    @abstractmethod
    def format(self, text):
        pass


# Конкретная реализация #1
class JsonFormatter(MessageFormatter):
    def format(self, text):
        return f'{{\"text\": \"{text}\"}}'


# Конкретная реализация #2
class XmlFormatter(MessageFormatter):
    def format(self, text):
        return f'<text>{text}</text>'


# Абстракция
class MessageSender(ABC):
    def __init__(self, formatter: MessageFormatter):
        self.formatter = formatter

    @abstractmethod
    def send(self, text):
        pass


# Расширенная абстракция #1
class EmailSender(MessageSender):
    def send(self, text):
        formatted_msg = self.formatter.format(text)
        # ... - код для отправки E-mail


# Расширенная абстракция #2
class SmsSender(MessageSender):
    def send(self, text):
        formatted_msg = self.formatter.format(text)
        # ... - код для отправки SMS


# Клиентский код
def main():
    json_formatter = JsonFormatter()
    xml_formatter = XmlFormatter()

    # Вместо 4-х классов - 4 комбинации с помощью 2-х классов
    json_email = EmailSender(json_formatter)
    json_sms = SmsSender(json_formatter)
    xml_email = EmailSender(xml_formatter)
    xml_sms = SmsSender(xml_formatter)
