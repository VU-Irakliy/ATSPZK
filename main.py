from searchbound import *
     
points = []
nodes = []
# Start = Node('A', weight=0)


# def make_tree(lost_parent, temp_points, r, names, flag): ####MULTITHREADING REQUIRED HERE MAYBE? NO
#     # print(temp_points[0])
#     if (temp_points[0] == 'A') & flag: 
#         # print("gav")
#         return
#     else:
#         for i in range(len(temp_points[1])):
#             # print(names)
#             if(temp_points[1][i] != 0) and (r[i] == 0) and (names[i] != 'A' or sum(r) == len(names) - 1):
#                 t = Node(names[i], parent=lost_parent, weight=temp_points[1][i])
#                 nodes.append(t)
#                 # print('meow', i)
#                 # print('mmmm',temp_points[1])
#                 # return
#                 s = r.copy()
#                 s[i] = 1
#                 make_tree(t, points[i], s, names, True)



def read_matr(filename, input):
#    nodes.append("A", weight=0)
    try:
        f = open(filename)
    except:
        print("Error: The file doesn't exist in the directory of the program")
        exit()
    names = f.readline().split()
    for i in range(len(names)):
        s = f.readline().split()
        ch = []
        for j in range(len(s)):
            # if j != i:
            ch.append(int(s[j]))
            # else:
            #     ch.append(0)
        points.append((names[i], ch))
        # matrix.append((names[i], ch))
    f.close()
    # print(points)
    r = [0] * len(points)
    # print(points[0], r)
    # if input == 1 or input == 2:
    #     if len(names) <= 10:
    #         make_tree(Start, points[0], r, names, False)
    #     else: 
    #         print('Please, choose ZK algorithm.')
    #         exit()


#WHEN WHICH ALGORITHM IS USED
#DFBNB IN ZHANG N KORF ALGORITHM IS USED WHEN THERE ARE A LOT OF INSTANCES AKA A LOT OF CITIES 
# (COMPARE TIME OF BOTH BFS AND DFBNB IN ZK ALGORITHM) 
def execute_the_algorithm(named_matrix, names, matrix, input):
    matrix = np.array(matrix)
    print(matrix)
    if input == 1:
        if len(matrix) <= 30:

            minimum = 0
            temp_minimum = 0
            used_rows = []
            starting_point = 0
            result = depthFirstBranchAndBound(matrix, minimum, temp_minimum, used_rows, starting_point)
            print("Result of Depth-First Branch-and-Bound: ")
            print(result)
        else:
            print('This is dangerous')
        # print(result[1])
        
    elif input == 2:
        minimum = 0
        
        result = bestFirstSearch(matrix)
        print("Result of Best-First Search: ")
        print("Minimum Branch: ",result[0])
        print("Minimum Cost: ", result[1])
    
    
    else: 
        #len(names) > ....:
            #DFBnB version
        #else:
            #BFS version
        result = start_ZK_algorithm(named_matrix, names, matrix)
        print(result)



#START MAIN
def main():
    # something = list(set((0,1,2,4)))
    # there = [[False,True,False,True,False,True,True,True,True,False],[False,True,2,True,False,True,True,True,True,False],
    # [False,True,False,True,1,True,True,True,True,False],
    # [False,True,False,True,3,True,True,True,True,False],
    # [False,True,False,True,False,True,True,True,True,False],[False,True,False,True,False,True,True,True,True,False]]
    # hi = there[something[2]]
    # print(hi)

    filename = 'matr100/matr3.txt' #100 nodes
    # filename = 'matr2a.txt'  #15 nodes [0, 8, 1, 7, 4, 12, 5, 13, 6, 2, 11, 14, 3, 10, 9, 0]
    # filename = 'matr2aaa.txt'
    # filename = 'matr3.txt' # 7 nodes
    # filename = 'matr1aa.txt' # 10 nodes
    # filename = 'matr3.txt'
    # filename = input("Enter the name of the file (e.g. example.txt). The matrix has to have first Node as A: ")
    if filename == 'exit':
        print('Program has exited.')
        exit()
    
    al_input = 3  #look at the line below
    # al_input = int(input("Which algorithm? (1-DFBnB, 2-BFS, any - ZK): "))
    
    read_matr(filename, al_input)
    print("The matrix has been created!")
    # if al_input == 1 or al_input == 2: 
    #     print("The tree has been created!")

    # print(nodes)
    # print(points)
    named_points = points.copy()
    matrix_points = []
    names = []
    for i in named_points:
        names.append(i[0])
        matrix_points.append(i[1])
    
    for i in matrix_points:
        # print(i)
        for j in range(0, len(i)):
            # print(j)
            if i[j] == 0:
                i[j] = math.nan
    
    #KEEP THESE COMMENTS
    # print(int(np.nanmin(matrix_points)))
    # print(RenderTree(Start, style=ContStyle()))
    # print(matrix_points)
    
    
   
    execute_the_algorithm(named_points, names, matrix_points, al_input)
    
   

main()
