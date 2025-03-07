from abc import ABC, abstractmethod


# Интерфейс элемента
class Shape(ABC):
    @abstractmethod
    def move(self, x: int, y: int):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


# Конкретный элемент #1
class Circle(Shape):
    def move(self, x: int, y: int):
        pass  # ...

    def accept(self, visitor):
        visitor.visit_circle(self)


# Конкретный элемент #2
class Rectangle(Shape):
    def move(self, x: int, y: int):
        pass  # ...

    def accept(self, visitor):
        visitor.visit_rectangle(self)


# Конкретный элемент #3
class CompoundShape(Shape):
    def move(self, x: int, y: int):
        pass  # ...

    def accept(self, visitor):
        visitor.visit_compound_shape(self)


# Интерфейс посетителя
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: Circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle):
        pass

    @abstractmethod
    def visit_compound_shape(self, compound_shape: CompoundShape):
        pass


# Конкретный посетитель #1
class XMLExportVisitor(Visitor):
    def visit_circle(self, circle: Circle):
        pass  # ...

    def visit_rectangle(self, rectangle: Rectangle):
        pass  # ...

    def visit_compound_shape(self, compound_shape: CompoundShape):
        pass  # ...


# Клиент
class Application:
    def __init__(self):
        self._shapes = []

    def main(self):
        xml_export = XMLExportVisitor()
        for shape in self._shapes:
            # Можно подставить любую логику, реализованную через Visitor
            shape.accept(xml_export)
