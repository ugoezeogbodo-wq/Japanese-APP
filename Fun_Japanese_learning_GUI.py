import Nihongo_Charater_Practice as ncp
import Kanji_Practice as kp
import Katakana_Practice as kap
import customtkinter as ctk
import Extra as ext
from PIL import Image

window = ctk.CTk()
window.title("Japanese Character Learning")
window.geometry("810x600")



cream = "#F6FFFA"
linen = "#E6E6DB"
grey = "#A0BBB2"
pink = "#DA7D91"
brown = "#8b4c41"
dgrey = "#507065"
dbrown = "#69362d"
dpink = "#D05A73"

hira_l = None
kana_l = None
kanji_l = None
start_l = None
target_l = None
one = None
two = None
three =  None
four = None
k_target_l = None
k_one = None
k_two = None
k_three = None
k_four = None
target_lt =None
feedback_t = None
feedback_label_t = None
romaji = None
entry_key = None
feedback_label = None
feedback = None
chest_pic = None
ghost_pic = None
k_target_lt = None
k_romaji = None
k_entry_key = None
k_feedback_t = None
k_feedback_label_t = None
k_feedback_label = None
k_feedback = None
k_feedback_f = None
text_just = None
mr_one= None
mr_two= None
mr_three= None
mr_four= None
mr_feedback_label= None
mr_feedback= None
text_just_t = None
mr_romaji = None
mr_entry_key = None
mr_feedback_t = None
mr_feedback_label_t = None
cstreak = None
kanji_nr_l = None
chest_text = None
ghost_text = None
kai_text = None
kai_pic = None
m_target_l = None
m_one= None
m_two= None
m_three= None
m_four= None
m_feedback_label= None
m_feedback= None
m_target_lt= None
m_romaji= None
m_entry_key= None
m_feedback_t= None
m_feedback_label_t= None
kai_picr = None


ctk.FontManager.load_font("Matcha Mint.ttf")
coolfont = "Matcha Mint"

main_frame = ctk.CTkFrame(window,fg_color=linen, border_color=brown, border_width=15)
main_frame.place(relx = 0.5, rely =0.5, relwidth =1.005, relheight = 1.005, anchor = ctk.CENTER)

cover = ctk.CTkFrame(window, fg_color=linen, border_color=brown, border_width=15)
cover.place(relx = 0.5, rely =0.5, relwidth =1.005, relheight = 1.005, anchor = ctk.CENTER)
cover.place_forget()



def start_up():


    intro_label = ctk.CTkLabel(main_frame, fg_color = cream, text="", corner_radius=5)
    intro_label.place(relx = 0.5, rely = 0.30, relwidth =0.90, relheight = .45, anchor=ctk.CENTER)

    hira_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Hiragana", text_color= cream, font = (coolfont, 43), hover_color=dgrey, command = lambda: (indicator(page=hira_mid),side_label(page = hira_mid)))
    hira_button.place(relx = .27, rely=.65, relwidth = .45, relheight = .15, anchor = ctk.CENTER)
   
    kata_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Katakana", text_color= cream, font = (coolfont, 43), hover_color=dgrey, command = lambda: (indicator(page=kana_mid),side_label(page = kana_mid)))
    kata_button.place(relx = .735, rely=.65, relwidth = .45, relheight = .15, anchor = ctk.CENTER)
  

    kanji_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Kanji", text_color= cream, font = (coolfont, 43), hover_color=dgrey, command = lambda: (indicator(page=kanji_mid_r),side_label(page = kanji_mr)))
    kanji_button.place(relx = .27, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)
  

    info_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Information", text_color= cream, font = (coolfont, 42), hover_color=dgrey)
    info_button.place(relx = .735, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)
    


