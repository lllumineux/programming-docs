from abc import ABC, abstractmethod


# Интерфейс итератора
class ProfileIterator(ABC):
    @abstractmethod
    def get_next(self) -> dict:
        pass

    @abstractmethod
    def has_more(self) -> bool:
        pass


# Конкретный итератор #1
class FacebookIterator(ProfileIterator):
    def __init__(self, facebook: 'Facebook', start_user_id: int, user_type: str):
        self.facebook = facebook
        self.start_user_id = start_user_id
        self.user_type = user_type
        self.index = 0
        self.users = self.facebook.social_graph_request(self.start_user_id, self.user_type)

    def get_next(self) -> dict:
        if self.has_more():
            result = self.users[self.index]
            self.index += 1
            return result

    def has_more(self) -> bool:
        return self.index < len(self.users)


# Интерфейс коллекции
class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, user_id: int) -> ProfileIterator:
        pass

    @abstractmethod
    def create_coworkers_iterator(self, user_id: int) -> ProfileIterator:
        pass


# Конкретная коллекция #1
class Facebook(SocialNetwork):
    def create_friends_iterator(self, user_id: int) -> ProfileIterator:
        return FacebookIterator(self, user_id, 'friends')

    def create_coworkers_iterator(self, user_id: int) -> ProfileIterator:
        return FacebookIterator(self, user_id, 'coworkers')

    def social_graph_request(self, user_id: int, user_type: str) -> list[dict]:
        return []  # ...


# Клиент
class Application:
    def main(self):
        # Можем выбирать между коллекциями и итераторами
        network = Facebook()
        iterator = network.create_friends_iterator(293)

        # Можем итерироваться не зная как устроена коллекция внутри
        while iterator.has_more():
            profile = iterator.get_next()
            # ...
