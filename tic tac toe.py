import tkinter as tk
from tkinter import messagebox as mb

class tictactoe:
    def __init__(self):
        self.currentplayer="X"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title(" Tic Tac Toe")

        self.buttonsgrid =[]
        for i in range (3):
            row=[]
            for j in  range(3):
                button=tk.Button(self.window,text ="",width=20,height=10,command=lambda i=i,j=j:self.make_move(i,j))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttonsgrid.append(row)
    def make_move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.currentplayer
            self.buttonsgrid[row][col].config(text=self.currentplayer)
            if self.chechk(self.currentplayer):
                mb.showinfo("Game Over","The Winner is"+self.currentplayer)
                self.window.quit()
            
            elif self.isdraw():
                mb.showinfo("Game Over","Its a Draw")
                self.window.quit()
            self.currentplayer="O" if self.currentplayer =="X" else "X"
    def chechk(self,player):
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if player == self.board[0][i] == self.board[0][i] == self.board[2][i]:
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
        if player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
        return False
    def isdraw(self):
         for row in self.board:
              if "" in row:
                   return False
              return True
            
    def run(self):
        self.window.mainloop()

game=tictactoe()
game.run()

        
        