def side_bar():
    global hira_l, kana_l, kanji_l, start_l, kanji_nr_l
    side  = ctk.CTkFrame(main_frame, fg_color=brown, border_width=0, corner_radius=0, bg_color="transparent")
    side.place(relx=0,rely=0.5,relwidth=.15,relheight = 1.05, anchor = "w")


    hira_go = ctk.CTkButton(side, fg_color=brown, text = "Hiragana", font = (coolfont, 17), hover_color=dbrown, text_color=cream, command = lambda: (indicator(page = hira_mid), side_label(page = hira_mid)) )
    hira_go.place(relx = .13, rely = .23,relwidth = .85, relheight = .075)
  

    hira_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    hira_l.place(relx = .07 , rely = 0.23 , relwidth = .05, relheight = .075)

    kana_go = ctk.CTkButton(side, fg_color=brown, text = "Katakana", font = (coolfont, 17), hover_color=dbrown, text_color=cream, command = lambda: (indicator(page = kana_mid), side_label(page=kana_mid)))
    kana_go.place(relx = .13, rely = .33,relwidth = .85, relheight = .075)
   

    kana_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    kana_l.place(relx = .07 , rely = 0.33 , relwidth = .05, relheight = .075)

    kanji_go = ctk.CTkButton(side, fg_color=brown, text = "Kanji \nRadicals", font = (coolfont, 17,), hover_color=dbrown, text_color=cream, command = lambda: (indicator(page = kanji_mid_r), side_label(page=kanji_mr)))
    kanji_go.place(relx = .13, rely = .43,relwidth = .85, relheight = .075)
   

    kanji_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    kanji_l.place(relx = .07 , rely = 0.43 , relwidth = .05, relheight = .075)

    start_go = ctk.CTkButton(side, fg_color=brown, text = "Start Page", font = (coolfont, 15), hover_color=dbrown, text_color=cream, command = lambda: indicator(page=start_up))
    start_go.place(relx = .13, rely = .13,relwidth = .85, relheight = .075)
   

    start_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    start_l.place(relx = .07 , rely = 0.13 , relwidth = .05, relheight = .075)

    kanji_nr_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    kanji_nr_l.place(relx = .07 , rely = 0.53 , relwidth = .05, relheight = .075)
    
    kanji_nr_go = ctk.CTkButton(side, fg_color=brown, text = "Kanji", font = (coolfont, 20,), hover_color=dbrown, text_color=cream, command = lambda: (indicator(page = kanji_mid), side_label(page=kanji_mid)))
    kanji_nr_go.place(relx = .13, rely = .53,relwidth = .85, relheight = .075)

    menu = ctk.CTkLabel(side, fg_color = pink, text = "Menu:", font = (coolfont,25), corner_radius=5)
    menu.place(relx = .5 , rely = 0.075 , relwidth = .88, relheight = .08, anchor = ctk.CENTER)

    if ext.page == 1 or ext.page == 2 or ext.page == 3 or ext.page == 4 or ext.page == 7 or ext.page == 8 or ext.page == 10 or ext.page == 11:
        invert = ctk.CTkButton(side, fg_color=pink, border_color=brown,corner_radius=5, font=(coolfont,15), text="Invert", bg_color="transparent", hover_color=dpink,
                            command=lambda:( ncp.invert_hira(target_l=target_l,one=one,two=two,three=three,four=four,invert=invert), 
                                kap.invert_kana(k_target_l=k_target_l,k_one=k_one,k_two=k_two,k_three=k_three,k_four=k_four, invert=invert),
                                kp.invert_mr(text_just=text_just,mr_one=mr_one,mr_two=mr_two,mr_three=mr_three,mr_four=mr_four,invert=invert, m_target_l=m_target_l,m_one=m_one,m_two=m_two,m_three=m_three,m_four=m_four)))
        invert.place(relx= 0.5, rely=.91, relwidth = .8, relheight= .07,anchor = ctk.CENTER )

    
        mode = ctk.CTkButton(side, fg_color=pink, border_color=brown,corner_radius=5, font=(coolfont,15), text="Invert", bg_color="transparent", hover_color=dpink,
                            command=lambda:( ncp.invert_hira(target_l=target_l,one=one,two=two,three=three,four=four,invert=invert), 
                                kap.invert_kana(k_target_l=k_target_l,k_one=k_one,k_two=k_two,k_three=k_three,k_four=k_four, invert=invert),
                                kp.invert_mr(text_just=text_just,mr_one=mr_one,mr_two=mr_two,mr_three=mr_three,mr_four=mr_four,invert=invert, m_target_l=m_target_l,m_one=m_one,m_two=m_two,m_three=m_three,m_four=m_four)))
        mode.place(relx= 0.5, rely=.86, relwidth = .8, relheight= .07,anchor = ctk.CENTER )
   







