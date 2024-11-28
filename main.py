from diaries.DiarySample import DiarySample
from diaries.K23124 import K23124Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           K23124Diary(),
           ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
