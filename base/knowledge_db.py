import pandas
from .base_events import GlobalEvent
from .base_persons import Person
from .base_reasons import Reason
from .base_results import  Result
from .base_terms import Term


class KnowledgeDatabase(object):

    def __init__(self, path):
        self._create_events(path)
        self._create_persons(path)

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

    