def hira_mid():  
   global target_l,one,two,three,four, chest_pic, chest_text
   ext.page = 67
   side_bar()



  

   chest_pic = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.chest_mid_image, text = "")
   chest_pic.place(relx = 0.295, rely = .5,relwidth = 0.25, relheight = 0.9, anchor= ctk.CENTER)

   chest_text = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.chest_text_image, text="", anchor ="w")
   chest_text.place(relx = .67, rely = .255 , relwidth = .57, relheight = .4, anchor = ctk.CENTER)

   hira_mcq = ctk.CTkButton(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=10, 
                            text="Multiple\n Choice", text_color=cream, hover_color=dbrown, font=(coolfont, 30), command=lambda: (indicator(page = hira_m), ncp.load_new_deck(target_l,one,two,three,four, target_lt=target_lt, romaji=romaji, indicator=indicator, finished=finished), side_label(page=hira_m)))
   hira_mcq.place(relx = 0.58, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
   hira_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Easier,\n reccomended \nfor begginers", text_color=dgrey, font=(coolfont,18, "italic"))
   hira_mcq_label.place(relx = 0.76, rely = .52, relwidth = .22, relheight = .17)

   hira_text = ctk.CTkButton(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=10, 
                               text="Text\n Answers", text_color=cream, hover_color=dbrown, font=(coolfont, 30), command=lambda: (indicator(page=hira_t), ncp.load_new_deck(target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji = romaji, indicator=indicator, finished=finished), side_label(page=hira_t)))
   hira_text.place(relx = 0.58, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
   hira_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Harder,\n requires \nsome \nmastery", text_color=dgrey, font=(coolfont,18, "italic"))
   hira_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)

def kana_mid(): 
    global ghost_pic, ghost_text
    ext.page =67
    side_bar()
    ghost_pic = ctk.CTkLabel(main_frame, fg_color=linen, text="", image=ext.ghost_mid_image)
    ghost_pic.place(relx = 0.295, rely = .5, anchor= ctk.CENTER)

    ghost_text = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.ghost_text_image, anchor="w")
    ghost_text.place(relx = .67, rely = .255 , relwidth = .57, relheight = .4, anchor = ctk.CENTER)

    kana_mcq = ctk.CTkButton(main_frame, fg_color=cream, border_color=brown, border_width=5, corner_radius=10, 
                            text="Multiple\n Choice", text_color=dgrey, hover_color=linen, font=(coolfont, 30), command=lambda: (indicator(page = kana_m), kap.load_new_deck(k_target_l=k_target_l,k_one=k_one,k_two=k_two,k_three=k_three,k_four=k_four, k_target_lt=k_target_lt, k_romaji=k_romaji), side_label(page=kana_m)))
    kana_mcq.place(relx = 0.58, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kana_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Easier. So I\nreccomend for \nbegginers", text_color=dgrey, font=(coolfont,17, "italic"))
    kana_mcq_label.place(relx = 0.76, rely = .52, relwidth = .2, relheight = .17)
    
    kana_text = ctk.CTkButton(main_frame, fg_color=cream, border_color=dgrey, border_width=5, corner_radius=10, 
                                   text="Text\n Answers", text_color=brown, hover_color=linen, font=(coolfont, 30), command = lambda: (indicator(page = kana_t), kap.load_new_deck(k_target_l=k_target_l,k_one=k_one,k_two=k_two,k_three=k_three,k_four=k_four, k_target_lt=k_target_lt, k_romaji=k_romaji),side_label(page=kana_t)))
    kana_text.place(relx = 0.58, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kana_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Harder.\n So requires \nsome \nmastery", text_color=dgrey, font=(coolfont,18, "italic"))
    kana_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)

def kanji_mid_r():
    global kai_picr
    ext.page = 67
    side_bar()
    kai_picr = ctk.CTkLabel(main_frame, fg_color=linen, image  = ext.kai_mid_rimage, text = "")
    kai_picr.place(relx = 0.305, rely = .7,relwidth = 0.25, relheight = 0.5, anchor= ctk.CENTER)
    kai_textr = ctk.CTkLabel(main_frame, fg_color=dpink)
    kai_textr.place(relx = .57, rely = .255 , relwidth = .78, relheight = .4, anchor = ctk.CENTER)

    kanji_mcqr = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=10, 
                                text="Multiple\n Choice", text_color=cream, hover_color=dpink, font=(coolfont, 30), command= lambda: (indicator(kanji_mr),kp.load_new_deck(text_just=text_just, mr_one=mr_one, mr_two=mr_two, mr_three=mr_three, mr_four=mr_four, text_just_t=text_just_t, mr_romaji=mr_romaji, indicator=indicator, finished=finished), side_label(page=kanji_mr)))
    kanji_mcqr.place(relx = 0.6, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kanji_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Super easy!\nreccomend for \nbegginers!", text_color=dpink, font=(coolfont,17, "italic"))
    kanji_mcq_label.place(relx = 0.765, rely = .52, relwidth = .2, relheight = .17)
        
    kanji_textr = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=10, 
                                       text="Text\n Answers", text_color=cream, hover_color=dpink, font=(coolfont, 30), command= lambda: (indicator(kanji_mrt), kp.load_new_deck(text_just=text_just, mr_one=mr_one, mr_two=mr_two, mr_three=mr_three, mr_four=mr_four, text_just_t=text_just_t, mr_romaji=mr_romaji, indicator=indicator, finished=finished),side_label(page = kanji_mr)))
    kanji_textr.place(relx = 0.6, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kanji_text_labelr = ctk.CTkLabel(main_frame,fg_color=linen, text= "Little hard!\n So it requires \nsome \nmastery", text_color=dpink, font=(coolfont,18, "italic"))
    kanji_text_labelr.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)


