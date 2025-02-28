from abc import ABC, abstractmethod


# Интерфейс продукта (типа #1)
class Button(ABC):
    @abstractmethod
    def render(self, label):
        pass


# Конкретный продукт #1 (типа #1)
class WinButton(Button):
    def render(self, label):
        return f'Win-кнопка "{label}"'


# Конкретный продукт #2 (типа #1)
class MacButton(Button):
    def render(self, label):
        return f'Mac-кнопка "{label}"'


# Интерфейс продукта (типа #2)
class Select(ABC):
    @abstractmethod
    def render(self, options):
        pass


# Конкретный продукт #1 (типа #2)
class WinSelect(Select):
    def render(self, options):
        return f'Win-селект {options}'


# Конкретный продукт #2 (типа #2)
class MacSelect(Select):
    def render(self, options):
        return f'Mac-селект {options}'


# Базовый класс фабрики
class Dialog(ABC):
    def show_warning(self):
        ok_button = self.create_button()
        ok_button.render(label='Ок')
        choices_select = self.create_select()
        choices_select.render(options=('Да', 'Нет'))

    # Фабричный метод (типа #1)
    @abstractmethod
    def create_button(self) -> Button:
        pass

    # Фабричный метод (типа #2)
    @abstractmethod
    def create_select(self) -> Select:
        pass


# Конкретная фабрика #1
class WinDialog(Dialog):
    def create_button(self) -> Button:
        return WinButton()

    def create_select(self) -> Select:
        return WinSelect()


# Конкретная фабрика #2
class MacDialog(Dialog):
    def create_button(self) -> Button:
        return MacButton()

    def create_select(self) -> Select:
        return MacSelect()


# Основной класс, в котором прописана вся логика работы
class Application:
    def __init__(self):
        self.dialog = None

    def initialize(self):
        config = self.get_config()

        if config['OS'] == 'Win':
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
