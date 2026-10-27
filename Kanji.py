import Extra as ext
import datetime as dt
import random
import Character_Dictionary as CD
import Shared as sh
import customtkinter as ctk
import Extra as ext
import json
import os


PROFILE_FILE = "limit_today.json"

new = []
ALL_RADSS = []
sub_stage = 0
needed = 0
disposable = []
new_rad = []
length = 0
current = []
available_n5 = []
available_n4 = []
available_n3 = []
available_n2 = []
available_n1 = []
available_ext1 = []
available_ext2 = []
available_ext3 = []
current_deck = ""
pressed = "No"
c_charcater = None
c_card = None
ans = None
c_meaning = None
c_button = None
count = 0
readings = []
rn = 0
time_left = 10.00
timer_a = None
pic = None
affirm = ["You're a matching master, I love watching you succeed", "Why are you so good at this already!? Amazing!", "Thats my " + ext.gender + "! You're a kanji master!"]
affirm2 = ["Goodjob!", "Woah, master!", "Thats my " + ext.gender + "!"]
affirm3 = ["Perfect match!", "Woah, you built that perfectly", "Amazing, you are great at this!"]


stages = {
    0: dt.timedelta(seconds=5),
    1: dt.timedelta(seconds=1),
    2: dt.timedelta(minutes=5),
    3: dt.timedelta(minutes=5),
    4: dt.timedelta(days=1),
    5: dt.timedelta(days=2),
    6: dt.timedelta(days=3),
    7: dt.timedelta(days=5),
    8: dt.timedelta(days=7),
    9: dt.timedelta(days=14),
    10: dt.timedelta(days=21)}


limit = 10
tries = 0

today = 6

unlearnt_5 = 0
unlearnt_4 = 0
unlearnt_3 = 0
unlearnt_2 = 0
unlearnt_1 = 0
unlearnt_ext_1 = 0
unlearnt_ext_2 = 0
unlearnt_ext_3 = 0

def button_change(c1,c2,c3,c4,c5):

    if len(new) == 0:
        pass
    else:
        if len(new) > 0:
            c1.configure(text=new[0]["character"], text_color=ext.cream)
        else:
            c1.configure(text=new[0]["character"],state="disabled", text_color=ext.pink,text_color_disabled=ext.pink)

        if len(new) > 1:
            c2.configure(text=new[1]["character"], state="normal", text_color=ext.cream)
        else:
            c2.configure(text=new[0]["character"], state="disabled", text_color=ext.pink,text_color_disabled=ext.pink)

        if len(new) > 2:
            c3.configure(text=new[2]["character"], state="normal", text_color=ext.cream)
        else:
            c3.configure(text=new[0]["character"], state="disabled", text_color=ext.pink,text_color_disabled=ext.pink)

        if len(new) > 3:
            c4.configure(text=new[3]["character"], state="normal", text_color=ext.cream)
        else:
            c4.configure(text=new[0]["character"], state="disabled", text_color=ext.pink,text_color_disabled=ext.pink)

        if len(new) > 4:
            c5.configure(text=new[4]["character"], state="normal", text_color=ext.cream)
        else:
            c5.configure(text=new[0]["character"], state="disabled", text_color=ext.pink,text_color_disabled=ext.pink)

def get_learn_data():
    return {
        "n_5": min(int(limit) - today, unlearnt_5),
        "n_4": min(int(limit) - today, unlearnt_4),
        "n_3": min(int(limit) - today, unlearnt_3),
        "n_2": min(int(limit) - today, unlearnt_2),
        "n_1": min(int(limit) - today, unlearnt_1),
        "ext_1": min(int(limit) - today, unlearnt_ext_1),
        "ext_2": min(int(limit) - today, unlearnt_ext_2),
        "ext_3": min(int(limit) - today, unlearnt_ext_3)
    }


