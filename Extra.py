from PIL import Image
import customtkinter as ctk

chest_mid = Image.open("chest_mid.jpe")
chest_mid_image = ctk.CTkImage(size = (202.5,540), light_image=chest_mid, dark_image=chest_mid )
