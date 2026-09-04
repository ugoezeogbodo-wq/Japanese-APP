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

resize_list = [
    (ghost_pic, ext.ghost_mid_image, 0.61), 
    (chest_pic, ext.chest_mid_image, 0.61)
    ]



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
  

    kanji_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Kanji", text_color= cream, font = (coolfont, 43), hover_color=dgrey, command = lambda: (indicator(page=kanji_mid),side_label(page = kanji_mid)))
    kanji_button.place(relx = .27, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)
  

    info_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Information", text_color= cream, font = (coolfont, 42), hover_color=dgrey)
    info_button.place(relx = .735, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)
    


def side_bar():
    global hira_l, kana_l, kanji_l, start_l
    side  = ctk.CTkFrame(main_frame, fg_color=brown, border_width=0, corner_radius=0, bg_color="transparent")
    side.place(relx=0,rely=0.5,relwidth=.15,relheight = 1.05, anchor = "w")

    hira_go = ctk.CTkButton(side, fg_color=brown, text = "Hiragana", font = (coolfont, 17), hover_color=dbrown, text_color=cream, command = lambda: (indicator(page = hira_mid), side_label(page = hira_mid)) )
    hira_go.place(relx = .13, rely = .43,relwidth = .85, relheight = .075)
  

    hira_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    hira_l.place(relx = .07 , rely = 0.43 , relwidth = .05, relheight = .075)

    kana_go = ctk.CTkButton(side, fg_color=brown, text = "Katakana", font = (coolfont, 17), hover_color=dbrown, text_color=cream, command = lambda: (indicator(page = kana_mid), side_label(page=kana_mid)))
    kana_go.place(relx = .13, rely = .23,relwidth = .85, relheight = .075)
   

    kana_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    kana_l.place(relx = .07 , rely = 0.23 , relwidth = .05, relheight = .075)

    kanji_go = ctk.CTkButton(side, fg_color=brown, text = "Kanji", font = (coolfont, 20,), hover_color=dbrown, text_color=cream, command = lambda: (indicator(page = kanji_mid), side_label(page=kanji_mid)))
    kanji_go.place(relx = .13, rely = .33,relwidth = .85, relheight = .075)
   

    kanji_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    kanji_l.place(relx = .07 , rely = 0.33 , relwidth = .05, relheight = .075)

    start_go = ctk.CTkButton(side, fg_color=brown, text = "Start Page", font = (coolfont, 15), hover_color=dbrown, text_color=cream, command = lambda: indicator(page=start_up))
    start_go.place(relx = .13, rely = .13,relwidth = .85, relheight = .075)
   

    start_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    start_l.place(relx = .07 , rely = 0.13 , relwidth = .05, relheight = .075)

    menu = ctk.CTkLabel(side, fg_color = pink, text = "Menu:", font = (coolfont,25), corner_radius=5)
    menu.place(relx = .5 , rely = 0.075 , relwidth = .88, relheight = .08, anchor = ctk.CENTER)

    if ext.page == 1 or ext.page == 2 or ext.page == 3 or ext.page == 4 :
        invert = ctk.CTkButton(side, fg_color=pink, border_color=brown,corner_radius=5, font=(coolfont,15), text="Invert", bg_color="transparent", hover_color=dpink,
                            command=lambda:( ncp.invert_hira(target_l=target_l,one=one,two=two,three=three,four=four,invert=invert), 
                                kap.invert_kana(k_target_l=k_target_l,k_one=k_one,k_two=k_two,k_three=k_three,k_four=k_four, invert=invert)))
        invert.place(relx= 0.5, rely=.91, relwidth = .8, relheight= .07,anchor = ctk.CENTER )
   







