import numpy as np

def show_payoff(payoff_matrix):
    #Use this Function to take actions and print GUI
    # Player1_actions : Strategies of Player 1
    # Player2_actions : Strategies of Player 2
    n=np.size(payoff_matrix, 1)
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
    #GUI_Payoff_Matrix(payoff_matrix,Player1_actions,Player2_actions)
    return None

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

 show_payoff(payoff_matrix)
 return None


Run()