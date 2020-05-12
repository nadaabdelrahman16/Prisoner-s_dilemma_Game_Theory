import numpy as np


def Run():
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

 #show_payoff(payoff_matrix)
 return None


Run()