def kanji_mid():
    global kai_pic, kai_text
    ext.page = 67
    side_bar()
    kai_pic = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.kai_mid_image, text = "")
    kai_pic.place(relx = 0.295, rely = .45,relwidth = 0.25, relheight = 0.8, anchor= ctk.CENTER)
    kai_text = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.kai_text_image, text="hiii", font=(coolfont, 30), anchor="w")
    kai_text.place(relx = .685, rely = .255 , relwidth = .56, relheight = .4, anchor = ctk.CENTER)
    
    kanji_mcq = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=10, 
                                    text="Multiple\n Choice", text_color=cream, hover_color=dpink, font=(coolfont, 30), command= lambda: (indicator(kanji_m),kp.load_new_deck_hira(m_target_l=m_target_l, m_one=m_one, m_two=m_two, m_three=m_three, m_four=m_four, m_target_lt=m_target_lt, m_romaji=m_romaji, indicator=indicator, finished=finished),side_label(page = kanji_m)))
    kanji_mcq.place(relx = 0.58, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kanji_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Super easy!\nreccomend for \nbegginers!", text_color=dpink, font=(coolfont,17, "italic"))
    kanji_mcq_label.place(relx = 0.76, rely = .52, relwidth = .2, relheight = .17)
            
    kanji_text = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=10, 
                                           text="Text\n Answers", text_color=cream, hover_color=dpink, font=(coolfont, 30), command= lambda: (indicator(kanji_mt), kp.load_new_deck_hira(m_target_l=m_target_l, m_one=m_one, m_two=m_two, m_three=m_three, m_four=m_four, m_target_lt=m_target_lt, m_romaji=m_romaji, indicator=indicator, finished=finished),side_label(page = kanji_m)))
    kanji_text.place(relx = 0.58, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kanji_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Little hard!\n So it requires \nsome \nmastery", text_color=dpink, font=(coolfont,18, "italic"))
    kanji_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)
    
    kanji_edit = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, text="Edit data", font = (coolfont, 15), hover_color=dpink,
                                   text_color=cream, corner_radius=5, border_width=5)
    kanji_edit.place(relx=0.29, rely=.9, relwidth = .2, relheight = .1, anchor = ctk.CENTER)

def hira_m():
    global target_l,one,two,three,four, feedback_label,feedback, cstreak
    ext.page = 1
    side_bar()

    
    
    feedback = ctk.CTkLabel(main_frame, fg_color=brown, image=ext.chest_begin_image, text="")
    feedback.place(relx = 0.57, rely = 0.23, anchor = ctk.CENTER)
    feedback.active_pil_image = ext.chest_begin_image._light_image

    feedback_f = ctk.CTkFrame(feedback, fg_color=brown,corner_radius=0, bg_color="transparent" )
    feedback_f.place(relx=.695, rely=.45, relwidth=.44, relheight=.53, anchor = ctk.CENTER)

    feedback_label = ctk.CTkLabel(feedback_f, fg_color=brown,corner_radius=0, bg_color="transparent", justify = "center", text = "Press the option that you believe to be correct to get started.", wraplength=300,font=(coolfont,19) )
    feedback_label.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    

    target_l = ctk.CTkLabel(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    target_l.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER )

    one = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = one, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    one.place(relx = 0.37, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    two = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = two, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize,indicator=indicator, finished=finished, cstreak=cstreak))
    two.place(relx = 0.77, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    three = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = three, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize,indicator=indicator, finished=finished, cstreak=cstreak))
    three.place(relx = 0.37, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    four = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = four, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize, indicator=indicator, finished=finished,cstreak=cstreak))
    four.place(relx = 0.77, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=brown)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)

    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=brown, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=cream, wraplength=300, corner_radius=10, border_color=dbrown, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)

