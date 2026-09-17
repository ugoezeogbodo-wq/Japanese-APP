import Character_Dictionary as CD
import datetime as dt
import random
import Extra as ext

stages = {
    0: dt.timedelta(seconds=5),
    1: dt.timedelta(minutes=1),
    2: dt.timedelta(minutes=5),
    3: dt.timedelta(minutes=10),
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
tries = 0

def status_check_hira():
    global queue, now
    now = dt.datetime.now()
    queue = []
    
    for nihon in CD.kanji_dataset_hira:
        if nihon["due_time_reading"] == None or nihon["due_time_reading"] <= now :
            queue.append(nihon)


def load_new_deck_hira(m_target_l, m_one, m_two, m_three, m_four, m_target_lt, m_romaji, indicator, finished):
    global target, final
    if ext.page == 10 or ext.page == 11:
        m_one.configure(state="normal", fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        m_two.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        m_three.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        m_four.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
    elif ext.page == 12:
        m_romaji.configure(fg_color = ext.pink, border_color = ext.cream)
        m_romaji.configure(state = "normal")
    status_check_hira()
    if queue == []:
        indicator(finished)
    else:
        target = random.choice(queue)
        disposable = []
        for char in CD.kanji_dataset_hira:
            if char != target:
                disposable.append(char)
        others = random.sample(disposable, k= 3)
        final = [target] + others
        random.shuffle(final)
        if ext.page == 10:
            m_target_l.configure(text = target["character"])
            print("What is the hiragana equivalent of", target["character"], "?")
            m_one.configure(text = final[0]["hiragana"]+"\n("+final[0]["romaji"]+")")
            m_two.configure(text = final[1]["hiragana"]+"\n("+final[1]["romaji"]+")")
            m_three.configure(text = final[2]["hiragana"]+"\n("+final[2]["romaji"]+")")
            m_four.configure(text = final[3]["hiragana"]+"\n("+final[3]["romaji"]+")")
        elif ext.page == 11:
            m_target_l.configure(text = target["hiragana"]+"("+target["romaji"]+")")
            print("What is the character of", target["romaji"], "?")
            m_one.configure(text = final[0]["character"])
            m_two.configure(text = final[1]["character"])
            m_three.configure(text = final[2]["character"])
            m_four.configure(text = final[3]["character"])   
        elif ext.page == 12:
            m_target_lt.configure(text = target["character"])
        

def check_answer_hira(button, m_target_l, m_one, m_two, m_three, m_four, m_target_lt,m_romaji,m_feedback_label, m_feedback, m_feedback_t, m_feedback_label_t,resize,indicator, finished,cstreak):
    global target, now
    now = dt.datetime.now()
    tries = 0
    if ext.page == 10 or ext.page == 11:
        user_ans = button.cget("text")
    elif ext.page == 12:
        user_ans = m_romaji.get().strip().lower()
    if user_ans == target["hiragana"] or user_ans == target ["character"] or user_ans == target["hiragana"]+"\n("+target["romaji"]+")" or user_ans ==target["romaji"]:
        if tries == 0:
            ext.streak += 1
            if ext.t_streak < ext.streak:
                ext.t_streak = ext.streak
            cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
        if ext.page == 10 or ext.page == 11:
            if ext.streak ==5:
                m_feedback.configure(image=ext.chest_5_image)
                m_feedback.active_pil_image = ext.chest_5_image._light_image
                resize()
                m_feedback_label.configure(text="Wow, you've gotten to a streak of 5! Can we make it to 10 next?")
            elif ext.streak == 10:
                m_feedback.configure(image=ext.chest_10_image)
                m_feedback.active_pil_image = ext.chest_10_image._light_image
                resize()
                m_feedback_label.configure(text="Woah...Streak of 10! Amazing..")
            else:
                m_feedback_label.configure(text="Goodjob, keep up the good work")
                m_feedback.configure(image = ext.chest_right_image)
                m_feedback.active_pil_image = ext.chest_right_image._light_image
                resize()
        if ext.page == 12:
            if ext.streak ==5:
                m_feedback_t.configure(image=ext.chest_5_image)
                m_feedback_t.active_pil_image = ext.chest_5_image._light_image
                resize()
                m_feedback_label_t.configure(text="Wow, you've gotten to a streak of 5!")
            elif ext.streak == 10:
                m_feedback_t.configure(image=ext.chest_10_image)
                m_feedback_t.active_pil_image = ext.chest_5_image._light_image
                resize()
                m_feedback_label_t.configure(text="Woah...Streak of 10! Amazing..")
            else:
                m_feedback_label_t.configure(text="Goodjob, keep up the good work")
                m_feedback_t.configure(image = ext.chest_right_image)
                m_feedback_t.active_pil_image = ext.chest_right_image._light_image
                resize()  
        if target["status_reading"] != 10 and tries != 1:
            target["status_reading"] += 1
        target["due_time"] = now + stages[target["status_reading"]]
        tries = 0   
        if ext.page == 10 or ext.page == 11:
            button.configure(fg_color = ext.right, border_color = ext.dright, hover_color = ext.right )
            m_one.configure(state="disabled"),
            m_two.configure(state="disabled"),
            m_three.configure(state="disabled"),
            m_four.configure(state="disabled"),
            button.after(1000, lambda: [load_new_deck_hira(m_target_l, m_one, m_two, m_three, m_four, m_target_lt, m_romaji, indicator, finished)])
        elif ext.page == 12:
            m_romaji.configure(fg_color = ext.right, border_color = ext.dright)
            m_romaji.configure(state = "disabled")
            m_romaji.after(250, lambda: [load_new_deck_hira(m_target_l, m_one, m_two, m_three, m_four, m_target_lt, m_romaji,indicator,finished), m_romaji.delete(0, "end")])      
    else:
                ext.streak = 0
                cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
                if ext.page == 10 or ext.page == 11:
                    button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
                elif ext.page == 12:
                    m_romaji.configure(fg_color = ext.wrong, border_color = ext.dwrong)
                    m_romaji.delete(0, "end")
                if tries != 1:
                    if ext.page == 10 or ext.page == 11:
                        m_feedback_label.configure(text="Oh no. Remember "+ target["mnemonic_reading"] )
                        m_feedback.configure(image = ext.chest_wrong_image)
                        m_feedback.active_pil_image = ext.chest_wrong_image._light_image
                        resize()
                    elif ext.page == 12:
                        m_feedback_label_t.configure(text="Oh no. Remember "+ target["mnemonic_reading"] )
                        m_feedback_t.configure(image = ext.chest_wrong_image)
                        m_feedback_t.active_pil_image = ext.chest_wrong_image._light_image
                        resize()
                if tries != 1:
                    if target["status_reading"] != 0:
                        if target["status_reading"] >= 5:
                            target["status_reading"] = max(1, target["status_reading"] - 2)
                        else:
                            target["status_reading"] = max(1, target["status_reading"] - 1)
                tries = 1
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

def load_new_deck(text_just, mr_one, mr_two, mr_three, mr_four, text_just_t, mr_romaji, indicator, finished):
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
            seen_symbols = {target["radical"]}
            seen_symbol = {target["meaning"]}
            for radical in CD.Radicals_b:
                symbol = radical["radical"]
                if symbol not in seen_symbols:
                    seen_symbols.add(symbol)
                    symbol = radical["meaning"]
                    if symbol not in seen_symbol:
                        seen_symbol.add(symbol)
                        disposable.append(radical)
            others = random.sample(disposable, k= 3)
            final = [target] + others
            random.shuffle(final)
        elif ext.page == 9:
            target = random.choice(queue)
            disposable = []
            seen_symbols = {target["radical"]}
            for radical in CD.Radicals:
                symbol = radical["radical"]
                if symbol not in seen_symbols:
                    seen_symbols.add(symbol)
                    disposable.append(radical)
            others = random.sample(disposable, k = 3)
            final = [target] + others
            random.shuffle(final)
        if ext.page == 7:
            text_just.configure(text = target["radical"]+ " (" + target["kanji_examples"]+ ")")
            print("What is the romaji equivalent of", target["radical"], "?")
            mr_one.configure(text = final[0]["meaning"])
            mr_two.configure(text = final[1]["meaning"])
            mr_three.configure(text = final[2]["meaning"])
            mr_four.configure(text = final[3]["meaning"])
        elif ext.page == 8:
            text_just.configure(text = target["meaning"])
            print("What is the character of", target["meaning"], "?")
            mr_one.configure(text = final[0]["radical"]+ " (" + final[0]["kanji_examples"] + ")")
            mr_two.configure(text = final[1]["radical"]+ " (" + final[1]["kanji_examples"] + ")")
            mr_three.configure(text = final[2]["radical"]+ " (" + final[2]["kanji_examples"] + ")")
            mr_four.configure(text = final[3]["radical"]+ " (" + final[3]["kanji_examples"] + ")")
        elif ext.page == 9:
            text_just_t.configure(text = target["radical"]+ " (" + target["kanji_examples"]+ ")")
        if target["meaning2"] is not None:
            print(target["meaning"]+".."+ target["meaning2"])





def check_answer(button, text_just, mr_one, mr_two, mr_three, mr_four, text_just_t,mr_romaji,mr_feedback_label, mr_feedback, mr_feedback_t, mr_feedback_label_t,resize, indicator, finished, cstreak):

    global target, now,tries
    now = dt.datetime.now()
    
   
    if ext.page == 7 or ext.page == 8:
        user_ans = button.cget("text")
    elif ext.page == 9:
         user_ans = mr_romaji.get().strip().lower()
    if user_ans == target["meaning"] or user_ans == target["radical"]+ " (" + target["kanji_examples"]+ ")" or user_ans == target["meaning2"]:
            if tries == 0:
                ext.streak += 1
                if ext.t_streak < ext.streak:
                    ext.t_streak = ext.streak
                cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
            if ext.page == 7 or ext.page ==8:
                if ext.streak ==5:
                    mr_feedback.configure(image=ext.chest_5_image)
                    mr_feedback.active_pil_image = ext.chest_5_image._light_image
                    resize()
                    mr_feedback_label.configure(text="Look at that; youve made it to a streak of 5! Knew you could do it! :3")
                elif ext.streak == 10:
                    mr_feedback.configure(image=ext.chest_10_image)
                    mr_feedback.active_pil_image = ext.chest_10_image._light_image
                    resize()
                    mr_feedback_label.configure(text="Thats my " + ext.gender + "! Streak of 10! Wooooooo!!")
                else:
                    mr_feedback_label.configure(text="HORRAYY! Look at you go! ;)")
                    mr_feedback.configure(image = ext.chest_right_image)
                    mr_feedback.active_pil_image = ext.chest_right_image._light_image
                    resize()
            if ext.page == 9:
                if ext.streak ==5:
                    mr_feedback_t.configure(image=ext.chest_5_image)
                    mr_feedback_t.active_pil_image = ext.chest_5_image._light_image
                    resize()
                    mr_feedback_label_t.configure(text="Look at that; youve made it to a streak of 5! Knew you could do it! :3")
                elif ext.streak == 10:
                    mr_feedback_t.configure(image=ext.chest_10_image)
                    mr_feedback_t.active_pil_image = ext.chest_5_image._light_image
                    resize()
                    mr_feedback_label_t.configure(text="Thats my " + ext.gender + "! Streak of 10! Wooooooo!!")
                else:
                    mr_feedback_label_t.configure(text="HORRAYY! Look at you go! ;)")
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
                button.after(1000, lambda: [load_new_deck(text_just=text_just, mr_one=mr_one, mr_two=mr_two, mr_three=mr_three, mr_four=mr_four, text_just_t=text_just_t, mr_romaji=mr_romaji,indicator=indicator, finished=finished)])
            elif ext.page == 9:
                 mr_romaji.configure(fg_color = ext.right, border_color = ext.dright)
                 mr_romaji.configure(state = "disabled")
                 mr_romaji.after(250, lambda: [load_new_deck(text_just, mr_one, mr_two, mr_three, mr_four, text_just_t, mr_romaji,indicator, finished), mr_romaji.delete(0, "end")])
    else:
            ext.streak = 0
            cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
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
                    if target["status"] >= 5:
                        target["status"] = max(1, target["status"] - 2)
                    else:
                        target["status"] = max(1, target["status"] - 1)
            tries = 1            

def invert_mr(text_just, mr_one, mr_two, mr_three, mr_four,invert, m_target_l, m_one, m_two,m_three,m_four):
    if ext.page == 7:
          ext.page = 8
          invert.configure(text_color= ext.pink, fg_color = ext.cream, hover_color = ext.linen)
          text_just.configure(text=target["meaning"])
          mr_one.configure(text = final[0]["radical"]+ " (" + final[0]["kanji_examples"] + ")")
          mr_two.configure(text = final[1]["radical"]+ " (" + final[1]["kanji_examples"] + ")")
          mr_three.configure(text = final[2]["radical"]+ " (" + final[2]["kanji_examples"] + ")")
          mr_four.configure(text = final[3]["radical"]+ " (" + final[3]["kanji_examples"] + ")")
    elif ext.page ==8:
        ext.page = 7
        invert.configure(text_color= ext.cream, fg_color = ext.pink, hover_color = ext.dpink)
        text_just.configure(text = target["radical"]+ " (" + target["kanji_examples"]+ ")")
        mr_one.configure(text = final[0]["meaning"],)
        mr_two.configure(text = final[1]["meaning"])
        mr_three.configure(text = final[2]["meaning"])
        mr_four.configure(text = final[3]["meaning"])
    elif ext.page == 10:
              ext.page = 11
              invert.configure(text_color= ext.pink, fg_color = ext.cream, hover_color = ext.linen)
              m_target_l.configure(text=target["hiragana"]+"("+target["romaji"]+")")
              m_one.configure(text = final[0]["character"])
              m_two.configure(text = final[1]["character"])
              m_three.configure(text = final[2]["character"])
              m_four.configure(text = final[3]["character"])
    elif ext.page == 11:
                ext.page == 10
                m_target_l.configure(text = target["character"])
                m_one.configure(text = final[0]["hiragana"]+"\n("+final[0]["romaji"]+")")
                m_two.configure(text = final[1]["hiragana"]+"\n("+final[1]["romaji"]+")")
                m_three.configure(text = final[2]["hiragana"]+"\n("+final[2]["romaji"]+")")
                m_four.configure(text = final[3]["hiragana"]+"\n("+final[3]["romaji"]+")")