def hira_mid():  
   global target_l,one,two,three,four, chest_pic
   ext.page = 67
   side_bar()



  

   chest_pic = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.chest_mid_image, text = "")
   chest_pic.place(relx = 0.295, rely = .5,relwidth = 0.25, relheight = 0.9, anchor= ctk.CENTER)

   chest_text = ctk.CTkLabel(main_frame, fg_color=brown)
   chest_text.place(relx = .7, rely = .255 , relwidth = .5, relheight = .4, anchor = ctk.CENTER)

   hira_mcq = ctk.CTkButton(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=10, 
                            text="Multiple\n Choice", text_color=cream, hover_color=dbrown, font=(coolfont, 30), command=lambda: (indicator(page = hira_m), ncp.load_new_deck(target_l,one,two,three,four, target_lt=target_lt, romaji=romaji), side_label(page=hira_m)))
   hira_mcq.place(relx = 0.6, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
   hira_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Easier,\n reccomended \nfor begginers", text_color=dgrey, font=(coolfont,18, "italic"))
   hira_mcq_label.place(relx = 0.765, rely = .52, relwidth = .2, relheight = .17)

   hira_text = ctk.CTkButton(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=10, 
                               text="Text\n Answers", text_color=cream, hover_color=dbrown, font=(coolfont, 30), command=lambda: (indicator(page=hira_t), ncp.load_new_deck(target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji = romaji), side_label(page=hira_t)))
   hira_text.place(relx = 0.6, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
   hira_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Harder,\n requires \nsome \nmastery", text_color=dgrey, font=(coolfont,18, "italic"))
   hira_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)

def kana_mid(): 
    global ghost_pic
    ext.page =67
    side_bar()
    ghost_pic = ctk.CTkLabel(main_frame, fg_color=linen, text="", image=ext.ghost_mid_image)
    ghost_pic.place(relx = 0.295, rely = .5, anchor= ctk.CENTER)

    ghost_text = ctk.CTkLabel(main_frame, fg_color=cream)
    ghost_text.place(relx = .7, rely = .255 , relwidth = .5, relheight = .4, anchor = ctk.CENTER)

    kana_mcq = ctk.CTkButton(main_frame, fg_color=cream, border_color=brown, border_width=5, corner_radius=10, 
                            text="Multiple\n Choice", text_color=dgrey, hover_color=linen, font=(coolfont, 30), command=lambda: (indicator(page = kana_m), kap.load_new_deck(k_target_l=k_target_l,k_one=k_one,k_two=k_two,k_three=k_three,k_four=k_four, k_target_lt=k_target_lt, k_romaji=k_romaji), side_label(page=kana_m)))
    kana_mcq.place(relx = 0.6, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kana_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Easier. So I\nreccomend for \nbegginers", text_color=dgrey, font=(coolfont,17, "italic"))
    kana_mcq_label.place(relx = 0.765, rely = .52, relwidth = .2, relheight = .17)
    
    kana_text = ctk.CTkButton(main_frame, fg_color=cream, border_color=dgrey, border_width=5, corner_radius=10, 
                                   text="Text\n Answers", text_color=brown, hover_color=linen, font=(coolfont, 30), command = lambda: (indicator(page = kana_t), kap.load_new_deck(k_target_l=k_target_l,k_one=k_one,k_two=k_two,k_three=k_three,k_four=k_four, k_target_lt=k_target_lt, k_romaji=k_romaji),side_label(page=kana_t)))
    kana_text.place(relx = 0.6, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kana_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Harder.\n So requires \nsome \nmastery", text_color=dgrey, font=(coolfont,18, "italic"))
    kana_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)

def kanji_mid():
    ext.page = 67
    side_bar()
    kai_pic = ctk.CTkLabel(main_frame, fg_color=pink)
    kai_pic.place(relx = 0.295, rely = .45,relwidth = 0.25, relheight = 0.8, anchor= ctk.CENTER)
    kai_text = ctk.CTkLabel(main_frame, fg_color=pink)
    kai_text.place(relx = .7, rely = .255 , relwidth = .5, relheight = .4, anchor = ctk.CENTER)

    kanji_mcq = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=10, 
                                text="Multiple\n Choice", text_color=cream, hover_color=dpink, font=(coolfont, 30))
    kanji_mcq.place(relx = 0.6, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kanji_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Super easy!\nreccomend for \nbegginers!", text_color=dpink, font=(coolfont,17, "italic"))
    kanji_mcq_label.place(relx = 0.765, rely = .52, relwidth = .2, relheight = .17)
        
    kanji_text = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, border_width=5, corner_radius=10, 
                                       text="Text\n Answers", text_color=cream, hover_color=dpink, font=(coolfont, 30))
    kanji_text.place(relx = 0.6, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kanji_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Little hard!\n So it requires \nsome \nmastery", text_color=dpink, font=(coolfont,18, "italic"))
    kanji_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)

    kanji_edit = ctk.CTkButton(main_frame, fg_color=pink, border_color=cream, text="Edit data", font = (coolfont, 15), hover_color=dpink,
                               text_color=cream, corner_radius=5, border_width=5)
    kanji_edit.place(relx=0.29, rely=.91, relwidth = .2, relheight = .1, anchor = ctk.CENTER)


def hira_m():
    global target_l,one,two,three,four, feedback_label,feedback
    ext.page = 1
    side_bar()

    
    
    feedback = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.chest_begin_image, text="")
    feedback.place(relx = 0.57, rely = 0.24, relwidth = 0.75, relheight = 0.4, anchor = ctk.CENTER)
    feedback.active_pil_image = ext.chest_begin_image._light_image

    feedback_f = ctk.CTkFrame(main_frame, fg_color=brown,corner_radius=0, bg_color="transparent" )
    feedback_f.place(relx=.715, rely=.22, relwidth=.4, relheight=.17, anchor = ctk.CENTER)

    feedback_label = ctk.CTkLabel(feedback_f, fg_color=brown,corner_radius=0, bg_color="transparent", justify = "center", text = "Press the option that you believe to be correct to get started.", wraplength=330,font=(coolfont,18) )
    feedback_label.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    

    target_l = ctk.CTkLabel(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    target_l.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER )

    one = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = one, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize))
    one.place(relx = 0.37, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    two = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = two, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize))
    two.place(relx = 0.77, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    three = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = three, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize))
    three.place(relx = 0.37, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    four = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40, "bold"), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = four, target_l=target_l, one=one, two=two, three=three, four=four, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize))
    four.place(relx = 0.77, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)

