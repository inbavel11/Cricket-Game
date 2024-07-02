import tkinter as tk
import random

class CricketGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Game")
        
        self.player_score = 0
        self.bot_score = 0
        self.player_wickets = 0
        self.bot_wickets = 0
        
        self.innings = 'player'  # Start with player innings
        
        self.label = tk.Label(root, text="Welcome to the Cricket Game!")
        self.label.pack()
        
        self.score_label = tk.Label(root, text=f"Player Score: {self.player_score}  Player Wickets: {self.player_wickets}  Bot Score: {self.bot_score}  Bot Wickets: {self.bot_wickets}")
        self.score_label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.play_button = tk.Button(root, text="Play!", command=self.play)
        self.play_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def play(self):
        if self.innings == 'player':
            self.player_innings()
        else:
            self.bot_innings()

    def player_innings(self):
        player_choice = self.entry.get()
        
        if player_choice.isdigit():
            player_run = int(player_choice)
            if player_run < 1 or player_run > 6:
                self.result_label.config(text="Please enter a number between 1 and 6")
                return
            
            bot_run = random.randint(1, 6)
            
            if player_run == bot_run:
                self.player_wickets += 1
                result_text = f"You're out! Bot predicted {bot_run}. Total Wickets: {self.player_wickets}"
            else:
                self.player_score += player_run
                result_text = f"You scored {player_run} runs! Bot predicted {bot_run}. Total Score: {self.player_score}"
            
            if self.player_wickets >= 3:  # End player innings after 3 wickets
                self.innings = 'bot'
                self.result_label.config(text=f"End of Player Innings. Total Score: {self.player_score}. Bot's turn to bat!")
                self.entry.delete(0, tk.END)
                return
            
            self.result_label.config(text=result_text)
            self.score_label.config(text=f"Player Score: {self.player_score}  Player Wickets: {self.player_wickets}  Bot Score: {self.bot_score}  Bot Wickets: {self.bot_wickets}")
        else:
            self.result_label.config(text="Please enter a valid number")
    
    def bot_innings(self):
        player_prediction = self.entry.get()
        
        if player_prediction.isdigit():
            player_prediction = int(player_prediction)
            if player_prediction < 1 or player_prediction > 6:
                self.result_label.config(text="Please enter a number between 1 and 6")
                return
            
            bot_run = random.randint(1, 6)
            
            if player_prediction == bot_run:
                self.bot_wickets += 1
                result_text = f"Bot is out! You predicted {bot_run}. Total Wickets: {self.bot_wickets}"
            else:
                self.bot_score += bot_run
                result_text = f"Bot scored {bot_run} runs! You predicted {player_prediction}. Total Score: {self.bot_score}"
            
            if self.bot_wickets >= 3:  # End bot innings after 3 wickets
                self.play_button.config(state="disabled")
                result_text += " Game Over!"
                if self.player_score > self.bot_score:
                    result_text += " You win!"
                elif self.player_score < self.bot_score:
                    result_text += " Bot wins!"
                else:
                    result_text += " It's a tie!"
            
            self.result_label.config(text=result_text)
            self.score_label.config(text=f"Player Score: {self.player_score}  Player Wickets: {self.player_wickets}  Bot Score: {self.bot_score}  Bot Wickets: {self.bot_wickets}")
            self.entry.delete(0, tk.END)
        else:
            self.result_label.config(text="Please enter a valid number")

if __name__ == "__main__":
    root = tk.Tk()
    game = CricketGame(root)
    root.mainloop()
