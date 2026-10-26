from PIL import Image
import customtkinter as ctk
import Character_Dictionary as cd
import Shared as sh

page = ""
name = ""
gender = "girl"
streak = 0
t_streak = 0
h_streak = 0 

rn = ""

review_5 = 0
review_4 = 0
review_3 = 0
review_2 = 0
review_1 = 0
review_ext_1 = 0
review_ext_2 = 0
review_ext_3 = 0
today = ""
last_today = -1
total_l = 0



deck_n = {
    "n_5": cd.Kanji_n5,
    "n_4": cd.Kanji_n4,
    "n_3": cd.Kanji_n3,
    "n_2": cd.Kanji_n2,
    "n_1": cd.Kanji_n1,
    "ext_1":cd.Extra_1,
    "ext_2":cd.Extra_2,
    "ext_3":cd.Extra_3
}

c_deck = ""
title1 = "COOL KANJI"
title2 = "Empty Deck"
title3 = "Empty Deck"

right = "#3A5F2D"
wrong = "#CC3F32"
dright ="#1F3C15"
dwrong = "#762720"
cream = ("#F6FFFA","#DFDFDF")
dcream = ("#C2C4C3","#C8CCCA")
linen = ("#E6E6DB","#313144")
dlinen = ("#CECEBB","#1F1F2C")
grey = ("#A0BBB2","#748376")
pink = ("#DA7D91","#C1529A")
brown = ("#8b4c41", "#241d2b")
dgrey = ("#507065","#506953")
dbrown = ("#69362d","#151019")
dpink = ("#D05A73","#8C3664")
bpink = ("#EFAAB9","#B7659D")
ddpink = ("#A14055","#712946")

ext1 = "N"
ext2 = "Y"
ext3 = "Y"

mode = ""

hiragana = Image.open("hiragana.png")
hiragana_d = Image.open("hiragana_d.png")
hiragana_image = ctk.CTkImage(size = (500,698), light_image=hiragana, dark_image=hiragana_d)

katakana = Image.open("katakana.png")
katakana_d = Image.open("katakana_d.png")
katakana_image = ctk.CTkImage(size = (500,698), light_image=katakana, dark_image=katakana_d)

new_deck = Image.open("new_deck.png")
new_deck_d = Image.open("new_deck_d.png")
new_deck_image = ctk.CTkImage(size = (591,342), light_image=new_deck, dark_image=new_deck_d)

add_card = Image.open("add_card.png")
add_card_d = Image.open("add_card_d.png")
add_card_image = ctk.CTkImage(size = (197,421), light_image=add_card, dark_image=add_card_d)

delete = Image.open("delete.png")
delete_d = Image.open("delete_d.png")
delete_image = ctk.CTkImage(size = (170,314), light_image=delete, dark_image=delete_d)



intro = Image.open("intro.png")
intro_d = Image.open("intro_d.png")
intro_image = ctk.CTkImage(size = (729,270), light_image=intro, dark_image=intro_d)

chest_mid = Image.open("chest_mid.png")
chest_mid_d = Image.open("chest_mid_d.png")
chest_mid_image = ctk.CTkImage(size = (202.5,540), light_image=chest_mid, dark_image=chest_mid_d )

chest_begin = Image.open("chest_begin.png")
chest_begin_d = Image.open("chest_begin_d.png")
chest_begin_image = ctk.CTkImage(size=(608,240),light_image=chest_begin,dark_image=chest_begin_d )

chest_wrong = Image.open("chest_wrong.png")
chest_wrong_d = Image.open("chest_wrong_d.png")
chest_wrong_image = ctk.CTkImage(size=(608,240),light_image=chest_wrong,dark_image=chest_wrong_d )

chest_right = Image.open("chest_right.png")
chest_right_d = Image.open("chest_right_d.png")
chest_right_image = ctk.CTkImage(size=(608,240),light_image=chest_right,dark_image=chest_right_d )

chest_right2 = Image.open("chest_right2.png")
chest_right2_d = Image.open("chest_right2_d.png")
chest_right2_image = ctk.CTkImage(size=(608,240),light_image=chest_right2,dark_image=chest_right2_d )


chest_10 = Image.open("chest_10.png")
chest_10_d = Image.open("chest_10_d.png")
chest_10_image = ctk.CTkImage(size=(608,240),light_image=chest_10,dark_image=chest_10_d)

