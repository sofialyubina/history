class Event:

    def __init__(self, event_id, start_year, start_month, start_day, end_year, end_month, end_day, event_):
        self.event_id = event_id
        self.event = event_
        self.date = [start_year, start_month, start_day, end_year, end_month, end_day]
        # self.stemmed_event = stemmed_event


# class SentensesWithKeys:
#     def __init__(self, sent_number_, event_id, text_):
#         self.event_id = event_id
#         self.sent_number = sent_number_
#         self.text = text_
#
#     def __repr__(self):
#         return str(self.event_id) + " " + str(self.sent_number)
