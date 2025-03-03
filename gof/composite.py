from abc import ABC, abstractmethod


# Компонент
class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass


# Лист
class File(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name

    def get_size(self) -> int:
        with open(f'{self.name}') as f:
            return len(f.read())


# Контейнер
class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children: list[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def get_size(self) -> int:
        return sum([x.get_size() for x in self.children])


# Клиентский код
def main():
    root_folder = Folder('Root')
    folder1, folder2 = Folder('Documents'), Folder('Media')
    file1, file2, file3 = File('document.txt'), File('image.jpg'), File('music.mp3')

    folder1.add(file1)
    folder2.add(file2)
    folder2.add(file3)
    root_folder.add(folder1)
    root_folder.add(folder2)

    # Рекурсивно рассчитает сумму размеров всех файлов во всех папках и вернёт результат
    root_size = root_folder.get_size()
