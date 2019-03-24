class Question:

    def __init__(self, question_id, question_, type_, event_id):
        self.question_id = question_id
        self.question = question_
        self.event_id = event_id
        self.set_type(type_)

    def get_type(self):
        return self.type

    def set_type(self, type_):
        if type_ not in ["D", "E"]:
            raise ValueError("Wrong question type")
        else:
            self.type = type_

