from diaries.AbstractDiary import AbstractDiary

class ShibayamaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日はショッピングを楽しみました。新しい服を買って、おいしいラーメンも食べました。充実した一日でした！"

    def get_author(self):
        return "Shibayama"