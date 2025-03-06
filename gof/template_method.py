from abc import ABC, abstractmethod


# Абстрактный класс
class DataReader(ABC):
    # Шаблонный метод
    def read_data(self):
        self.open_source()
        data = self.extract_data()
        parsed_data = self.parse_data(data)
        self.close_source()
        return parsed_data

    # Шаг #1
    @abstractmethod
    def open_source(self):
        pass

    # Шаг #2
    @abstractmethod
    def extract_data(self):
        pass

    # Шаг #3
    @abstractmethod
    def parse_data(self, data):
        pass

    # Шаг #4
    @abstractmethod
    def close_source(self):
        pass


# Конкретный класс #1
class FileDataReader(DataReader):
    def open_source(self):
        return None  # ...

    def extract_data(self):
        return ''  # ...

    def parse_data(self, data):
        return {}  # ...

    def close_source(self):
        return None  # ...


# Конкретный класс #2
class DatabaseDataReader(DataReader):
    def open_source(self):
        return None  # ...

    def extract_data(self):
        return ''  # ...

    def parse_data(self, data):
        return {}  # ...

    def close_source(self):
        return None  # ...


# Клиентский код
def main():
    # Можем читать данные из разных источников, реализуя лишь конкретные шаги, а не весь алгоритм
    file_reader = FileDataReader()
    file_reader.read_data()
    db_reader = DatabaseDataReader()
    db_reader.read_data()
