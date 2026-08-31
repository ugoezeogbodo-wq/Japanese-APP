from PIL import Image
import customtkinter as ctk

page = ""

right = "#3A5F2D"
wrong = "#CC3F32"
dright ="#1F3C15"
dwrong = "#762720"
cream = "#F6FFFA"
linen = "#E6E6DB"
grey = "#A0BBB2"
pink = "#DA7D91"
brown = "#8b4c41"
dgrey = "#507065"
dbrown = "#69362d"
dpink = "#D05A73"

chest_mid = Image.open("chest_mid.png")
chest_mid_image = ctk.CTkImage(size = (202.5,540), light_image=chest_mid, dark_image=chest_mid )

chest_begin = Image.open("chest_begin.png")
chest_begin_image = ctk.CTkImage(size=(608,240),light_image=chest_begin,dark_image=chest_begin )

chest_wrong = Image.open("chest_wrong.png")
chest_wrong_image = ctk.CTkImage(size=(608,240),light_image=chest_wrong,dark_image=chest_wrong )

chest_right = Image.open("chest_right.png")
chest_right_image = ctk.CTkImage(size=(608,240),light_image=chest_right,dark_image=chest_right )

chest_10 = Image.open("chest_10.png")
chest_10_image = ctk.CTkImage(size=(608,240),light_image=chest_10,dark_image=chest_10 )

chest_5 = Image.open("chest_5.png")
chest_5_image = ctk.CTkImage(size=(608,240),light_image=chest_5,dark_image=chest_5 )

ghost_mid = Image.open("ghost_mid.png")
ghost_mid_image = ctk.CTkImage(size = (202.5,540), light_image=ghost_mid, dark_image=ghost_mid )

ghost_begin = Image.open("ghost_begin.png")
ghost_begin_image = ctk.CTkImage(size=(608,240),light_image=ghost_begin,dark_image=ghost_begin )

ghost_wrong = Image.open("ghost_wrong.png")
ghost_wrong_image = ctk.CTkImage(size=(608,240),light_image=ghost_wrong,dark_image=ghost_wrong )

ghost_right = Image.open("ghost_right.png")
ghost_right_image = ctk.CTkImage(size=(608,240),light_image=ghost_right,dark_image=ghost_right )

ghost_10 = Image.open("ghost_10.png")
ghost_10_image = ctk.CTkImage(size=(608,240),light_image=ghost_10,dark_image=ghost_10 )

ghost_5 = Image.open("ghost_5.png")
ghost_5_image = ctk.CTkImage(size=(608,240),light_image=ghost_5,dark_image=ghost_5 )