chest_5 = Image.open("chest_5.png")
chest_5_d = Image.open("chest_5_d.png")
chest_5_image = ctk.CTkImage(size=(608,240),light_image=chest_5,dark_image=chest_5_d )

chest_text = Image.open("chest_text.png")
chest_text_d = Image.open("chest_text_d.png")
chest_text_image = ctk.CTkImage(size=(462,240),light_image=chest_text,dark_image=chest_text_d)

ghost_mid = Image.open("ghost_mid.png")
ghost_mid_d = Image.open("ghost_mid_d.png")
ghost_mid_image = ctk.CTkImage(size = (202.5,540), light_image=ghost_mid, dark_image=ghost_mid_d )

ghost_begin = Image.open("ghost_begin.png")
ghost_begin_d = Image.open("ghost_begin_d.png")
ghost_begin_image = ctk.CTkImage(size=(608,240),light_image=ghost_begin,dark_image=ghost_begin_d )

ghost_wrong = Image.open("ghost_wrong.png")
ghost_wrong_d = Image.open("ghost_wrong_d.png")
ghost_wrong_image = ctk.CTkImage(size=(608,240),light_image=ghost_wrong,dark_image=ghost_wrong_d )

ghost_right = Image.open("ghost_right.png")
ghost_right_d = Image.open("ghost_right_d.png")
ghost_right_image = ctk.CTkImage(size=(608,240),light_image=ghost_right,dark_image=ghost_right_d )

ghost_right2 = Image.open("ghost_right2.png")
ghost_right2_d = Image.open("ghost_right2_d.png")
ghost_right2_image = ctk.CTkImage(size=(608,240),light_image=ghost_right2,dark_image=ghost_right2_d )

ghost_10 = Image.open("ghost_10.png")
ghost_10_d = Image.open("ghost_10_d.png")
ghost_10_image = ctk.CTkImage(size=(608,240),light_image=ghost_10,dark_image=ghost_10_d)

ghost_5 = Image.open("ghost_5.png")
ghost_5_d = Image.open("ghost_5_d.png")
ghost_5_image = ctk.CTkImage(size=(608,240),light_image=ghost_5,dark_image=ghost_5_d )

ghost_text = Image.open("ghost_text.png")
ghost_text_d = Image.open("ghost_text_d.png")
ghost_text_image = ctk.CTkImage(size=(462,240),light_image=ghost_text,dark_image=ghost_text_d )

kai_mid_r = Image.open("kai_mid_r.png")
kai_mid_r_d = Image.open("kai_mid_r_d.png")
kai_mid_rimage = ctk.CTkImage(size = (202.5,300), light_image=kai_mid_r, dark_image=kai_mid_r_d )

kai_begin_r = Image.open("kai_begin_r.png")
kai_begin_r_d = Image.open("kai_begin_r_d.png")
kai_begin_rimage = ctk.CTkImage(size = (202.5,300), light_image=kai_begin_r, dark_image=kai_begin_r_d )

kai_right2_r = Image.open("kai_right2_r.png")
kai_right2_r_d = Image.open("kai_right2_r_d.png")
kai_right2_rimage = ctk.CTkImage(size = (202.5,300), light_image=kai_right2_r, dark_image=kai_right2_r_d )

kai_right_r = Image.open("kai_right_r.png")
kai_right_r_d = Image.open("kai_right_r_d.png")
kai_right_rimage = ctk.CTkImage(size = (202.5,300), light_image=kai_right_r, dark_image=kai_right_r_d )

kai_wrong_r = Image.open("kai_wrong_r.png")
kai_wrong_r_d = Image.open("kai_wrong_r_d.png")
kai_wrong_rimage = ctk.CTkImage(size = (202.5,300), light_image=kai_wrong_r, dark_image=kai_wrong_r_d )

kai_10_r = Image.open("kai_10_r.png")
kai_10_r_d = Image.open("kai_10_r_d.png")
kai_10_rimage = ctk.CTkImage(size = (202.5,300), light_image=kai_10_r, dark_image=kai_10_r_d )

