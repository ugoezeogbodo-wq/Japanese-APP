import Character_Dictionary as CD
import datetime as dt
import random

import customtkinter as ctk
import Extra as ext


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
    

def load_new_deck(target_l, one, two, three, four):
    global target 
    one.configure(state="normal", fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
    two.configure(state="normal",fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
    three.configure(state="normal",fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
    four.configure(state="normal",fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
    status_check()
    if queue == []:
        print("You're all caught up! Good Job!")
    if ext.page == 1:
        target = random.choice(queue)
        target_l.configure(text = target["character"])
        disposable = []
        for char in CD.hiragana_dataset:
            if char != target:
                disposable.append(char)
        others = random.sample(disposable, k= 3)
        final = [target] + others
        random.shuffle(final)
        print("What is the romaji equivalent of", target["character"], "?")
        one.configure(text = final[0]["romaji"])
        two.configure(text = final[1]["romaji"])
        three.configure(text = final[2]["romaji"])
        four.configure(text = final[3]["romaji"])
            


def check_answer(button, target_l, one, two, three, four):
    global target, now
    now = dt.datetime.now()
    tries = 0
    user_ans = button.cget("text")
    if user_ans == target["romaji"]:
            print("Goodjob!")
            if target["status"] != 10 and tries != 1:
                target["status"] += 1
            target["due_time"] = now + stages[target["status"]]
            button.configure(fg_color = ext.right, border_color = ext.dright, hover_color = ext.right )
            tries = 0
            one.configure(state="disabled"),
            two.configure(state="disabled"),
            three.configure(state="disabled"),
            four.configure(state="disabled"),
            button.after(1000, lambda: [
            
        load_new_deck(target_l, one, two, three, four)
    ])
    else:
            button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
            if tries != 1:
                print("Oh no..Remember", target["mnemonic"] )
            if tries != 1:
                if target["status"] != 0:
                    target["status"] -= 1
                tries = 1
    

        
            



