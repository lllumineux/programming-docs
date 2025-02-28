from abc import ABC, abstractmethod


# Интерфейс прототипа
class Prototype(ABC):
    color: str

    @abstractmethod
    def clone(self):
        pass


# Хранилище прототипов
class PrototypeRegistry:
    def __init__(self):
        self._objects = {}

    def add_object(self, idx: int, obj: Prototype):
        self._objects[idx] = obj

    def get_by_id(self, idx: int):
        return self._objects[idx]

    def get_by_color(self, color: str) -> list[Prototype]:
        return [
            obj.clone()
            for obj in self._objects.values()
            if obj.color == color
        ]


# Конкретный прототип #1
class Button(Prototype):
    def __init__(self, color, text):
        self.color = color
        self.text = text

    def clone(self):
        new_btn = super().__new__(Button)
        new_btn.__init__(color=self.color, text=self.text)
        return new_btn


# Конкретный прототип #2
class Background(Prototype):
    def __init__(self, color):
        self.color = color

    def clone(self):
        new_bg = super().__new__(Background)
        new_bg.__init__(color=self.color)
        return new_bg


# Основной класс, в котором прописана вся логика работы
class Application:
    def __init__(self):
        self.registry = PrototypeRegistry()

    def main(self):
        btn = Button('#000', 'Test')
        self.registry.add_object(id(btn), btn)
        new_black_btn_lst = self.registry.get_by_color('#000')
