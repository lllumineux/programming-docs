from abc import ABC, abstractmethod


# Интерфейс посредника
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: 'Component', event: str):
        pass


# Конкретный посредник #1
class AuthenticationDialog(Mediator):
    def __init__(self):
        self.title = ''
        self.login_or_register_checkbox = Checkbox(self)
        self.login_username = Textbox(self)
        self.login_password = Textbox(self)
        self.signup_username = Textbox(self)
        self.signup_password = Textbox(self)
        self.signup_email = Textbox(self)
        self.ok_btn = Button(self)
        self.cancel_btn = Button(self)

    def notify(self, sender, event):
        if sender == self.login_or_register_checkbox and event == 'check':
            if self.login_or_register_checkbox.checked:
                self.title = 'Вход'
                self.login_username.is_hidden, self.login_password.is_hidden = True, True
                self.signup_username.is_hidden, self.signup_password.is_hidden = False, False
            else:
                self.title = 'Регистрация'
                self.signup_username.is_hidden, self.signup_password.is_hidden = True, True
                self.login_username.is_hidden, self.login_password.is_hidden = False, False

        if sender == self.ok_btn and event == 'click':
            if self.login_or_register_checkbox.checked:
                # ...
                user_found = False
                if not user_found:
                    pass  # ...
            else:
                pass  # ...


# Базовый класс компонента
class Component:
    def __init__(self, dialog: Mediator):
        self.dialog = dialog
        self.is_hidden = False 

    def click(self):
        self.dialog.notify(self, 'click')

    def keypress(self):
        self.dialog.notify(self, 'keypress')


# Компонент #1
class Button(Component):
    pass  # ...


# Компонент #2
class Textbox(Component):
    pass  # ...


# Компонент #3
class Checkbox(Component):
    def __init__(self, dialog: Mediator):
        super().__init__(dialog)
        self.checked = False

    def check(self):
        self.checked = not self.checked
        self.dialog.notify(self, 'check')

    # ...
