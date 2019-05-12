import pandas

from base.base_events import Event
from base.base_persons import Person
from base.base_reasons import Reason
from base.base_results import Result
from base.base_terms import Term

from tasks.tasks_dates import TasksDate
from tasks.tasks_events import TasksEvent
from tasks.tasks_persons import TasksPerson
from tasks.tasks_reasons import TasksReason
from tasks.tasks_results import TasksResult
from tasks.tasks_terms import TasksTerm

import os


class KnowledgeDatabase(object):

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
                                                 start_month = row["start_month"],
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
                                                        level=row["level"],
                                                        question=["question"])

    def _create_tasks_event(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_events.csv"))
        self.tasks_event = {}
        for index, row in data.iterrows():
            self.tasks_event[row["task_id"]] = TasksEvent(task_id=row["task_id"],
                                                          event_id=row["event_id"],
                                                          level=row["level"],
                                                          question=["question"])

    def _create_tasks_person(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_persons.csv"))
        self.tasks_person = {}
        for index, row in data.iterrows():
            self.tasks_person[row["task_id"]] = TasksPerson(task_id=row["task_id"],
                                                            person_id=row["person_id"],
                                                            level=row["level"])

    def _create_tasks_result(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_results.csv"))
        self.tasks_result = {}
        for index, row in data.iterrows():
            self.tasks_result[row["task_id"]] = TasksResult(task_id=row["task_id"],
                                                            result_id=["result_id"],
                                                            level=row["level"])

    def _create_tasks_reason(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_reasons.csv"))
        self.tasks_reason = {}
        for index, row in data.iterrows():
            self.tasks_reason[row["task_id"]] = TasksReason(task_id=row["task_id"],
                                                            reason_id=row["reason_id"],
                                                            level=row["level"])

    def _create_tasks_terms(self, path):
        data = pandas.read_csv(os.path.join(path, "tasks_terms.csv"))
        self.tasks_term = {}
        for index, row in data.iterrows():
            self.tasks_term[row["task_id"]] = TasksTerm(task_id=row["task_id"],
                                                        term_id=row["term_id"],
                                                        level=row["level"])

    def get_event(self, event_id):
        return self.events[event_id]