kai_5_r = Image.open("kai_5_r.png")
kai_5_r_d = Image.open("kai_5_r_d.png")
kai_5_rimage = ctk.CTkImage(size = (202.5,300), light_image=kai_5_r, dark_image=kai_5_r_d )

kai_mid = Image.open("kai_mid.png")
kai_mid_d = Image.open("kai_mid_d.png")
kai_mid_image = ctk.CTkImage(size = (202.5,480), light_image=kai_mid, dark_image=kai_mid_d )

kai_text = Image.open("kai_text.png")
kai_text_d = Image.open("kai_text_d.png")
kai_text_image = ctk.CTkImage(size=(462,240),light_image=kai_text,dark_image=kai_text_d)

kai_begin = Image.open("kai_begin.png")
kai_begin_d = Image.open("kai_begin_d.png")
kai_begin_image = ctk.CTkImage(size = (202.5,300), light_image=kai_begin, dark_image=kai_begin_d )

kai_right2 = Image.open("kai_right2.png")
kai_right2_d = Image.open("kai_Right2_d.png")
kai_right2_image = ctk.CTkImage(size = (202.5,300), light_image=kai_right2, dark_image=kai_right2_d )

kai_right = Image.open("kai_right.png")
kai_right_d = Image.open("kai_right_d.png")
kai_right_image = ctk.CTkImage(size = (202.5,300), light_image=kai_right, dark_image=kai_right_d )

kai_wrong = Image.open("kai_wrong.png")
kai_wrong_d = Image.open("kai_wrong_d.png")
kai_wrong_image = ctk.CTkImage(size = (202.5,300), light_image=kai_wrong, dark_image=kai_wrong_d )

kai_10 = Image.open("kai_10.png")
kai_10_d = Image.open("kai_10_d.png")
kai_10_image = ctk.CTkImage(size = (202.5,300), light_image=kai_10, dark_image=kai_10_d )

kai_5 = Image.open("kai_5.png")
kai_5_d = Image.open("kai_5_d.png")
kai_5_image = ctk.CTkImage(size = (202.5,300), light_image=kai_5, dark_image=kai_5_d )

kai_finished = Image.open("kai_finished.png")
kai_finished_d = Image.open("kai_finished_d.png")
kai_finished_image = ctk.CTkImage(size = (648,510), light_image=kai_finished, dark_image=kai_finished_d )

limit = Image.open("limit.png")
limit_d = Image.open("limit_d.png")
limit_image = ctk.CTkImage(size = (648,510), light_image=limit, dark_image=limit_d )

edit = Image.open("edit.png")
edit_d = Image.open("edit_d.png")
edit_image = ctk.CTkImage(size = (656,234), light_image=edit, dark_image=edit_d )

radical_build = Image.open("radical_build.png")
radical_build_d = Image.open("radical_build_d.png")
radical_build_image = ctk.CTkImage(size = (361,247), light_image=radical_build, dark_image=radical_build_d )

radical = Image.open("radical.png")
radical_d = Image.open("radical_d.png")
radical_image = ctk.CTkImage(size = (361,247), light_image=radical, dark_image=radical_d )

radical_wrong = Image.open("radical_wrong.png")
radical_wrong_d = Image.open("radical_wrong_d.png")
radical_wrong_image = ctk.CTkImage(size = (361,247), light_image=radical_wrong, dark_image=radical_wrong_d )

meaning_begin = Image.open("meaning_begin.png")
meaning_begin_d = Image.open("meaning_begin_d.png")
meaning_begin_image = ctk.CTkImage(size = (276,494), light_image=meaning_begin, dark_image=meaning_begin_d )

meaning_wrong = Image.open("meaning_wrong.png")
meaning_wrong_d = Image.open("meaning_wrong_d.png")
meaning_wrong_image = ctk.CTkImage(size = (276,494), light_image=meaning_wrong, dark_image=meaning_wrong_d )

meaning_idle = Image.open("meaning_idle.png")
meaning_idle_d = Image.open("meaning_idle_d.png")
meaning_idle_image = ctk.CTkImage(size = (276,494), light_image=meaning_idle, dark_image=meaning_idle_d )

meaning_right = Image.open("meaning_right.png")
meaning_right_d = Image.open("meaning_right_d.png")
meaning_right_image = ctk.CTkImage(size = (276,494), light_image=meaning_right, dark_image=meaning_right_d )



