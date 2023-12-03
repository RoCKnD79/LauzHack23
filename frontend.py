import tkinter
import tkinter.messagebox
import customtkinter

from PIL import Image
import os


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
#customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("LogiMood")
        self.geometry(f"{1100}x{580}")
        self.configure(bg_color="#000000", fg_color="#000000")

        self._fg_color ="#000000"
        self.iconbitmap("logimood_icon.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        current_path = os.path.dirname(os.path.realpath(__file__))
        self.logi_image = customtkinter.CTkImage(Image.open(current_path + "\images\logimood_icon.png"), size=(100, 100))

        self.select_image = customtkinter.CTkImage(Image.open(current_path + "\images\select_icon.png"))
        self.edit_image = customtkinter.CTkImage(Image.open(current_path + "\images\edit_icon.png"))
        self.mouse_image = customtkinter.CTkImage(Image.open(current_path + "\images\mouse_icon.png"))
        self.settings_image = customtkinter.CTkImage(Image.open(current_path + "\images\settings_icon.png"))


        self.auto_icon = customtkinter.CTkImage(Image.open(current_path + "\images\\brain_icon.png"))
        self.game_icon = customtkinter.CTkImage(Image.open(current_path + "\images\game_icon.png"))
        self.relax_icon = customtkinter.CTkImage(Image.open(current_path + "\images\\relax_icon.png"))
        self.sleep_icon = customtkinter.CTkImage(Image.open(current_path + "\images\sleep_icon.png"))
        self.work_icon = customtkinter.CTkImage(Image.open(current_path + "\images\work_icon.png"))

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=40, corner_radius=0, fg_color="#212225")
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=" ", image=self.logi_image) #, fg_color="#000000", bg_color="#000000",)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 20))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.mode_button_event, fg_color="#212225", image= self.select_image, text_color="#1388E5")
        self.sidebar_button_1.grid(row=1, column=0, padx=(30, 100), pady=(60,20))
        self.sidebar_button_1.configure(text="Mode   ", font=customtkinter.CTkFont(size=25, weight="bold"))

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.mode_button_event, fg_color="#212225", image= self.mouse_image)
        self.sidebar_button_2.grid(row=2, column=0, padx=(30, 100), pady=20)
        self.sidebar_button_2.configure(text="Devices", font=customtkinter.CTkFont(size=25, weight="bold", ))

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.mode_button_event, fg_color="#212225", image= self.edit_image)
        self.sidebar_button_3.grid(row=3, column=0, padx=(30, 100), pady=20)
        self.sidebar_button_3.configure(text="Custom", font=customtkinter.CTkFont(size=25, weight="bold", ))

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_input_dialog_event, fg_color="#212225", image=self.settings_image)
        self.sidebar_button_4.grid(row=4, column=0, padx=(30, 100), pady=20)
        self.sidebar_button_4.configure(text="Option  ", font=customtkinter.CTkFont(size=25, weight="bold"))


        # self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
        #                                                                command=self.change_appearance_mode_event)
        # self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        # self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        # self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, bg_color="#000000", fg_color="transparent", height=50)
        self.scrollable_frame.grid(row=0, column=1, padx=(0,10), sticky="nsew")
        #self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # create sidebar frame with widgets
        # self.main_frame = customtkinter.CTkFrame(self, width=40, corner_radius=0, fg_color="transparent")
        # self.main_frame.grid(row=0, column=1, rowspan=1, sticky="nsew",ipadx=70 ,ipady=0)
        # self.main_frame.grid_rowconfigure(4, weight=1)
        # self.logo_label = customtkinter.CTkLabel(self.main_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.main_button_1 = customtkinter.CTkButton(self.scrollable_frame, command=self.auto_button_event, width=150, height=150, image=self.auto_icon)
        self.main_button_1.grid(row=0, column=0, padx=(20, 10), pady=10)
        self.main_button_1.configure(text="Auto", font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.main_button_2 = customtkinter.CTkButton(self.scrollable_frame, command=self.game_button_event, width=150, height=150, image=self.game_icon,fg_color="#212225")
        self.main_button_2.grid(row=0, column=1, padx=10, pady=10)
        self.main_button_2.configure(text="Game", font=customtkinter.CTkFont(size=15, weight="bold"))

        self.main_button_3 = customtkinter.CTkButton(self.scrollable_frame, command=self.work_button_event, width=150, height=150, image=self.work_icon ,fg_color="#212225")
        self.main_button_3.grid(row=0, column=2, padx=10, pady=10)
        self.main_button_3.configure(text="Work", font=customtkinter.CTkFont(size=15, weight="bold"))

        self.main_button_4 = customtkinter.CTkButton(self.scrollable_frame, command=self.sleep_button_event, width=150, height=150, image=self.sleep_icon ,fg_color="#212225")
        self.main_button_4.grid(row=1, column=0, padx=(20, 10), pady=10)
        self.main_button_4.configure(text="Sleep", font=customtkinter.CTkFont(size=15, weight="bold"))

        self.main_button_5 = customtkinter.CTkButton(self.scrollable_frame, command=self.relax_button_event, width=150, height=150, image=self.relax_icon, fg_color="#212225")
        self.main_button_5.grid(row=1, column=1, padx=10, pady=10)
        self.main_button_5.configure(text="Relax", font=customtkinter.CTkFont(size=15, weight="bold"))

        self.main_button_7 = customtkinter.CTkButton(self.scrollable_frame, command=self.new_button_event, width=150, height=150,fg_color="#000000") #, hover_color="#212225")
        self.main_button_7.grid(row=1, column=2, padx=10, pady=10)
        self.main_button_7.configure(text="+", font=customtkinter.CTkFont(size=120, weight="bold"))
        
        self.main_button_8 = customtkinter.CTkButton(self.scrollable_frame, command=self.new_button_event, width=150, height=150,fg_color="#000000") #, hover_color="#212225")
        self.main_button_8.grid(row=2, column=0, padx=10, pady=10)
        self.main_button_8.configure(text=" ", font=customtkinter.CTkFont(size=120, weight="bold"), state="disable")
        

        #create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="#000000", bg_color="transparent")
        self.slider_progressbar_frame.grid(row=0, column=2, sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

        self.mood_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Mood", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.mood_label.grid(row=0, column=0, padx=(0,0), pady=(20,20))

        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="horizontal", width=130, height=12, progress_color="#4354be")
        self.progressbar_1.grid(row=1, column=1, padx=(0, 20))
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="horizontal", width=130, height=12, progress_color="#0995e6")
        self.progressbar_2.grid(row=2, column=1, padx=(0, 20))
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="horizontal", width=130, height=12, progress_color="#33cc33")
        self.progressbar_3.grid(row=3, column=1, padx=(0, 20))
        self.progressbar_4 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="horizontal", width=130, height=12, progress_color="#d6cb22")
        self.progressbar_4.grid(row=4, column=1, padx=(0, 20))
        self.progressbar_5 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="horizontal", width=130, height=12, progress_color="#ff0000")
        self.progressbar_5.grid(row=5, column=1, pady = (0,50), padx=(0, 20))

        self.happy_label    = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Sleepy     ", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.happy_label.grid(row=1, column=0,)
        self.angry_labe2    = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Calmness", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.angry_labe2.grid(row=2, column=0,)
        self.stressed_labe3 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Happy     ", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.stressed_labe3.grid(row=3, column=0,)
        self.sleepy_labe4   = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Neutral   ", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sleepy_labe4.grid(row=4, column=0,)
        self.sleepy_labe5   = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Angry     ", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sleepy_labe5.grid(row=5, column=0,pady = (0,20))

        # self.statistic_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.statistic_frame.grid(row=1, column=6, sticky="nsew")

        self.taping_speed_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Typing Speed", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.taping_speed_label.grid(row=6, column=0, padx=0, pady=(0, 0))
        self.taping_speed_value = customtkinter.CTkLabel(self.slider_progressbar_frame, text="0", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.taping_speed_value.grid(row=6, column=1, padx=0, pady=(0, 0))

        self.average_error_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Average Error", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.average_error_label.grid(row=7, column=0, padx=0, pady=(0, 0))
        self.average_error_value = customtkinter.CTkLabel(self.slider_progressbar_frame, text="0", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.average_error_value.grid(row=7, column=1, padx=0, pady=(0, 0))

        self.auto_button_event()



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def mode_button_event(self):
        #self.main_frame.configure()
        pass

    def statistic_button_event(self):
        print("sidebar_button click")



    def auto_button_event(self):
        self.main_button_1.configure(fg_color="#1388E5")
        self.main_button_2.configure(fg_color="#212225")
        self.main_button_3.configure(fg_color="#212225")
        self.main_button_4.configure(fg_color="#212225")
        self.main_button_5.configure(fg_color="#212225")
        self.display_auto_mode()


    def game_button_event(self):
        self.main_button_1.configure(fg_color="#212225")
        self.main_button_2.configure(fg_color="#1388E5")
        self.main_button_3.configure(fg_color="#212225")
        self.main_button_4.configure(fg_color="#212225")
        self.main_button_5.configure(fg_color="#212225")
        self.display_game_mode()


    def work_button_event(self):
        self.main_button_1.configure(fg_color="#212225")
        self.main_button_2.configure(fg_color="#212225")
        self.main_button_3.configure(fg_color="#1388E5")
        self.main_button_4.configure(fg_color="#212225")
        self.main_button_5.configure(fg_color="#212225")
        self.display_work_mode()


    def sleep_button_event(self):
        self.main_button_1.configure(fg_color="#212225")
        self.main_button_2.configure(fg_color="#212225")
        self.main_button_3.configure(fg_color="#212225")
        self.main_button_4.configure(fg_color="#1388E5")
        self.main_button_5.configure(fg_color="#212225")
        self.display_sleep_mode()


    def relax_button_event(self):
        self.main_button_1.configure(fg_color="#212225")
        self.main_button_2.configure(fg_color="#212225")
        self.main_button_3.configure(fg_color="#212225")
        self.main_button_4.configure(fg_color="#212225")
        self.main_button_5.configure(fg_color="#1388E5")
        self.display_relax_mode()


    def new_button_event(self):
        # self.main_button_1.configure(fg_color="#212225")
        # self.main_button_2.configure(fg_color="#212225")
        # self.main_button_3.configure(fg_color="#212225")
        # self.main_button_4.configure(fg_color="#212225")
        # self.main_button_5.configure(fg_color="#212225")
        # self.main_button_6.configure(fg_color="#1388E5")
        pass

    def open_input_dialog_event(self):
        self.dialog = customtkinter.CTkInputDialog(text="Keyboard preferences", title="Option")
        #self.dialog.configure()
        
        self.age_label = customtkinter.CTkLabel(self.dialog, text="Age", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.age_label.grid(row=0, column=0, padx=0, pady=(0, 0))
        # self.average_error_value2 = customtkinter.CTkLabel(self.dialog, text="0", font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.average_error_value2.grid(row=7, column=1, padx=0, pady=(0, 0))
        #print("CTkInputDialog:", self.dialog.get_input())

    def display_auto_mode(self):
        self.main_auto_frame = customtkinter.CTkFrame(self, width=40, corner_radius=0, fg_color="#000000")
        self.main_auto_frame.grid(row=1, column=1, rowspan=3, sticky="nsew",ipadx=70 ,ipady=0)
        self.auto_textbox = customtkinter.CTkTextbox(self.main_auto_frame,width=500, height=70, font=customtkinter.CTkFont(size=15, weight="bold"), fg_color="#000000", bg_color="#000000")
        self.auto_textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 40), sticky="nsew")
        self.auto_textbox.insert("end", "Determines your mood continuously and adapts your embience optimally for the best possible user experience !")
        switch = customtkinter.CTkSwitch(master=self.main_auto_frame, text=f"Music Recommendation" ,font=customtkinter.CTkFont(size=15, weight="bold"),)
        switch.grid(row=1, column=0, padx=10, pady=(0, 20))
        switch = customtkinter.CTkSwitch(master=self.main_auto_frame, text=f"Play Music                    ", font=customtkinter.CTkFont(size=15, weight="bold"),)
        switch.grid(row=2, column=0, padx=10, pady=(0, 20))


    def display_game_mode(self):
        self.main_game_frame = customtkinter.CTkFrame(self, width=40, corner_radius=0, fg_color="#000000")
        self.main_game_frame.grid(row=1, column=1, rowspan=3, sticky="nsew",ipadx=70 ,ipady=0)
        self.game_textbox = customtkinter.CTkTextbox(self.main_auto_frame,width=500, height=70, font=customtkinter.CTkFont(size=15, weight="bold"), fg_color="#000000", bg_color="#000000")
        self.game_textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 40), sticky="nsew")
        self.game_textbox.insert("end", "")
        self.game_label = customtkinter.CTkLabel(self.main_game_frame, text="Current game :", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.game_label.grid(row=1, column=0, padx=30, pady=(30,20))
        self.game_label = customtkinter.CTkLabel(self.main_game_frame, text="Launch a game to see more option !", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.game_label.grid(row=2, column=0, padx=30, pady=(0,20))



    def display_work_mode(self):
        self.main_work_frame = customtkinter.CTkFrame(self, width=40, corner_radius=0, fg_color="green")
        self.main_work_frame.grid(row=1, column=1, rowspan=3, sticky="nsew",ipadx=70 ,ipady=0)

    def display_sleep_mode(self):
        self.main_sleep_frame = customtkinter.CTkFrame(self, width=40, corner_radius=0, fg_color="yellow")
        self.main_sleep_frame.grid(row=1, column=1, rowspan=3, sticky="nsew",ipadx=70 ,ipady=0)

    def display_relax_mode(self):
        self.main_relax_frame = customtkinter.CTkFrame(self, width=40, corner_radius=0, fg_color="pink")
        self.main_relax_frame.grid(row=1, column=1, rowspan=3, sticky="nsew",ipadx=70 ,ipady=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
