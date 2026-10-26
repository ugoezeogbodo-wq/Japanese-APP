import json
import random
import datetime as dt
import Character_Dictionary as cd

with open("kradfile-3.6.2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

RADICAL_DB = data["kanji"]

sample = RADICAL_DB.get("語")

for kanji in cd.Kanji_n5:
    sample = RADICAL_DB.get(kanji["character"])
    print(sample)


