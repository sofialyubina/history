import pandas
from enum import Enum
import numpy as np

from .base_events import Event
from .base_persons import Person
from .base_reasons import Reason
from .base_results import Result
from .base_terms import Term

from ..tasks.tasks_dates import TasksDate
from ..tasks.tasks_events import TasksEvent
from ..tasks.tasks_persons import TasksPerson
from ..tasks.tasks_reasons import TasksReason
from ..tasks.tasks_results import TasksResult
from ..tasks.tasks_terms import TasksTerm

import os


class KnowledgeDatabase(object):

    class TaskType(str, Enum):
        DATE = "date"
        EVENT = "event"
        PERSON = "person"
        TERM = "term"
        REASON = "reason"
        RESULT = "result"

    def __init__(self, path):
        self._create_events(path)
        self._create_persons(path)
        self._create_reasons(path)
        self._create_results(path)
        self._create_terms(path)
        self._create_tasks_date(path)
        self._create_tasks_event(path)
        self._create_tasks_person(path)
        self._create_tasks_reason(path)
        self._create_tasks_result(path)
        self._create_tasks_terms(path)

    def _create_events(self, path):
        data = pandas.read_csv(os.path.join(path, "events.csv"))
        self.events = {}
        for index, row in data.iterrows():
            self.events[row["event_id"]] = Event(event_id=row["event_id"],
                                                 start_year=row["start_year"],
                                                 start_month=row["start_month"],
                                                 start_day=row["start_day"],
                                                 end_year=row["end_year"],
                                                 end_month=row["end_month"],
                                                 end_day=row["end_day"],
                                                 event_=row["event"])

    def _create_persons(self, path):
        data = pandas.read_csv(os.path.join(path, "persons.csv"))
        self.persons = {}
        for index, row in data.iterrows():
            self.persons[row["person_id"]] = Person(person_id=row["person_id"],
                                                    name=row["name"],
                                                    description=["description"])

    def _create_terms(self, path):
        data = pandas.read_csv(os.path.join(path, "terms.csv"))
        self.terms = {}
        for index, row in data.iterrows():
            self.terms[row["term_id"]] = Term(term_id=row["term_id"],
                                              term=row["term"],
                                              definition=row["definition"])

    def _create_reasons(self, path):
        data = pandas.read_csv(os.path.join(path, "reasons.csv"))
        self.reasons = {}
        for index, row in data.iterrows():
            self.reasons[row["reason_id"]] = Reason(reason_id=row["reason_id"],
                                                    event_id=row["event_id"],
                                                    description=row["description"])

    def _create_results(self, path):
        data = pandas.read_csv(os.path.join(path, "results.csv"))
        self.results = {}
        for index, row in data.iterrows():
            self.results[row["result_id"]] = Result(result_id=row["esult_id"],
                                                    event_id=row["event_id"],
                                                    description=row["description"])

    def _create_tasks_date(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_dates.csv"))
        self.tasks_date = {}
        for index, row in data.iterrows():
            self.tasks_date[row["task_id"]] = TasksDate(task_id=row["task_id"],
                                                        event_id=row["event_id"],
                                                        question=row["question"],
                                                        level=row["level"],
                                                        database=self)

    def _create_tasks_event(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_events.csv"))
        self.tasks_event = {}
        for index, row in data.iterrows():
            self.tasks_event[row["task_id"]] = TasksEvent(task_id=row["task_id"],
                                                          event_id=row["event_id"],
                                                          level=row["level"],
                                                          question=row["question"],
                                                          database=self)

    def _create_tasks_person(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_persons.csv"))
        self.tasks_persons = {}
        for index, row in data.iterrows():
            self.tasks_persons[row["task_id"]] = TasksPerson(task_id=row["task_id"],
                                                             person_id=row["person_id"],
                                                             level=row["level"],
                                                             database=self)

    def _create_tasks_result(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_results.csv"))
        self.tasks_result = {}
        for index, row in data.iterrows():
            self.tasks_result[row["task_id"]] = TasksResult(task_id=row["task_id"],
                                                            result_id=["result_id"],
                                                            level=row["level"],
                                                            database=self)

    def _create_tasks_reason(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_reasons.csv"))
        self.tasks_reason = {}
        for index, row in data.iterrows():
            self.tasks_reason[row["task_id"]] = TasksReason(task_id=row["task_id"],
                                                            reason_id=row["reason_id"],
                                                            level=row["level"],
                                                            database=self)

    def _create_tasks_terms(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_terms.csv"))
        self.tasks_term = {}
        for index, row in data.iterrows():
            self.tasks_term[row["task_id"]] = TasksTerm(task_id=row["task_id"],
                                                        term_id=row["term_id"],
                                                        level=row["level"],
                                                        database=self)

    def get_event(self, event_id):
        return self.events[event_id]

    def get_person(self, person_id):
        return self.persons[person_id]

    def get_term(self, term_id):
        return self.terms[term_id]

    def get_result(self, result_id):
        return self.results[result_id]

    def get_reason(self, reason_id):
        return self.reasons[reason_id]

    def get_task_date(self, task_id):
        return self.tasks_date[task_id]

    def get_task_event(self, task_id):
        return self.tasks_event[task_id]

    def get_task_person(self, task_id):
        return self.tasks_persons[task_id]

    def get_task_term(self, task_id):
        return self.tasks_term[task_id]

    def get_task_result(self, task_id):
        return self.tasks_result[task_id]

    def get_task_reason(self, task_id):
        return self.tasks_reason[task_id]

    def get_random_task_id(self, task_type):
        if task_type == self.TaskType.DATE:
            tasks = self.tasks_date
        elif task_type == self.TaskType.EVENT:
            tasks = self.tasks_event
        elif task_type == self.TaskType.TERM:
            tasks = self.tasks_term
        elif task_type == self.TaskType.PERSON:
            tasks = self.tasks_persons
        elif task_type == self.TaskType.RESULT:
            tasks = self.tasks_result
        elif task_type == self.TaskType.REASON:
            tasks = self.tasks_reason
        else:
            raise ValueError("Not supported task type {}".format(task_type))

        # return random task_id
        return np.random.choice(list(tasks.keys()))

    def get_task(self, task_id, task_type):
        if task_type == self.TaskType.DATE:
            return self.get_task_date(task_id)
        elif task_type == self.TaskType.EVENT:
            return self.get_task_event(task_id)
        elif task_type == self.TaskType.TERM:
            return self.get_task_term(task_id)
        elif task_type == self.TaskType.PERSON:
            return self.get_task_person(task_id)
        elif task_type == self.TaskType.RESULT:
            return self.get_task_result(task_id)
        elif task_type == self.TaskType.REASON:
            return self.get_task_reason(task_id)
        else:
            raise ValueError("Not supported task type {}".format(task_type))
