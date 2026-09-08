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
final = []
advanced = False
streak = 0
tries = 0

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

def status_check():
    global queue, now
    now = dt.datetime.now()
    queue = []
    if ext.page == 7 or ext.page == 8:
        for radical in CD.Radicals_b:
            if radical["due_time"] == None  or radical["due_time"] <= now :
                queue.append(radical)
    elif ext.page == 9:
        for radical in CD.Radicals:
            if radical["due_time"] == None  or radical["due_time"] <= now :
                queue.append(radical)

def load_new_deck(mr_target_l, mr_one, mr_two, mr_three, mr_four, mr_target_lt, mr_romaji, indicator, finished):
    global target ,final
    if ext.page == 7 or ext.page == 8:
        mr_one.configure(state="normal", fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        mr_two.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        mr_three.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        mr_four.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
    elif ext.page ==9:
        mr_romaji.configure(fg_color = ext.pink, border_color = ext.cream)
        mr_romaji.configure(state = "normal")
    status_check()
    if queue == []:
        indicator(finished)
    else:
        if ext.page == 7 or ext.page == 8:
            target = random.choice(queue)
            disposable = []
            for radical in CD.Radicals_b:
                if radical["radical"] != target["radical"]:
                    disposable.append(radical)
            others = random.sample(disposable, k= 3)
            final = [target] + others
            random.shuffle(final)
        elif ext.page == 9:
            target = random.choice(queue)
            disposable = []
            for radical in CD.Radicals:
                if radical["radical"] != target["radical"]:
                    disposable.append(radical)
            others = random.sample(disposable, k = 3)
            final = [target] + others
            random.shuffle(final)
        if ext.page == 7:
            mr_target_l.configure(text = target["radical"])
            print("What is the romaji equivalent of", target["radical"], "?")
            mr_one.configure(text = final[0]["meaning"])
            mr_two.configure(text = final[1]["meaning"])
            mr_three.configure(text = final[2]["meaning"])
            mr_four.configure(text = final[3]["meaning"])
        elif ext.page == 8:
            mr_target_l.configure(text = target["meaning"])
            print("What is the character of", target["meaning"], "?")
            mr_one.configure(text = final[0]["radical"])
            mr_two.configure(text = final[1]["radical"])
            mr_three.configure(text = final[2]["radical"])
            mr_four.configure(text = final[3]["radical"])
        elif ext.page == 9:
            mr_target_lt.configure(text = target["radical"])
        if target["meaning2"] is not None:
            print(target["meaning"]+".."+ target["meaning2"])





def check_answer(button, mr_target_l, mr_one, mr_two, mr_three, mr_four, mr_target_lt,mr_romaji,mr_feedback_label, mr_feedback, mr_feedback_t, mr_feedback_label_t,resize, indicator, finished):

    global target, now, streak, tries
    now = dt.datetime.now()
    
   
    if ext.page == 7 or ext.page == 8:
        user_ans = button.cget("text")
    elif ext.page == 9:
         user_ans = mr_romaji.get().strip().lower()
    if user_ans == target["meaning"] or user_ans == target["radical"] or user_ans == target["meaning2"]:
            if tries == 0:
                streak += 1
            if ext.page == 7 or ext.page ==8:
                if streak ==5:
                    mr_feedback.configure(image=ext.chest_5_image)
                    mr_feedback.active_pil_image = ext.chest_5_image._light_image
                    resize()
                    mr_feedback_label.configure(text="Look at that; youve made it to a streak of 5! Knew you could do it! :3 \n Kanji Examples for uuu: " + target["kanji_examples"])
                elif streak == 10:
                    mr_feedback.configure(image=ext.chest_10_image)
                    mr_feedback.active_pil_image = ext.chest_10_image._light_image
                    resize()
                    mr_feedback_label.configure(text="Thats my " + ext.gender + "! Streak of 10! Wooooooo!! Kanji examples:" + target["kanji_examples"])
                else:
                    mr_feedback_label.configure(text="HORRAYY! Look at you go! ;)\n Kanji examples: " + str(target["kanji_examples"]))
                    mr_feedback.configure(image = ext.chest_right_image)
                    mr_feedback.active_pil_image = ext.chest_right_image._light_image
                    resize()
            if ext.page == 9:
                if streak ==5:
                    mr_feedback_t.configure(image=ext.chest_5_image)
                    mr_feedback_t.active_pil_image = ext.chest_5_image._light_image
                    resize()
                    mr_feedback_label_t.configure(text="Look at that; youve made it to a streak of 5! Knew you could do it! :3 \n Kanji Examples for uuu: " + target["kanji_examples"])
                elif streak == 10:
                    mr_feedback_t.configure(image=ext.chest_10_image)
                    mr_feedback_t.active_pil_image = ext.chest_5_image._light_image
                    resize()
                    mr_feedback_label_t.configure(text="Thats my " + ext.gender + "! Streak of 10! Wooooooo!! Kanji examples:" + target["kanji_examples"])
                else:
                    mr_feedback_label_t.configure(text="HORRAYY! Look at you go! ;)\n Kanji examples: " + str(target["kanji_examples"]))
                    mr_feedback_t.configure(image = ext.chest_right_image)
                    mr_feedback_t.active_pil_image = ext.chest_right_image._light_image
                    resize()
            if target["status"] != 10 and tries != 1:
                target["status"] += 1
            target["due_time"] = now + stages[target["status"]]
            tries = 0
            if ext.page == 7 or ext.page == 8:
                button.configure(fg_color = ext.right, border_color = ext.dright, hover_color = ext.right )
                mr_one.configure(state="disabled"),
                mr_two.configure(state="disabled"),
                mr_three.configure(state="disabled"),
                mr_four.configure(state="disabled"),
                button.after(1000, lambda: [load_new_deck(mr_target_l, mr_one, mr_two, mr_three, mr_four, mr_target_lt, mr_romaji,indicator, finished)])
            elif ext.page == 9:
                 mr_romaji.configure(fg_color = ext.right, border_color = ext.dright)
                 mr_romaji.configure(state = "disabled")
                 mr_romaji.after(250, lambda: [load_new_deck(mr_target_l, mr_one, mr_two, mr_three, mr_four, mr_target_lt, mr_romaji,indicator, finished), mr_romaji.delete(0, "end")])
    else:
            streak = 0
            if ext.page == 7 or ext.page == 8:
                button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
            elif ext.page == 9:
                 mr_romaji.configure(fg_color = ext.wrong, border_color = ext.dwrong)
                 mr_romaji.delete(0, "end")
            if tries != 1:
                if ext.page == 7 or ext.page == 8:
                    mr_feedback_label.configure(text="Oh no. Remember "+ target["mnemonic"] )
                    mr_feedback.configure(image = ext.chest_wrong_image)
                    mr_feedback.active_pil_image = ext.chest_wrong_image._light_image
                    resize()
                elif ext.page == 9:
                    mr_feedback_label_t.configure(text="Oh no. Remember "+ target["mnemonic"] )
                    mr_feedback_t.configure(image = ext.chest_wrong_image)
                    mr_feedback_t.active_pil_image = ext.chest_wrong_image._light_image
                    resize()
            if tries != 1:
                if target["status"] != 0:
                    target["status"] -= 1
                tries = 1            

def invert_mr(mr_target_l, mr_one, mr_two, mr_three, mr_four,invert):
    if ext.page == 7:
          ext.page = 8
          invert.configure(text_color= ext.pink, fg_color = ext.cream, hover_color = ext.linen)
          mr_target_l.configure(text=target["meaning"])
          mr_one.configure(text = final[0]["radical"])
          mr_two.configure(text = final[1]["radical"])
          mr_three.configure(text = final[2]["radical"])
          mr_four.configure(text = final[3]["radical"])
    elif ext.page ==8:
        ext.page = 7
        invert.configure(text_color= ext.cream, fg_color = ext.pink, hover_color = ext.dpink)
        mr_target_l.configure(text=target["radical"])
        mr_one.configure(text = final[0]["meaning"],)
        mr_two.configure(text = final[1]["meaning"])
        mr_three.configure(text = final[2]["meaning"])
        mr_four.configure(text = final[3]["meaning"])