def update(n_5_info,n_4_info,n_3_info,n_2_info,n_1_info,ext_1_info,ext_2_info,ext_3_info):
    global unlearnt_5,unlearnt_4,unlearnt_3,unlearnt_2,unlearnt_1,unlearnt_ext_1,unlearnt_ext_2,unlearnt_ext_3, available_n5,available_n4,available_n3,available_n2,available_n1,available_ext1,available_ext2,available_ext3
    decks = ["n_5","n_4","n_3","n_2","n_1", "ext_1","ext_2","ext_3"]
    now = dt.datetime.now()
    unlearnt_5 = 0
    unlearnt_4 = 0
    unlearnt_3 = 0
    unlearnt_2 = 0
    unlearnt_1 = 0
    unlearnt_ext_1 = 0
    unlearnt_ext_2 = 0
    unlearnt_ext_3 = 0
    available_n5 = []
    available_n4 = []
    available_n3 = []
    available_n2 = []
    available_n1 = []
    available_ext1 = []
    available_ext2 = []
    available_ext3 = []
    ext.review_5 = 0
    ext.review_4 = 0
    ext.review_3 = 0
    ext.review_2 = 0
    ext.review_1 = 0
    ext.review_ext_1 = 0
    ext.review_ext_2 = 0
    ext.review_ext_3 = 0

    #once decks are mde update updte to alow empty dek


    for deck in decks:
        if ext.deck_n[deck]:
            list = ext.deck_n[deck]

            if deck == "n_5":
                for kanji in list:
                    if kanji["status_meaning"] < 1:
                        unlearnt_5 += 1
                        available_n5.append(kanji)
                    
                    
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_5 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_5 += 1

                print(unlearnt_5)
                n_5_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_5) + "\nUnlearnt: " + str(unlearnt_5))

            if deck == "n_4":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_4 += 1
                        available_n4.append(kanji)
                   
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_4 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_4 += 1
                n_4_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_4) + "\nUnlearnt: " + str(unlearnt_4))
                
            if deck == "n_3":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_3 += 1
                        available_n3.append(kanji)
                    
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_3 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_3 += 1
                n_3_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_3) + "\nUnlearnt: " + str(unlearnt_3))
                
            if deck == "n_2":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_2 += 1
                        available_n2.append(kanji)
                   
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_2 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_2 += 1
                n_2_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_2) + "\nUnlearnt: " + str(unlearnt_2))
                
            if deck == "n_1":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_1 += 1
                        available_n1.append(kanji)
                   
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_1 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_1 += 1
                n_1_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_1) + "\nUnlearnt: " + str(unlearnt_1))

            if deck == "ext_1":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_ext_1 += 1
                        available_ext1.append(kanji)
                    
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_ext_1 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_ext_1 += 1
                ext_1_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_ext_1) + "\nUnlearnt: " + str(unlearnt_ext_1))

            if deck == "ext_2":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_ext_2 += 1
                        available_ext2.append(kanji)
                    
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_ext_2 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_ext_2 += 1
                ext_2_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_ext_2) + "\nUnlearnt: " + str(unlearnt_ext_2))

            if deck == "ext_3":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_ext_3 += 1
                        available_ext3.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_meaning"] <= now:
                        ext.review_ext_3 += 1
                    if kanji["due_time_reading"] is not None and kanji["due_time_reading"] <= now:
                        ext.review_ext_3 += 1
                ext_3_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_ext_3) + "\nUnlearnt: " + str(unlearnt_ext_3))


