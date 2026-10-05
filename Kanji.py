import Extra as ext
import datetime as dt
import random
import Character_Dictionary as CD
import Shared as sh

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


limit = 10

today = 0

unlearnt_5 = 0
unlearnt_4 = 0
unlearnt_3 = 0
unlearnt_2 = 0
unlearnt_1 = 0
unlearnt_ext_1 = 0
unlearnt_ext_2 = 0
unlearnt_ext_3 = 0

def button_change(c1,c2,c3,c4,c5):

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
        "n_5": min(limit - today, unlearnt_5),
        "n_4": min(limit - today, unlearnt_4),
        "n_3": min(limit - today, unlearnt_3),
        "n_2": min(limit - today, unlearnt_2),
        "n_1": min(limit - today, unlearnt_1),
        "ext_1": min(limit - today, unlearnt_ext_1),
        "ext_2": min(limit - today, unlearnt_ext_2),
        "ext_3": min(limit - today, unlearnt_ext_3)
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

    #once decks are mde update updte to alow empty dek


    for deck in decks:
        if ext.deck_n[deck]:
            list = ext.deck_n[deck]

            if deck == "n_5":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_5 += 1
                        available_n5.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_5 += 1
                print(unlearnt_5)
                n_5_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_5) + "\nUnlearnt: " + str(unlearnt_5))

            if deck == "n_4":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_4 += 1
                        available_n4.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_4 += 1
                n_4_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_4 + "Unlearnt: " + str(unlearnt_4)))
                
            if deck == "n_3":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_3 += 1
                        available_n3.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_3 += 1
                n_3_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_3 + "Unlearnt: " + str(unlearnt_3)))
                
            if deck == "n_2":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_2 += 1
                        available_n2.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_2 += 1
                n_2_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_2 + "Unlearnt: " + str(unlearnt_2)))
                
            if deck == "n_1":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_1 += 1
                        available_n1.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_1 += 1
                n_1_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_1 + "Unlearnt: " + str(unlearnt_1)))

            if deck == "ext_1":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_ext_1 += 1
                        available_ext1.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_ext_1 += 1
                ext_1_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_ext_1) + "\nUnlearnt: " + str(unlearnt_ext_1))

            if deck == "ext_2":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_ext_2 += 1
                        available_ext2.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_ext_2 += 1
                ext_2_info.configure(text = "Ready to Learn: "+ str(get_learn_data[deck]) + "\n Ready to Review: " + str(ext.review_ext_2) + "\nUnlearnt: " + str(unlearnt_ext_2))

            if deck == "ext_3":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        unlearnt_ext_3 += 1
                        available_ext3.append(kanji)
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_ext_3 += 1
                ext_3_info.configure(text = "Ready to Learn: "+ str(get_learn_data()[deck]) + "\n Ready to Review: " + str(ext.review_ext_3) + "\nUnlearnt: " + str(unlearnt_ext_3))


