from .task import Task


class TasksReason(Task):

    def __init__(self, task_id, reason_id, level, database):
        self.task_id = task_id
        self.reason_id = reason_id
        self.level = level
        self.database = database
        reason = database.results[reason_id]
        event = database.events[reason.event_id]
        self.question = "Назовите последствия данного события:" + event.event

    def score(self, answer):
        return True