def kanji_mr():
    global text_just,mr_one,mr_two,mr_three,mr_four, mr_feedback_label,mr_feedback
    ext.page = 7
    side_bar()

    
    
    mr_feedback = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.chest_begin_image, text="")
    mr_feedback.place(relx = 0.57, rely = 0.23, anchor = ctk.CENTER)
    mr_feedback.active_pil_image = ext.chest_begin_image._light_image

    mr_feedback_f = ctk.CTkFrame(mr_feedback, fg_color=pink,corner_radius=0, bg_color="transparent" )
    mr_feedback_f.place(relx=.695, rely=.45, relwidth=.44, relheight=.53, anchor = ctk.CENTER)

    mr_feedback_label = ctk.CTkLabel(mr_feedback_f, fg_color=pink,corner_radius=0, bg_color="transparent", justify = "center", text = "Press the option that you believe to be correct to get started.", wraplength=300,font=(coolfont,19) )
    mr_feedback_label.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    

    mr_target_l = ctk.CTkLabel(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    mr_target_l.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER )

    text_just = ctk.CTkLabel(mr_target_l, fg_color = pink, font=(coolfont,55, "bold"))
    text_just.place(relx=.39,rely=.5,relwidth=.7,relheight=.9, anchor = ctk.CENTER)

    mr_one = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer(button = mr_one, text_just=text_just, mr_one=mr_one, mr_two=mr_two, mr_three=mr_three, mr_four=mr_four, text_just_t=text_just_t, mr_romaji=romaji, mr_feedback_label=mr_feedback_label,mr_feedback=mr_feedback, mr_feedback_t=feedback_t, mr_feedback_label_t=mr_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    mr_one.place(relx = 0.37, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    mr_two = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer(button = mr_two, text_just=text_just, mr_one=mr_one, mr_two=mr_two, mr_three=mr_three, mr_four=mr_four, text_just_t=text_just_t, mr_romaji=romaji, mr_feedback_label=mr_feedback_label,mr_feedback=mr_feedback, mr_feedback_t=feedback_t, mr_feedback_label_t=mr_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    mr_two.place(relx = 0.77, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    mr_three = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer(button = mr_three, text_just=text_just, mr_one=mr_one, mr_two=mr_two, mr_three=mr_three, mr_four=mr_four, text_just_t=text_just_t, mr_romaji=romaji, mr_feedback_label=mr_feedback_label,mr_feedback=mr_feedback, mr_feedback_t=feedback_t, mr_feedback_label_t=mr_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    mr_three.place(relx = 0.37, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    mr_four = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer(button = mr_four,text_just=text_just, mr_one=mr_one, mr_two=mr_two, mr_three=mr_three, mr_four=mr_four, text_just_t=text_just_t, mr_romaji=romaji, mr_feedback_label=mr_feedback_label,mr_feedback=mr_feedback, mr_feedback_t=feedback_t, mr_feedback_label_t=mr_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    mr_four.place(relx = 0.77, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=pink)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)
    
    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=pink, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=cream, wraplength=300, corner_radius=10, border_color=cream, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)

def kanji_m():
    global m_target_l,m_one,m_two,m_three,m_four, m_feedback_label,m_feedback
    ext.page = 10
    side_bar()

    
    
    m_feedback = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.chest_begin_image, text="")
    m_feedback.place(relx = 0.57, rely = 0.23, anchor = ctk.CENTER)
    m_feedback.active_pil_image = ext.chest_begin_image._light_image

    m_feedback_f = ctk.CTkFrame(m_feedback, fg_color=pink,corner_radius=0, bg_color="transparent" )
    m_feedback_f.place(relx=.695, rely=.45, relwidth=.44, relheight=.53, anchor = ctk.CENTER)

    m_feedback_label = ctk.CTkLabel(m_feedback_f, fg_color=pink,corner_radius=0, bg_color="transparent", justify = "center", text = "Press the option that you believe to be correct to get started.", wraplength=300,font=(coolfont,19) )
    m_feedback_label.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    

    m_target_l = ctk.CTkLabel(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    m_target_l.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER )


    m_one = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer_hira(button = m_one, m_target_l=m_target_l, m_one=m_one, m_two=m_two, m_three=m_three, m_four=m_four, m_target_lt=m_target_lt, m_romaji=m_romaji, m_feedback_label=m_feedback_label,m_feedback=m_feedback, m_feedback_t=m_feedback_t, m_feedback_label_t=m_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    m_one.place(relx = 0.37, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    m_two = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer_hira(button = m_two, m_target_l=m_target_l, m_one=m_one, m_two=m_two, m_three=m_three, m_four=m_four, m_target_lt=m_target_lt, m_romaji=m_romaji, m_feedback_label=m_feedback_label,m_feedback=m_feedback, m_feedback_t=m_feedback_t, m_feedback_label_t=m_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    m_two.place(relx = 0.77, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    m_three = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer_hira(button = m_three, m_target_l=m_target_l, m_one=m_one, m_two=m_two, m_three=m_three, m_four=m_four, m_target_lt=m_target_lt, m_romaji=m_romaji, m_feedback_label=m_feedback_label,m_feedback=m_feedback, m_feedback_t=m_feedback_t, m_feedback_label_t=m_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    m_three.place(relx = 0.37, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    m_four = ctk.CTkButton(main_frame, fg_color=pink, corner_radius=5, border_color=cream, font=(coolfont,40, "bold"), border_width=5, hover_color=dpink, command=lambda: kp.check_answer_hira(button = m_four, m_target_l=m_target_l, m_one=m_one, m_two=m_two, m_three=m_three, m_four=m_four, m_target_lt=m_target_lt, m_romaji=m_romaji, m_feedback_label=m_feedback_label,m_feedback=m_feedback, m_feedback_t=m_feedback_t, m_feedback_label_t=m_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    m_four.place(relx = 0.77, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=pink)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)
    
    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=pink, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=cream, wraplength=300, corner_radius=10, border_color=cream, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)

def kana_m():
    global k_target_l,k_one,k_two,k_three,k_four, k_feedback_label,k_feedback, k_feedback_f

    ext.page = 3
    side_bar()
    
    k_feedback = ctk.CTkLabel(main_frame, fg_color=grey, image=ext.ghost_begin_image, text = "")
    k_feedback.place(relx = 0.57, rely = 0.24, anchor = ctk.CENTER)
    k_feedback.active_pil_image = ext.ghost_begin_image._light_image

    k_feedback_f = ctk.CTkFrame(k_feedback, fg_color="white",corner_radius=0, bg_color="transparent" )
    k_feedback_f.place(relx=.693, rely=.45, relwidth=.5, relheight=.65, anchor = ctk.CENTER)
    
    k_feedback_label = ctk.CTkLabel(k_feedback_f, fg_color="white",corner_radius=0, bg_color="transparent", justify = "center", text = "Just press something.. I don't really care.", wraplength=300,font=(coolfont,23), text_color=dgrey)
    k_feedback_label.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    

    k_target_l = ctk.CTkLabel(main_frame, fg_color=cream, border_color=dgrey, border_width=5, corner_radius=5, font=(coolfont,55, "bold"), text_color=brown)
    k_target_l.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER )

    k_one = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_one, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize,cstreak=cstreak))
    k_one.place(relx = 0.37, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    k_two = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_two, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize,cstreak=cstreak))
    k_two.place(relx = 0.77, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    k_three = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_three, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize, cstreak=cstreak))
    k_three.place(relx = 0.37, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    k_four = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_four, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize, cstreak=cstreak))
    k_four.place(relx = 0.77, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=cream)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)
    
    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=cream, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=brown, wraplength=300, corner_radius=10, border_color=dgrey, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)


def hira_t():
    global target_lt, romaji, entry_key, feedback_t, feedback_label_t, cstreak
    ext.page = 5
    side_bar()
    
    feedback_t = ctk.CTkLabel(main_frame, fg_color=linen, image =ext.chest_begin_image, text="")
    feedback_t.place(relx = 0.57, rely = 0.23,anchor = ctk.CENTER)
    feedback_t.active_pil_image = ext.chest_begin_image._light_image

    feedback_ft = ctk.CTkFrame(feedback_t, fg_color=brown,corner_radius=0, bg_color="transparent" )
    feedback_ft.place(relx=.695, rely=.45, relwidth=.44, relheight=.53, anchor = ctk.CENTER)
    
    feedback_label_t = ctk.CTkLabel(feedback_ft, fg_color=brown,corner_radius=0, bg_color="transparent", justify = "center", text = "Once you've input your answer just press the enter key to submit.", wraplength=330,font=(coolfont,18) )
    feedback_label_t.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    
    target_lt = ctk.CTkLabel(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    target_lt.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER) 

    romaji = ctk.CTkEntry(main_frame, fg_color=brown, font=(coolfont, 40), placeholder_text="", justify = "center", border_width=5, border_color=dbrown)      
    romaji.place(relx= 0.57, rely = .77, relwidth = .5, relheight = .2, anchor = ctk.CENTER)  

    entry_key = ctk.CTkButton(main_frame, fg_color="transparent", hover= None)  
    romaji.bind("<Return>", lambda _event: ncp.check_answer(target_l=target_l,one=one,two=two,three=three,four=four,button=entry_key, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize,indicator=indicator, finished=finished, cstreak=cstreak))
    entry_key.place(relx=0, rely=0,relwidth=.001, relheight = .0001) 

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=brown)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)
    
    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=brown, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=cream, wraplength=300, corner_radius=10, border_color=dbrown, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)

