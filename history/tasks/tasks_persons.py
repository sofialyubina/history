from .task import Task
from ..algorithms import matching


class TasksPerson(Task):

    def __init__(self, task_id, person_id,  level, database):
        self.task_id = task_id
        self.person_id = person_id
        self.level = level
        self.database = database
        self.person = self.database.get_person(person_id)
        self.question = "Кто это? {}".format(self.person.description)

    def score(self, answer):
        result = matching.matching(self.person.name, answer)
        return result