def learn(button, character, info,radic,radica, mnemonic,c1,c2,c3,c4,c5,indicator,finished,finished_pic,resize):
    global new,current_deck, sub_stage

    sub_stage = 0

    if button == "n_5":
       if int(today) < int(limit):
            current_deck = "show"
            take = min(5,int(limit) - today,unlearnt_5)
            print(take)
            new = random.sample(available_n5, k= take)
            character.configure(text = new[0]["character"])
            if str(new[0]["meaning2"]):
                info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
            else:
                info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
            radicals = ", ".join(new[0]["radicals"])
            radic.configure(text = "Radical(s) Present:")
            radica.configure(text = str(radicals))
            mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
       else:
            indicator(finished)
            resize()
           
    if button == "n_4":
           if int(today) < int(limit):
                current_deck = "show"
                take = min(5,int(limit) - today,unlearnt_4)
                print(take)
                new = random.sample(available_n4, k= take)
                character.configure(text = new[0]["character"])
                if str(new[0]["meaning2"]):
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
           else:
                indicator(finished)
                
    if button == "n_3":
            if int(today) < int(limit):
                current_deck = "show"
                take = min(5,int(limit) - today,unlearnt_3)
                print(take)
                new = random.sample(available_n3, k= take)
                character.configure(text = new[0]["character"])
                if str(new[0]["meaning2"]):
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
            else:
                indicator(finished)
                
    if button == "n_2":
            if int(today) < int(limit):
                current_deck = "show"
                take = min(5,int(limit) - today,unlearnt_2)
                print(take)
                new = random.sample(available_n2, k= take)
                character.configure(text = new[0]["character"])
                if str(new[0]["meaning2"]):
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
                indicator(finished)
                
    if button == "n_1":
            if int(today) < int(limit):
                current_deck = "show"
                take = min(5,int(limit) - today,unlearnt_1)
                print(take)
                new = random.sample(available_n1, k= take)
                character.configure(text = new[0]["character"])
                if str(new[0]["meaning2"]):
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
            else:
                indicator(finished)
                
    if button == "ext_1":
           if int(today) < int(limit):
                current_deck = "nshow"
                take = min(5,int(limit) - today,unlearnt_ext_1)
                print(take)
                new = random.sample(available_ext1, k= take)
                character.configure(text = new[0]["character"])
                if str(new[0]["meaning2"]):
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
                indicator(finished)
                
    if button == "ext_2":
            if int(today) < int(limit):
                current_deck = "nshow"
                take = min(5,int(limit)- today,unlearnt_ext_2)
                print(take)
                new = random.sample(available_ext2, k= take)
                character.configure(text = new[0]["character"])
                if str(new[0]["meaning2"]):
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
            else:
                indicator(finished)
                
    if button == "ext_3":
            if int(today) < int(limit):
                current_deck = "nshow"
                take = min(5,int(limit)- today,unlearnt_ext_3)
                print(take)
                new = random.sample(available_ext3, k= take)
                character.configure(text = new[0]["character"])
                if str(new[0]["meaning2"]):
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + str(new[0]["meaning2"]) + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Meaning mnemonic:\n " + new[0]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[0]["mnemonic_reading"])
                indicator(finished)
                
    button_change(c1,c2,c3,c4,c5)

    

