import numpy as np
from anytree import *
import math

#DOCUMENTATION: 
# anytree
"""
https://anytree.readthedocs.io/en/latest/ 
https://anytree.readthedocs.io/en/latest/tricks/weightededges.html

"""


def depthFirstBranchAndBound(tree, minimum_cost, temp_cost):
    if len(tree.children) > 0:
        i = 0
        while(i < len(tree.children)):
            if minimum_cost > (temp_cost + tree.children[i].weight) or minimum_cost == 0:
                temp_cost += tree.children[i].weight
                # print("Current cost:", temp_cost)
                minimum_cost = depthFirstBranchAndBound(tree.children[i], 
                                            minimum_cost, temp_cost)
                temp_cost-=tree.children[i].weight
                
            i += 1

        return minimum_cost
    else:
        minimum_cost = temp_cost
        # print(tree)
        # print("CURRENT MINIMUM COST:", minimum_cost)
        return minimum_cost


def bestFirstSearch(tree):
    priority_queue = []
    closed = []
    i = 0
    if(len(tree.children)>0):
        while(i < len(tree.children)):
            priority_queue_member = (tree.children[i], tree.children[i].weight )
            priority_queue.append(priority_queue_member)
            i += 1
        priority_queue = sorted(priority_queue, key= lambda x: x[1])
        reached_minimum = False
    
        while(i < len(priority_queue) or reached_minimum == False):
            # print(priority_queue[0][0])
            if(len(priority_queue[0][0].children) > 0):

                temp_branch = priority_queue.pop(0)
                # print('Processing ',temp_branch)
                closed.append(temp_branch)
                if(len(temp_branch[0].children) > 0):
                    y = 0
                    while(y < len(temp_branch[0].children)):
                        temp_cost = temp_branch[1]
                        priority_queue_member = (temp_branch[0].children[y], (temp_branch[0].children[y].weight + temp_cost) )
                        priority_queue.append(priority_queue_member)
                        # print('WHat', priority_queue)
                        y += 1
                        
                    priority_queue = sorted(priority_queue, key= lambda x: x[1])
                    
            else:
                temp_branch = priority_queue.pop(0)
                reached_minimum = True
                # print(temp_branch)
                # print("SO   ", temp_branch[0])
                return temp_branch

            i+=1


 

def ZK_algorithm(named_matrix, names, matrix):
    #result = \
    assignment_hungarian(named_matrix, names, matrix)
    '''
    if we have a complete tour:
        return result
    else:
        loop:
            we find the subproblem to deconstruct (condition construction in progress...)
            choose which one to deconstruct
            sub_n (amount of nodes in subtour)
            we choose which 
    '''

# print(int(np.nanmin(matrix_points)))
#if you want to check if it's nan then do "if math.isnan(x): then ...."
def assignment_hungarian(named_matrix, names, matrix):
    temp_matrix = matrix.copy()
    # print(temp_matrix)
    for i in temp_matrix:
        cur_min = int(np.nanmin(i))
        for j in range(0, len(i)):
            if math.isnan(i[j]) != True:
                i[j] = i[j] - cur_min
    # print(temp_matrix)

    for i in range(0, len(temp_matrix)):
        temp_array = []
        for j in range(0, len(temp_matrix)):
            temp_array.append(temp_matrix[j][i])
        cur_min = int(np.nanmin(temp_array))
        for j in range(0, len(temp_matrix)):
            if math.isnan(temp_matrix[j][i]) != True:
                temp_matrix[j][i] = temp_matrix[j][i] - cur_min
            
    print(temp_matrix)
    something = findminstroken(temp_matrix, 0, 0, len(temp_matrix)**2, strikethrough(temp_matrix, len(temp_matrix)))
    # max_l = len(temp_matrix)
    # l = 0
    # while(flag):
    #     if(l < max_l):
    #         flag = True
    #     else:

    print(something)
            
    # return 
    ...

def strikethrough(matr, x_len):
    t_matr = matr.copy()
    for i in range(len(t_matr)):
        for j in range(len(t_matr[i])):
            t_matr[i][j] = 0
    # print("strike1", t_matr)
    for i in range(x_len):
        for j in range(x_len):
            if math.isnan(matr[i][j]):
                for k in range(x_len):
                    t_matr[k][j] += 1
                for k in range(x_len):
                    t_matr[i][k] += 1
    # print('strike2', t_matr)
    return t_matr

def countstroken(t_matr):
    count = 0
    for i in range(len(t_matr)):
        for j in range(len(t_matr[i])):
            if t_matr[i][j] > 0:
                # print("HELLO")
                count += 1
    print('count', count)              #COUNT DOESN'T INCREASE
    return count

def findminstroken(matr, i0, j0, rmin, tmin):
    # print('i0 is', i0)
    if i0 >= len(matr):
        return tmin
    # print('j0 is', j0)
    if j0 >= len(matr[i0]):
        return tmin
    m = matr.copy()
    # print('oh la la', m)
    m[i0][j0] = 0
    # print('ho hoh o', m)
    t_matr = strikethrough(m, len(matr))
    r = countstroken(t_matr)
    if (r >= rmin):
        tmin = t_matr
    tmin2 = findminstroken(m, i0, j0 + 1, rmin, tmin)
    tmin3 = findminstroken(m, i0 + 1, j0, rmin, tmin)
    tc2 = countstroken(tmin2)
    tc3 = countstroken(tmin3)
    if tc2 >= r:
        tmin = tmin2
        r = tc2
    if tc3 > r:
        tmin = tmin3
        r = tc3
    return tmin

