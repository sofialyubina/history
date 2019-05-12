from tasks.task import Task


class TasksReason(Task):

    def __init__(self, task_id, reason_id, level):
        self.task_id = task_id
        self.reason_id = reason_id
        self.level = level
