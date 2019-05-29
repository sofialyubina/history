from tasks.task import Task
from algorithms import matching


class TasksDate(Task):
    def __init__(self, task_id, event_id, question, level, database):
        self.task_id = task_id
        self.event_id = event_id
        self.question = question
        self.level = level
        self.database = database

    def score(self, answer):
        event = self.database.events[self.event_id]
        result = matching.matching(event.start_year, answer)
        return result
