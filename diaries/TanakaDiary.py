from diaries.AbstractDiary import AbstractDiary

class TanakaDiary(AbstractDiary):

    def get_date(self):
        return "2021-11-28"

    def get_summary(self):
        return "楽しい1日だった"

    def get_author(self):
        return "Tanaka"
