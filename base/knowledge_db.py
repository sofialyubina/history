import pandas
from .base_events import GlobalEvent
from .base_persons import Person
from .base_reasons import Reason
from .base_results import Result
from .base_terms import Term
from tasks.tasks_dates import TasksDate
from tasks.tasks_events import TasksEvent
from tasks.tasks_persons import TasksPerson
from tasks.tasks_reasons import TasksReason
from tasks.tasks_results import TasksResult
from tasks.tasks_terms import TasksTerm


class KnowledgeDatabase(object):

    def __init__(self, path):
        self._create_events(path)
        self._create_persons(path)
        self._create_reasons(path)
        self._create_results(path)
        self._create_terms(path)
        self._create_tasks_date(path)

    def _create_events(self, path):
        data = pandas.read_csv(path+"/events.csv")
        events = []
        for index, row in data.iterrows():
            events.append(GlobalEvent(event_id=row["event_id"], start_year=row["start_year"],
                                      start_month = row["start_month"], start_day=row["start_day"],
                                      end_year=row["end_year"], end_month=row["end_month"],
                                      end_day=row["end_day"], event_=row["event"]))

    def _create_persons(self, path):
        data = pandas.read_csv(path+"/persons.csv")
        persons = []
        for index, row in data.iterrows():
            persons.append(Person(person_id=row["person_id"], name=row["name"], description=["description"]))

    def _create_terms(self, path):
        data = pandas.read_csv(path+"/terms.csv")
        terms = []
        for index, row in data.iterrows():
            terms.append(Term(term_id=row["term_id"], term=row["term"], definition=row["definition"]))

    def _create_reasons(self, path):
        data = pandas.read_csv(path + "/reasons.csv")
        reasons = []
        for index, row in data.iterrows():
            reasons.append(Reason(reason_id=row["reason_id"], event_id=row["event_id"], description=row["description"]))

    def _create_results(self, path):
        data = pandas.read_csv(path + "/results.csv")
        results = []
        for index, row in data.iterrows():
            results.append(Result(result_id=row["reason_id"], event_id=row["event_id"], description=row["description"]))

    def _create_tasks_date(self, path):
        data = pandas.read_csv(path + "/tasks_date.csv")
        tasks_date = []
        for index, row in data.iterrows():
            tasks_date.append(TasksDate(task_id=row["task_id"], event_id=row["event_id"], level=row["level"], question=["question"]))

    def _create_tasks_event(self, path):
        data = pandas.read_csv(path + "/tasks_event.csv")
        tasks_event = []
        for index, row in data.iterrows():
            tasks_event.append(TasksEvent(task_id=row["task_id"], event_id=row["event_id"], level=row["level"], question=["question"]))


    def _create_tasks_person(self, path):
        data = pandas.read_csv(path + "/tasks_person.csv")
        tasks_person = []
        for index, row in data.iterrows():
            tasks_person.append(
                TasksPerson(task_id=row["task_id"], person_id=row["person_id"], level=row["level"]))

    def _create_tasks_result(self, path):
        data = pandas.read_csv(path + "/tasks_result.csv")
        tasks_result = []
        for index, row in data.iterrows():
            tasks_result.append(
                TasksResult(task_id=row["task_id"], result_id=["result_id"], level=row["level"]))

    def _create_tasks_reason(self, path):
        data = pandas.read_csv(path + "/tasks_reason.csv")
        tasks_reason = []
        for index, row in data.iterrows():
            tasks_reason.append(
                TasksReason(task_id=row["task_id"], reason_id=row["reason_id"], level=row["level"]))

    def _create_tasks_terms(self, path):
        data = pandas.read_csv(path + "/tasks_term.csv")
        tasks_term = []
        for index, row in data.iterrows():
            tasks_term.append(
                TasksTerm(task_id=row["task_id"], term_id=row["term_id"], level=row["level"]))

