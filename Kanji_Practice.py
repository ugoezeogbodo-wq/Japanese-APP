import Character_Dictionary as CD
import datetime as dt
import random

stages = {
    0: dt.timedelta(seconds=5),
    1: dt.timedelta(minutes=1),
    2: dt.timedelta(minutes=5),
    3: dt.timedelta(minutes=5),
    4: dt.timedelta(days=1),
    5: dt.timedelta(days=2),
    6: dt.timedelta(days=3),
    7: dt.timedelta(days=5),
    8: dt.timedelta(days=7),
    9: dt.timedelta(days=14),
    10: dt.timedelta(days=21)}


queue = []
now = dt.datetime.now()
target = []

def status_check_hira():
    global queue, now
    now = dt.datetime.now()
    queue = []
    
    for nihon in CD.kanji_dataset:
        if nihon["due_time_reading"] == None or nihon["due_time_reading"] <= now :
            queue.append(nihon)


def load_new_deck_hira():
    global target
    status_check_hira()
    if queue == []:
        print("You're all caught up! Good Job!")
    else:
        target = random.choice(queue)
        disposable = []
        for char in CD.kanji_dataset:
            if char != target:
                disposable.append(char)
        others = random.sample(disposable, k= 3)
        final = [target] + others
        random.shuffle(final)
        print("What is the hiragana equivalent of", target["character"], "?")
        for char in final:
            print(char["hiragana"])
        check_answer_hira()

def check_answer_hira():
    global target, now
    now = dt.datetime.now()
    status = False
    tries = 0
    while status == False:
        user_ans = input()
        if user_ans == target["hiragana"]:
            print("Goodjob!")
            if target["status_reading"] != 10 and tries != 1:
                target["status_reading"] += 1
            target["due_time_reading"] = now + stages[target["status_reading"]]
            status = True
        else:
            if tries != 1:
                print("OHNO! Remember", target["mnemonic_reading"])
            if tries != 1:
                if target["status_reading"] != 0:
                    target["status_reading"] -= 1
            tries = 1
    load_new_deck_hira()

def status_check_eng():
    global queue, now
    now = dt.datetime.now()
    queue = []
    
    for nihon in CD.kanji_dataset:
        if nihon["due_time_meaning"] == None or nihon["due_time_meaning"] <= now :
            queue.append(nihon)


def load_new_deck_eng():
    global target
    status_check_eng()
    if queue == []:
        print("You're all caught up! Good Job!")
    else:
        target = random.choice(queue)
        disposable = []
        for char in CD.kanji_dataset:
            if char != target:
                disposable.append(char)
        others = random.sample(disposable, k= 3)
        final = [target] + others
        random.shuffle(final)
        print("What is the english meaning of", target["character"], "?")
        for char in final:
            print(char["meaning"])
        check_answer_eng()

def check_answer_eng():
    global target, now
    now = dt.datetime.now()
    status = False
    tries = 0
    while status == False:
        user_ans = input()
        if user_ans == target["meaning"]:
            print("Goodjob!")
            if target["status_meaning"] != 10 and tries != 1:
                target["status_meaning"] += 1
            target["due_time_meaning"] = now + stages[target["status_meaning"]]
            status = True
        else:
            if tries != 1:
                print("OHNO! Remember", target["mnemonic_meaning"])
            if tries != 1:
                if target["status_meaning"] != 0:
                    target["status_meaning"] -= 1
            tries = 1
    load_new_deck_eng()
            



