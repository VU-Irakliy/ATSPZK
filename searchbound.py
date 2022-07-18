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
countess = 0
def depthFirstBranchAndBound(matrix, minimum_cost, temp_cost, used_rows, starting_point):
    if len(used_rows) == 0:
        used_rows.append(starting_point)
        children = np.array([i for i in range(1, len(matrix))])
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
                    temp_cost -= matrix[starting_point][0]

            else:
                children = np.array([i for i in range(1, len(matrix)) if i not in copy_copy ])
                for i in children:
                    if minimum_cost > (temp_cost + matrix[starting_point][i]) or minimum_cost == 0:
                        temp_cost += matrix[starting_point][i]
                        minimum_cost = depthFirstBranchAndBound(matrix, minimum_cost, temp_cost, copy_copy, i)
                        temp_cost -= matrix[starting_point][i]
                    # else:
                    #     print(used_rows)
        else:
            # print(used_rows)
            
            minimum_cost = temp_cost
            print(minimum_cost)
            # print(used_rows)
        
        return minimum_cost
    
def bestFirstSearch(matrix): 
    priority_queue = []  ##### used_rows, weight
    # priority_queue = priority_queue
    # closed = []
    main_children = [i for i in range(1, len(matrix))]
    used_rows = [0]
    for i in main_children:
        temp = used_rows.copy()
        temp.append(i)
        hq.heappush(priority_queue, [temp, matrix[0][i]])
    del temp
    priority_queue = sorted(priority_queue, key= lambda x: x[1])
    reached_minimum = False
    count = 0
    while reached_minimum == False:
        if len(priority_queue[0][0]) != (len(matrix) + 1):
            temp = priority_queue.pop(0) ####used_rows, weight
            # closed.append(temp)
            if count % 10000 == 0:
                print(temp[1])
                
            count += 1
            if len(temp[0]) == len(matrix):
                temp_cost = temp[1]
                last_num = temp[0][-1]
                pp = temp[0].copy()
                pp.append(0)
                #use insert
                hq.heappush(priority_queue, [pp, (temp_cost + matrix[last_num][0])])
                
            else:

                children = [i for i in range(1, len(matrix)) if i not in temp[0]]
                for i in children:
                    temp_cost = temp[1]
                    last_num = temp[0][-1]
                    pp = temp[0].copy()
                    pp.append(i)
                    #use insert
                    '''
                    if weight is more than max, add to the end
                    if equal, to the end

                    if less, than we got through the list, until we find the member that has weight bigger than our weight
                    and put it at the front of it
                    '''
                    hq.heappush(priority_queue,[pp, (temp_cost + matrix[last_num][i])])
            priority_queue = sorted(priority_queue, key= lambda x: x[1])
        else:
            temp_branch = priority_queue.pop(0)
            reached_minimum = True
    
    return temp_branch
 
# def bestFirstSearch(matrix): 
#     priority_queue = []  ##### used_rows, weight
#     # priority_queue = priority_queue
#     # closed = []
#     main_children = [i for i in range(1, len(matrix))]
#     used_rows = [0]
#     for i in main_children:
#         temp = used_rows.copy()
#         temp.append(i)
#         priority_queue.append([temp, matrix[0][i]])
#     del temp
#     priority_queue = sorted(priority_queue, key= lambda x: x[1])
#     reached_minimum = False
#     count = 0
#     while reached_minimum == False:
#         if len(priority_queue[0][0]) != (len(matrix) + 1):
#             temp = priority_queue.pop(0) ####used_rows, weight
#             # closed.append(temp)
#             if count % 10000 == 0:
#                 print(temp)
#             count += 1
#             if len(temp[0]) == len(matrix):
#                 temp_cost = temp[1]
#                 last_num = temp[0][-1]
#                 pp = temp[0].copy()
#                 pp.append(0)
#                 priority_queue.append([pp, (temp_cost + matrix[last_num][0])])
                
#             else:

#                 children = [i for i in range(1, len(matrix)) if i not in temp[0]]
#                 for i in children:
#                     temp_cost = temp[1]
#                     last_num = temp[0][-1]
#                     pp = temp[0].copy()
#                     pp.append(i)
#                     priority_queue.append([pp, (temp_cost + matrix[last_num][i])])
#             priority_queue = sorted(priority_queue, key= lambda x: x[1])
#         else:
#             temp_branch = priority_queue.pop(0)
#             reached_minimum = True
    
#     return temp_branch




'''
END
'''

