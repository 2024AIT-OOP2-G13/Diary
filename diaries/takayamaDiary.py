from diaries.AbstractDiary import AbstractDiary

class takayamaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日の講義はむずかしかったです"

    def get_author(self):
        return "Takayama"