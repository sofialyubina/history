from .task import Task
from ..algorithms import matching


class TasksDate(Task):
    def __init__(self, task_id, event_id, question, level, database):
        self.task_id = task_id
        self.event_id = event_id
        self.question = question
        self.level = level
        self.database = database

    def score(self, answer):
        event = self.database.events[self.event_id]
        string = answer
        string2 = string.split(" ")
        for i in range(len(string2)):
            if string2[i].islower():
                continue
            else:
                number = string2[i]

        result = matching.matching(event.start_year, number)
        return result
