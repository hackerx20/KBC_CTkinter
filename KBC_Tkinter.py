# <<<---------------------- NICE IDEA BY CAN BE VALID ONLY FOR A SHELL ---------------->>>

# Ques_list=[]
# def Ques_list_Input():
#     global Ques_list
#     for i in range(10):
#         Ques_list.append(input("Enter question to be added:"))
# Options_list=[]
# def Options_list_Input():
#     global Options_list
#     for i in range(10):
#         Options_list.append(list(input("Enter four options of the above question seperated by space:")))

# CorrectAnswer_list=[]
# def Ques_list_Input():
#     global CorrectAnswer_list_list
#     for i in range(10):
#         CorrectAnswer_list.append(input("Correct answer to the above question:"))

# <<<---------------------- MAIN WAY TO MAKE A GUI KBC PLATFORM ------------------------>>>

#importing Questions , Options , and Correct Answers Lists
from Questions import questions
from Options import options
from CorrectAnswer import correct_answers


#importing the required modules for the GUI KBC PLATFORM
import random
import customtkinter as ctk #to use this customtkinter module  use the command   <<<-------$source myenv/bin/activate----->>>>
# import tkinter.font as tkFont
# import os
#Creating a root window
root= ctk.CTk()


# font_path = os.path.join(os.getcwd(), "KBC_CTkinter/Happy_Monkey/HappyMonkey-Regular.ttf")
# custom_font= tkFont.Font(family="HappyMonkey-Regular", size=20)
# custom_font=ctk.CTkFont(family="HappyMonkey-Regular", size=20)

# custom_font_path = "YourFont.ttf"  # Ensure the path is correct
# # Set the default font


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


root.geometry("800x400")
root.title("Kaun_Banega_Crorepati_(KBC)...") #TITLE OF THE ROOT WINDOW
root.config(bg="#000066")  #background color to the calculator


#Creating Global variables for use in different functions
current_question_index = 0
score=0
time_remaining = 15  # Set the time limit for each question (in seconds)
timer_label = None  # A label to show the countdown
timer_running = False

# <<< ------------------------- SET ----------------------------------------- >>>

#Creating a empty set and the entering 10 different numbers in random order for the KBC questions
question_index_list=[]
while (len(question_index_list)<10):
    question_number = random.randrange(0,100) 
    if question_number not in question_index_list:
        question_index_list.append(question_number)

# <<<------------------------------------------------------------------------- >>>

# <<<----------------- Creating button width for different buttons ---------------------->>>
button_width=0.4
button_height=0.1


label_width=0.9
label_height=0.1

button_next_height=0.1
button_next_width=0.9

# <<<------------------------------------------------------------------------------------>>>

# Add padding and hover effect for buttons
# def on_enter(e):
#     e.widget['background'] = '#4C4C4C'

# def on_leave(e):
#     e.widget['background'] = e.widget.default_bg



# Timer countdown function
def start_timer():
    global time_remaining, timer_running
    if time_remaining > 0:
        time_remaining -= 1
        timer_label.configure(text=f"Time left: {time_remaining}")
        root.after(1000, start_timer)  # Call this function again after 1 second
    else:
        timer_running = False
        Go_Onto_Next_Question()  # Time's up, move to the next question

# <<< --------------------------- WE CAN USE THIS METHOD TOO ---------------------- >>> 
#Function to create buttons
# def create_button(text, command, row, column, bg, fg="white", columnspan=1):
#     button = ctk.CTkButton(root, text=text, command=command, width=5, font=("Helvetica", 16), bg=bg, fg=fg, activebackground="#4C4C4C", bd=0, highlightthickness=0)
#     button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)
#     button.default_bg = bg  # Store original color
#     button.bind("<Enter>", on_enter)  # Hover effect
#     button.bind("<Leave>", on_leave)
#     return button
# label = ctk.Label(root, text="Kaun Banega Crorepati?", font=("Arial", 20), fg="red").grid(row=0, columnspan=2)

# options_list = []

current_widgets=[] # List

