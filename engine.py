import numpy as np

class game_board:
    def __init__(self):
        self.board=2+np.zeros((3,3))
    def legal_move(self,x,y):
        if(self.board[x][y]==2):
            return True
        else:
            return False
    def make_move(player,x,y):
game=game_board()
print(game.legal_move(0,0))