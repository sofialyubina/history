from history.base.knowledge_db import KnowledgeDatabase
from history.tasks.tasks_dates import TasksDate

path = "../history/data"
database = KnowledgeDatabase(path)


for task_type in [KnowledgeDatabase.TaskType.DATE,
                  KnowledgeDatabase.TaskType.EVENT,
                  KnowledgeDatabase.TaskType.TERM,
                  KnowledgeDatabase.TaskType.PERSON,
                  KnowledgeDatabase.TaskType.REASON,
                  KnowledgeDatabase.TaskType.RESULT]:

    task_id = database.get_random_task_id(task_type)
    task = database.get_task(task_id, task_type)

    print(task.question)
    user_answer = input()

    print(task.score(user_answer))
