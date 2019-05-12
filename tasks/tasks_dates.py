from .task import Task
from ..algorithms import matching

class TasksDate(Task):
    def __init__(self, task_id, event_id, question, level):
        self.task_id = task_id
        self.event_id = event_id
        self.question = question
        self.level = level

    def score(self, answer):
        words = matching.get_words(answer)
        # ... do something ...
        return 0
