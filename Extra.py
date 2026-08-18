from PIL import Image
import customtkinter as ctk

page = ""

right = "#3A5F2D"
wrong = "#CC3F32"
dright ="#1F3C15"
dwrong = "#762720"
ream = "#F6FFFA"
linen = "#E6E6DB"
grey = "#A0BBB2"
pink = "#DA7D91"
brown = "#8b4c41"
dgrey = "#507065"
dbrown = "#69362d"
dpink = "#D05A73"

chest_mid = Image.open("chest_mid.jpe")
chest_mid_image = ctk.CTkImage(size = (202.5,540), light_image=chest_mid, dark_image=chest_mid )
