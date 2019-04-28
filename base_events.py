class Global_Events:

    def __init__(self, event_id, start_year_, start_month_, start_day_,end_year_, end_month_, end_day_, event_, stemmed_event):
        self.event_id = event_id
        self.event = event_
        self.date = [start_year_, start_month_, start_day_, end_year_, end_month_, end_day_]
        self.stemmed_event = stemmed_event


class Sentenses_with_keys:
    def __init__(self, sent_number_, event_id, text_):
        self.event_id = event_id
        self.sent_number = sent_number_
        self.text = text_

    def __repr__(self):
        return str(self.event_id) + " " + str(self.sent_number)