import customtkinter as ctk

def light():
    # light theme
    ctk.set_appearance_mode("light")

def dark():
    # dark theme
    ctk.set_appearance_mode("dark")

def send():

    # dictionnaire des response
    responses = {
        "bonjour": "salut comment je peut t'aider",
        "comment tu va": "j'vais super bien",
        "il est quelle heure": "jsuis basé sur un dictionnaire de response je connais pas l'heure"
    }

    message = user_input.get()

    if message.strip() != "":
        chat_history.configure(state = "normal")

        chat_history.insert("end", "user:\n")
        chat_history.insert("end", message + "\n\n")

        if message in responses:
            bot_response = responses[message]
            chat_history.insert("end", "bot:\n")
            chat_history.insert("end", bot_response + "\n\n")
        else:
            chat_history.insert("end", "bot:\n" + "je ne comprend pas" + "\n\n")


        chat_history.configure(state = "disabled")
        chat_history.see("end")
        user_input.delete(0, "end")

#configurer la main window
root = ctk.CTk()
root.geometry("500x600")
root.resizable(False, False)
root.title("Chat Bot")

#padx = 5, pady = 5, fill = "both",

# En-tête
header = ctk.CTkFrame(root, fg_color="transparent")
header.pack(anchor = "center", ipadx = 45, expand = True)

btn_light = ctk.CTkButton(
    header,
    text = "light",
    text_color = "black",
    width = 80,
    height = 50,
    font = ("Arial", 18),
    fg_color = "#E0E0E0",
    command = light)
btn_light.pack(side = "left")
btn_dark = ctk.CTkButton(
    header,
    text = "dark",
    width = 80,
    height = 50,
    font = ("Arial", 18),
    fg_color="#2B2B2B",
    hover_color = "#EDEDED",
    command = dark)
btn_dark.pack(side = "right")

header_text = ctk.CTkLabel(
    header,
    text = "Welcome to Chat Bot!",
    font = ("Verdana", 20),
)
header_text.pack(padx = 5, pady = 10)

#zone d'affichage des messages
chat_history = ctk.CTkTextbox(
    root,
    height = 450,
    width = 450,
    state = "disabled",
)
chat_history.tag_config("user", foreground = "white")
chat_history.tag_config("bot", foreground = "green")
chat_history.pack(padx = 10, pady = 10, fill = "both", expand = True)

#champ de saisie utilisateur
user_input_frame = ctk.CTkFrame(root)
user_input_frame.pack(padx = 10, pady = 10, fill = "both",)

user_input = ctk.CTkEntry(user_input_frame, placeholder_text = 'ask question....', width = 335)
user_input.pack(side = "left")

send_button = ctk.CTkButton(user_input_frame, text = 'Send', command = send)
send_button.pack(side = "right")

root.mainloop()