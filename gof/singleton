# Одиночка (классический стиль)
class Connection:
    _instance = None

    @staticmethod
    def get_instance(*args, **kwargs):
        if Connection._instance is None:
            Connection._instance = Connection(*args, **kwargs)
        return Connection._instance


# Одиночка (Python стиль)
class Proxy:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Основной класс, в котором прописана вся логика работы
class Application:
    def main(self):
        # con1 и con2 будут одним и тем же объектом, то же можно сказать про pr1 и pr2

        con1 = Connection.get_instance()
        con2 = Connection.get_instance()

        pr1 = Proxy()
        pr2 = Proxy()