def learn(button, character, info,radic,radica, mnemonic,c1,c2,c3,c4,c5):
    global new,current_deck

    if button == "n_5":
       if today < limit:
            current_deck = "show"
            take = min(5,limit - today,unlearnt_5)
            print(take)
            new = random.sample(available_n5, k= take)
            character.configure(text = new[0]["character"])
            if new[0]["meaning2"]:
                info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
            else:
                info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
            radicals = ", ".join(new[0]["radicals"])
            radic.configure(text = "Radical(s) Present:")
            radica.configure(text = str(radicals))
            mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    if button == "n_4":
           if today < limit:
                current_deck = "show"
                take = min(5,limit - today,unlearnt_4)
                print(take)
                new = random.sample(available_n4, k= take)
                character.configure(text = new[0]["character"])
                if new[0]["meaning2"]:
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    if button == "n_3":
            if today < limit:
                current_deck = "show"
                take = min(5,limit - today,unlearnt_3)
                print(take)
                new = random.sample(available_n3, k= take)
                character.configure(text = new[0]["character"])
                if new[0]["meaning2"]:
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    if button == "n_2":
            if today < limit:
                current_deck = "show"
                take = min(5,limit - today,unlearnt_2)
                print(take)
                new = random.sample(available_n2, k= take)
                character.configure(text = new[0]["character"])
                if new[0]["meaning2"]:
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    if button == "n_1":
            if today < limit:
                current_deck = "show"
                take = min(5,limit - today,unlearnt_1)
                print(take)
                new = random.sample(available_n1, k= take)
                character.configure(text = new[0]["character"])
                if new[0]["meaning2"]:
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    if button == "ext_1":
           if today < limit:
                current_deck = "nshow"
                take = min(5,limit - today,unlearnt_ext_1)
                print(take)
                new = random.sample(available_ext1, k= take)
                character.configure(text = new[0]["character"])
                if new[0]["meaning2"]:
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    if button == "ext_2":
            if today < limit:
                current_deck = "nshow"
                take = min(5,limit - today,unlearnt_ext_2)
                print(take)
                new = random.sample(available_ext2, k= take)
                character.configure(text = new[0]["character"])
                if new[0]["meaning2"]:
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    if button == "ext_3":
            if today < limit:
                current_deck = "nshow"
                take = min(5,limit - today,unlearnt_ext_3)
                print(take)
                new = random.sample(available_ext3, k= take)
                character.configure(text = new[0]["character"])
                if new[0]["meaning2"]:
                    info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                else:
                    info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")")
                radicals = ", ".join(new[0]["radicals"])
                radic.configure(text = "Radical(s) Present:")
                radica.configure(text = str(radicals))
                mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
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
            info.configure(text = "Meanings: " + new[button]["meaning"] + "/" + new[button]["meaning2"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")" + "\nType: " + new[button]["type"])
        else:
            info.configure(text = "Meaning: " + new[button]["meaning"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")" + "\nType: " + new[button]["type"])
        radicals = ", ".join(new[button]["radicals"])
        radica.configure(text = str(radicals))
        mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[button]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[button]["mnemonic_reading"])
    else:
        if new[button]["meaning2"]:
                info.configure(text = "Meanings: " + new[button]["meaning"] + "/" + new[button]["meaning2"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")")
        else:
                info.configure(text = "Meaning: " + new[button]["meaning"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")")
        radicals = ", ".join(new[button]["radicals"])
        radica.configure(text = str(radicals))
        mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[button]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[button]["mnemonic_reading"])

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
    if new[sub_stage]["meaning2"]:
        target.configure(text = "Target Kanji Meanings: " + new[sub_stage]["meaning"] + "/" + new[sub_stage]["meaning2"])
    else:
        target.configure(text = "Target Kanji Meaning: " + new[sub_stage]["meaning"])

    length = len(new[sub_stage]["radicals"])
    print(length)

    needed = 8 - length
    assemble.configure(text = "Current Selection: " + ("___ " * length))    

    print(ALL_RADSS)
    for rad in set(ALL_RADSS):
        if rad not in new[sub_stage]["radicals"]:
            disposable.append(rad)
    print(disposable)

    others = random.sample(disposable, k= needed)

    for rad in new[sub_stage]["radicals"]:
        new_rad.append(rad)

    final = new_rad + others
    random.shuffle(final)

    b1.configure(text = final[0])
    b2.configure(text = final[1])
    b3.configure(text = final[2])
    b4.configure(text = final[3])
    b5.configure(text = final[4])
    b6.configure(text = final[5])
    b7.configure(text = final[6])
    b8.configure(text = final[7])
                            
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

def check(target, assemble, choices,b1,b2,b3,b4,b5,b6,b7,b8):
    global current, new_rad,sub_stage,length
    if length == len(current):
        print(current)
        print(new_rad)
        if sorted(current) == sorted(new_rad):
            current = []
            disposable = []
            print("Match!")
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
                if new[sub_stage]["meaning2"]:
                    target.configure(text = "Target Kanji Meanings: " + new[sub_stage]["meaning"] + "/" + new[sub_stage]["meaning2"])
                else:
                    target.configure(text = "Target Kanji Meaning: " + new[sub_stage]["meaning"]) 
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
                
                b1.configure(text = final[0])
                b2.configure(text = final[1])
                b3.configure(text = final[2])
                b4.configure(text = final[3])
                b5.configure(text = final[4])
                b6.configure(text = final[5])
                b7.configure(text = final[6])
                b8.configure(text = final[7])
            if sub_stage == len(new):
                print("All done!")
        else: 
            print("Try again!")
    else:
        print("You still need to add "+ str(-1 * (len(current)-length)) + " more radical(s)!")

get_radicals()
