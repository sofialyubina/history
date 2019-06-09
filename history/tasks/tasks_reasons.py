from .task import Task
from ..algorithms import matching


class TasksReason(Task):

    def __init__(self, task_id, reason_id, level, database):
        self.task_id = task_id
        self.reason_id = reason_id
        self.level = level
        self.database = database
        self.reason = database.reasons[reason_id]
        self.event = database.events[self.reason.event_id]
        self.question = "Назовите причины данного события: " + self.event.event

    def score(self, answer):
        return matching.match_with_answer(self.reason.description, answer)
