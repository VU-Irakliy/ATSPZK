# from unittest import result

# from psutil import users
from re import M
from zk import *


def depthFirstBranchAndBound(matrix, minimum_cost, temp_cost, used_rows, starting_point): # Depth-First Branch and Bound
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
                    
        else:
            
            minimum_cost = temp_cost
            # This is just used to see what it's current minimum is (To see how fast it's perfoming)
            
        
        return minimum_cost
    

 


def bestFirstSearch(matrix): # Best-First Search
    priority_queue = []  
    # I decided not to include Closed Set, because it's useless in it's current form
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
        temp_branch = priority_queue.pop(0) 
    
        if len(temp_branch[0]) != (len(matrix) + 1):
            
            # This is just used to see what it's current minimum is (To see how fast it's perfoming)
            # if count % 10000 == 0:
            #     print(temp_branch[1])   
            # count += 1
           
            if len(temp_branch[0]) == len(matrix):
    
                temp_cost = temp_branch[1]
                last_num = temp_branch[0][-1]
                
                temp_path = temp_branch[0].copy()
                temp_path.append(0)
                
                priority_queue.append([temp_path, (temp_cost + matrix[last_num][0])])
                
            else:

                children = [i for i in range(1, len(matrix)) if i not in temp_branch[0]]
                for i in children:
                    temp_cost = temp_branch[1]
                    last_num = temp_branch[0][-1]
                    
                    temp_path = temp_branch[0].copy()
                    temp_path.append(i)
 
                    priority_queue.append([temp_path, (temp_cost + matrix[last_num][i])])
            priority_queue = sorted(priority_queue, key= lambda x: x[1])
        else:
            reached_minimum = True
    
    return temp_branch

