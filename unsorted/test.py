from base.knowledge_db import KnowledgeDatabase

path = "../data"
database = KnowledgeDatabase(path)
event = database.get_event(4)
print(event.event)