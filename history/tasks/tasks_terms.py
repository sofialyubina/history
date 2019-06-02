from .task import Task


class TasksTerm(Task):

    def __init__(self, task_id, term_id, level, database):
        self.task_id = task_id
        self.term_id = term_id
        self.level = level
        self.database = database

    def score(self, answer):
        return 0

