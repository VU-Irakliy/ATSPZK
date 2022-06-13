# from unittest import result
import numpy as np
from anytree import *
import math

#DOCUMENTATION: 
# anytree
"""
https://anytree.readthedocs.io/en/latest/ 
https://anytree.readthedocs.io/en/latest/tricks/weightededges.html

"""

'''
THESE USE TREE DATA STRUCTURES

'''
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
                        priority_queue_member = (temp_branch[0].children[y], 
                                            (temp_branch[0].children[y].weight + temp_cost) )
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


'''
END
'''

'''THIS ONE USES BOTH...'''
def ZK_algorithm(named_matrix, names, matrix):
    #result = \
    curr_result = assignment_hungarian(named_matrix, names, matrix)
    print("RESULT ARE:", curr_result)
    ...#try to connect them
    #then 
    '''
    if we have a complete tour:
        final_cost = 0
        path = []
        for i in range(len(curr_result)):
            final_cost += curr_result[i][2]
            path.append(curr_result[i][0])
            if(i = len(curr_result) - 1):
                path.append(curr_result[i][1])
        result = [path, final_cost]
        return result
        
    else:
        loop:
            we find the subproblem to deconstruct (condition construction in progress...)
            choose which one to deconstruct
            sub_n (amount of nodes in subtour)
            we choose which 
    '''
 
 
 
'''
THESE USE MATRIX DATA STRUCTURE
'''
# print(int(np.nanmin(matrix_points)))
# if you want to check if it's nan then do "if math.isnan(x): then ...."


"""
Assignment Problem Reference:  https://python.plainenglish.io/hungarian-algorithm-introduction-python-implementation-93e7c0890e15
Explanation on how this code works can be partially explained there.
"""

def minimum_zero(matrix_with_0s, lined_zero):
    
    min_row = [len(matrix_with_0s) + 100, -1]
    # i -> row
    for i in range(len(matrix_with_0s)):
        if  np.sum(matrix_with_0s[i] == True) > 0 and min_row[0] > np.sum(matrix_with_0s[i] == True):
            min_row = [np.sum(matrix_with_0s[i] == True), i]
        
    # Marked the specific row and column as False
    zero_index = np.where(matrix_with_0s[min_row[1]] == True)[0][0]
    lined_zero.append((min_row[1], zero_index))
    # print('\n',matrix_with_0s)
    # print('soooo',matrix_with_0s[:, zero_index])
    # print('HUH',matrix_with_0s[zero_index])
    matrix_with_0s[min_row[1], :] = False
    
    matrix_with_0s[:, zero_index] = False



def possible_solution(matrix):
    curr_matrix = matrix

    #Transform the matrix to boolean matrix(0 = True, others = False)
    matr_with_0s = (curr_matrix  == 0)
    # print(matr_with_0s)
    matr_with_0s_temp = matr_with_0s.copy()

    lined_zeros = []
    #Recording possible answer positions by marked_zero
    while (True in matr_with_0s_temp):
        minimum_zero(matr_with_0s_temp, lined_zeros)
    
    lined_rows_0 = []
    lined_columns_0 = []
    for i in range(len(lined_zeros)):
        lined_rows_0.append(lined_zeros[i][0])
        lined_columns_0.append(lined_zeros[i][1])
    not_lined_rows = list(set(range(len(curr_matrix))) - set(lined_rows_0))

    lined_columns = []
    not_lined_flag = True
    while not_lined_flag:
        not_lined_flag = False
        for i in range(len(not_lined_rows)):
            row_array = matr_with_0s[not_lined_rows[i]]
            for j in range(len(row_array)):
                #Step 2-2-2
                if row_array[j] == True and j not in lined_columns:
                #Step 2-2-3
                    lined_columns.append(j)
                    not_lined_flag = True

        for row, col in lined_zeros:
			#Step 2-2-4
            if row not in not_lined_rows and col in lined_columns:
                #Step 2-2-5
                not_lined_rows.append(row)
                not_lined_flag = True
    
    lined_rows = list(set(range(len(matrix))) - set(not_lined_rows))
    result = [lined_zeros, lined_rows, lined_columns]
    return result


def change_matrix(matrix, lined_rows, lined_columns):
    curr_matrix = matrix.copy()
    non_zero = []
    
    for i in range(len(curr_matrix)):
        if i not in lined_rows:
            for j in range(len(curr_matrix)):
                if j not in lined_columns:
                    non_zero.append(curr_matrix[i][j])
    
    
    min_num = np.nanmin(non_zero)
    for i in range(len(curr_matrix)):
	    if i not in lined_rows:
		    for j in range(len(curr_matrix)):
			    if (j not in lined_columns) and (math.isnan(curr_matrix[i][j]) == False):
				    curr_matrix[i][j] = curr_matrix[i][j] - min_num
    
    # print('bye') 
    # Ignore the IDE error here... 
    for i in range(len(lined_rows)):
        for j in range(len(lined_columns)):
            curr_matrix[lined_rows[i]][lined_columns[j]] = curr_matrix[lined_rows[i], lined_columns[j]] + min_num
    
    return curr_matrix


"""
WE GOTTA MODIFY THIS WITH INCLUDE, EXCLUDE AND 'THE ONES THAT ARE BEING DECOMPOSED IN THIS SUBTREE' (IF THERE IS A EDGE THAT IS IN DECOMPOSED, THEN ADD IT TO INCLUDE)
ALSO WE WILL HAVE A STORAGE OF ALL EXISTING SUBPROBLEMS THAT HAVE SUBTOURS, SO DON'T MAKE A DUPLICATE?

"""
def assignment_hungarian(named_matrix, names, matrix):
    temp_matrix = matrix.copy()

    temp_matrix = np.array(temp_matrix)
    # print(temp_matrix)

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
            
    # print('\n',temp_matrix)
    count = 0
    while count < len(matrix):
        #result[0] = , result[1] = , result[2] = ... 
        result = possible_solution(temp_matrix)
        # result = [temp_matrix, [0,1,2,3], []]
        # print(len(result[1]))
        # print(len(result[2]))
        count = len(result[1]) + len(result[2])
        # print('count', count)
        if count < len(temp_matrix):
            # print('NOOOOOOOOOOOOO')
            temp_matrix = change_matrix(temp_matrix, 
                                        result[1],
                                        result[2])
    
    l = 0
    main_result = []
    # print(r)
    # print('SOOO', result)
    result = result[0]
    # print('AAAND', result)
    # print(names)
    # print(names[0])
    while l < len(result):
        i = result[l][0]
        j = result[l][1]

        # print(re)
        # print(j[l])
        # tupling = [names[i], names[j]]
        # print('FUUUCK',matrix)
        tempest = [names[i], names[j], matrix[i][j]]
        main_result.append(tempest)
        l += 1
        
    return main_result
    # something = findminstroken(temp_matrix, 0, 0, len(temp_matrix)**2, strikethrough(temp_matrix, len(temp_matrix)))
