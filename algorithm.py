from searchbound import *
from datetime import datetime as dt

def read_matr(filename, points):
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
            ch.append(int(s[j]))
            
        points.append((names[i], ch))
    f.close()
   

def execute_the_algorithm(named_matrix, names, matrix, input, method):
    matrix = np.array(matrix)
    print(matrix)
    if input == 1:
        
        minimum = 0
        temp_minimum = 0
        used_rows = []
        starting_point = 0
        result = depthFirstBranchAndBound(matrix, minimum, temp_minimum, used_rows, starting_point)
        print("Result of Depth-First Branch-and-Bound: ")
        print(result, '\n')
        return result
        
        
    elif input == 2:
        minimum = 0
        
        result = bestFirstSearch(matrix)
        print("Result of Best-First Search: ")
        print("Minimum Branch: ",result[0])
        print("Minimum Cost: ", result[1], '\n')
        return result[1]
    
    
    else: 
        
        result = start_ZK_algorithm(named_matrix, names, matrix, method)
        print(result, '\n')
        return result



#START MAIN
def start(filename, al_input, method):
 
    # filename = 'matr100/matr3.txt' #100 nodes
    # filename = 'matr2a.txt'  #15 nodes [0, 8, 1, 7, 4, 12, 5, 13, 6, 2, 11, 14, 3, 10, 9, 0]
    # # filename = 'matr2aaa.txt'
    # # filename = 'matr3.txt' # 7 nodes
    # filename = 'matr1aa.txt' # 10 nodes
    # filename = 'matr3.txt'
    # filename = input("Enter the name of the file (e.g. example.txt). The matrix has to have first Node as A: ")
    if filename == 'exit':
        print('Program has exited.')
        exit()
    points = []
    nodes = []
    read_matr(filename, points)
    print("The matrix has been created!")
    
    


    named_points = points.copy()
    matrix_points = []
    names = []
    for i in named_points:
        names.append(i[0])
        matrix_points.append(i[1])
    
    for i in matrix_points:
        for j in range(0, len(i)):
            if i[j] == 0:
                i[j] = math.nan
    # Start
    start_time = dt.now()
    result = execute_the_algorithm(named_points, names, matrix_points, al_input, method)
    end_time = dt.now()
    #End
    difference = end_time - start_time
    return result, difference
    #return ( end_time - start_time   or total_time (if took longer than other algorithm))
    
   
# filename = 'matr1a.txt'
# start(filename, 2, 0)
