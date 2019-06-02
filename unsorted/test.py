from history.base.knowledge_db import KnowledgeDatabase
from history.tasks.tasks_dates import TasksDate

path = "../data"
database = KnowledgeDatabase(path)
task = database.tasks_date[3]
print(task.question)
user_answer = input()

print(task.score(user_answer))

