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


queue_r = []
queue_m = []
now = dt.datetime.now()
target = []
final = []
advanced = False
tries = 0
m = ""
r = ""
track = 0 
affirm = ["Hooray! You got itttt!", "Now thats what i call precision!", "You're a master already! So cool!"]
affirm2 = ["Thats it! Knew you could do it!", "Look at you go, not a second passes when u dont impress me!", "I cant help but smile when you do so well!"]
def which_deck():
    if ext.c_deck == "N_5 Deck":
        ext.c_deck = ext.deck_n["n_5"]
    if ext.c_deck == "N_4 Deck":
        ext.c_deck = ext.deck_n["n_4"]
    if ext.c_deck == "N_3 Deck":
        ext.c_deck = ext.deck_n["n_3"]
    if ext.c_deck == "N_2 Deck":
        ext.c_deck = ext.deck_n["n_2"]
    if ext.c_deck == "N_1 Deck":
        ext.c_deck = ext.deck_n["n_1"]
    if ext.c_deck == ext.title1:
        ext.c_deck = ext.deck_n["ext_1"]
    if ext.c_deck == ext.title2:
        ext.c_deck = ext.deck_n["ext_2"]
    if ext.c_deck == ext.title3:
        ext.c_deck = ext.deck_n["ext_3"]

    
    print("Hello")
    
    
    
    
def status_check_hira():
    global queue_r, now, queue_m
    now = dt.datetime.now()
    queue_r = []
    queue_m = []

    which_deck()
    

    for nihon in ext.c_deck:
        if nihon["due_time_reading"] != None and nihon["due_time_reading"] <= now :
            queue_r.append(nihon)
        if nihon["due_time_meaning"] != None and nihon["due_time_meaning"] <= now :
            queue_m.append(nihon) 
    print(queue_m)

