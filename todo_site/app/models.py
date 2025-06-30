import os


class TodoModel:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.todos = self._load()

    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines()]
        return []

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for task in self.todos:
                f.write(task + "\n")

    def add(self, task):
        if task:
            self.todos.append(task)
            self._save()

    def delete(self, index):
        if 0 <= index < len(self.todos):
            self.todos.pop(index)
            self._save()

    def get_all(self):
        return self.todos
