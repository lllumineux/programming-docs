from abc import ABC, abstractmethod


# Интерфейс продукта
class Button(ABC):
    @abstractmethod
    def render(self, label):
        pass


# Конкретный продукт #1
class WinButton(Button):
    def render(self, label):
        return f'Win-кнопка "{label}"'


# Конкретный продукт #2
class MacButton(Button):
    def render(self, label):
        return f'Mac-кнопка "{label}"'


# Базовый класс фабрики
class Dialog(ABC):
    def show_warning(self):
        ok_button = self.create_button()
        ok_button.render('Ок')

    # Фабричный метод
    @abstractmethod
    def create_button(self) -> Button:
        pass


# Конкретная фабрика #1
class WinDialog(Dialog):
    def create_button(self) -> Button:
        return WinButton()


# Конкретная фабрика #2
class MacDialog(Dialog):
    def create_button(self) -> Button:
        return MacButton()


# Основной класс, в котором прописана вся логика работы
class Application:
    def __init__(self):
        self.dialog = None

    def initialize(self):
        config = self.get_config()

        if config['OS'] == 'Windows':
            self.dialog = WinDialog()
        elif config['OS'] == 'Mac':
            self.dialog = MacDialog()
        else:
            raise Exception('Unknown OS')

    def get_config(self):
        with open('os.txt') as f:
            return {'OS': f.read()}

    def main(self):
        self.initialize()
        # Не нужно писать if-else, т.к. уже сконфигурировали вначале
        self.dialog.show_warning()
