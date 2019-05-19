from tasks.task import Task
from algorithms import matching
from base.knowledge_db import KnowledgeDatabase

path = "../data"
database = KnowledgeDatabase(path)


class TasksDate(Task):
    def __init__(self, task_id, event_id, question, level):
        self.task_id = task_id
        self.event_id = event_id
        self.question = question
        self.level = level

    def score(self, answer):
        answer = matching.get_words(answer)
        event = database.get_event(self.event_id)
        result = matching.matching(event.date, answer)
        return result
