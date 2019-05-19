from tasks.task import Task
from algorithms import matching
from base.knowledge_db import KnowledgeDatabase

path = "../data"
database = KnowledgeDatabase(path)



class TasksPerson(Task):

    def __init__(self, task_id, person_id,  level):
        self.task_id = task_id
        self.person_id = person_id
        self.level = level

    def score(self, answer):
        answer = matching.get_words(answer)
        person = database.persons(self.person_id)
        result = matching.matching(person.name, answer)
        return result