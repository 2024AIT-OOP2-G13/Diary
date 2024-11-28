from diaries.AbstractDiary import AbstractDiary
<<<<<<< Updated upstream
class NagataniDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-09"
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。
講義についていくのはしんどかった。

"""
=======

class takayamaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日の講義はむずかしかったです"

>>>>>>> Stashed changes
    def get_author(self):
        return "Takayama"