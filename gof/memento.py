# Снимок
class Snapshot:
    def __init__(self, text, cur_x, cur_y):
        self._text = text
        self._cur_x = cur_x
        self._cur_y = cur_y

    @property
    def text(self):
        return self._text

    @property
    def cur_x(self):
        return self._cur_x

    @property
    def cur_y(self):
        return self._cur_y


# Создатель
class Editor:
    def __init__(self):
        self._text = ''
        self._cur_x = 0
        self._cur_y = 0

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def cursor(self):
        return self._cur_x, self._cur_y

    @cursor.setter
    def cursor(self, value):
        self._cur_x, self._cur_y = value

    def create_snapshot(self):
        return Snapshot(self._text, self._cur_x, self._cur_y)

    def restore_snapshot(self, snapshot: Snapshot):
        self._text = snapshot.text
        self._cur_x = snapshot.cur_x
        self._cur_y = snapshot.cur_y


# Опекун
class EditorHistory:
    def __init__(self, editor: Editor):
        self.editor = editor
        self.history: list[Snapshot] = []

    def save(self):
        snapshot = self.editor.create_snapshot()
        self.history.append(snapshot)

    def undo(self):
        last_snapshot = self.history.pop()
        if not last_snapshot:
            raise IndexError
        self.editor.restore_snapshot(last_snapshot)


# Клиентский код
class Application:
    def main(self):
        editor = Editor()
        editor_history = EditorHistory(editor)

        editor.text = 'Старое состояние'
        editor.cursor = (10, 2)
        editor_history.save()

        editor.text = 'Новое состояние'
        editor.cursor = (20, 3)
        editor_history.undo()
