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

def status_check():
    global queue, now
    now = dt.datetime.now()
    queue = []
    check = 0
    for nihon in CD.hiragana_dataset:
        if nihon["status"] > 5:
            check += 1
        
    for nihon in CD.hiragana_dataset:
        if nihon["due_time"] == None or nihon["due_time"] <= now :
            queue.append(nihon)

    if check > 40:
        for nihon in CD.hira_2_dataset:
            if nihon["due_time"] == None or nihon["due_time"] <= now :
                        queue.append(nihon)   
    

def load_new_deck():
    global target
    status_check()
    if queue == []:
        print("You're all caught up! Good Job!")
    else:
        target = random.choice(queue)
        disposable = []
        for char in CD.hiragana_dataset:
            if char != target:
                disposable.append(char)
        others = random.sample(disposable, k= 3)
        final = [target] + others
        random.shuffle(final)
        print("What is the romaji equivalent of", target["character"], "?")
        for char in final:
            print(char["romaji"])
        check_answer()

def check_answer():
    global target, now
    now = dt.datetime.now()
    status = False
    tries = 0
    while status == False:
        user_ans = input()
        if user_ans == target["romaji"]:
            print("Goodjob!")
            if target["status"] != 10 and tries != 1:
                target["status"] += 1
            target["due_time"] = now + stages[target["status"]]
            status = True
        else:
            if tries != 1:
                print("OHNO! Remember", target["mnemonic"])
            if tries != 1:
                if target["status"] != 0:
                    target["status"] -= 1
            tries = 1
    load_new_deck()

        
            



