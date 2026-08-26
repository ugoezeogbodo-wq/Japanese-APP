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
final = []
advanced = False

def status_check():
    global queue, now, advanced
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
        advanced = True
        for nihon in CD.hira_2_dataset:
            if nihon["due_time"] == None or nihon["due_time"] <= now :
                        queue.append(nihon)   

    

def load_new_deck(target_l, one, two, three, four, target_lt, romaji):
    global target ,final, advanced
    if ext.page == 1 or ext.page ==2:
        one.configure(state="normal", fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
        two.configure(state="normal",fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
        three.configure(state="normal",fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
        four.configure(state="normal",fg_color = ext.brown, border_color = ext.dbrown, hover_color =ext.dbrown)
    elif ext.page ==5:
        romaji.configure(fg_color = ext.brown, border_color = ext.dbrown)
        romaji.configure(state = "normal")
    status_check()
    if queue == []:
        print("You're all caught up! Good Job!")
    target = random.choice(queue)
    disposable = []
    for char in CD.hiragana_dataset:
        if char != target:
            disposable.append(char)
    if advanced == True:
        for char in CD.hira_2_dataset:
            if char != target:
                disposable.append(char)
    others = random.sample(disposable, k= 3)
    final = [target] + others
    random.shuffle(final)
    if ext.page == 1:
        target_l.configure(text = target["character"])
        print("What is the romaji equivalent of", target["character"], "?")
        one.configure(text = final[0]["romaji"])
        two.configure(text = final[1]["romaji"])
        three.configure(text = final[2]["romaji"])
        four.configure(text = final[3]["romaji"])
    elif ext.page == 2:
         target_l.configure(text = target["romaji"])
         print("What is the character of", target["romaji"], "?")
         one.configure(text = final[0]["character"])
         two.configure(text = final[1]["character"])
         three.configure(text = final[2]["character"])
         four.configure(text = final[3]["character"])
    elif ext.page == 5:
        target_lt.configure(text = target["character"]) 
            


def check_answer(button, target_l, one, two, three, four, target_lt,romaji,feedback_label):
    global target, now
    now = dt.datetime.now()
    tries = 0
    if ext.page == 1 or ext.page == 2:
        user_ans = button.cget("text")
    elif ext.page == 5:
         user_ans = romaji.get().strip().lower()
    if user_ans == target["romaji"] or user_ans == target["character"]:
            feedback_label.configure(text="Goodjob, keep up the good work")
            if target["status"] != 10 and tries != 1:
                target["status"] += 1
            target["due_time"] = now + stages[target["status"]]
            tries = 0
            if ext.page == 1 or ext.page == 2:
                button.configure(fg_color = ext.right, border_color = ext.dright, hover_color = ext.right )
                one.configure(state="disabled"),
                two.configure(state="disabled"),
                three.configure(state="disabled"),
                four.configure(state="disabled"),
                button.after(1000, lambda: [load_new_deck(target_l, one, two, three, four, target_lt, romaji)])
            elif ext.page == 5:
                 romaji.configure(fg_color = ext.right, border_color = ext.dright)
                 romaji.configure(state = "disabled")
                 romaji.after(250, lambda: [load_new_deck(target_l, one, two, three, four, target_lt, romaji), romaji.delete(0, "end")])
    else:
            if ext.page == 1 or ext.page ==2:
                button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
            elif ext.page == 5:
                 romaji.configure(fg_color = ext.wrong, border_color = ext.dwrong)
                 romaji.delete(0, "end")
            if tries != 1:
                feedback_label.configure(text="Oh no. Remember "+ target["mnemonic"] )
            if tries != 1:
                if target["status"] != 0:
                    target["status"] -= 1
                tries = 1
    
def invert_hira(target_l, one, two, three, four,invert):
    if ext.page == 1:
          ext.page = 2
          invert.configure(text_color= ext.pink, fg_color = ext.cream, hover_color = ext.linen)
          target_l.configure(text=target["romaji"])
          one.configure(text = final[0]["character"])
          two.configure(text = final[1]["character"])
          three.configure(text = final[2]["character"])
          four.configure(text = final[3]["character"])
    elif ext.page ==2:
        ext.page = 1
        invert.configure(text_color= ext.cream, fg_color = ext.pink, hover_color = ext.dpink)
        target_l.configure(text=target["character"])
        one.configure(text = final[0]["romaji"],)
        two.configure(text = final[1]["romaji"])
        three.configure(text = final[2]["romaji"])
        four.configure(text = final[3]["romaji"])


        
            



