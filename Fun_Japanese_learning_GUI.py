import Nihongo_Charater_Practice as ncp
import Kanji_Practice as kp
import Katakana_Practice as kap
import customtkinter as ctk
import Extra as ext


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



ctk.FontManager.load_font("Matcha Mint.ttf")
coolfont = "Matcha Mint"

main_frame = ctk.CTkFrame(window,fg_color=linen, border_color=brown, border_width=15)
main_frame.place(relx = 0.5, rely =0.5, relwidth =1.005, relheight = 1.005, anchor = ctk.CENTER)



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

    invert = ctk.CTkButton(side, fg_color=pink, border_color=brown,corner_radius=5, font=(coolfont,15), text="Invert", bg_color="transparent", hover_color=dpink,command=lambda: ncp.invert_but(target_l=target_l,one=one,two=two,three=three,four=four,invert=invert))
    invert.place(relx= 0.5, rely=.91, relwidth = .8, relheight= .07,anchor = ctk.CENTER )
   







def hira_mid():  
   global target_l,one,two,three,four
   side_bar()


   chest_mid_image = ctk.CTkImage(size = (202.5,540), light_image=ext.chest_mid, dark_image=ext.chest_mid )

   chest_pic = ctk.CTkLabel(main_frame, fg_color=linen, image=chest_mid_image, text = "")
   chest_pic.place(relx = 0.295, rely = .5,relwidth = 0.25, relheight = 0.9, anchor= ctk.CENTER)
   chest_text = ctk.CTkLabel(main_frame, fg_color=brown)
   chest_text.place(relx = .7, rely = .255 , relwidth = .5, relheight = .4, anchor = ctk.CENTER)

   hira_mcq = ctk.CTkButton(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=10, 
                            text="Multiple\n Choice", text_color=cream, hover_color=dbrown, font=(coolfont, 30), command=lambda: (indicator(page = hira_m), ncp.load_new_deck(target_l,one,two,three,four)))
   hira_mcq.place(relx = 0.6, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
   hira_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Easier,\n reccomended \nfor begginers", text_color=dgrey, font=(coolfont,18, "italic"))
   hira_mcq_label.place(relx = 0.765, rely = .52, relwidth = .2, relheight = .17)

   hira_text = ctk.CTkButton(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=10, 
                               text="Text\n Answers", text_color=cream, hover_color=dbrown, font=(coolfont, 30))
   hira_text.place(relx = 0.6, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
   hira_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Harder,\n requires \nsome \nmastery", text_color=dgrey, font=(coolfont,18, "italic"))
   hira_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)

def kana_mid():
    side_bar()
    ghost_pic = ctk.CTkLabel(main_frame, fg_color=cream)
    ghost_pic.place(relx = 0.295, rely = .5,relwidth = 0.25, relheight = 0.9, anchor= ctk.CENTER)
    ghost_text = ctk.CTkLabel(main_frame, fg_color=cream)
    ghost_text.place(relx = .7, rely = .255 , relwidth = .5, relheight = .4, anchor = ctk.CENTER)

    kana_mcq = ctk.CTkButton(main_frame, fg_color=cream, border_color=brown, border_width=5, corner_radius=10, 
                            text="Multiple\n Choice", text_color=dgrey, hover_color=linen, font=(coolfont, 30))
    kana_mcq.place(relx = 0.6, rely = .6, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kana_mcq_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Easier. So I\nreccomend for \nbegginers", text_color=dgrey, font=(coolfont,17, "italic"))
    kana_mcq_label.place(relx = 0.765, rely = .52, relwidth = .2, relheight = .17)
    
    kana_text = ctk.CTkButton(main_frame, fg_color=cream, border_color=dgrey, border_width=5, corner_radius=10, 
                                   text="Text\n Answers", text_color=brown, hover_color=linen, font=(coolfont, 30))
    kana_text.place(relx = 0.6, rely = .84, relwidth = .3, relheight = .2, anchor = ctk.CENTER )
    kana_text_label = ctk.CTkLabel(main_frame,fg_color=linen, text= "Harder.\n So requires \nsome \nmastery", text_color=dgrey, font=(coolfont,18, "italic"))
    kana_text_label.place(relx = 0.76, rely = .75, relwidth = .22, relheight = .17)

def kanji_mid():
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
    global target_l,one,two,three,four
    side_bar()
    ext.page = 1
    feedback = ctk.CTkLabel(main_frame, fg_color=brown)
    feedback.place(relx = 0.57, rely = 0.24, relwidth = 0.75, relheight = 0.4, anchor = ctk.CENTER)

    target_l = ctk.CTkLabel(main_frame, fg_color=brown, border_color=dbrown, border_width=5, corner_radius=5, font=(coolfont,55, "bold"))
    target_l.place(relx= 0.57, rely= 0.5, relwidth = 0.8, relheight = 0.2, anchor = ctk.CENTER )

    one = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = one, target_l=target_l, one=one, two=two, three=three, four=four))
    one.place(relx = 0.37, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    two = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = two, target_l=target_l, one=one, two=two, three=three, four=four))
    two.place(relx = 0.77, rely = .7, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    three = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = three, target_l=target_l, one=one, two=two, three=three, four=four))
    three.place(relx = 0.37, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
    four = ctk.CTkButton(main_frame, fg_color=brown, corner_radius=5, border_color=dbrown, font=(coolfont,40), border_width=5, hover_color=dbrown, command=lambda: ncp.check_answer(button = four, target_l=target_l, one=one, two=two, three=three, four=four))
    four.place(relx = 0.77, rely = .88, relwidth = .37, relheight = 0.17, anchor = ctk.CENTER)
   


    

start_up()

def side_label(page):
    global hira_l, kana_l, kanji_l, start_l
    if page == hira_mid:
        hira_l.configure(fg_color = brown)
    if page == kana_mid:
        kana_l.configure(fg_color = brown)
    if page == kanji_mid:
        kanji_l.configure(fg_color = brown)



def indicator(page):

    for child in main_frame.winfo_children():
        child.destroy()

    page()


window.mainloop()