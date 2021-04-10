import numpy as np
import itertools

class P1():
    def Strictly_Player1(self,StrictlyMatrix,StrictP1_action):
        n = StrictlyMatrix.shape[0]
        m = StrictlyMatrix.shape[1]
        # player 1
        arr = np.array([], dtype=int)
        for i in range(n):
            arr = np.append(arr, i)
        perm = list(itertools.permutations(arr, 2))
        r = np.random.randint(0, len(perm))
        c1 = (perm[r])
        j = 0
        while (j < m):
            # print(StrictlyMatrix[c1[0]][j][0])
            # print(StrictlyMatrix[c1[1]][j][0])
            if (StrictlyMatrix[c1[0]][j][0] > StrictlyMatrix[c1[1]][j][0]):
                j += 1
                if (j == m):
                    no_delete = set()
                    StrictlyMatrix = np.delete(StrictlyMatrix, c1[1], 0)
                    StrictP1_action=np.delete(StrictP1_action,c1[1])
                    # print(StrictlyMatrix)
                    no_delete.add(str(c1[1]))
                    perm = [x for x in perm if not no_delete & set(str(x))]

                    if (len(perm) == 0):
                        break
                    else:
                        r = np.random.randint(0, len(perm))
                        c1 = perm[r]
                        j = 0
            else:
                perm.remove(perm[r])
                if (len(perm) == 0):
                    break
                else:
                    r = np.random.randint(0, len(perm))
                    c1 = perm[r]
                    j = 0
        print("Player1",StrictlyMatrix)
        return StrictlyMatrix,StrictP1_action



    def weakly_Player1(self,weaklyMatrix,weaklyP1_action):
        n = weaklyMatrix.shape[0]
        m = weaklyMatrix.shape[1]
        # player 1
        arr = np.zeros(n,dtype=int)
        for i in range(n):
            arr[i]=i
        perm = list(itertools.permutations(arr, 2))
        r = np.random.randint(0,len(perm))
        c1 = (perm[r])
        j = 0
        arr_size = np.size(arr, 0)
        while (j < m):
            # print(weaklyMatrix[c1[0]][j][0])
            # print(weaklyMatrix[c1[1]][j][0])
            if (weaklyMatrix[c1[0]][j][0] >= weaklyMatrix[c1[1]][j][0]):
                j += 1
                if (j == m):
                    no_delete = set()
                    weaklyMatrix = np.delete(weaklyMatrix, c1[1], 0)
                    weaklyP1_action=np.delete(weaklyP1_action,c1[1])
                    # print(StrictlyMatrix)
                    no_delete.add(str(c1[1]))
                    n -= 1
                    perm = [x for x in perm if not no_delete & set(str(x))]
                    arr_size -= 1

                    if (len(perm) == 0):
                        break
                    else:
                        r = np.random.randint(0, len(perm))
                        c1 = perm[r]
                        j = 0
            else:
                perm.remove(perm[r])
                if (len(perm) == 0):
                    break
                else:
                    r = np.random.randint(0, len(perm))
                    c1 = perm[r]
                    j = 0
        print("p1",weaklyMatrix)
        return weaklyMatrix,weaklyP1_action
