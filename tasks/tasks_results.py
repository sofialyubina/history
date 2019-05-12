from .task import Task


class TasksResult(Task):

    def __init__(self, task_id, result_id, level):
        self.task_id = task_id
        self.result_id = result_id
        self.level = level
