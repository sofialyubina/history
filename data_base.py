class Global_Events:

    def __init__(self, event_id, year_, month_, day_, level_, event_, stemmed_event):
        self.event_id = event_id
        self.event = event_
        self.date = [year_, month_, day_]
        self.level = level_
        self.stemmed_event = stemmed_event


class Sentenses_with_keys:
    def __init__(self, sent_number_, event_id, text_):
        self.event_id = event_id
        self.sent_number = sent_number_
        self.text = text_

    def __repr__(self):
        return str(self.event_id) + " " + str(self.sent_number)