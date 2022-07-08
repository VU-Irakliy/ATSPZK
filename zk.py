from assignment import *

'''THIS ONE USES BOTH...'''
#this will also have a division of BFS and DFBnB
def start_ZK_algorithm(named_matrix, names, matrix):
    
    # cand = []
    empty = [] #for the first run only
    
    curr_result = assignment_hungarian(named_matrix, names, matrix, empty, empty)
    Start = Node("Start", weight = curr_result[1])
    
    # print('Min total', min_total)
    nodes = [(x[0], x[1]) for x in curr_result[0]]
    print(nodes)
    list_of_coords = make_tours(names, curr_result[0])
    # print(len_of_tours)

    print("CHRIS IS BAKA")
    if len(list_of_coords) == 1: ###IF WE ONLY HAVE 1 SUBTOUR/COMPLETE TOUR
        cost = 0
        for list in list_of_coords:
            for coord in list:
                cost += matrix[coord[0]][coord[1]]
        return cost

    print('HAA!')
    min_total = curr_result[1]
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

    if len(nodes) >= 1000:  ##DFBnB
        include = []
        exclude = []        
        ...
        # for i in cand:
        #     exclude.append(i)
        #     zk_algorithm
        #     exclude = []
    else: #BFS

        result = BFS_zk_algorithm(named_matrix, names, matrix, cand, Start, min_total)
        return result
        

            
        # print(assignment_hungarian(named_matrix, names, matrix, include, exclude))
        # A2 = Node("A2", parent = A1, weight = assignment_hungarian(named_matrix, names, matrix, include, exclude, cand)[1])
        # for i in cand:
        #     exclude.append(i)
        #     BFS_zk_algorithm
        #     exclude = []
    # if len(include) != 0:    THIS IS FOR THE OTHER FUNCTION
                    
            
def BFS_zk_algorithm(named_matrix, names, matrix, cand, Start, min_total): #IF COMPLETE TOUR, THEN RETURN MINIMUM COST AND WE'RE DONE
    print('WELL CUM')
    priority_queue = []
    inc_excludes = []
    used_nums = []
    for i in range(len(cand)):
        exclude = []
        include = []
        bran = 'A' + str(i)
        exclude.append(cand[i])
        curr = assignment_hungarian(named_matrix, names, matrix, include, exclude)
        ##THEY HAVE INCLUDE. ADD THEM.
        print('MINININI', curr[1])
        include = get_include(names, curr, cand)
        inc_excludes.append([exclude, include, curr[1]])
        # exclude = []
        valu = Node(bran, parent = Start, weight = curr[1])
        priority_queue.append([valu, curr[0], curr[1]])
        used_nums.append(i)
    ##[]
    exclude = []
    include = []
    inc_excludes = sorted(inc_excludes, key= lambda x: x[2]) ### x[0] - EXCLUDE, x[1] - INCLUDE, x[2] - WEIGHT 
    print(inc_excludes)
    min_not_found = True
    priority_queue = sorted(priority_queue, key= lambda x: x[2])
    #[[Node('/Start/A1', weight=13), 13], [Node('/Start/A2', weight=14), 14], 
    # [Node('/Start/A0', weight=15), 15]]
    #valu = Node(bran, parent = closed[-1], weight = curr[1])
    # priority_queue = sorted(priority_queue, key= lambda x: x[2])
    #closed[[Node, cand], [Node, cand], [Node, cand], [Node, cand]]
    print(priority_queue)
    closed_priority = []
    closed_additions = [] #include and exclude
    i = 0
    while min_not_found:
        if min_not_found == False:
            break
        else:
            temps_prio = priority_queue.pop(0)
            temp_branch, temp_paths, temp_weight = temps_prio
            temps_ie = inc_excludes.pop(0)
            temp_exc =  temps_ie[0]
            temp_inc = temps_ie[1]

            closed_priority.append(temps_prio)
            closed_additions.append(temps_ie)

            tours = make_tours(names, temp_paths)
            if len(tours) == 1:
                cost = 0
                for list in tours:
                    for coord in list:
                        cost += matrix[coord[0]][coord[1]]
                return cost
            

            #
            ...
            # BFS_zk_algorithm(named_matrix, names, matrix, 
            #             include, exclude, cand, priority_queue, min_not_found) #can min_not_found from this func influence one here????
                        ##IF NO, then we should return it
                        #WE ALSO HAVE TO PUT THE ONES THAT WE DID ON CLOSED, SO WE CAN FOCUS ON NEW ONES ON PRIORITY QUEUE
        
        if min_not_found == False:
            break


def DFBnB_zk_algorithm():
    ...
 

def get_include(names, curr_result, cand):
    nodes = [(x[0], x[1]) for x in curr_result[0]]
    print('Candidates', cand) #A -0, G - 6  [B, E] [E,F] [F,B] [[1, 4], [4, 5], [5, 1]]
    print('Nodes ',nodes)
    coords = []
    for j in nodes:
        temp = []
        for l in j:
            for i in range(len(names)):
                if names[i] == l:
                    temp.append(i)
        coords.append(temp)
    # print(coords)
    include =[]
    for i in cand:
        
        for j in coords:
            if i == j:
                print('i',i)
                print('j', j)
                include.append(i)
    return include


def make_tours(names, curr_nodes): ##curr[0]
    nodes = [(x[0], x[1]) for x in curr_nodes]
    print(nodes)
    coords = []
    for j in nodes:
        temp = []
        for l in j:
            for i in range(len(names)):
                if names[i] == l:
                    temp.append(i)
        coords.append(temp)
    # print(coords)
    # print('YAHPPPPP')
    tours = []
    # list_of_tours = []
    used_nodes = [] ###use a map
#     used_nodes = new Map()

# used_nodes.put(node[node], 1/0/TRUE/FALSE);
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
                                if nodes[m] not in used_nodes: #what about deleting it?
                                    # if node[node] in used_nodes -> NO
                                    #     USE:
                                    #     used_nodes.get(node[node]): 
                                    #     #do stuff
                                    tours.append([nodes[m][0], nodes[m][1]])
                                    used_nodes.append(nodes[m])
                                    list_of_coords.append([coords[m]])
                                    # list_of_tours.append([nodes[m]])
                                    flag = False
                                    break
                        if flag == False:
                            break
    return list_of_coords