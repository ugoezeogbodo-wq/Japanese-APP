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

ctk.FontManager.load_font("Matcha Mint.ttf")
coolfont = "Matcha Mint"

main_frame = ctk.CTkFrame(window,fg_color=linen, border_color=brown, border_width=15)
main_frame.place(relx = 0.5, rely =0.5, relwidth =1, relheight = 1, anchor = ctk.CENTER)

def start_up():

    intro_label = ctk.CTkLabel(main_frame, fg_color = cream, text="", corner_radius=5)
    intro_label.place(relx = 0.5, rely = 0.30, relwidth =0.90, relheight = .45, anchor=ctk.CENTER)

    hira_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Hiragana", text_color= cream, font = (coolfont, 43), hover_color=dgrey)
    hira_button.place(relx = .27, rely=.65, relwidth = .45, relheight = .15, anchor = ctk.CENTER)

    kata_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Katakana", text_color= cream, font = (coolfont, 43), hover_color=dgrey)
    kata_button.place(relx = .735, rely=.65, relwidth = .45, relheight = .15, anchor = ctk.CENTER)

    kanji_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Kanji", text_color= cream, font = (coolfont, 43), hover_color=dgrey)
    kanji_button.place(relx = .27, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)

    info_button = ctk.CTkButton(main_frame,fg_color=grey, text= "Information", text_color= cream, font = (coolfont, 42), hover_color=dgrey)
    info_button.place(relx = .735, rely=.83, relwidth = .45, relheight = .15, anchor = ctk.CENTER)

start_up()

window.mainloop()