def kana_m():
    global k_target_l,k_one,k_two,k_three,k_four, k_feedback_label,k_feedback

    ext.page = 3
    side_bar()
    
    k_feedback = ctk.CTkLabel(main_frame, fg_color=linen, image=ext.ghost_begin_image, text = "")
    k_feedback.place(relx = 0.57, rely = 0.24, relwidth = 0.75, relheight = 0.4, anchor = ctk.CENTER)
    k_feedback.active_pil_image = ext.ghost_begin_image._light_image

    k_feedback_f = ctk.CTkFrame(main_frame, fg_color="blue",corner_radius=0, bg_color="transparent" )
    k_feedback_f.place(relx=.693, rely=.22, relwidth=.35, relheight=.17, anchor = ctk.CENTER)
    
    k_feedback_label = ctk.CTkLabel(k_feedback_f, fg_color="white",corner_radius=0, bg_color="transparent", justify = "center", text = "Just press something.. I don't really care.", wraplength=360,font=(coolfont,20), text_color=dgrey)
    k_feedback_label.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)

    k_target_l = ctk.CTkLabel(main_frame, fg_color=cream, border_color=dgrey, border_width=5, corner_radius=5, font=(coolfont,55, "bold"), text_color=brown)
    k_target_l.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER )

    k_one = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_one, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize))
    k_one.place(relx = 0.37, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    k_two = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_two, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize))
    k_two.place(relx = 0.77, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    k_three = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_three, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize))
    k_three.place(relx = 0.37, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    k_four = ctk.CTkButton(main_frame, fg_color=cream, corner_radius=5, border_color=brown,text_color=dgrey, font=(coolfont,40, "bold"), border_width=5, hover_color=linen, command=lambda: kap.check_answer(button = k_four, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize))
    k_four.place(relx = 0.77, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)

def kanji_m():
    print("k")

def hira_t():
    global target_lt, romaji, entry_key, feedback_t, feedback_label_t
    ext.page = 5
    side_bar()
    
    feedback_t = ctk.CTkLabel(main_frame, fg_color=linen, image =ext.chest_begin_image)
    feedback_t.place(relx = 0.57, rely = 0.24, relwidth = 0.75, relheight = 0.4, anchor = ctk.CENTER)
    feedback_t.active_pil_image = ext.chest_begin_image._light_image

    feedback_ft = ctk.CTkFrame(main_frame, fg_color=brown,corner_radius=0, bg_color="transparent" )
    feedback_ft.place(relx=.715, rely=.22, relwidth=.4, relheight=.17, anchor = ctk.CENTER)
    
    feedback_label_t = ctk.CTkLabel(feedback_ft, fg_color=brown,corner_radius=0, bg_color="transparent", justify = "center", text = "Once you've input your answer just press the enter key to submit.", wraplength=330,font=(coolfont,18) )
    feedback_label_t.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    
    target_lt = ctk.CTkLabel(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    target_lt.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER) 

    romaji = ctk.CTkEntry(main_frame, fg_color=brown, font=(coolfont, 40), placeholder_text="", justify = "center", border_width=5, border_color=dbrown)      
    romaji.place(relx= 0.57, rely = .77, relwidth = .5, relheight = .2, anchor = ctk.CENTER)  

    entry_key = ctk.CTkButton(main_frame, fg_color="transparent", hover= None)  
    romaji.bind("<Return>", lambda _event: ncp.check_answer(target_l=target_l,one=one,two=two,three=three,four=four,button=entry_key, target_lt=target_lt, romaji=romaji, feedback_label=feedback_label,feedback=feedback, feedback_t=feedback_t, feedback_label_t=feedback_label_t,resize=resize))
    entry_key.place(relx=0, rely=0,relwidth=.001, relheight = .0001) 

def kana_t():
    global k_target_lt, k_romaji, k_entry_key, k_feedback_t, k_feedback_label_t
    ext.page = 6
    side_bar()
    
    
    k_feedback_t = ctk.CTkLabel(main_frame, fg_color=linen, image =ext.ghost_begin_image)
    k_feedback_t.place(relx = 0.57, rely = 0.24, relwidth = 0.75, relheight = 0.4, anchor = ctk.CENTER)
    k_feedback_t.active_pil_image = ext.ghost_begin_image._light_image

    k_feedback_ft = ctk.CTkFrame(main_frame, fg_color="white",corner_radius=0, bg_color="transparent" )
    k_feedback_ft.place(relx=.715, rely=.22, relwidth=.4, relheight=.17, anchor = ctk.CENTER)
    
    k_feedback_label_t = ctk.CTkLabel(k_feedback_ft, fg_color="white",corner_radius=0, bg_color="transparent", justify = "center", text = "Sigh, to submit your answer press the enter key.", wraplength=330,font=(coolfont,18), text_color=dgrey)
    k_feedback_label_t.place(relx=.5, rely=.5, relwidth=1, relheight=1, anchor = ctk.CENTER)
    
    k_target_lt = ctk.CTkLabel(main_frame, fg_color=cream, border_color=dgrey, border_width=5, corner_radius=5, font=(coolfont,55, "bold"),text_color=dbrown)
    k_target_lt.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER) 

    k_romaji = ctk.CTkEntry(main_frame, fg_color=cream, font=(coolfont, 40), placeholder_text="", justify = "center", border_width=5, border_color=dbrown, text_color=dgrey)      
    k_romaji.place(relx= 0.57, rely = .77, relwidth = .5, relheight = .2, anchor = ctk.CENTER)  

    k_entry_key = ctk.CTkButton(main_frame, fg_color="transparent", hover= None)  
    k_romaji.bind("<Return>", lambda _event: kap.check_answer(button = k_four, k_target_l=k_target_l, k_one=k_one, k_two=k_two, k_three=k_three, k_four=k_four,k_target_lt=k_target_lt, k_romaji=k_romaji, k_feedback_label=k_feedback_label,k_feedback=k_feedback,k_feedback_t=k_feedback_t,k_feedback_label_t=k_feedback_label_t, resize=resize))
    k_entry_key.place(relx=0, rely=0,relwidth=.001, relheight = .0001) 



