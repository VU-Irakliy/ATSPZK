from algorithm import *

def main():
    hello = int(input('Would you like to run it a matrix or do an experiment? (0 - matrix, 1 - my my,any - experiment) \n'))

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
        al_input = 3
        method = 2
        result = start(filename, al_input, method)
       
        # exit()
        method = 1
        result_2 = start(filename, al_input, method)
        print(result)
        print(result_2)

        # folder = 
        ...
    else:
        method = int(input('Which method of ZK algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n any - Best-First Search\n Type here: '))
        cities = input('How many cities? \n 100, 200, 300, 400, 500 \n')
        results = []
        times = []
        for i in range(1, 101):
            filename = 'matr' + cities + '/matr' + str(i) + '.txt'
            result, time = start(filename, 3, method) #here we should capture time and a result, then store them for the sake of the presentation
            results.append([i, result])
            times.append([i, time])
        ####https://docs-python.ru/standart-library/modul-datetime-python/klass-timedelta-modulja-datetime/
        
        print(results)
        print(time)






main()
