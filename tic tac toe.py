import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.game_board = tk.Frame(self.root)
        self.game_board.pack()
        self.buttons = []
        self.x_state = [0] * 9
        self.z_state = [0] * 9
        self.turn = True

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.game_board, text="", command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        player = "X" if self.turn else "O"
        if self.turn:
            self.x_state[row * 3 + column] = 1
        else:
            self.z_state[row * 3 + column] = 1
        self.buttons[row][column].config(text=player)
        cwin = self.check_win(self.x_state, self.z_state, row * 3 + column)
        if cwin != -1:
            self.game_over(cwin)
        else:
            self.turn = not self.turn

    def check_win(self, x_state, z_state, latest_move):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if latest_move in win:
                if all(x_state[i] for i in win):
                    return 1
                elif all(z_state[i] for i in win):
                    return 0
        return -1

    def game_over(self, winner):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")
        if winner == 1:
            messagebox.showinfo("Game Over", "X Won the match!")
        elif winner == 0:
            messagebox.showinfo("Game Over", "O Won the match!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
