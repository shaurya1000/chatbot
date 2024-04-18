import tkinter as tk
from tkinter import scrolledtext, Button, Label, END
import random
import re

responses = {
    "how are you": ["I'm doing well, thank you!", "Not too bad, how about you?", "I'm great! What about you?",
                    "Feeling good today!", "Everything is fine, thanks for asking!"],
    "hows the weather today": ["Clear skies, suitable for a good walk outside", "It's a little cloudy, you should keep an umbrella handy", "It's always raining in Abbotsford"],
    "when is my last exam": "According to your schedule, it will be on April 22nd",
}

class ChatBox(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry("550x650")
        self.configure(bg="#f0f0f0")

        self.AppHeader = Label(self, text="My Chat App", bg="Navy Blue", fg="beige", font=("Arial", 27))
        self.AppHeader.pack(fill=tk.X, expand=True)

        self.DisplayText = scrolledtext.ScrolledText(self, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 12))
        self.DisplayText.pack(fill=tk.BOTH, expand=True)

        self.DisplayText.tag_config("user", foreground='Navy Blue')
        self.DisplayText.tag_config("bot", foreground='Dark Green')

        self.InputText = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=2, font=("Arial", 12))
        self.InputText.pack(fill=tk.BOTH, expand=True)

        self.SendButton = Button(self, text="Send", font=("Arial", 12), command=self.FuncSendText, bg="#4CAF50", fg="white")
        self.SendButton.pack()

    def FuncSendText(self):
        UserInput = self.InputText.get("1.0", END).strip().lower()
        UserInput = re.sub(r'[^\w\s]', '', UserInput)  # Remove punctuation
        if UserInput:
            self.DisplayText.config(state=tk.NORMAL)
            self.DisplayText.insert(tk.END, "YOU: " + UserInput + "\n", "user")
            bot_response = self.get_bot_response(UserInput)
            self.DisplayText.insert(tk.END, "BOT: " + bot_response + "\n", "bot")
            self.DisplayText.config(state=tk.DISABLED)
            self.InputText.delete("1.0", END)

    def get_bot_response(self, user_input):
        for key in responses:
            if key in user_input:
                if isinstance(responses[key], list):
                    return random.choice(responses[key])
                else:
                    return responses[key]
        return "I'm sorry, I didn't understand that."

class ChatApp:
    def __init__(self):
        self.chatbox1 = ChatBox("Prototype 1")
        self.chatbox1.mainloop()

if __name__ == "__main__":
    app = ChatApp()