def kana_t():
    global k_target_lt, k_romaji, k_entry_key, k_feedback_t, k_feedback_label_t
    ext.page = 6
    side_bar()
    
    
    k_feedback_t = ctk.CTkLabel(main_frame, fg_color=linen, image =ext.ghost_begin_image, text = "")
    k_feedback_t.place(relx = 0.57, rely = 0.24,anchor = ctk.CENTER)
    k_feedback_t.active_pil_image = ext.ghost_begin_image._light_image

    k_feedback_ft = ctk.CTkFrame(k_feedback_t, fg_color="white",corner_radius=0, bg_color="transparent" )
    k_feedback_ft.place(relx=.693, rely=.45, relwidth=.5, relheight=.65, anchor = ctk.CENTER)
    
    k_feedback_label_t = ctk.CTkLabel(k_feedback_ft, fg_color="white",corner_radius=0, bg_color="transparent", justify = "center", text = "Sigh, to submit your answer press the enter key.", wraplength=300,font=(coolfont,18), text_color=dgrey)
    k_feedback_label_t.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    
    k_target_lt = ctk.CTkLabel(main_frame, fg_color=cream, border_color=dgrey, border_width=5, corner_radius=5, font=(coolfont,55, "bold"),text_color=dbrown)
    k_target_lt.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER) 

    k_romaji = ctk.CTkEntry(main_frame, fg_color=cream, font=(coolfont, 40), placeholder_text="", justify = "center", border_width=5, border_color=dbrown, text_color=dgrey)      
    k_romaji.place(relx= 0.57, rely = .77, relwidth = .5, relheight = .2, anchor = ctk.CENTER)  

    k_entry_key = ctk.CTkButton(main_frame, fg_color="transparent", hover= None)  
    k_romaji.bind("<Return>", lambda _event: kap.check_answer(button = k_four, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize,cstreak=cstreak))
    k_entry_key.place(relx=0, rely=0,relwidth=.001, relheight = .0001) 

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=cream)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)
        
    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=cream, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=brown, wraplength=300, corner_radius=10, border_color=dgrey, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)

