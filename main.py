from diaries.DiarySample import DiarySample
from diaries.TanakaDiary import TanakaDiary
from diaries.K23124 import K23124Diary
from diaries.ShibayamaDiary import ShibayamaDiary
from diaries.SuzukiDiary import SuzukiDiary
# ↓のリストには、メンバーの各日記が格納されます。

diaries = [DiarySample(), 
           SuzukiDiary(),
           ShibayamaDiary(),
           K23124Diary(),
           TanakaDiary(),
           ] 


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
