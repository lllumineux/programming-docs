from abc import ABC, abstractmethod


# Интерфейс состояния
class State(ABC):
    def __init__(self, tg_bot):
        self._bot = tg_bot

    @abstractmethod
    def handle_msg(self, msg):
        pass

    @abstractmethod
    def handle_exit(self):
        pass


# Конкретное состояние #1
class EnterCommandState(State):
    def handle_msg(self, msg):
        if msg.lower() == 'старт':
            self._bot.send_message('Привет! Как тебя зовут?')
            self._bot.set_state(EnterNameState(self._bot))
        elif msg.lower() == 'стоп':
            self._bot.send_message('Пока!')
            self._bot.set_state(StopState(self._bot))
        elif msg.lower() == '...':
            pass  # ...

    def handle_exit(self):
        pass


# Конкретное состояние #2
class EnterNameState(State):
    def handle_msg(self, msg):
        self._bot.context['name'] = msg
        self._bot.send_message(f'Приятно познакомиться, {msg}! Сколько тебе лет?')
        self._bot.set_state(EnterAgeState(self._bot))

    def handle_exit(self):
        self._bot.send_message(f'Подожди! Я даже не знаю как тебя зовут!')


# Конкретное состояние #3
class EnterAgeState(State):
    def handle_msg(self, msg):
        try:
            age = int(msg)
            self._bot.context['age'] = age
            self._bot.send_message(f'Тебе {age} лет. Спасибо за информацию!')
            self._bot.set_state(EnterCommandState(self._bot))
        except ValueError:
            self._bot.send_message('Пожалуйста, введи число.')

    def handle_exit(self):
        self._bot.send_message(f'Подожди! Я даже не знаю сколько тебе лет!')


# Конкретное состояние #4
class StopState(State):
    def handle_msg(self, msg):
        self._bot.send_message('Диалог завершён!')

    def handle_exit(self):
        pass


# Контекст
class TelegramBot:
    def __init__(self):
        self._state: State = EnterCommandState(self)
        self.context = {}

    def set_state(self, state: State):
        self._state = state

    def handle_msg(self, msg: str):
        self._state.handle_msg(msg)

    def handle_exit(self):
        self._state.handle_exit()

    def send_message(self, text: str):
        print(text)