def kanji_mrt():
    global text_just_t, mr_romaji, mr_entry_key, mr_feedback_t, mr_feedback_label_t
    ext.page = 9
    side_bar()
    
    mr_feedback_t = ctk.CTkLabel(main_frame, fg_color=linen, image =ext.chest_begin_image, text="")
    mr_feedback_t.place(relx = 0.57, rely = 0.23,anchor = ctk.CENTER)
    mr_feedback_t.active_pil_image = ext.chest_begin_image._light_image

    mr_feedback_ft = ctk.CTkFrame(mr_feedback_t, fg_color=brown,corner_radius=0, bg_color="transparent" )
    mr_feedback_ft.place(relx=.695, rely=.45, relwidth=.44, relheight=.53, anchor = ctk.CENTER)
    
    mr_feedback_label_t = ctk.CTkLabel(mr_feedback_ft, fg_color=brown,corner_radius=0, bg_color="transparent", justify = "center", text = "Once you've input your answer just press the enter key to submit.", wraplength=330,font=(coolfont,18) )
    mr_feedback_label_t.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    
    mr_target_lt = ctk.CTkLabel(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    mr_target_lt.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER) 

    text_just_t = ctk.CTkLabel(mr_target_lt, fg_color = pink, font=(coolfont,55, "bold"))
    text_just_t.place(relx=.39,rely=.5,relwidth=.7,relheight=.9, anchor = ctk.CENTER)

    mr_romaji = ctk.CTkEntry(main_frame, fg_color=brown, font=(coolfont, 40), placeholder_text="", justify = "center", border_width=5, border_color=cream)      
    mr_romaji.place(relx= 0.57, rely = .77, relwidth = .5, relheight = .2, anchor = ctk.CENTER)  

    mr_entry_key = ctk.CTkButton(main_frame, fg_color="transparent", hover= None)  
    mr_romaji.bind("<Return>", lambda _event: kp.check_answer(text_just=text_just,mr_one=mr_one,mr_two=mr_two,mr_three=mr_three,mr_four=mr_four,button=mr_entry_key, text_just_t=text_just_t, mr_romaji=mr_romaji, mr_feedback_label=mr_feedback_label,mr_feedback=mr_feedback, mr_feedback_t=mr_feedback_t, mr_feedback_label_t=mr_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    mr_entry_key.place(relx=0, rely=0,relwidth=.001, relheight = .0001)

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=pink)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)
        
    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=pink, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=cream, wraplength=300, corner_radius=10, border_color=cream, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)

def kanji_mt():
    global m_target_lt, m_romaji, m_entry_key, m_feedback_t, m_feedback_label_t
    ext.page = 12
    side_bar()
    
    m_feedback_t = ctk.CTkLabel(main_frame, fg_color=linen, image =ext.chest_begin_image, text="")
    m_feedback_t.place(relx = 0.57, rely = 0.23,anchor = ctk.CENTER)
    m_feedback_t.active_pil_image = ext.chest_begin_image._light_image

    m_feedback_ft = ctk.CTkFrame(m_feedback_t, fg_color=brown,corner_radius=0, bg_color="transparent" )
    m_feedback_ft.place(relx=.695, rely=.45, relwidth=.44, relheight=.53, anchor = ctk.CENTER)
    
    m_feedback_label_t = ctk.CTkLabel(m_feedback_ft, fg_color=brown,corner_radius=0, bg_color="transparent", justify = "center", text = "Once you've input your answer just press the enter key to submit.", wraplength=330,font=(coolfont,18) )
    m_feedback_label_t.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    
    m_target_lt = ctk.CTkLabel(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    m_target_lt.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER) 

    m_romaji = ctk.CTkEntry(main_frame, fg_color=brown, font=(coolfont, 40), placeholder_text="", justify = "center", border_width=5, border_color=cream)      
    m_romaji.place(relx= 0.57, rely = .77, relwidth = .5, relheight = .2, anchor = ctk.CENTER)  

    m_entry_key = ctk.CTkButton(main_frame, fg_color="transparent", hover= None)  
    m_romaji.bind("<Return>", lambda _event: kp.check_answer_hira(m_target_l=m_target_lt,m_one=m_one,m_two=m_two,m_three=m_three,m_four=m_four,button=m_entry_key, m_target_lt=m_target_lt, m_romaji=m_romaji, m_feedback_label=m_feedback_label,m_feedback=m_feedback, m_feedback_t=m_feedback_t, m_feedback_label_t=m_feedback_label_t,resize=resize, indicator=indicator, finished=finished, cstreak=cstreak))
    m_entry_key.place(relx=0, rely=0,relwidth=.001, relheight = .0001)

    cstreak_frame = ctk.CTkFrame(main_frame, fg_color=pink)
    cstreak_frame.place(relx= 0.86, rely=.45, relwidth = 0.2, relheight = .07, anchor = ctk.CENTER)
        
    cstreak = ctk.CTkLabel(cstreak_frame, fg_color=pink, font=(coolfont,12,"italic"), anchor="center", text="Current streak: 0 \nHighest streak: 0 ", text_color=cream, wraplength=300, corner_radius=10, border_color=cream, border_width=3)
    cstreak.place(relx= .5, rely=.5, relwidth = 1, relheight = 1, anchor = ctk.CENTER)
