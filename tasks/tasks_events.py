from tasks.task import Task


class TasksEvent(Task):

    def __init__(self, task_id, event_id, question, level):
        self.task_id = task_id
        self.event_id = event_id
        self.question = question
        self.level = level

