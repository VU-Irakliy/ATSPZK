from assignment import *

'''THIS ONE USES BOTH...'''
#this will also have a division of BFS and DFBnB
def start_ZK_algorithm(named_matrix, names, matrix):
    include = []
    exclude = []
    # cand = []
    
    
    curr_result = assignment_hungarian(named_matrix, names, matrix, include, exclude)
    Start = Node("Start", weight = curr_result[1])
    min_total = curr_result[1]
    nodes = [(x[0], x[1]) for x in curr_result[0]]
    print(nodes)
    coords = []
    for j in nodes:
        temp = []
        for l in j:
            for i in range(len(names)):
                if names[i] == l:
                    temp.append(i)
        coords.append(temp)
    print(coords)
    tours = []
    # list_of_tours = []
    used_nodes = []
    flag = True
    list_of_coords = []#######################TODO : RENAME NODES TO PATHS!!! DON'T BE ILLITERATE
    while len(used_nodes) != len(nodes):
        for node in range(len(nodes)):
            if len(used_nodes) == 0:
                tours.append([nodes[node][0], nodes[node][1]])
                used_nodes.append(nodes[node])
                list_of_coords.append([coords[node]])
                # list_of_tours.append([nodes[node]])
            else:
                if nodes[node] not in used_nodes:
                    flag = True
                    
                    for j in range(len(tours)):
                        if tours[j][-1] == nodes[node][0]:
                            tours[j].append(nodes[node][1])
                            used_nodes.append(nodes[node])
                            list_of_coords[j].append(coords[node])
                            # list_of_tours[j].append(nodes[node])
                        elif j == (len(tours) -1) and tours[j][0] == tours[j][-1]:
                            for m in range(len(nodes)):
                                if nodes[m] not in used_nodes:
                                    tours.append([nodes[m][0], nodes[m][1]])
                                    used_nodes.append(nodes[m])
                                    list_of_coords.append([coords[m]])
                                    # list_of_tours.append([nodes[m]])
                                    flag = False
                                    break
                        if flag == False:
                            break
    print(list_of_coords)
    # print(used_nodes)
    # print(list_of_tours)
    if len(list_of_coords) == 1:
        #return result
        ...
    len_of_tours = []

    for i in range(len(list_of_coords)):
         len_of_tours.append(len(list_of_coords[i]))
    #if include, then we copy the list of coords, check where in list of coords each path located then we find it, take it away and decrease the len of subtour
    print(len_of_tours)
    ### WE CHOOSE MIN() FUNCTION FOR RESULT OF ONE OF THEM, BECAUSE THERE IS NO SOLUTION FOR IF THERE ARE MORE THAN ONE SUBTOUR WITH MIN AMOUNT OF
    ### EDGES TO ELIMINATE, THEREFORE THIS IS THE CURRENT METHOD
    cand = list_of_coords[len_of_tours.index(min(len_of_tours))]
    #here we don't do anything with include, cause this is a starting function
    # cand = [min_len_subtour]
    # cand = len_of_tours[min_len_subtour]

    # myStr = "domain"
    # myVal = "pythonforbeginners.com"
    # moduleName = __name__
    # currModule = sys.modules[moduleName]
    # setattr(currModule, myStr,myVal)
    # print(domain)


    if len(nodes) >= 1000:  ##DFBnB
        ...
        # for i in cand:
        #     exclude.append(i)
        #     zk_algorithm
        #     exclude = []
    else: #BFS
        ...
        priority_queue = []
        closed = []
        excludes = []
        min_not_found = True
        for i in range(len(cand)):
            bran = 'A' + str(i)
            exclude.append(cand[i])
            curr = assignment_hungarian(named_matrix, names, matrix, include, exclude)
            excludes.append([exclude, curr[1]])
            exclude = []
            valu = Node(bran, parent = Start, weight = curr[1])
            priority_queue.append([valu, curr[1]])
        excludes = sorted(excludes, key= lambda x: x[1])
        print(excludes)
        # priority_queue = sorted(priority_queue, key= lambda x: x[1])
        priority_queue = sorted(priority_queue, key= lambda x: x[1])
        print(priority_queue)
        BFS_zk_algorithm

            
        # print(assignment_hungarian(named_matrix, names, matrix, include, exclude))
        # A2 = Node("A2", parent = A1, weight = assignment_hungarian(named_matrix, names, matrix, include, exclude, cand)[1])
        # for i in cand:
        #     exclude.append(i)
        #     BFS_zk_algorithm
        #     exclude = []
    # if len(include) != 0:    THIS IS FOR THE OTHER FUNCTION
                    
            
def BFS_zk_algorithm(named_matrix, names, matrix, include, exclude, cand, priority_queue ): #IF COMPLETE TOUR, THEN RETURN MINIMUM COST AND WE'RE DONE
    """
    resulting_complete tours = [] (DFBnB)
    min_result = 0 (BFS)

    if complete:
        BFS:
        min_result = ass_result[1]
        return

        
    if not complete:
        we pick the subtour
        IF include > 0:
            we substract the number of edges to eliminate from that subtour
            check all tours
        which one has minimum number of edges to elminate:
            our_pick = []
            if len(resulting_subtours) == 1: for formality
                our_pick = resulting_subtours[0]
            else:
                pick resulting_subtours[0]
            cand = dissolve the subtour into edges
            create children
            generate their names/variables
            add each one of them 1 unique edge from cand and from their parent's exclude to child's exclude
            add your resulting include to them


            
            
        tours
    """

  
    """
    include = []
    exclude = []
    cand = []
    A1 = Node("A1", weight = assignment_hungarian(named_matrix, names, matrix, include, exclude, cand)[1])
    A/B/D/C

    A2 = Node("A2", parent = A1, weight = assignment_hungarian(named_matrix, names, matrix, include, exclude, cand)[1])
    """

def DFBnB_zk_algorithm():
    ...
 
