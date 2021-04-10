import numpy as np
from tkinter import *
import pandas as pd
class GT():

 def GUI_Payoff_Matrix(self,payoff_matrix,Player1_actions,Player2_actions):
    # Use this Function to create payoff matrix in GUI
    # Player1_actions : Strategies of Player 1
    # Player2_actions : Strategies of Player 2
    n = np.size(payoff_matrix, 0)
    m = np.size(payoff_matrix, 1)

    main = Tk()
    main.title("Payoff Matrix")
    main.iconbitmap('games.ico')
    for i in range(n+1):
        for j in range(m+1):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            if (i==0)and (j==0):
                continue
            elif(i==0):
                e.insert(END, Player2_actions[j-1])
                continue
            elif(j == 0):
                e.insert(END, Player1_actions[i-1])
                continue
            else:
                e.insert(END, ('(',int(payoff_matrix[i-1][j-1][0]),',',int(payoff_matrix[i-1][j-1][1]),')'))
    # Run GUI
    main.mainloop()
    return None

 def show_payoff(self,payoff_matrix):
    #Use this Function to take actions and print GUI
    # Player1_actions : Strategies of Player 1
    # Player2_actions : Strategies of Player 2
    n=np.size(payoff_matrix, 0)
    m=np.size(payoff_matrix, 1)
    Player1_actions=np.array([],dtype=str)
    Player2_actions = np.array([],dtype=str)

    for i in range(n):
        action=str(input("Enter Strategies's name for Player 1 "))
        Player1_actions=np.append(Player1_actions,action)
    for i in range(m):
        action=str(input("Enter Strategies's name for Player 2 "))
        Player2_actions=np.append(Player2_actions,action)

    # cols = pd.MultiIndex.from_product([lable_one, lable_two])
    # p = pd.DataFrame(payoff_matrix.T.reshape(2, -1), index=row, columns=cols)
    GT.GUI_Payoff_Matrix(self,payoff_matrix,Player1_actions,Player2_actions)
    return Player1_actions,Player2_actions



 def Run(self):
# Used this Function to take inputs and it 's the Main Function
# n : number of Strategies for Player 1
# m : number of Strategies for Player 2

  n = int(input("Enter the number of Player1's actions : "))
  m = int(input("Enter the number of Player2's actions: "))

  print("Enter each profile of payoff in a single line (separated by space): ")
  t = list(tuple(map(int,input().split())) for r in range(n*m))
  payoff=np.asarray([sublist for sublist in t])

# User input of payoffs matrix
  payoff_matrix=np.zeros((n,m,2))
  counter=0
  for i in range(n):
       for j in range(m):
           payoff_matrix[i][j]=payoff[counter]
           counter+=1
  Player1_actions,Player2_actions=GT.show_payoff(self,payoff_matrix)
  return payoff_matrix,Player1_actions,Player2_actions


