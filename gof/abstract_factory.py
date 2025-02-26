from abc import ABC, abstractmethod


# Интерфейс первого продукта (Button)
class Button(ABC):
    @abstractmethod
    def render(self, label):
        pass


# Конкретный первый продукт (WindowsButton)
class WindowsButton(Button):
    def render(self, label):
        return f'Windows-кнопка "{label}"'


# Конкретный первый продукт (MacButton)
class MacButton(Button):
    def render(self, label):
        return f'Mac-кнопка "{label}"'


# Интерфейс второго продукта (Text)
class Text(ABC):
    @abstractmethod
    def render(self, content):
        pass


# Конкретный второй продукт (WindowsText)
class WindowsText(Text):
    def render(self, content):
        return f'Windows-текст "{content}"'


# Конкретный второй продукт (MacText)
class MacText(Text):
    def render(self, content):
        return f'Mac-текст "{content}"'


# Интерфейс третьего продукта (Picture)
class Picture(ABC):
    @abstractmethod
    def render(self, path):
        pass


# Конкретный третий продукт (WindowsPicture)
class WindowsPicture(Picture):
    def render(self, path):
        return f'Windows-картинка "{path}"'


# Конкретный третий продукт (MacPicture)
class MacPicture(Picture):
    def render(self, path):
        return f'Mac-картинка "{path}"'


# Базовый класс фабрики (Dialog)
class Dialog(ABC):
    def show_warning(self):
        ok_button = self.create_button()
        ok_button.render(label='Ок')
        explanation_text = self.create_text()
        explanation_text.render(content='Ок')
        emoji_picture = self.create_picture()
        emoji_picture.render(path='/emoji/warning.png')

    # Фабричный метод первый
    @abstractmethod
    def create_button(self) -> Button:
        pass

    # Фабричный метод второй
    @abstractmethod
    def create_text(self) -> Text:
        pass

    # Фабричный метод третий
    @abstractmethod
    def create_picture(self) -> Picture:
        pass


# Конкретная фабрика (WindowsDialog)
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_text(self) -> Text:
        return WindowsText()

    def create_picture(self) -> Picture:
        return WindowsPicture()


# Конкретная фабрика (MacDialog)
class MacDialog(Dialog):
    def create_button(self) -> Button:
        return MacButton()

    def create_text(self) -> Text:
        return MacText()

    def create_picture(self) -> Picture:
        return MacPicture()


# Основной класс, в котором прописана вся логика работы
class Application:
    def __init__(self):
        self.dialog = None

    def initialize(self):
        config = self.get_config()

        if config['OS'] == 'Windows':
            self.dialog = WindowsDialog()
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
