from assignment import *


def start_ZK_algorithm(named_matrix, names, matrix, method):
    
    empty = [] #for the first run only
    # exclude = [[5,1]]
    # curr_result = assignment_hungarian(named_matrix, names, matrix, empty, exclude)
    curr_result = assignment_hungarian(named_matrix, names, matrix, empty, empty)

    
    # paths = [(x[0], x[1]) for x in curr_result[0]]
    list_of_coords = make_tours(names, curr_result[0])
    # print('Start ',list_of_coords)
    
    # exit()
    if len(list_of_coords) == 1: ###IF WE ONLY HAVE 1 SUBTOUR/COMPLETE TOUR
        cost = 0
        for list in list_of_coords:
            for coord in list:
                cost += matrix[coord[0]][coord[1]]
        print('Result was achieved without going through the Branch and Bound')
        return cost

    min_total = curr_result[1]
    len_of_tours = []

    for i in range(len(list_of_coords)):
        len_of_tours.append(len(list_of_coords[i]))
    # print('So So ',len_of_tours)

    ### We choose min() function to get the resulting subtour, because there is no solution for if there is more than one subtour with min amount of
    ### edges to eliminate, therefore this is the current method
    cand = list_of_coords[len_of_tours.index(min(len_of_tours))]
    # print('Candidates',cand)
  
    
    if method == 1:  ## This is Depth-First Branch and Bound Method
        
        children = []
       
        for i in range(len(cand)):
            exclude = []
            include = []
            exclude.append(cand[i])
            
            curr = assignment_hungarian(named_matrix, names, matrix, include, exclude)
            
            include = get_include(names, curr, cand)
          
            children.append([curr[0], exclude, include, curr[1]]) ### x[0] - PATH RESULT,  x[1] - EXCLUDE, x[2] - INCLUDE, x[3] - WEIGHT 
        
        minimum = 0
        # print(children)
        for i in children:
            curr_cost = i[3]
            # print('Throw it back\n')
            if minimum == 0 or minimum > (curr_cost):
                minimum =  DFBnB_zk_algorithm(named_matrix, names, matrix, i, minimum)
        result = minimum
        print('ZK DFBnB Result')
        

    else: # This is Best-First Search Method
        result = BFS_zk_algorithm(named_matrix, names, matrix, cand, min_total)
        print("ZK BFS Result")

    return result
    
                    
def DFBnB_zk_algorithm( named_matrix, names, matrix, data, minimum): # Depth-First Branch and Bound Method
    temp_paths, temp_exc, temp_inc, temp_weight = data
    tours = make_tours(names, temp_paths)
    if len(tours) == 1:
        cost = 0
        # print('Sussy baka',tours)
        for list in tours:
            for coord in list:
                cost += matrix[coord[0]][coord[1]]
        return cost
    # print('Tours ',tours)
    len_of_tours = []
    for i in range(len(tours)):
        count = 0
        for j in tours:
            if j in temp_inc:
                count += 1
        len_of_tours.append(len(tours[i]) - count)
    cand = tours[len_of_tours.index(min(len_of_tours))]
    for i in temp_inc:
        if i in cand:
            um = cand.pop(cand.index(i))
            del um
    children = []
    for i in range(len(cand)):
        exclude = temp_exc.copy()
        exclude.append(cand[i])
        
        include = temp_inc.copy()
        
        curr = assignment_hungarian(named_matrix, names, matrix, include, exclude)
        if curr == (None, None):
            return minimum

        temp_temp_inc = get_include(names, curr, cand)
        for j in temp_temp_inc:
            if j not in include:
                include.append(j)
        children.append([curr[0], exclude, include, curr[1]])

    for i in children:
        curr_cost = i[3]        ### x[0] - PATH RESULT,  x[1] - EXCLUDE, x[2] - INCLUDE, x[3] - WEIGHT 
        
        if minimum == 0 or minimum > (curr_cost): #### [curr[0], exclude, include, curr[1]]
            temp = minimum
            minimum =  DFBnB_zk_algorithm(named_matrix, names, matrix, i, minimum)

    result = minimum
    return result
            


