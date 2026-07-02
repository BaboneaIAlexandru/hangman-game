import customtkinter as ctk
import sys
from os import path
from PIL import Image
from engine import choose_word

def resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        return path.join(sys._MEIPASS,relative_path)
    return path.join(path.abspath("."),relative_path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x600")
        self.title("Hangman Game")
        self.resizable(False,False)

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme(resource_path("assets/themes/lavender.json"))

        self.difficulties=["Easy","Medium","Hard"]
        self.wrong_answers=0

        self.word=""
        self.guessed_letters=[]

        self.key_buttons = {}
        self.keys=[
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"]
        ]

        self.setup_ui()
        self.start_new_game()

        self.bind("<Key>",self.physical_key_pressed)
        

    def setup_ui(self):

        self.frame_options=ctk.CTkFrame(self, fg_color="transparent",width=400,height=35)
        self.frame_options.pack(fill="both")

        self.frame_sprites=ctk.CTkFrame(self,fg_color="transparent",width=400,height=300)
        self.frame_sprites.pack(fill="both")

        self.frame_word=ctk.CTkFrame(self,fg_color="transparent",width=400,height=55)
        self.frame_word.pack(fill="both")

        self.frame_keys=ctk.CTkFrame(self,fg_color="transparent",width=400,height=210)
        self.frame_keys.pack(fill="both",expand=True)

        self.optionmenu_difficulty=ctk.CTkOptionMenu(self.frame_options,width=85,height=25,values=self.difficulties,command=lambda x:self.start_new_game())
        self.optionmenu_difficulty.pack(side="left",pady=5,padx=5)

        self.button_new_game=ctk.CTkButton(self.frame_options,width=85,height=25,text="New Game",command=self.start_new_game)
        self.button_new_game.pack(side="right",pady=5,padx=5)

        self.label_sprites=ctk.CTkLabel(self.frame_sprites,text="",
            image=ctk.CTkImage(
            light_image=Image.open(resource_path(f"assets/lightmode_sprites/{self.wrong_answers}.png")),
            dark_image=Image.open(resource_path(f"assets/darkmode_sprites/{self.wrong_answers}.png")),
            size=(300,300)),
            width=400,height=300)
        self.label_sprites.pack()

        self.label_word_display=ctk.CTkLabel(self.frame_word,text="",font=("Arial",28,"bold"),text_color=("#000000","#FFFFFF"))
        self.label_word_display.pack(expand=True)

        for i,row in enumerate(self.keys):
            frame_row=ctk.CTkFrame(self.frame_keys,fg_color="transparent")
            
            if i==0:
                frame_row.pack(pady=(50,6))
            else:
                frame_row.pack(pady=6)

            for key in row:
                btn=ctk.CTkButton(
                    frame_row,
                    text=key,
                    width=34,           
                    height=42,          
                    font=("Arial",14,"bold"), 
                    corner_radius=8,    
                    command=lambda l=key:self.pressed_key(l)
                )
                btn.pack(side="left",padx=2.5) 
                
                self.key_buttons[key]=btn
        
    def update_sprite(self):
        new_sprite=ctk.CTkImage(
            light_image=Image.open(resource_path(f"assets/lightmode_sprites/{self.wrong_answers}.png")),
            dark_image=Image.open(resource_path(f"assets/darkmode_sprites/{self.wrong_answers}.png")),
            size=(300,300)
        )
        self.label_sprites.configure(image=new_sprite)

    def update_word_display(self):
        displayed_word=""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word+=letter+" "
            else:
                displayed_word+="_ "
        self.label_word_display.configure(text=displayed_word.strip())

    def start_new_game(self):
        self.wrong_answers=0
        self.guessed_letters=[]
        self.update_sprite()

        self.label_word_display.configure(text_color=("#000000", "#FFFFFF"))

        for btn in self.key_buttons.values():
            btn.configure(state="normal")
        
        difficulty=self.optionmenu_difficulty.get()

        self.word=choose_word(difficulty)

        self.update_word_display()

    def pressed_key(self,letter):
        if self.key_buttons[letter].cget("state")=="disabled":
            return

        self.key_buttons[letter].configure(state="disabled")

        if letter in self.word:
            self.guessed_letters.append(letter)
            self.update_word_display()

            win=True
            for l in self.word:
                if l not in self.guessed_letters:
                    win=False
                    break
            
            if win:
                self.label_word_display.configure(text_color="#00ff15")
                self.disable_keys()

        else:
            self.wrong_answers+=1
            self.update_sprite()

            if self.wrong_answers==6:
                self.label_word_display.configure(text=" ".join(self.word),text_color="#FF0000")
                self.disable_keys()
            
    def disable_keys(self):
        for btn in self.key_buttons.values():
            btn.configure(state="disabled")
    
    def physical_key_pressed(self,event):
        key=event.char.upper()
        if key in self.key_buttons:
            self.pressed_key(key)

app=App()
if __name__=="__main__":
    app.mainloop()