start_up()

def side_label(page):
    global hira_l, kana_l, kanji_l, start_l
    if page == hira_mid or page == hira_m or page == hira_t:
        hira_l.configure(fg_color = brown)
    if page == kana_mid or page == kana_m or page == kana_t:
        kana_l.configure(fg_color = brown)
    if page == kanji_mid:
        kanji_l.configure(fg_color = brown)



def indicator(page):
    global ghost_pic
    cover.place(relx=0.5, rely=0.5, relwidth=1.005, relheight=1.005, anchor=ctk.CENTER)
    cover.lift()  
    cover.update()

    for child in main_frame.winfo_children():
        child.destroy()
        
    
    page()
    resize()
    cover.update_idletasks()
    cover.place_forget()

def resize_static(label, image, per, min_h, mode, min_w):
    
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
        new_h = int(new_w / aspect_ratio)

    
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

    resize_static(ghost_pic, ext.ghost_mid_image, per = 0.62, min_h=350, mode = "h", min_w=0)
    resize_static(chest_pic,ext.chest_mid_image, per=0.61, min_h=350, mode="h", min_w=0)
    resize_static(k_feedback,None, per = 0.425, min_h=0, mode="w", min_w=608)
    resize_static(k_feedback_t,None, per = 0.425, min_h=0, mode="w", min_w=608)
    resize_static(feedback,None, per = 0.425, min_h=0, mode="w", min_w=608)
    resize_static(feedback_t,None, per = 0.425, min_h=0, mode="w", min_w=608)

window.bind("<Configure>", resize)


window.mainloop()