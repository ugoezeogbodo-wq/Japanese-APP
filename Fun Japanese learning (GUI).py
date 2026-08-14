import Nihongo_Charater_Practice as ncp
import Kanji_Practice as kp
import Katakana_Practice as kap
import customtkinter as ctk


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

ctk.FontManager.load_font("Matcha Mint.ttf")
coolfont = "Matcha Mint"

main_frame = ctk.CTkFrame(window,fg_color=linen, border_color=brown, border_width=15)
main_frame.place(relx = 0.5, rely =0.5, relwidth =1.005, relheight = 1.005, anchor = ctk.CENTER)



def start_up():


    intro_label = ctk.CTkLabel(main_frame, fg_color = cream, text="", corner_radius=5)
    intro_label.place(relx = 0.5, rely = 0.30, relwidth =0.90, relheight = .45, anchor=ctk.CENTER)

    hira_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Hiragana", text_color= cream, font = (coolfont, 43), hover_color=dgrey, command = lambda: indicator(page=hira_mid))
    hira_button.place(relx = .27, rely=.65, relwidth = .45, relheight = .15, anchor = ctk.CENTER)

    kata_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Katakana", text_color= cream, font = (coolfont, 43), hover_color=dgrey)
    kata_button.place(relx = .735, rely=.65, relwidth = .45, relheight = .15, anchor = ctk.CENTER)

    kanji_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Kanji", text_color= cream, font = (coolfont, 43), hover_color=dgrey)
    kanji_button.place(relx = .27, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)

    info_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Information", text_color= cream, font = (coolfont, 42), hover_color=dgrey)
    info_button.place(relx = .735, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)


def side_bar():
    side  = ctk.CTkFrame(main_frame, fg_color=brown, border_width=0, corner_radius=0)
    side.place(relx=0,rely=0.5,relwidth=.15,relheight = 1.05, anchor = "w")

    hira_go = ctk.CTkButton(side, fg_color=brown, text = "Hiragana", font = (coolfont, 17), hover_color=dbrown, text_color=cream)
    hira_go.place(relx = .13, rely = .43,relwidth = .85, relheight = .075)

    hira_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    hira_l.place(relx = .07 , rely = 0.43 , relwidth = .05, relheight = .075)

    kana_go = ctk.CTkButton(side, fg_color=brown, text = "Katakana", font = (coolfont, 17), hover_color=dbrown, text_color=cream)
    kana_go.place(relx = .13, rely = .23,relwidth = .85, relheight = .075)

    kana_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    kana_l.place(relx = .07 , rely = 0.23 , relwidth = .05, relheight = .075)

    kanji_go = ctk.CTkButton(side, fg_color=brown, text = "Kanji", font = (coolfont, 20,), hover_color=dbrown, text_color=cream)
    kanji_go.place(relx = .13, rely = .33,relwidth = .85, relheight = .075)

    kanji_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    kanji_l.place(relx = .07 , rely = 0.33 , relwidth = .05, relheight = .075)

    start_go = ctk.CTkButton(side, fg_color=brown, text = "Start Page", font = (coolfont, 15), hover_color=dbrown, text_color=cream, command = lambda: indicator(page=start_up))
    start_go.place(relx = .13, rely = .13,relwidth = .85, relheight = .075)

    start_l = ctk.CTkLabel(side, fg_color = pink, text = "", corner_radius=2)
    start_l.place(relx = .07 , rely = 0.13 , relwidth = .05, relheight = .075)

    menu = ctk.CTkLabel(side, fg_color = pink, text = "Menu:", font = (coolfont,25), corner_radius=5)
    menu.place(relx = .5 , rely = 0.075 , relwidth = .88, relheight = .08, anchor = ctk.CENTER)







def hira_mid():
   side_bar()

start_up()

def indicator(page):
    for child in main_frame.winfo_children():
        child.destroy()

    page()

window.mainloop()