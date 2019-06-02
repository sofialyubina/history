from .task import Task


class TasksResult(Task):

    def __init__(self, task_id, result_id, level, database):
        self.task_id = task_id
        self.result_id = result_id
        self.level = level
        self.database = database
        result = database.results[result_id]
        event = database.events[result.event_id]
        self.question = "Назовите последствия данного события:" + event.event

    def score(self, answer):
        return True
