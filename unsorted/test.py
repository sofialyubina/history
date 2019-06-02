from history.base.knowledge_db import KnowledgeDatabase
from history.tasks.tasks_dates import TasksDate

path = "../data"
database = KnowledgeDatabase(path)

task_type = KnowledgeDatabase.TaskType.DATE
task_id = database.get_random_task_id(task_type)

task = database.get_task(task_id, task_type)

print(task.question)
user_answer = input()

print(task.score(user_answer))

