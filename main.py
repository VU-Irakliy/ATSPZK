from algorithm import *

def main():
    print("Remember, all input that have a number mentioned as input, accepts only numbers as input")
    hello = int(input('Would you like to run it a matrix or do an experiment? (0 - matrix, 1 - demo for file creation, any - experiment) \n '))

    if hello == 0:
        filename = input('Which matrix? (Filename has to end with .txt) \n')
        al_input = int(input("Which algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n 2 - Best-First Search \n any - Zhang & Korf's Algorithm\n Type here: "))
        if al_input == 2 or al_input == 1:
            method = 0
        else:
            method = int(input('Which method of ZK algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n any - Best-First Search\n Type here: '))
        start(filename, al_input, method)
    elif hello == 1:
        filename = 'matr2aaa.txt' ## 30 NODES
        # filename = 'matr3.txt'
        testie = 'test'
        f = 'results' + testie
        m = open(f, 'w')
      
        
        
        al_input = 3
        method = 2
        result = start(filename, al_input, method)
       
        # # exit()
        method = 1
        result_2 = start(filename, al_input, method)
        # print(result)
        # print(result_2)
        um = input("Type something here: ")
        m.write('Testing \n')
        m.write("BFS \n" + str(result) + "\nDFBnB \n" + str(result_2) + "\n That's all, folks." + um)


        # folder = 
        m.close()
        ...
    else:
        # method = int(input('Which method of ZK algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n any - Best-First Search\n Type here: '))
        cities = input('How many cities? \n 100, 200, 300, 400, 500 \n')
        # um = int(input('Do you have your results.txt file ready? 1 - Yes'))
        results_dfbnb = []
        times_dfbnb = []
        results_bfs = []
        times_bfs = []
        j = 1
        # if um == 1:
        for r in range(1, 1001, j):
            
            filename = 'matr' + cities + '/matr' + str(r) + '.txt'
            print(r)
            result_d, time_d = start(filename, 3, 1) #here we should capture time and a result, then store them for the sake of the presentation
            results_dfbnb.append([r, result_d])
            times_dfbnb.append([r, time_d])
            result, time = start(filename, 3, 2) #here we should capture time and a result, then store them for the sake of the presentation
            results_bfs.append([r, result])
            times_bfs.append([r, time])
            if r == 20:
                j = 5
            elif r == 100:
                j = 10 
        ####https://docs-python.ru/standart-library/modul-datetime-python/klass-timedelta-modulja-datetime/
        print('DFBnB')
        print(results_dfbnb)
        print(times_dfbnb)
        print('BFS')
        print(results_bfs)
        print(times_bfs)

        f = 'results_'+ cities + '.txt'

        m = open(f, 'w')
        m.write("Result of ATSP with matrices with the size of " + cities + '!\n')
        m.write("DFBnB\n" + str(results_dfbnb) + "\n" + str(times_dfbnb) + "\n")
        m.write("BFS\n" + str(results_bfs) + "\n" + str(times_bfs) + "\n")
        
        m.close()




# r= 5, 10, 20, 100, 130, 


main()
