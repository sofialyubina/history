from .task import Task
from ..algorithms import matching


class TasksPerson(Task):

    def __init__(self, task_id, description_id,  level, database):
        self.task_id = task_id
        self.description_id = description_id
        self.level = level
        self.database = database
        self.person = self.database.get_person(description_id)
        self.question = "Кто это? {}".format(self.person.description)

    def score(self, answer):
        result = matching.match_with_answer(self.person.name, answer)
        return result
