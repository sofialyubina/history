from .task import Task


class TasksReason(Task):

    def __init__(self, task_id, reason_id, level, database):
        self.task_id = task_id
        self.reason_id = reason_id
        self.level = level
        self.database = database

    def score(self, answer):
        return 0


