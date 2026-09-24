import Extra as ext
import datetime as dt
import random

new = []

def update(n_5_info,n_4_info,n_3_info,n_2_info,n_1_info,ext_1_info,ext_2_info,ext_3_info):

    decks = ["n_5","n_4","n_3","n_2","n_1", "ext_1","ext_2","ext_3"]
    now = dt.datetime.now()
    for deck in decks:
        if ext.deck_n[deck]:
            list = ext.deck_n[deck]

            if deck == "n_5":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_5 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_5 += 1
                n_5_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_5) + "\nUnlearnt: " + str(ext.unlearnt_5))

            if deck == "n_4":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_4 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_4 += 1
                n_4_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_4 + "Unlearnt: " + str(ext.unlearnt_4)))
                
            if deck == "n_3":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_3 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_3 += 1
                n_3_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_3 + "Unlearnt: " + str(ext.unlearnt_3)))
                
            if deck == "n_2":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_2 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_2 += 1
                n_2_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_2 + "Unlearnt: " + str(ext.unlearnt_2)))
                
            if deck == "n_1":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_1 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_1 += 1
                n_1_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_1 + "Unlearnt: " + str(ext.unlearnt_1)))

            if deck == "ext_1":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_ext_1 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_ext_1 += 1
                ext_1_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_ext_1) + "\nUnlearnt: " + str(ext.unlearnt_ext_1))

            if deck == "ext_2":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_ext_2 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_ext_2 += 1
                ext_2_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_ext_2) + "\nUnlearnt: " + str(ext.unlearnt_ext_2))

            if deck == "ext_3":
                for kanji in list:
                    if kanji["status_meaning"] <= 1:
                        ext.unlearnt_ext_3 += 1
                    if kanji["due_time_meaning"] is not None and kanji["due_time_reading"] is not None and kanji["due_time_meaning"] <= now and kanji["due_time_reading"] <= now:
                        ext.review_ext_3 += 1
                ext_3_info.configure(text = "Ready to Learn: "+ str(ext.learn[deck]) + "\n Ready to Review: " + str(ext.review_ext_3) + "\nUnlearnt: " + str(ext.unlearnt_ext_3))

def learn(button, character, info,radic,radica, mnemonic,c1,c2,c3,c4,c5):
    global new
    if button == "n_5":
       if ext.today < ext.limit:
            take = min(5,ext.limit - ext.today)
            new = random.sample(ext.deck_n[button], k= take)
            character.configure(text = new[0]["character"])
            if new[0]["meaning2"]:
                info.configure(text = "Meanings: " + new[0]["meaning"] + "/" + new[0]["meaning2"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
            else:
                info.configure(text = "Meaning: " + new[0]["meaning"] + "\nReading: " + new[0]["hiragana"] + " (" + new[0]["romaji"] + ")" + "\nType: " + new[0]["type"])
            radicals = ", ".join(new[0]["radicals"])
            radic.configure(text = "Radical(s) Present:")
            radica.configure(text = str(radicals))
            mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[0]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[0]["mnemonic_reading"])
    c1.configure(text = new[0]["character"])
    c2.configure(text = new[1]["character"])
    c3.configure(text = new[2]["character"])
    c4.configure(text = new[3]["character"])
    c5.configure(text = new[4]["character"])
    

def update_learn(number,button,c1,c2,c3,c4,c5,character,info,radica,mnemonic):
    c1.configure(state = "normal")
    c2.configure(state = "normal")
    c3.configure(state = "normal")
    c4.configure(state = "normal")
    c5.configure(state = "normal")
    number.configure(state = "disabled")
    character.configure(text = new[button]['character'])
    if new[button]["meaning2"]:
        info.configure(text = "Meanings: " + new[button]["meaning"] + "/" + new[button]["meaning2"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")" + "\nType: " + new[button]["type"])
    else:
        info.configure(text = "Meaning: " + new[button]["meaning"] + "\nReading: " + new[button]["hiragana"] + " (" + new[button]["romaji"] + ")" + "\nType: " + new[button]["type"])
    radicals = ", ".join(new[button]["radicals"])
    radica.configure(text = str(radicals))
    mnemonic.configure(text = "Mnemonic to help you with meaning: " + new[button]["mnemonic_meaning"] + "\nMnemonic to help you with the reading: " + new[button]["mnemonic_reading"])
    
