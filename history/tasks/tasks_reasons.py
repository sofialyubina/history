from .task import Task
from ..algorithms import matching


class TasksReason(Task):

    def __init__(self, task_id, reason_id, level, database, threshold):
        self.task_id = task_id
        self.reason_id = reason_id
        self.level = level
        self.thresold = threshold
        self.database = database
        self.reason = database.reasons[reason_id]
        self.event = database.events[self.reason.event_id]
        self.question = "Назовите причины данного события: " + self.event.event

    def score(self, answer):
        #return matching.calc_vectors_score(self.reason.description, answer, self.database.vectors) >= self.thresold
        return matching.calc_vectors_score(self.reason.description, answer, self.database.vectors) >= 0.5
