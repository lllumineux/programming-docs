# Легковес
class ObjectType:
    def __init__(self, name: str, texture: str):
        self.name = name
        self.texture = texture

    def render(self, canvas, x, y):
        pass  # ...


# Контекст
class Object:
    def __init__(self, x: int, y: int, o_type: ObjectType):
        self.x = x
        self.y = y
        self.o_type = o_type

    def render(self, canvas):
        self.o_type.render(canvas, self.x, self.y)


# Фабрика легковесов
class ObjectTypeFactory:
    _object_types: list[ObjectType] = []

    # Фабричный метод
    @classmethod
    def get_object(cls, name, texture):
        ot = next((o for o in cls._object_types if o.name == name and o.texture == texture), None)
        if not ot:
            ot = ObjectType(name, texture)
            cls._object_types.append(ot)
        return ot


# Клиент
class ObjectStorage:
    def __init__(self):
        self._objects: list[Object] = []

    def add_object(self, x, y, name, texture):
        o_type = ObjectTypeFactory.get_object(name, texture)
        # Много объектов с одинаковой текстурой будут занимать не сильно больше места, чем 1
        obj = Object(x, y, o_type)
        self._objects.append(obj)

    def render(self, canvas):
        for obj in self._objects:
            obj.render(canvas)
