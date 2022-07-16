# from unittest import result

# from psutil import users
from re import M
from zk import *


'''
THESE USE TREE DATA STRUCTURES

'''

# min cost = 14
# 5 + 11 + 16 + 12 + 16
# - 12 - 16 - 11 - 5 

def depthFirstBranchAndBound(matrix, minimum_cost, temp_cost, used_rows, starting_point):
    if len(used_rows) == 0:
        used_rows.append(starting_point)
        children = [i for i in range(1, len(matrix))]
        for i in children:
            if minimum_cost > (temp_cost + matrix[starting_point][i]) or minimum_cost == 0:
                temp_cost += matrix[starting_point][i]
                minimum_cost = depthFirstBranchAndBound(matrix, minimum_cost, temp_cost, used_rows, i)
                temp_cost -= matrix[starting_point][i]
        return minimum_cost
    else:
        if len(used_rows) != (len(matrix) + 1):
            copy_copy = used_rows.copy()
            copy_copy.append(starting_point)
            if len(copy_copy ) == len(matrix):
                copy_copy.append(0)
                if minimum_cost > (temp_cost + matrix[starting_point][0]) or minimum_cost == 0:
                    temp_cost += matrix[starting_point][0]
                    minimum_cost = depthFirstBranchAndBound(matrix, minimum_cost, temp_cost, copy_copy , 0)

            else:
                children = [i for i in range(1, len(matrix)) if i not in copy_copy ]
                for i in children:
                    if minimum_cost > (temp_cost + matrix[starting_point][i]) or minimum_cost == 0:
                        temp_cost += matrix[starting_point][i]
                        minimum_cost = depthFirstBranchAndBound(matrix, minimum_cost, temp_cost, copy_copy, i)
                        temp_cost -= matrix[starting_point][i]
        else:
            minimum_cost = temp_cost
        
        return minimum_cost
 
def bestFirstSearch(matrix): 
    priority_queue = []  ##### used_rows, weight
    # priority_queue = priority_queue
    closed = []
    main_children = [i for i in range(1, len(matrix))]
    used_rows = [0]
    for i in main_children:
        temp = used_rows.copy()
        temp.append(i)
        priority_queue.append([temp, matrix[0][i]])
    del temp
    priority_queue = sorted(priority_queue, key= lambda x: x[1])
    reached_minimum = False
    count = 0
    while reached_minimum == False:
        if len(priority_queue[0][0]) != (len(matrix) + 1):
            temp = priority_queue.pop(0) ####used_rows, weight
            closed.append(temp)
            if count % 100 == 0:
                print(closed[-1])
            count += 1
            if len(temp[0]) == len(matrix):
                temp_cost = temp[1]
                last_num = temp[0][-1]
                pp = temp[0].copy()
                pp.append(0)
                priority_queue.append([pp, (temp_cost + matrix[last_num][0])])
                
            else:

                children = [i for i in range(1, len(matrix)) if i not in temp[0]]
                for i in children:
                    temp_cost = temp[1]
                    last_num = temp[0][-1]
                    pp = temp[0].copy()
                    pp.append(i)
                    priority_queue.append([pp, (temp_cost + matrix[last_num][i])])
            priority_queue = sorted(priority_queue, key= lambda x: x[1])
        else:
            temp_branch = priority_queue.pop(0)
            reached_minimum = True
    
    return temp_branch



#                 # print(temp_branch)
#                 # print("SO   ", temp_branch[0])
#                 return temp_branch
        



                    
#             else:
#                 temp_branch = priority_queue.pop(0)
#                 reached_minimum = True
#                 # print(temp_branch)
#                 # print("SO   ", temp_branch[0])
#                 return temp_branch



# def bestFirstSearch(tree):
#     priority_queue = []
#     closed = []
#     i = 0
#     if(len(tree.children)>0):
#         while(i < len(tree.children)):
#             priority_queue_member = (tree.children[i], tree.children[i].weight )
#             priority_queue.append(priority_queue_member)
#             i += 1
#         priority_queue = sorted(priority_queue, key= lambda x: x[1])
#         reached_minimum = False
    
#         while(reached_minimum == False): 
#             # print(priority_queue[0][0])
#             if(len(priority_queue[0][0].children) > 0):

#                 temp_branch = priority_queue.pop(0)
#                 # print('Processing ',temp_branch)
#                 closed.append(temp_branch)
#                 if(len(temp_branch[0].children) > 0):
#                     y = 0
#                     while(y < len(temp_branch[0].children)):
#                         temp_cost = temp_branch[1]
#                         priority_queue_member = (temp_branch[0].children[y], 
#                                             (temp_branch[0].children[y].weight + temp_cost) )
#                         priority_queue.append(priority_queue_member)
#                         # print('WHat', priority_queue)
#                         y += 1
                        
#                     priority_queue = sorted(priority_queue, key= lambda x: x[1])
                    
#             else:
#                 temp_branch = priority_queue.pop(0)
#                 reached_minimum = True
#                 # print(temp_branch)
#                 # print("SO   ", temp_branch[0])
#                 return temp_branch


'''
END
'''

