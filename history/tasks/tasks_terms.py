from .task import Task


class TasksTerm(Task):

    def __init__(self, task_id, term_id, level, database):
        self.task_id = task_id
        self.term_id = term_id
        self.level = level
        self.database = database
        term = self.database.terms[term_id]
        self.question = "Дайте определение термину - " + term.term

    def score(self, answer):
        return True