def update_learn(number,button,c1,c2,c3,c4,c5,character,info,radica,mnemonic):
    c1.configure(state = "normal")
    c2.configure(state = "normal")
    c3.configure(state = "normal")
    c4.configure(state = "normal")
    c5.configure(state = "normal")
    button_change(c1,c2,c3,c4,c5)
    number.configure(state = "disabled")
    character.configure(text = new[button]['character'])
    if current_deck == "show":
        if new[button]["meaning2"]:
            info.configure(text = "Meanings: " + new[button]["meaning"] + "/" + str(new[button]["meaning2"]) + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")" + "\nType: " + new[button]["type"])
        else:
            info.configure(text = "Meaning: " + new[button]["meaning"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")" + "\nType: " + new[button]["type"])
        radicals = ", ".join(new[button]["radicals"])
        radica.configure(text = str(radicals))
        mnemonic.configure(text = "Meaning mnemonic:\n " + new[button]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[button]["mnemonic_reading"])
    else:
        if str(new[button]["meaning2"]):
                info.configure(text = "Meanings: " + new[button]["meaning"] + "/" + str(new[button]["meaning2"]) + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")")
        else:
                info.configure(text = "Meaning: " + new[button]["meaning"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")")
        radicals = ", ".join(new[button]["radicals"])
        radica.configure(text = str(radicals))
        mnemonic.configure(text = "Meaning mnemonic:\n " + new[button]["mnemonic_meaning"] + "\n\nReading mnemonic:\n " + new[button]["mnemonic_reading"])

def get_radicals():
    for rad in CD.Radicals:
        ALL_RADSS.append(rad["radical"])
    print(ALL_RADSS)
    
def radical_show(target, assemble, choices,b1,b2,b3,b4,b5,b6,b7,b8):
    global length, new_rad
    get_radicals()
    needed = 0
    disposable = []
    new_rad = []
    length = 0

    random.shuffle(new)
    target.configure(text = "Target Kanji: " + new[sub_stage]["character"])
   
    length = len(new[sub_stage]["radicals"])
    print(length)

    needed = 8 - length
    assemble.configure(text = "Current Selection: " + ("___ " * length))    

    
    for rad in set(ALL_RADSS):
        if rad not in new[sub_stage]["radicals"] and rad not in ('口', '囗'):
            disposable.append(rad)
    print(disposable)

    others = random.sample(disposable, k= needed)

    for rad in new[sub_stage]["radicals"]:
        new_rad.append(rad)

    final = new_rad + others
    random.shuffle(final)

    b1.configure(text = final[0], fg_color = ext.pink)
    b2.configure(text = final[1], fg_color = ext.pink)
    b3.configure(text = final[2], fg_color = ext.pink)
    b4.configure(text = final[3], fg_color = ext.pink)
    b5.configure(text = final[4], fg_color = ext.pink)
    b6.configure(text = final[5], fg_color = ext.pink)
    b7.configure(text = final[6], fg_color = ext.pink)
    b8.configure(text = final[7], fg_color = ext.pink)
                            
def radical_press(button, assemble, choices,b1,b2,b3,b4,b5,b6,b7,b8):
    global current
    if len(current) != length:
        button.configure(state = "disabled")
        chosen = button.cget("text")
        current.append(chosen)
        text = "Current Selection: " + " ".join(current) + (" ___" * (length - len(current)))
        assemble.configure(text = text)

def undo(assemble,b1,b2,b3,b4,b5,b6,b7,b8):
    global current
    button_list = [b1,b2,b3,b4,b5,b6,b7,b8]
    if len(current) != 0:
        last_item = current[-1]
        current = current[:-1]
        text = "Current Selection: " + " ".join(current) + (" ___" * (length - len(current)))
        assemble.configure(text = text)
        for button in button_list:
            but_txt = button.cget("text")
            if but_txt == last_item:
                button.configure(state = "normal")

def check(target, assemble, choices,b1,b2,b3,b4,b5,b6,b7,b8,done, undo,check,learn_kai):
    global current, new_rad,sub_stage,length,tries,affirm3
    if length == len(current):
        print(current)
        print(new_rad)
        if sorted(current) == sorted(new_rad):
            
            tries = 0
            current = []
            disposable = []
            print("Match!")
            rand = random.randint(0,2)
            learn_kai.configure(text = affirm3[rand])
            b1.configure(state = "normal")
            b2.configure(state = "normal")
            b3.configure(state = "normal")
            b4.configure(state = "normal")
            b5.configure(state = "normal")
            b6.configure(state = "normal")
            b7.configure(state = "normal")
            b8.configure(state = "normal")
            sub_stage += 1
            if sub_stage < len(new):
                target.configure(text = "Target Kanji: " + new[sub_stage]["character"])
                length = len(new[sub_stage]["radicals"])
                assemble.configure(text = "Current Selection: " + ("___ " * length))
                needed = 8 - length
                for rad in set(ALL_RADSS):
                        if rad not in new[sub_stage]["radicals"]:
                            disposable.append(rad)
                print(disposable)
                
                others = random.sample(disposable, k= needed)

                new_rad = []
                for rad in new[sub_stage]["radicals"]:
                    new_rad.append(rad)
                
                final = new_rad + others
                random.shuffle(final)
                
                b1.configure(text = final[0], fg_color = ext.pink)
                b2.configure(text = final[1], fg_color = ext.pink)
                b3.configure(text = final[2], fg_color = ext.pink)
                b4.configure(text = final[3], fg_color = ext.pink)
                b5.configure(text = final[4], fg_color = ext.pink)
                b6.configure(text = final[5], fg_color = ext.pink)
                b7.configure(text = final[6], fg_color = ext.pink)
                b8.configure(text = final[7], fg_color = ext.pink)
            if sub_stage == len(new):
                done.place(relx=.85,rely=.92,relwidth = .15,relheight = .1, anchor = ctk.CENTER)
                undo.configure(state = "disabled")
                check.configure(state = "disabled")
                b1.configure(state = "disabled")
                b2.configure(state = "disabled")
                b3.configure(state = "disabled")
                b4.configure(state = "disabled")
                b5.configure(state = "disabled")
                b6.configure(state = "disabled")
                b7.configure(state = "disabled")
                b8.configure(state = "disabled")
        else: 
            print("Try again!")
            learn_kai.configure(text = "Hmm not quite right.. Here I highlighted one of the correct radicals to help you!")
            if tries != 1:
                help = new_rad[0]
                if b1.cget("text") == help:
                    b1.configure(fg_color = ext.grey)
                if b2.cget("text") == help:
                    b2.configure(fg_color = ext.grey)
                if b3.cget("text") == help:
                    b3.configure(fg_color = ext.grey)
                if b4.cget("text") == help:
                    b4.configure(fg_color = ext.grey)
                if b5.cget("text") == help:
                    b5.configure(fg_color = ext.grey)
                if b6.cget("text") == help:
                    b6.configure(fg_color = ext.grey)
                if b7.cget("text") == help:
                    b7.configure(fg_color = ext.grey)
                if b8.cget("text") == help:
                    b8.configure(fg_color = ext.grey)
                tries = 1
    else:
        print("You still need to add "+ str(-1 * (len(current)-length)) + " more radical(s)!")
        learn_kai.configure(text = "You still need to add "+ str(-1 * (len(current)-length)) + " more radical(s)!")

def meaning_connect_function(meaning_connect,indicator,page, meaning2_connect):
    global new,count
    if sub_stage == len(new):
        indicator(page)
        for i in range(len(new)):
            meaning_connect(new[i]["character"])
        random.shuffle(new)
        for i in range(len(new)):
            meaning2_connect(new[i]["meaning"])
        count = 0


def meaning_connect_but(button,done1,kai,talk,resize):
    global pressed,c_charcater, c_card, ans, c_meaning, c_button, count,affirm
    ans = button.cget("text")


    if pressed == "No":
        ans = button.cget("text")
        for card in new:
            if ans == card["character"]:
                c_charcater = "Y"
                c_meaning = "N"
                c_card = card
                talk.configure(text = "Now press the matching meaning, you got it!")
                button.configure(fg_color = ext.ddpink, state = "disabled")
                c_button = button
                pressed = "Yes"
            elif ans == card["meaning"]:
                c_charcater = "N"
                c_meaning = "Y"
                c_card = card
                c_button = button
                print(c_card)
                talk.configure(text = "Now press the matching character, you got it!")
                button.configure(fg_color = ext.ddpink, state = "disabled")
                pressed = "Yes"
        kai.configure(image = ext.meaning_idle_image)
        if ext.mode == "D":
                kai.active_pil_image = ext.meaning_idle_image._dark_image
        else:
                kai.active_pil_image = ext.meaning_idle_image._light_image
        resize()

    else:
        
            if c_charcater == "Y":
                for card in new:
                    if ans == card["character"]:
                        print("Please press a meaning card")
                        pressed = "No"
                        c_charcater = None
                        c_meaning = None
                        talk.configure(text = "You're meant to press a meaning card! There on the right side. Try again, you can do it!")
                        c_button.configure(fg_color = ext.dpink, state = "normal")
                        kai.configure(image = ext.meaning_wrong_image)
                        if ext.mode == "D":
                                kai.active_pil_image = ext.meaning_wrong_image._dark_image
                        else:
                                kai.active_pil_image = ext.meaning_wrong_image._light_image
                                resize()
                        break
                    elif ans == card["meaning"]:
                        if ans == c_card["meaning"]:
                            pressed = "No"
                            c_charcater = None
                            c_meaning = None
                            rand = random.randint(0,2)
                            talk.configure(text = affirm[rand])
                            print("Goodjob!!")
                            kai.configure(image = ext.meaning_right_image)
                            if ext.mode == "D":
                                kai.active_pil_image = ext.meaning_right_image._dark_image
                            else:
                                kai.active_pil_image = ext.meaning_right_image._light_image
                            resize()
                            c_button.destroy()
                            button.destroy()
                            count += 1
                            break
                        else:
                            c_charcater = None
                            c_meaning = None
                            pressed = "No"
                            mne = c_card["mnemonic_meaning"]
                            talk.configure(text = "Hmm thats not it just try to remember " + mne)
                            print("Ooops, try again")
                            kai.configure(image = ext.meaning_wrong_image)
                            if ext.mode == "D":
                                kai.active_pil_image = ext.meaning_wrong_image._dark_image
                            else:
                                kai.active_pil_image = ext.meaning_wrong_image._light_image
                            resize()
                            c_button.configure(fg_color = ext.dpink, state = "normal")
                            break

                    
                    
            if c_charcater == "N":
                for card in new:
                    if ans == card["meaning"]:
                        print("Please press a character card")
                        pressed = "No"
                        c_charcater = None
                        c_meaning = None
                        c_button.configure(fg_color = ext.dpink,state = "normal")
                        talk.configure(text = "You're meant to press a character card! There on the left side. Try again, you can do it!")
                        kai.configure(image = ext.meaning_wrong_image)
                        if ext.mode == "D":
                            kai.active_pil_image = ext.meaning_wrong_image._dark_image
                        else:
                            kai.active_pil_image = ext.meaning_wrong_image._light_image
                        resize()
                        break
                    elif ans == card["character"]:
                        if ans == c_card["character"]:
                            pressed = "No"
                            c_charcater = None
                            c_meaning = None
                            print("Goodjob!!")
                            rand = random.randint(0,2)
                            talk.configure(text = affirm[rand])
                            kai.configure(image = ext.meaning_right_image)
                            if ext.mode == "D":
                                kai.active_pil_image = ext.meaning_right_image._dark_image
                            else:
                                kai.active_pil_image = ext.meaning_right_image._light_image
                            resize()
                            c_button.destroy()
                            button.destroy()
                            count += 1
                            break
                        else:
                            c_charcater = None
                            c_meaning = None
                            pressed = "No"
                            print("Ooops, try again")
                            mne = c_card["mnemonic_meaning"]
                            talk.configure(text = "Hmm thats not it just try to remember " + mne)
                            kai.configure(image = ext.meaning_wrong_image)
                            if ext.mode == "D":
                                kai.active_pil_image = ext.meaning_wrong_image._dark_image
                            else:
                                kai.active_pil_image = ext.meaning_wrong_image._light_image
                            resize()
                            c_button.configure(fg_color = ext.dpink,state = "normal")
                            break
    if count == len(new):
        print("Done")
        kai.configure(image = ext.meaning_right_image)
        if ext.mode == "D":
            kai.active_pil_image = ext.meaning_right_image._dark_image
        else:
            kai.active_pil_image = ext.meaning_right_image._light_image
        resize()
        done1.place(relx=.28,rely=.5,relwidth = .5,relheight = .3, anchor = ctk.CENTER)

def get_reading():
    global readings
    readings = []
    for kanji in CD.Kanji_n5:
        readings.append(kanji)
    readings = random.sample(readings, k= 8)
    
def remove_learn():
    global card, today
    for card in new:
        now = dt.datetime.now()
        card["status_reading"] = 1
        card["status_meaning"] = 1
        card["due_time_reading"] = now + stages[card["status_reading"]]
        card["due_time_meaning"] = now + stages[card["status_reading"]]
    today = today + len(new)
    ext.total_l += len(new)

def whacka_start(nine,timer,kanji_label,window, start, one_button,two_button,three_button,five_button,four_button,six_button,seven_button,eight_button,nine_button, indicator,kanji_mid,talk,kai,resize):
    global rn,new
    get_reading()

    if rn < len(new):
        print(rn)
        kanji_label.configure(text = new[rn]["character"])
        readings.append(new[rn])
        random.shuffle(readings)
        nine(readings[0]["romaji"],readings[1]["romaji"],readings[2]["romaji"],readings[3]["romaji"],readings[4]["romaji"],readings[5]["romaji"],readings[6]["romaji"],readings[7]["romaji"],readings[8]["romaji"],readings[0]["hiragana"],readings[1]["hiragana"],readings[2]["hiragana"],readings[3]["hiragana"],readings[4]["hiragana"],readings[5]["hiragana"],readings[6]["hiragana"],readings[7]["hiragana"],readings[8]["hiragana"])
        time_update(timer,window,start, one_button,two_button,three_button,five_button,four_button,six_button,seven_button,eight_button,nine_button,talk,kai,resize) 
    else:
        if pic is not None:
            window.after_cancel(pic)
        one_button.configure(state = "disabled")
        two_button.configure(state = "disabled")
        three_button.configure(state = "disabled")
        four_button.configure(state = "disabled")
        five_button.configure(state = "disabled")
        six_button.configure(state = "disabled")
        seven_button.configure(state = "disabled")
        eight_button.configure(state = "disabled")
        nine_button.configure(state = "disabled")
        kai.configure(image = ext.meaning_right_image)
        if ext.mode == "D":
            kai.active_pil_image = ext.meaning_right_image._dark_image
        else:
            kai.active_pil_image = ext.meaning_right_image._light_image
        resize()
        talk.configure(text = "Yippee, youre done learning these cards. Press finish then feel free to go review them! Good job!")
        start.configure(text = "Finish", state = "normal", command = lambda: indicator(kanji_mid))
        remove_learn()
        print("banzai")
       
def time_update(timer,window,start, one_button,two_button,three_button,five_button,four_button,six_button,seven_button,eight_button,nine_button,talk,kai,resize):
    global rn, time_left,timer_a,new
    timer.configure(text = "Time left: " + str(time_left))
    if time_left > 0:
        time_left = time_left - 1
        timer_a = window.after(1000, lambda: time_update(timer,window,start, one_button,two_button,three_button,five_button,four_button,six_button,seven_button,eight_button,nine_button,talk,kai,resize))
    elif time_left == 0:
        timer.configure(text = "Time left: " + str(round(time_left,2)))
        one_button.configure(state = "disabled")
        two_button.configure(state = "disabled")
        three_button.configure(state = "disabled")
        four_button.configure(state = "disabled")
        five_button.configure(state = "disabled")
        six_button.configure(state = "disabled")
        seven_button.configure(state = "disabled")
        eight_button.configure(state = "disabled")
        nine_button.configure(state = "disabled")
        kai.configure(image = ext.meaning_wrong_image)
        if ext.mode == "D":
            kai.active_pil_image = ext.meaning_wrong_image._dark_image
        else:
            kai.active_pil_image = ext.meaning_wrong_image._light_image
        resize()
        talk.configure(text = "Appears you ran outta time.. Here try to remember " + new[rn]["mnemonic_reading"])
        print("Oops, outa time!")
        rn = 0
        start.configure(state ="normal", text = "Try Again")

def reading_press(button,nine,timer,kanji_label,window,start,list, one_button,two_button,three_button,five_button,four_button,six_button,seven_button,eight_button,nine_button, indicator,kanji_mid,talk,kai,resize): 
    global rn,time_left,timer_a,pic,affirm2
    
    ans = button.cget("text")
    print(ans)
    print(ans.startswith(new[rn]["romaji"]))
    print(new[rn]["romaji"])
    if ans.startswith(new[rn]["romaji"]):
        time_left = 10.00
        rn = rn + 1 
        if pic is not None:
            window.after_cancel(pic)
            
        kai.configure(image = ext.meaning_right_image)
        if ext.mode == "D":
            kai.active_pil_image = ext.meaning_right_image._dark_image
        else:
            kai.active_pil_image = ext.meaning_right_image._light_image
        resize()

        rand = random.randint(0,2)
        talk.configure(text = affirm2[rand])
        pic = window.after(1500,lambda: change(kai,talk,resize))
        if timer_a is not None:
            window.after_cancel(timer_a)
        whacka_start(nine,timer,kanji_label,window,start, one_button,two_button,three_button,five_button,four_button,six_button,seven_button,eight_button,nine_button, indicator,kanji_mid,talk,kai,resize)
        
    else:
        time_left = 10.00
        kai.configure(image = ext.meaning_wrong_image)
        if ext.mode == "D":
            kai.active_pil_image = ext.meaning_wrong_image._dark_image
        else:
            kai.active_pil_image = ext.meaning_wrong_image._light_image
        resize()
        talk.configure(text = "Thats not quite right.. Try to remember " + new[rn]["mnemonic_reading"])
        rn = 0
        if timer_a is not None:
            window.after_cancel(timer_a)

        one_button.configure(state = "disabled")
        two_button.configure(state = "disabled")
        three_button.configure(state = "disabled")
        four_button.configure(state = "disabled")
        five_button.configure(state = "disabled")
        six_button.configure(state = "disabled")
        seven_button.configure(state = "disabled")
        eight_button.configure(state = "disabled")
        nine_button.configure(state = "disabled")

        start.configure(state ="normal", text = "Try Again")

def change(kai,talk,resize):
    kai.configure(image = ext.meaning_idle_image)
    if ext.mode == "D":
        kai.active_pil_image = ext.meaning_idle_image._dark_image
    else:
        kai.active_pil_image = ext.meaning_idle_image._light_image
    resize()

    talk.configure(text = "What could it be....")


get_radicals()

def save_user_profile():

    initial_profile = {
                "limit": limit,
                "today": today,
    }
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(initial_profile, f, indent=4, ensure_ascii=False, default = str)
    print("Users profille saved!")

if os.path.exists(PROFILE_FILE):
    try:
        if os.path.getsize(PROFILE_FILE) == 0:
            print("character_PROFILE.json is empty. Populating it now...")
            save_user_profile()

        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            saved_profile = json.load(f)

            limit = saved_profile.get("limit", limit)
            today = saved_profile.get("today", today)
        
        print("Character progress loaded successfully!")
    except Exception as e:
        print(f"Error loading character data: {e}") 