from .task import Task
from ..algorithms import matching


class TasksResult(Task):

    def __init__(self, task_id, result_id, level, database, threshold):
        self.task_id = task_id
        self.result_id = result_id
        self.level = level
        self.database = database
        self.threshold = threshold
        self.result = database.results[result_id]
        self.event = database.events[self.result.event_id]
        self.question = "Назовите последствия данного события: " + self.event.event

    def score(self, answer):
        return matching.calc_vectors_score(self.result.description, answer, self.database.vectors) >= self.threshold