def finished():
    side_bar()

    finished =  ctk.CTkLabel(main_frame, fg_color = brown)
    finished.place(rely=0.5, relx=0.565,relwidth = 0.8, relheight= 0.85, anchor = ctk.CENTER)

finished()

def side_label(page):
    global hira_l, kana_l, kanji_l, start_l
    if page == hira_mid or page == hira_m or page == hira_t:
        hira_l.configure(fg_color = brown)
    if page == kana_mid or page == kana_m or page == kana_t:
        kana_l.configure(fg_color = brown)
    if  page == kanji_mr:
        kanji_l.configure(fg_color = brown)
    if page == kanji_mid or page == kanji_m:
        kanji_nr_l.configure(fg_color = brown)



def indicator(page):
    global ghost_pic
    ext.streak = 0
    ext.t_streak = 0
    cover.place(relx=0.5, rely=0.5, relwidth=1.005, relheight=1.005, anchor=ctk.CENTER)
    cover.lift()  
    cover.update()

    for child in main_frame.winfo_children():
        child.destroy()
        
    
    page()
    resize()
    cover.update_idletasks()
    cover.place_forget()

def resize_static(label, image, per, min_h, mode, min_w, text_label):
    
    if label is None:
        return

    try:
        if not label.winfo_exists():
            return
    except Exception:
        return

    win_w = window.winfo_width()
    win_h = window.winfo_height()

    if win_h <= 100 or win_w <= 100:
        return

    try:
        light_pil = image._light_image
        dark_pil = image._dark_image
    except Exception:
        light_pil = label.active_pil_image
        dark_pil = label.active_pil_image

    orig_w, orig_h = light_pil.size
    aspect_ratio = orig_w / orig_h

    if mode == "h":
        new_h = max(min_h, int(win_h * per))
        new_w = int(new_h * aspect_ratio)
    else:
        new_w = max(min_w, int(win_w * per))
        new_h = min(int(new_w / aspect_ratio), 600)

    new_wrap = max(200, int(new_w * 0.50) - 40)
    if label:
        label.configure(width=new_w, height=new_h)
    if text_label:
        text_label.configure(wraplength = new_wrap)

    scaled_img = ctk.CTkImage(
        light_image=light_pil,
        dark_image=dark_pil,
        size=(new_w, new_h)
    )

    label.configure(image=scaled_img)
    label.image_ref = scaled_img





def resize(e=None):
    if e is not None and e.widget != window:
            return

    resize_static(ghost_pic, ext.ghost_mid_image, per = 0.62, min_h=350, mode = "h", min_w=0, text_label=None)
    resize_static(chest_pic,ext.chest_mid_image, per=0.61, min_h=350, mode="h", min_w=0, text_label=None)
    resize_static(kai_pic,ext.kai_mid_image, per=0.54, min_h=350, mode="h", min_w=0, text_label=None)
    resize_static(kai_picr,ext.kai_mid_rimage,per=0.33,min_h=300,mode = "h", min_w=0, text_label=None)
    resize_static(k_feedback,None, per = 0.425, min_h=0, mode="w", min_w=608,text_label = k_feedback_label)
    resize_static(k_feedback_t,None, per = 0.4, min_h=0, mode="w", min_w=608, text_label = k_feedback_label_t)
    resize_static(feedback,None, per = 0.39, min_h=0, mode="w", min_w=608,text_label=feedback_label)
    resize_static(feedback_t,None, per = 0.425, min_h=0, mode="w", min_w=608,text_label=feedback_label_t)
    resize_static(mr_feedback_t,None, per = 0.425, min_h=0, mode="w", min_w=608,text_label=mr_feedback_label_t)
    resize_static(mr_feedback,None, per = 0.39, min_h=0, mode="w", min_w=608,text_label=mr_feedback_label)   
    resize_static(chest_text,ext.chest_text_image,per=0.32,min_h = 240, mode = "w", min_w=462, text_label=None) 
    resize_static(ghost_text,image=ext.ghost_text_image,per=0.32,min_h = 240, mode = "w", min_w = 462, text_label=None)
    resize_static(kai_text,image=ext.kai_text_image,per=0.31,min_h = 240, mode = "w", min_w = 462, text_label=None)
        

window.bind("<Configure>", resize)


window.mainloop()