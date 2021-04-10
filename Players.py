import numpy as np
import  Run_Game
import copy
import Player1
import Player2
from sympy import Symbol
from sympy.solvers import solve

class Player(Run_Game.GT,Player1.P1,Player2.P2):
    payoffMatrix=None
    Player1_actions=None
    Player2_actions=None
    def strictly_dominated(self,payoffMatrix,StrictP1_action,StrictP2_action):
        counter=2
        c=0
        while(c<counter):
           if (len(StrictP1_action) == 1 and (len(StrictP2_action) == 1)):
                break
           else:
            if (payoffMatrix.shape[0]!= 1):
              StrictlyMatrix = payoffMatrix
              payoffMatrix, StrictP1_action = self.Strictly_Player1(StrictlyMatrix, StrictP1_action)
              StrictlyMatrix2, StrictP2_action = self.Strictly_Player2(payoffMatrix, StrictP2_action)
              payoffMatrix = StrictlyMatrix2
              c+=1
              if c==0:
               break
        self.GUI_Payoff_Matrix(payoffMatrix,StrictP1_action,StrictP2_action)

Game=Player()
Game.payoffMatrix,Game.Player1_actions,Game.Player2_actions=Game.Run()
print(" 1- strictly dominated")
print(" 2- weakly dominated")
print(" 3- category of symmetric game")
print(" 4- to apply positive affine transformation")
print(" 5- expected Payoff and mixed equlibrium")
print(" 6- pure Nash")
print(" 7- Strict pure Nash")
print(" 8- THP")
i=int(input("Enter Number of Function to use "))
if(i==1):
    Game.strictly_dominated(Game.payoffMatrix, Game.Player1_actions, Game.Player2_actions)
# if(i==2):
#     Game.weakly_dominated(Game.payoffMatrix,Game.Player1_actions,Game.Player2_actions)
# if(i==3):
#     Game.category_game(Game.payoffMatrix)
# if(i==4):
#     Game.positive_affine_transformation(Game.payoffMatrix,Game.Player1_actions,Game.Player2_actions)
# if(i==5):
#     Game.expected_Payoff(Game.payoffMatrix,Game.Player1_actions,Game.Player2_actions)
# if(i==6):
#     Game.pure_Nash(Game.payoffMatrix)
# if(i==7):
#     Game.pure_strict_Nash(Game.payoffMatrix)
# if(i==8):
#     Game.THP(Game.payoffMatrix)