from searchbound import *
from datetime import datetime as dt

##USED TO BE CALLED algorithm.py

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
    # print(matrix)
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
        
        result, without = start_ZK_algorithm(named_matrix, names, matrix, method)
        print(result, '\n')
        return result, without



#START MAIN
def start(filename, al_input, method):
 

    # if filename == 'exit':
    #     print('Program has exited.')
    #     exit()
    points = []
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
    # Start time
    start_time = dt.now()
    if al_input != 1 and al_input != 2:
        
        result, without = execute_the_algorithm(named_points, names, matrix_points, al_input, method)
        end_time = dt.now()
        #End time
        difference = end_time - start_time
        print('Time it took (in seconds):', difference.seconds)
        return result, difference.seconds, without
    else:
        result = execute_the_algorithm(named_points, names, matrix_points, al_input, method)
        end_time = dt.now()
        #End time
        difference = end_time - start_time
        print('Time it took (in seconds):', difference.seconds, '\n')
        return result, difference.seconds
    
