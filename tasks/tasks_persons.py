from tasks.task import Task
from algorithms import matching


class TasksPerson(Task):

    def __init__(self, task_id, person_id,  level, database):
        self.task_id = task_id
        self.person_id = person_id
        self.level = level
        self.database = database

    def score(self, answer):
        answer = matching.get_words(answer)
        person = self.database.persons(self.person_id)
        result = matching.matching(person.name, answer)
        return result