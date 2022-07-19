from searchbound import *
     
points = []
nodes = []

def read_matr(filename):
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
        
    elif input == 2:
        minimum = 0
        
        result = bestFirstSearch(matrix)
        print("Result of Best-First Search: ")
        print("Minimum Branch: ",result[0])
        print("Minimum Cost: ", result[1])
    
    
    else: 
        
        result = start_ZK_algorithm(named_matrix, names, matrix, method)
        print(result)



#START MAIN
def main():
 
    # filename = 'matr100/matr3.txt' #100 nodes
    filename = 'matr2a.txt'  #15 nodes [0, 8, 1, 7, 4, 12, 5, 13, 6, 2, 11, 14, 3, 10, 9, 0]
    # filename = 'matr2aaa.txt'
    # filename = 'matr3.txt' # 7 nodes
    # filename = 'matr1aa.txt' # 10 nodes
    # filename = 'matr3.txt'
    # filename = input("Enter the name of the file (e.g. example.txt). The matrix has to have first Node as A: ")
    if filename == 'exit':
        print('Program has exited.')
        exit()
    read_matr(filename)
    print("The matrix has been created!")
    al_input = 2  
    method = 2
    # al_input = int(input("Which algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n 2 - Best-First Search \n any - Zhang & Korf's Algorithm"))
    # if al_input == 2 or al_input == 1:
    #     method = 0
    # else:
    #     method = int(input('Which method of ZK algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n any - Best-First Search'))


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
   
    execute_the_algorithm(named_points, names, matrix_points, al_input, method)
    
   

main()
