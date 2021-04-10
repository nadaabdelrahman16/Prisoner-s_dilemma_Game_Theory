import numpy as np
import itertools

class P2():

    def Strictly_Player2(self,StrictlyMatrix,StrictP2_action):
        #Player2
        n = StrictlyMatrix.shape[0]
        m = StrictlyMatrix.shape[1]
        arr = np.array([], dtype=int)
        for i in range(m):
            arr = np.append(arr, i)
        perm = list(itertools.permutations(arr, 2))
        r = np.random.randint(0, len(perm))
        c1 = (perm[r])
        i = 0
        arr_size = np.size(arr, 0)
        while (i < n):
            # print(StrictlyMatrix[i][c1[0]][1])
            # print(StrictlyMatrix[i][c1[1]][1])
            if (StrictlyMatrix[i][c1[0]][1] > StrictlyMatrix[i][c1[1]][1]):
                i += 1
                if (i == n):
                    no_delete = set()
                    StrictlyMatrix = np.delete(StrictlyMatrix, c1[1], 1)
                    StrictP2_action=np.delete(StrictP2_action,c1[1])
                    no_delete.add(str(c1[1]))
                    perm = [x for x in perm if not no_delete & set(str(x))]
                    arr_size -= 1
                    m-=1

                    if (len(perm) == 0):
                        break
                    else:
                        r = np.random.randint(0, len(perm))
                        c1 = perm[r]
                        i = 0
            else:
                perm.remove(perm[r])
                if (len(perm) == 0):
                    break
                else:
                    r = np.random.randint(0, len(perm))
                    c1 = perm[r]
                    i= 0
        print("p2", StrictlyMatrix)
        return StrictlyMatrix,StrictP2_action
