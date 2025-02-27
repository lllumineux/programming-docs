from abc import ABC, abstractmethod


# Первый продукт (Page)
class Page:
    pass


# Второй продукт (Guide)
class Guide:
    pass


# Интерфейс строителя
class Builder(ABC):
    @abstractmethod
    def set_header(self, label):
        pass

    @abstractmethod
    def set_slideshow(self, image_paths):
        pass

    @abstractmethod
    def set_comments_block(self, is_allowed):
        pass

    @abstractmethod
    def set_footer(self, links):
        pass


# Конкретный первый строитель (PageBuilder)
class PageBuilder(Builder):
    def __init__(self):
        self.page = Page()

    def set_header(self, label):
        pass

    def set_slideshow(self, image_paths):
        pass

    def set_comments_block(self, is_allowed):
        pass

    def set_footer(self, links):
        pass

    def get_result(self) -> Page:
        return self.page


# Конкретный второй строитель (GuideBuilder)
class GuideBuilder(Builder):
    def __init__(self):
        self.guide = Guide()

    def set_header(self, label):
        pass

    def set_slideshow(self, image_paths):
        pass

    def set_comments_block(self, is_allowed):
        pass

    def set_footer(self, links):
        pass

    def get_result(self) -> Guide:
        return self.guide


# Директор
class Director:
    def construct_main_page(self, builder):
        builder.set_header(label='Главная страница')
        builder.set_slideshow(image_paths=('images/1.png', 'images/2.png'))
        builder.set_comments_block(is_allowed=False)
        builder.set_footer(links=('https://t.me/lllumineux',))


# Основной класс, в котором прописана вся логика работы
class Application:
    def make_page(self):
        director = Director()

        # Не нужно повторять шаги, т.к. они уже прописаны в Director

        page_builder = PageBuilder()
        director.construct_main_page(page_builder)
        page = page_builder.get_result()

        guide_builder = GuideBuilder()
        director.construct_main_page(guide_builder)
        guide = guide_builder.get_result()

        return page, guide