def Display_questions( **dict):
    global current_widgets, button_width, button_height, label__width, label_height
    for widget in current_widgets:
        widget.destroy()
    current_widgets.clear()

    # global options_list
    # options_list = options_as_list
    # for i in range(4):
        # bg = "white" if i!= correct_answers_as_string.index(options_as_list[i]) else "lightgray"
        # button = create_button(options_as_list[i], lambda option=options_as_list[i], correct_answer=correct_answers_as_string: check_answer(option, correct_answer), row=i+3, column=1, bg=bg)
        # options.append(button)
    # create_button(list[1], command= lambda: check_for_correct_answer(list[1],string_2) , row=2, column=1, bg="#333333")
    # create_button(list[2], command= lambda: check_for_correct_answer(list[2],string_2) , row=2, column=2, bg="#333333")
    # create_button(list[3], command= lambda: check_for_correct_answer(list[3],string_2) , row=3, column=1, bg="#333333")
    # create_button(list[4], command= lambda: check_for_correct_answer(list[4],string_2) , row=3, column=2, bg="#333333")
    # return question_label, options
    question_label = ctk.CTkLabel(root, text=dict["string_1"], text_color="White",corner_radius=20,font=("Arial", 24))
    btn_1= ctk.CTkButton(root,text=dict["my_list"][0], border_width=5, border_color="grey", corner_radius=50,command= lambda: combined_function(dict["my_list"][0],dict["string_2"],btn_1),font=("Arial", 20))
    btn_2= ctk.CTkButton(root,text=dict["my_list"][1], border_width=5, border_color="grey", corner_radius=50,command= lambda: combined_function(dict["my_list"][1],dict["string_2"],btn_2),font=("Arial", 20))
    btn_3= ctk.CTkButton(root,text=dict["my_list"][2], border_width=5, border_color="grey", corner_radius=50,command= lambda: combined_function(dict["my_list"][2],dict["string_2"],btn_3),font=("Arial", 20))
    btn_4= ctk.CTkButton(root,text=dict["my_list"][3], border_width=5, border_color="grey", corner_radius=50,command= lambda: combined_function(dict["my_list"][3],dict["string_2"],btn_4),font=("Arial", 20))


    question_label.place(relx=0.05, rely=0.2, relwidth=label_width, relheight=label_height)
    btn_1.place(relx=0.05, rely=0.35, relwidth=button_width, relheight=button_height)
    btn_2.place(relx=0.55, rely=0.35, relwidth=button_width, relheight=button_height)
    btn_3.place(relx=0.05, rely=0.5, relwidth=button_width, relheight=button_height)
    btn_4.place(relx=0.55, rely=0.5, relwidth=button_width, relheight=button_height)


    btn_1.configure(hover_color="#FFCC00")
    btn_2.configure(hover_color="#FFCC00")
    btn_3.configure(hover_color="#FFCC00")
    btn_4.configure(hover_color="#FFCC00")
    
    global timer_label
    timer_label = ctk.CTkLabel(root, text=f"Time left: {time_remaining}", font=("Arial", 20), text_color="red")
    timer_label.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.1)

    global score
    score_label = ctk.CTkLabel(root, text=f"Your Score: {score}",fg_color="#000066", font=("Arial", 24))
    score_label.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.1)
    current_widgets.extend([btn_1,btn_2,btn_3,btn_4, question_label, timer_label,score_label])


def check_for_correct_answer( string_1, string_2):
    global score
    if string_1 == string_2:
        score+=1



def Change_color(button):
    button.configure( fg_color="green")


# <<<----------------- We can animate the button too after the press ---------------->>>
# def animate_button(button):
#     button.place(relwidth=0.43, relheight=0.17)



def combined_function(string_1, string_2, button):
    check_for_correct_answer(string_1,string_2)
    # animate_button(button)
    Change_color(button)



def Go_Onto_Next_Question():
    global current_question_index, question_index_list
    if current_question_index<10:
        Display_questions(string_1=questions[question_index_list[current_question_index]], my_list =options[question_index_list[current_question_index]], string_2=correct_answers[question_index_list[current_question_index]])
        current_question_index=current_question_index + 1
        progress_bar.set(current_question_index / 10)
    else:
        display_score_window()


def display_score_window():
    global current_widgets, score
    for widget in current_widgets:
        widget.destroy()
    current_widgets.clear()
    score_label = ctk.CTkLabel(root, text=f"Your Score: {score}",fg_color="#000066", font=("Arial", 24))
    score_label.place(relx=0.05, rely=0.4, relwidth=label_width, relheight=0.2)
    btn_next.configure(command=root.destroy)

# <<<-----------------SET BACKGROUND IMAGE----------------------->>>
# bg_image = ctk.CTkLabel(root, text="", image=ctk.CTkImage(Image.open("/home/shivansh-tiwari/coding/KBC_CTkinter/BGimage/bg.jpg")))
# bg_image.place(relx=0,rely=0,relwidth=1, relheight=1)

#<<<------------------------------------------------------------->>>


# <<<-----------------ADDING A PROGRESS BAR----------------------->>>
progress_bar = ctk.CTkProgressBar(root)
progress_bar.place(relx=0.05, rely=0.92, relwidth=0.9, relheight=0.05)
#<<<--------------------------------------------------------------->>>

label=ctk.CTkLabel(root, text="Kaun Banega Crorepati....(KBC)",font=("Arial", 24))
label.place(relx=0.05, rely=0.2, relwidth=label_width, relheight=label_height)
current_widgets.append(label)
btn_next = ctk.CTkButton(root, text="Next", border_width=5, border_color="grey",command=Go_Onto_Next_Question,font=("Arial", 20))
btn_next.configure(hover_color="#FFCC00", text_color="grey")
btn_next.place(relx=0.05, rely=0.7, relwidth=button_next_width, relheight=button_next_height)

root.mainloop()
