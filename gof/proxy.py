from abc import ABC, abstractmethod


# Интерфейс сервиса
class YouTubeParserInterface(ABC):
    @abstractmethod
    def get_video(self, video_id: int) -> dict:
        pass


# Сервис (например, импортированный из библиотеки)
class YouTubeParser(YouTubeParserInterface):
    def get_video(self, video_id: int) -> dict:
        return {}  # ...


# Заместитель
class CachedYouTubeParser(YouTubeParserInterface):
    def __init__(self, service: YouTubeParser):
        self._service = service
        self._cache: dict[int, dict] = {}

    def get_video(self, video_id: int) -> dict:
        if video_id not in self._cache:
            self._cache[video_id] = self._service.get_video(video_id)
        return self._cache.get(video_id)


# Клиентский код
def main():
    parser = YouTubeParser()
    cached_parser = CachedYouTubeParser(parser)
    cached_parser.get_video(938)
    # При последующих вызовах возвращает кэшированное видео, а не выполняет долгий запрос
    cached_parser.get_video(938)
