import Character_Dictionary as CD
import datetime as dt
import random
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
advanced = False

def status_check():
    global queue, now, advanced
    now = dt.datetime.now()
    queue = []
    check = 0
    for nihon in CD.katakana_dataset:
        if nihon["status"] > 5:
            check += 1
        
    for nihon in CD.katakana_dataset:
        if nihon["due_time"] == None or nihon["due_time"] <= now :
            queue.append(nihon)

    if check > 40:
        advanced = True
        for nihon in CD.kana_2_dataset:
            if nihon["due_time"] == None or nihon["due_time"] <= now :
                        queue.append(nihon) 
    

def load_new_deck(k_target_l, k_one, k_two, k_three, k_four):
    global target ,final, advanced
    k_one.configure(state="normal", fg_color = ext.cream, border_color = ext.brown, hover_color =ext.linen)
    k_two.configure(state="normal",fg_color = ext.cream, border_color = ext.brown, hover_color =ext.linen)
    k_three.configure(state="normal",fg_color = ext.cream, border_color = ext.brown, hover_color =ext.linen)
    k_four.configure(state="normal",fg_color = ext.cream, border_color = ext.brown, hover_color =ext.linen)
    status_check()
    if queue == []:
        print("You're all caught up! Good Job!")
    target = random.choice(queue)
    disposable = []
    for char in CD.katakana_dataset:
        if char != target:
            disposable.append(char)
    if advanced == True:
        for char in CD.kana_2_dataset:
            if char != target:
                disposable.append(char)
    others = random.sample(disposable, k= 3)
    final = [target] + others
    random.shuffle(final)
    if ext.page == 3:
        k_target_l.configure(text = target["character"])
        print("What is the romaji equivalent of", target["character"], "?")
        k_one.configure(text = final[0]["romaji"])
        k_two.configure(text = final[1]["romaji"])
        k_three.configure(text = final[2]["romaji"])
        k_four.configure(text = final[3]["romaji"])
    elif ext.page == 4:
         k_target_l.configure(text = target["romaji"])
         print("What is the character of", target["romaji"], "?")
         k_one.configure(text = final[0]["character"])
         k_two.configure(text = final[1]["character"])
         k_three.configure(text = final[2]["character"])
         k_four.configure(text = final[3]["character"])

def check_answer(button, k_target_l, k_one, k_two, k_three, k_four):
    global target, now
    now = dt.datetime.now()
    tries = 0
    user_ans = button.cget("text")
    if user_ans == target["romaji"] or user_ans == target["character"]:
            print("Goodjob!")
            if target["status"] != 10 and tries != 1:
                target["status"] += 1
            target["due_time"] = now + stages[target["status"]]
            button.configure(fg_color = ext.right, border_color = ext.dright, hover_color = ext.right )
            tries = 0
            k_one.configure(state="disabled"),
            k_two.configure(state="disabled"),
            k_three.configure(state="disabled"),
            k_four.configure(state="disabled"),
            button.after(1000, lambda: [
            
        load_new_deck(k_target_l, k_one, k_two, k_three, k_four)
    ])
    else:
            button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
            if tries != 1:
                print("Oh no..Remember", target["mnemonic"] )
            if tries != 1:
                if target["status"] != 0:
                    target["status"] -= 1
                tries = 1

def invert_kana(k_target_l, k_one, k_two, k_three, k_four,invert):
    if ext.page == 3:
          ext.page = 4
          invert.configure(text_color= ext.pink, fg_color = ext.cream, hover_color = ext.linen)
          k_target_l.configure(text=target["romaji"])
          k_one.configure(text = final[0]["character"])
          k_two.configure(text = final[1]["character"])
          k_three.configure(text = final[2]["character"])
          k_four.configure(text = final[3]["character"])
    elif ext.page ==4:
        ext.page = 3
        invert.configure(text_color= ext.cream, fg_color = ext.pink, hover_color = ext.dpink)
        k_target_l.configure(text=target["character"])
        k_one.configure(text = final[0]["romaji"],)
        k_two.configure(text = final[1]["romaji"])
        k_three.configure(text = final[2]["romaji"])
        k_four.configure(text = final[3]["romaji"])       
            

