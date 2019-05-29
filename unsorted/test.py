from base.knowledge_db import KnowledgeDatabase
from tasks.tasks_dates import TasksDate

path = "../data"
database = KnowledgeDatabase(path)
task = database.tasks_date[3]
print(task.question)
user_answer = input()
print(task.score(database.events[database.get_tasks_date(3).event_id].start_year), user_answer)
