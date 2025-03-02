# Интерфейс клиента
class XmlLogger:
    def print_log(self, msg):
        xml_str = f'<message>{msg}</message>'
        print(f'Logging: {xml_str}')


# Сервис (например, импортированный из библиотеки)
class JsonLogger:
    def get_log_entry(self, message):
        return {'message': message}
    
    # Можем только сохраняться 
    def save_log(self, message):
        with open('logs.json', 'a+') as f:
            f.write(str(self.get_log_entry(message)))


# Адаптер
class JsonToXmlAdapter(XmlLogger):
    def __init__(self, json_logger):
        self._json_logger = json_logger

    def print_log(self, msg):
        json_log = self._json_logger.get_log_entry(msg)
        json_str = str(json_log)
        print(f'Logging: {json_str}')


# Клиентский код
class Application:
    def main(self):
        xml_logger = XmlLogger()
        old_json_logger = JsonLogger()
        json_logger = JsonToXmlAdapter(old_json_logger)
        
        # Вместо сохранения логов в json формате - можем их печатать, вместе с логами в xml формате
        xml_logger.print_log('test')
        json_logger.print_log('test')
