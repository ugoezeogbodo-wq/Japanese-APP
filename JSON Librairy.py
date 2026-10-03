import json

with open("kradfile-3.6.2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

RADICAL_DB = data["kanji"]

sample = RADICAL_DB.get("語")
print(sample)