def BFS_zk_algorithm(named_matrix, names, matrix, cand, min_total): # Best-First Search Method
    priority_queue = []
    
    for i in range(len(cand)):
        exclude = []
        include = []
        exclude.append(cand[i])
        
        curr = assignment_hungarian(named_matrix, names, matrix, include, exclude)
        
        include = get_include(names, curr, cand)
        
        priority_queue.append([curr[0], exclude, include, curr[1]])
   
    min_not_found = True
    priority_queue = sorted(priority_queue, key= lambda x: x[3])  ### x[0] - PATH RESULT,  x[1] - EXCLUDE, x[2] - INCLUDE, x[3] - WEIGHT 
   
   
    closed_priority = []
    i = 0
    while min_not_found:
        if min_not_found == False:
            break
        else:
            temps_prio = priority_queue.pop(0)
            temp_paths, temp_exc, temp_inc, temp_weight = temps_prio
           

            closed_priority.append(temps_prio)
            tours = make_tours(names, temp_paths)
            if len(tours) == 1:
                # print(tours)
                min_not_found = False
                cost = 0
                for list in tours:
                    for coord in list:
                        cost += matrix[coord[0]][coord[1]]
                return cost
            
            len_of_tours = []
            for i in range(len(tours)):
                count = 0
                for j in tours:
                    if j in temp_inc:
                        count += 1
                len_of_tours.append(len(tours[i]) - count)
            candid = tours[len_of_tours.index(min(len_of_tours))]
            for i in temp_inc:
                if i in candid:
                    um = candid.pop(candid.index(i))
                    del um
            
            for i in range(len(candid)):
                exclude = temp_exc.copy()
                exclude.append(candid[i])
                
                include = temp_inc.copy()
                
               
                curr = assignment_hungarian(named_matrix, names, matrix, include, exclude)
                
                    
                
                temp_temp_inc = get_include(names, curr, candid)
                for j in temp_temp_inc:
                    if j not in include:
                        include.append(j)
                
                priority_queue.append([curr[0], exclude, include, curr[1]])
                del include
                del exclude
            
            priority_queue = sorted(priority_queue, key= lambda x: x[3])
        if min_not_found == False:
            break



    
 

def get_include(names, curr_result, cand): # This function gets paths that need to be in include
    paths = [(x[0], x[1]) for x in curr_result[0]]
   
    coords = []
    for j in paths:
        temp = []
        for l in j:
            for i in range(len(names)):
                if names[i] == l:
                    temp.append(i)
        coords.append(temp)
    include = []
    for i in cand:
        
        for j in coords:
            if i == j:
                include.append(i)
    return include


def make_tours(names, curr_paths): ## This function creates tours from current assignment problem results
    paths = [(x[0], x[1]) for x in curr_paths]
    
    coords = []
    for j in paths:
        temp = []
        for l in j:
            for i in range(len(names)):
                if names[i] == l:
                    temp.append(i)
        coords.append(temp)
   
    tours = []
    used_paths = [] 
    flag = True
    list_of_coords = []

    while len(used_paths) != len(paths):
        for path in range(len(paths)):
            if len(used_paths) == 0:
                tours.append([paths[path][0], paths[path][1]])
                used_paths.append(paths[path])
                list_of_coords.append([coords[path]])
            else:
                if paths[path] not in used_paths:
                    flag = True
                    
                    for j in range(len(tours)):
                        if tours[j][-1] == paths[path][0]:
                            tours[j].append(paths[path][1])
                            used_paths.append(paths[path])
                            list_of_coords[j].append(coords[path])

                        elif j == (len(tours) -1) and tours[j][0] == tours[j][-1]:
                            for m in range(len(paths)):
                                if paths[m] not in used_paths: 
                                    tours.append([paths[m][0], paths[m][1]])
                                    used_paths.append(paths[m])
                                    list_of_coords.append([coords[m]])
                                    flag = False
                                    break

                        if flag == False:
                            break
    return list_of_coords