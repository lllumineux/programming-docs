from abc import ABC, abstractmethod


# Интерфейс обработчика
class HandlerInterface(ABC):
    @abstractmethod
    def handle(self, request: dict):
        pass


# Базовый обработчик
class BaseHandler(HandlerInterface):
    def __init__(self, next_handler=None):
        self._next = next_handler

    def handle(self, request: dict):
        if not self._next:
            return None
        return self._next.handle(request)


# Конкретный обработчик #1
class AuthenticationHandler(BaseHandler):
    def handle(self, request):
        if not request['user']:
            raise PermissionError
        return super().handle(request)


# Конкретный обработчик #2
class AuthorizationHandler(BaseHandler):
    def handle(self, request):
        if request['role'] != 'admin':
            return PermissionError
        return super().handle(request)


# Конкретный обработчик #3
class RequestHandler(BaseHandler):
    def handle(self, request):
        pass  # ...


# Клиентский код
class Application:
    def main(self):
        chain = AuthenticationHandler(AuthorizationHandler(RequestHandler()))
        chain.handle(request={'user': 'test', 'role': 'admin'})