def load_new_deck_0(target_l, one, two, three, four, target_lt, romaji, indicator, finished):
    global target,final,m,r
    if ext.page == 10 or ext.page == 11:
        one.configure(state="normal", fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        two.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        three.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
        four.configure(state="normal",fg_color = ext.pink, border_color = ext.cream, hover_color =ext.dpink)
    elif ext.page == 12:
        romaji.configure(fg_color = ext.pink, border_color = ext.cream)
        romaji.configure(state = "normal") 

    status_check_hira() 

    if queue_m == [] and queue_r == []:
        print("supes cool")
        indicator(finished)
    else:
        random_integer = random.randint(1, 2)
        if queue_m != [] and queue_r != []:
            if random_integer == 1:
                target = random.choice(queue_m)
                m = "y"
                r = "n"
            else:
                target = random.choice(queue_r)
                r = "y"
                m = "n"
        elif queue_m == [] and queue_r != []:
            target = random.choice(queue_r)
            r = "y"
            m = "n"
        elif queue_m != [] and queue_r == []:
            target = random.choice(queue_m)
            m = "y"
            r = "n"
        disposable = []
        if len(ext.c_deck) >= 4:
            for card in ext.c_deck:
                if card != target:
                    disposable.append(card)
        else:
            for card in CD.Kanji_n5:
                if card != target:
                    disposable.append(card)
        others = random.sample(disposable, k= 3)
        final = [target] + others
        random.shuffle(final)
        if ext.page == 10:
            if m == "y":
                target_l.configure(text = target["character"])
                print("What is the meaning of", target["character"], "?")
                one.configure(text = final[0]["meaning"])
                two.configure(text = final[1]["meaning"])
                three.configure(text = final[2]["meaning"])
                four.configure(text = final[3]["meaning"]) 
            else:
                target_l.configure(text = target["character"])
                print("What is the romaji equivalent of", target["character"], "?")
                one.configure(text = final[0]["hiragana"] + "\n(" + final[0]["romaji"] + ")")
                two.configure(text = final[1]["hiragana"]+ "\n(" + final[1]["romaji"] + ")")
                three.configure(text = final[2]["hiragana"]+ "\n(" + final[2]["romaji"] + ")")
                four.configure(text = final[3]["hiragana"]+ "\n(" + final[3]["romaji"] + ")")
        elif ext.page == 11:
            if m == "y":
                target_l.configure(text = target["meaning"])
                print("What is the character of", target["character"], "?")
                one.configure(text = final[0]["character"])
                two.configure(text = final[1]["character"])
                three.configure(text = final[2]["character"])
                four.configure(text = final[3]["character"])
            else:
                target_l.configure(text = target["hiragana"] + "(" + target["romaji"] + ")")
                print("What is the romaji equivalent of", target["character"], "?")
                one.configure(text = final[0]["character"])
                two.configure(text = final[1]["character"])
                three.configure(text = final[2]["character"])
                four.configure(text = final[3]["character"])
        elif ext.page == 12:
            if m == "y":
                target_lt.configure(text = "(M) " + target["character"])
            else:
                target_lt.configure(text = "(R) " + target["character"])

def check_answer_0(button, target_l, one, two, three, four, target_lt,romaji,feedback_label, feedback, feedback_t, feedback_label_t,resize,indicator, finished,cstreak):
    global target,now,tries,affirm2, track
    now = dt.datetime.now()

    if ext.page == 10 or ext.page == 11:
            user_ans = button.cget("text")
    elif ext.page == 12:
             user_ans = romaji.get().strip().lower()


    if ext.page == 10 or ext.page == 11:
        if user_ans.startswith(target["hiragana"]) or user_ans == target["character"] or user_ans == target["meaning"] or user_ans == target["romaji"]:
            if tries == 0:
                ext.streak += 1
                if ext.t_streak < ext.streak:
                    ext.t_streak = ext.streak
                if ext.t_streak > ext.h_streak:
                    ext.h_streak = ext.t_streak
                cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
            if ext.page == 10 or ext.page == 11:
                if ext.streak ==5:
                    feedback.configure(image=ext.kai_5_image)
                    if ext.mode == "D":
                        feedback.active_pil_image = ext.kai_5_image._dark_image
                    else:
                        feedback.active_pil_image = ext.kai_5_image._light_image
                    resize()
                    feedback_label.configure(text="That's my " + ext.gender + "! Look at that streak of 5")
                elif ext.streak == 10:
                    feedback.configure(image=ext.kai_10_image)
                    if ext.mode == "D":
                        feedback.active_pil_image = ext.kai_10_image._dark_image
                    else:
                        feedback.active_pil_image = ext.kai_10_image._light_image
                    resize()
                    feedback_label.configure(text="STREAK OF 10!. Thats amazing! I'm so proud of you!")
                else:
                                        chose = random.randint(0,2)
                                        feedback_label.configure(text= affirm2[chose])
                                        if track == 0:
                                            feedback.configure(image = ext.kai_right_image)
                                            track = 1
                                            if ext.mode == "D":
                                                feedback.active_pil_image = ext.kai_right_image._dark_image
                                            else:
                                                feedback.active_pil_image = ext.kai_right_image._light_image
                                        else:
                                            feedback.configure(image = ext.kai_right2_image) 
                                            track = 0
                                            if ext.mode == "D":
                                                feedback.active_pil_image = ext.kai_right2_image._dark_image
                                            else:
                                                feedback.active_pil_image = ext.kai_right2_image._light_image
                                        resize()
            if m ==  "y":
                if target["status_meaning"] != 10 and tries != 1:
                    target["status_meaning"] += 1
                if tries == 0 :
                    target["due_time_meaning"] = now + stages[target["status_meaning"]]
            else:
                if target["status_reading"] != 10 and tries != 1:
                    target["status_reading"] += 1
                if tries == 0 :
                    target["due_time_reading"] = now + stages[target["status_reading"]]    
            tries = 0
            if ext.page == 10 or ext.page == 11:
                button.configure(fg_color = ext.right, border_color = ext.dright, hover_color = ext.right )
                one.configure(state="disabled"),
                two.configure(state="disabled"),
                three.configure(state="disabled"),
                four.configure(state="disabled"),
                button.after(1000, lambda: [load_new_deck_0(target_l, one, two, three, four, target_lt, romaji, indicator, finished)])
            
        else:
        
                ext.streak = 0
                cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
                if ext.page == 10 or ext.page == 11:
                    button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
                elif ext.page == 12:
                    romaji.configure(fg_color = ext.wrong, border_color = ext.dwrong)
                    romaji.delete(0, "end")
                if tries != 1:
                    if ext.page == 10 or ext.page == 11:
                        if m == "y":
                            feedback_label.configure(text="Don't worry, we all make mistakes. Remember "+ target["mnemonic_meaning"] )
                            feedback.configure(image = ext.kai_wrong_image)
                            if ext.mode == "D":
                                feedback.active_pil_image = ext.kai_wrong_image._dark_image
                            else:
                                feedback.active_pil_image = ext.kai_wrong_image._light_image
                            resize()
                        else:
                            feedback_label.configure(text="Don't worry, we all make mistakes. Remember "+ target["mnemonic_reading"] )
                            feedback.configure(image = ext.kai_wrong_image)
                            if ext.mode == "D":
                                feedback.active_pil_image = ext.kai_wrong_image._dark_image
                            else:
                                feedback.active_pil_image = ext.kai_wrong_image._light_image
                            resize()
                if tries != 1:
                    if m == "y":
                        if target["status_meaning"] != 0:
                            if target["status_meaning"] >= 5:
                                target["status_meaning"] = max(1, target["status_meaning"] - 2,)
                            else:
                                target["status_meaning"] = max(1, target["status_meaning"] - 1)
                    else:
                        if target["status_reading"] != 0:
                            if target["status_reading"] >= 5:
                                target["status_reading"] = max(1, target["status_reading"] - 2,)
                            else:
                                target["status_reading"] = max(1, target["status_reading"] - 1)
                tries = 1
                print(user_ans)
                print(target)




    if ext.page == 12:
            if m == "y":
                if user_ans == target["romaji"]:
                    feedback_label_t.configure(text= "It seems you typed the the romaji instead of the meaning, dont worry you wont be penalized! Try again!")
                    feedback_t.configure(image = ext.kai_wrong_image)
                    if ext.mode == "D":
                        feedback_t.active_pil_image = ext.kai_wrong_image._light_image
                    else:
                        feedback_t.active_pil_image = ext.kai_wrong_image._light_image
                    resize()
                    print("meani ng")
                    return
                elif user_ans.startswith(target["hiragana"]) or user_ans == target["character"] or user_ans == target["meaning"] or user_ans == target["meaning2"]:
                                print("correct")
                                if tries == 0:
                                    ext.streak += 1
                                    if ext.t_streak < ext.streak:
                                        ext.t_streak = ext.streak
                                    if ext.t_streak > ext.h_streak:
                                        ext.h_streak = ext.t_streak
                                    cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
                                if ext.page == 12:
                                    if ext.streak ==5:
                                        feedback_t.configure(image=ext.kai_5_image)
                                        if ext.mode == "D":
                                            feedback_t.active_pil_image = ext.kai_5_image._dark_image
                                        else:
                                            feedback_t.active_pil_image = ext.kai_5_image._light_image
                                        resize()
                                        feedback_label_t.configure(text="That's my " + ext.gender + "! Look at that streak of 5")
                                    elif ext.streak == 10:
                                        feedback_t.configure(image=ext.kai_10_image)
                                        if ext.mode == "D":
                                            feedback_t.active_pil_image = ext.kai_10_image._dark_image
                                        else:
                                            feedback_t.active_pil_image = ext.kai_10_image._light_image
                                        resize()
                                        feedback_label_t.configure(text="STREAK OF 10!. Thats amazing! I'm so proud of you!")
                                    else:
                                                            chose = random.randint(0,2)
                                                            feedback_label_t.configure(text= affirm2[chose])
                                                            if track == 0:
                                                                feedback_t.configure(image = ext.kai_right_image)
                                                                track = 1
                                                                if ext.mode == "D":
                                                                    feedback_t.active_pil_image = ext.kai_right_image._dark_image
                                                                else:
                                                                    feedback_t.active_pil_image = ext.kai_right_image._light_image
                                                            else:
                                                                feedback_t.configure(image = ext.kai_right2_image) 
                                                                track = 0
                                                                if ext.mode == "D":
                                                                    feedback_t.active_pil_image = ext.kai_right2_image._dark_image
                                                                else:
                                                                    feedback_t.active_pil_image = ext.kai_right2_image._light_image
                                                            resize()
                                if m ==  "y":
                                    if target["status_meaning"] != 10 and tries != 1:
                                        target["status_meaning"] += 1
                                    if tries == 0 :
                                        target["due_time_meaning"] = now + stages[target["status_meaning"]]
                                else:
                                    if target["status_reading"] != 10 and tries != 1:
                                        target["status_reading"] += 1
                                    if tries == 0 :
                                        target["due_time_reading"] = now + stages[target["status_reading"]]    
                                tries = 0
                                if ext.page == 12:
                                    romaji.configure(fg_color = ext.right, border_color = ext.dright)
                                    romaji.configure(state = "disabled")
                                    romaji.after(250, lambda: [load_new_deck_0(target_l, one, two, three, four, target_lt, romaji,indicator,finished), romaji.delete(0, "end")])
                else:
                                    print("wrong")
                                    ext.streak = 0
                                    cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
                                    if ext.page == 10 or ext.page == 11:
                                        button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
                                    elif ext.page == 12:
                                        romaji.configure(fg_color = ext.wrong, border_color = ext.dwrong)
                                        romaji.delete(0, "end")
                                    if tries != 1:
                                        if ext.page == 12:
                                            if m == "y":
                                                feedback_label_t.configure(text="Don't worry, we all make mistakes. Remember "+ target["mnemonic_meaning"] )
                                                feedback_t.configure(image = ext.kai_wrong_image)
                                                if ext.mode == "D":
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._dark_image
                                                else:
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._light_image
                                                resize()
                                            else:
                                                feedback_label_t.configure(text="Don't worry, we all make mistakes. Remember "+ target["mnemonic_reading"])
                                                feedback_t.configure(image = ext.kai_wrong_image)
                                                if ext.mode == "D":
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._dark_image
                                                else:
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._light_image
                                                resize()
                                    if tries != 1:
                                        if m == "y":
                                            if target["status_meaning"] != 0:
                                                if target["status_meaning"] >= 5:
                                                    target["status_meaning"] = max(1, target["status_meaning"] - 2,)
                                                else:
                                                    target["status_meaning"] = max(1, target["status_meaning"] - 1)
                                        else:
                                            if target["status_reading"] != 0:
                                                if target["status_reading"] >= 5:
                                                    target["status_reading"] = max(1, target["status_reading"] - 2,)
                                                else:
                                                    target["status_reading"] = max(1, target["status_reading"] - 1)
                                    tries = 1
                                    print(user_ans)
                                    print(target)




            elif r == "y":
                if user_ans == target["meaning"] or user_ans == target["meaning2"]:
                                    feedback_label_t.configure(text= "It seems you typed the meaning instead of the romaji, dont worry you wnot be penalized! Try again!")
                                    feedback_t.configure(image = ext.kai_wrong_image)
                                    if ext.mode == "D":
                                        feedback_t.active_pil_image = ext.kai_wrong_image._dark_image
                                    else:
                                        feedback_t.active_pil_image = ext.kai_wrong_image._light_image
                                    resize()
                                    print("reading")
                elif user_ans.startswith(target["hiragana"]) or user_ans == target["character"] or user_ans == target["romaji"]:
                                print("correct")
                                if tries == 0:
                                    ext.streak += 1
                                    if ext.t_streak < ext.streak:
                                        ext.t_streak = ext.streak
                                    if ext.t_streak > ext.h_streak:
                                        ext.h_streak = ext.t_streak
                                    cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
                                if ext.page == 12:
                                    if ext.streak ==5:
                                        feedback_t.configure(image=ext.kai_5_image)
                                        if ext.mode == "D":
                                            feedback_t.active_pil_image = ext.kai_5_image._dark_image
                                        else:
                                            feedback_t.active_pil_image = ext.kai_5_image._light_image
                                        resize()
                                        feedback_label_t.configure(text="That's my " + ext.gender + "! Look at that streak of 5")
                                    elif ext.streak == 10:
                                        feedback_t.configure(image=ext.kai_10_image)
                                        if ext.mode == "D":
                                            feedback_t.active_pil_image = ext.kai_10_image._dark_image
                                        else:
                                            feedback_t.active_pil_image = ext.kai_10_image._light_image
                                        resize()
                                        feedback_label_t.configure(text="STREAK OF 10!. Thats amazing! I'm so proud of you!")
                                    else:
                                                            chose = random.randint(0,2)
                                                            feedback_label_t.configure(text= affirm2[chose])
                                                            if track == 0:
                                                                feedback_t.configure(image = ext.kai_right_image)
                                                                track = 1
                                                                if ext.mode == "D":
                                                                    feedback_t.active_pil_image = ext.kai_right_image._dark_image
                                                                else:
                                                                    feedback_t.active_pil_image = ext.kai_right_image._light_image
                                                            else:
                                                                feedback_t.configure(image = ext.kai_right2_image) 
                                                                track = 0
                                                                if ext.mode == "D":
                                                                    feedback_t.active_pil_image = ext.kai_right2_image._dark_image
                                                                else:
                                                                    feedback_t.active_pil_image = ext.kai_right2_image._light_image
                                                            resize()
                                if m ==  "y":
                                    if target["status_meaning"] != 10 and tries != 1:
                                        target["status_meaning"] += 1
                                    if tries == 0 :
                                        target["due_time_meaning"] = now + stages[target["status_meaning"]]
                                else:
                                    if target["status_reading"] != 10 and tries != 1:
                                        target["status_reading"] += 1
                                    if tries == 0 :
                                        target["due_time_reading"] = now + stages[target["status_reading"]]    
                                tries = 0
                                if ext.page == 12:
                                    romaji.configure(fg_color = ext.right, border_color = ext.dright)
                                    romaji.configure(state = "disabled")
                                    romaji.after(250, lambda: [load_new_deck_0(target_l, one, two, three, four, target_lt, romaji,indicator,finished), romaji.delete(0, "end")])
                else:
                                    print("wrong")
                                    ext.streak = 0
                                    cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
                                    if ext.page == 10 or ext.page == 11:
                                        button.configure(fg_color = ext.wrong, border_color = ext.dwrong, state ="disabled" )
                                    elif ext.page == 12:
                                        romaji.configure(fg_color = ext.wrong, border_color = ext.dwrong)
                                        romaji.delete(0, "end")
                                    if tries != 1:
                                        if ext.page == 12:
                                            if m == "y":
                                                feedback_label_t.configure(text="Don't worry, we all make mistakes. Remember "+ target["mnemonic_meaning"] )
                                                feedback_t.configure(image = ext.kai_wrong_image)
                                                if ext.mode == "D":
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._dark_image
                                                else:
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._light_image
                                                resize()
                                            else:
                                                feedback_label_t.configure(text="Don't worry, we all make mistakes. Remember "+ target["mnemonic_meaning"] )
                                                feedback_t.configure(image = ext.kai_wrong_image)
                                                if ext.mode == "D":
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._dark_image
                                                else:
                                                    feedback_t.active_pil_image = ext.kai_wrong_image._light_image
                                                resize()
                                    if tries != 1:
                                        if m == "y":
                                            if target["status_meaning"] != 0:
                                                if target["status_meaning"] >= 5:
                                                    target["status_meaning"] = max(1, target["status_meaning"] - 2,)
                                                else:
                                                    target["status_meaning"] = max(1, target["status_meaning"] - 1)
                                        else:
                                            if target["status_reading"] != 0:
                                                if target["status_reading"] >= 5:
                                                    target["status_reading"] = max(1, target["status_reading"] - 2,)
                                                else:
                                                    target["status_reading"] = max(1, target["status_reading"] - 1)
                                    tries = 1
                                    print(user_ans)
                                    print(target)                    
            


    














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

    global target, now,tries,track,affirm
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
                if ext.t_streak > ext.h_streak:
                    ext.h_streak = ext.t_streak
                cstreak.configure(text = "Current streak: " + str(ext.streak) + " \nHighest streak: " + str(ext.t_streak)+ " ")
            if ext.page == 7 or ext.page ==8:
                if ext.streak ==5:
                    mr_feedback.configure(image=ext.kai_5_rimage)
                    if ext.mode == "D":
                        mr_feedback.active_pil_image = ext.kai_5_image._light_image
                    else:
                        mr_feedback.active_pil_image = ext.kai_5_rimage._light_image
                    resize()
                    mr_feedback_label.configure(text="Look at that; youve made it to a streak of 5! Knew you could do it! :3")
                elif ext.streak == 10:
                    mr_feedback.configure(image=ext.kai_10_rimage)
                    if ext.mode == "D":
                        mr_feedback.active_pil_image = ext.kai_10_rimage._dark_image
                    else:
                        mr_feedback.active_pil_image = ext.kai_10_rimage._light_image
                    resize()
                    mr_feedback_label.configure(text="Thats my " + ext.gender + "! Streak of 10! Wooooooo!!")
                else:
                    chose = random.randint(0,2)
                    mr_feedback_label.configure(text= affirm[chose])
                    if track == 0:
                        mr_feedback.configure(image = ext.kai_right_rimage)
                        track = 1
                        if ext.mode == "D":
                            mr_feedback.active_pil_image = ext.kai_right_rimage._dark_image
                        else:
                            mr_feedback.active_pil_image = ext.kai_right_rimage._light_image
                    else:
                        mr_feedback.configure(image = ext.kai_right2_rimage) 
                        track = 0
                        if ext.mode == "D":
                            mr_feedback.active_pil_image = ext.kai_right2_rimage._dark_image
                        else:
                            mr_feedback.active_pil_image = ext.kai_right2_rimage._light_image
                                
                    resize()
            if ext.page == 9:
                if ext.streak ==5:
                    mr_feedback_t.configure(image=ext.kai_5_image)
                    if ext.mode == "D":
                        mr_feedback_t.active_pil_image = ext.kai_5_rimage._dark_image
                    else:
                        mr_feedback_t.active_pil_image = ext.kai_5_rimage._light_image
                    resize()
                    mr_feedback_label_t.configure(text="Look at that; youve made it to a streak of 5! Knew you could do it! :3")
                elif ext.streak == 10:
                    mr_feedback_t.configure(image=ext.kai_10_image)
                    if ext.mode == "D":
                        mr_feedback_t.active_pil_image = ext.kai_10_rimage._dark_image
                    else:
                        mr_feedback_t.active_pil_image = ext.kai_10_rimage._light_image
                    resize()
                    mr_feedback_label_t.configure(text="Thats my " + ext.gender + "! Streak of 10! Wooooooo!!")
                else:
                                        chose = random.randint(0,2)
                                        mr_feedback_label_t.configure(text= affirm[chose])
                                        if track == 0:
                                            mr_feedback_t.configure(image = ext.kai_right_rimage)
                                            track = 1
                                            if ext.mode == "D":
                                                mr_feedback_t.active_pil_image = ext.kai_right_rimage._dark_image
                                            else:
                                                mr_feedback_t.active_pil_image = ext.kai_right_rimage._light_image
                                        else:
                                            mr_feedback_t.configure(image = ext.kai_right2_rimage) 
                                            track = 0
                                            if ext.mode == "D":
                                                mr_feedback_t.active_pil_image = ext.kai_right2_rimage._dark_image
                                            else:
                                                mr_feedback_t.active_pil_image = ext.kai_right2_rimage._light_image
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
                    mr_feedback_label.configure(text="Don't worry give it another go just remember "+ target["mnemonic"] )
                    mr_feedback.configure(image = ext.kai_wrong_rimage)
                    if ext.mode == "D":
                        mr_feedback.active_pil_image = ext.kai_wrong_rimage._dark_image
                    else:
                        mr_feedback.active_pil_image = ext.kai_wrong_rimage._light_image
                                        
                    resize()
                elif ext.page == 9:
                    mr_feedback_label_t.configure(text="Don't worry give it another go just remember "+ target["mnemonic"] )
                    mr_feedback_t.configure(image = ext.kai_wrong_rimage)
                    if ext.mode == "D":
                        mr_feedback_t.active_pil_image = ext.kai_wrong_rimage._dark_image
                    else:
                        mr_feedback_t.active_pil_image = ext.kai_wrong_rimage._light_image
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
              if r == "y":
                m_target_l.configure(text=target["hiragana"]+"("+target["romaji"]+")")
                m_one.configure(text = final[0]["character"])
                m_two.configure(text = final[1]["character"])
                m_three.configure(text = final[2]["character"])
                m_four.configure(text = final[3]["character"])
              else:
                m_target_l.configure(text=target["meaning"])
                m_one.configure(text = final[0]["character"])
                m_two.configure(text = final[1]["character"])
                m_three.configure(text = final[2]["character"])
                m_four.configure(text = final[3]["character"])  
    elif ext.page == 11:
                ext.page = 10
                invert.configure(text_color= ext.cream, fg_color = ext.pink, hover_color = ext.dpink)
                if r == "y":
                    m_target_l.configure(text = target["character"])
                    m_one.configure(text = final[0]["hiragana"]+"\n("+final[0]["romaji"]+")")
                    m_two.configure(text = final[1]["hiragana"]+"\n("+final[1]["romaji"]+")")
                    m_three.configure(text = final[2]["hiragana"]+"\n("+final[2]["romaji"]+")")
                    m_four.configure(text = final[3]["hiragana"]+"\n("+final[3]["romaji"]+")")
                else:
                    m_target_l.configure(text = target["character"])
                    m_one.configure(text = final[0]["meaning"])
                    m_two.configure(text = final[1]["meaning"])
                    m_three.configure(text = final[2]["meaning"])
                    m_four.configure(text = final[3]["meaning"])

