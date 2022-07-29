from algorithm import *

def main():
    print("Remember, all input that have a number mentioned as input, accepts only numbers as input")
    hello = int(input('Would you like to run it a matrix or do an experiment? (0 - matrix, 1 - demo for experiment,\n 2 - BFS and DFBnB experiment, 3 - experiment with all algorithms \n any - ZK experiment) \n '))

    if hello == 0:
        filename = input('Which matrix? (Filename has to end with .txt) \n')
        al_input = int(input("Which algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n 2 - Best-First Search \n any - Zhang & Korf's Algorithm\n Type here: "))
        if al_input == 2 or al_input == 1:
            method = 0
        else:
            method = int(input('Which method of ZK algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n any - Best-First Search\n Type here: '))
        start(filename, al_input, method)
        
    elif hello == 1:
        filename = input('Which File? (.txt): ')
        # filename = 'matr100/matr40.txt'
        # filename = 'matr2aaa.txt' ## 30 NODES
        # filename = 'matr3.txt'
        testie = 'test'
        f = 'results' + testie
        m = open(f, 'w')
      
        ####### METHOD 1: DFBNB, METHOD 2: BFS
        
        al_input = 3
       
        # while i != 10:
        method = 1
        result= start(filename, al_input, method)
        print('DFBnB ',result)
        # # exit()
        method = 2
        result_2= start(filename, al_input, method)
        print('BFS ',result_2)
        
        
        
        # um = input("Type something here: ")
        # m.write('Testing \n')
        # m.write("DFBnB \n" + str(result) + "\nBFS \n" + str(result_2) + "\n That's all, folks." + um)


        # # folder = 
        # m.close()
        ...
    elif hello == 2: #REGULAR BFS AND DFBNB EXPERIMENT
        cities = input('How many cities? \n 100, 200, 300, 400, 500 \n')
        results_dfbnb = []
        times_dfbnb = []
        results_bfs = []
        times_bfs = []
        
        # if um == 1:
        for r in range(1, 21):
            
            filename = 'matr' + cities + '/matr' + str(r) + '.txt'
            result_df, time_df = start(filename, 1, 1)
            result_bf, time_bf = start(filename, 2, 1)
            results_dfbnb.append([r, result_df])
            times_dfbnb.append([r, time_df])
            results_bfs.append([r, result_bf])
            times_bfs.append([r, time_bf])
        
        f = 'REG_results_'+ cities + 'r' + str(r) + '.txt'

        m = open(f, 'w')
        m.write("Result of ATSP with matrices with the size of " + cities + '!\n')
        m.write("Regular \nDFBnB\n" + str(results_dfbnb) + "\n" + str(times_dfbnb) + "\n")
        m.write("BFS\n" + str(results_bfs) + "\n" + str(times_bfs) + "\n")
        
        m.close()
        
        ...
    elif hello == 3:
        cities = input("How many cities? ")
        prev = int(input("From which r value to start from? 1, 25, 150? "))
        results_dfbnb = []
        times_dfbnb = []
        results_bfs = []
        times_bfs = []
        zkresults_dfbnb = []
        zktimes_dfbnb = []
        zkresults_bfs = []
        zktimes_bfs = []
        end = 0
        step = 1
        if prev >= 1 and prev <= 20:
            end =  21
        elif prev == 25:
            end = 131
            step = 5
        elif prev == 150:
            end = 999
            step = 50

        for r in range(prev, end, step):
            filename = 'matr' + cities + '/matr' + str(r) + '.txt'
            result_df, time_df = start(filename, 1, 1)
            result_bf, time_bf = start(filename, 2, 1)
            results_dfbnb.append([r, result_df])
            times_dfbnb.append([r, time_df])
            results_bfs.append([r, result_bf])
            times_bfs.append([r, time_bf])

            result_d, time_d, without_d = start(filename, 3, 1)
            result, time, without = start(filename, 3, 2)
            zkresults_dfbnb.append([r, result_d])
            zktimes_dfbnb.append([r, time_d])
            zkresults_bfs.append([r, result])
            zktimes_bfs.append([r, time])
        f = 'ALL_results_'+ cities + 'r' + '20' + '.txt'
        m = open(f, 'w')
        m.write("Result of ATSP with matrices with the size of " + cities + '!\n')
        m.write("Regular \nDFBnB\n" + str(results_dfbnb) + "\n" + str(times_dfbnb) + "\n")
        m.write("BFS\n" + str(results_bfs) + "\n" + str(times_bfs) + "\n")
        m.write("ZK \nDFBnB\n" + str(zkresults_dfbnb) + "\n" + str(zktimes_dfbnb) + "\n")
        m.write("BFS\n" + str(zkresults_bfs) + "\n" + str(zktimes_bfs) + "\n")

        
        m.close()
            

        ...
    else:
        # method = int(input('Which method of ZK algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n any - Best-First Search\n Type here: '))
        cities = input('How many cities? \n 100, 200, 300, 400, 500 \n')
        prev = int(input('What was the previous r value finished? '))
        
        if prev == 0:
            prev = 1
        elif prev == 20:
            prev = 25
        elif prev == 130:
            prev = 150
        # um = int(input('Do you have your results.txt file ready? 1 - Yes'))
        results_dfbnb = []
        times_dfbnb = []
        results_bfs = []
        times_bfs = []
        
        if prev == 1:
            for r in range(prev, 21):
                
                filename = 'matr' + cities + '/matr' + str(r) + '.txt'
                print(r)
                result_d, time_d, without_d = start(filename, 3, 1) #here we should capture time and a result, then store them for the sake of the presentation
                
                if without_d == True:
                    results_dfbnb.append([r, result_d])
                    times_dfbnb.append([r, time_d])
                    print("Since it didn't reach BnB, we give the same time and result to BFS variation \n \n")
                    results_bfs.append([r, result_d])
                    times_bfs.append([r, time_d])
                else:
                    result, time, without = start(filename, 3, 2) #here we should capture time and a result, then store them for the sake of the presentation
                    if without == True:
                        print("Since it didn't reach BnB, we give the same time and result to DFBnB variation as well \n \n")
                        results_dfbnb.append([r, result])
                        times_dfbnb.append([r, time])
                        results_bfs.append([r, result])
                        times_bfs.append([r, time])
                    else:
                        results_dfbnb.append([r, result_d])
                        times_dfbnb.append([r, time_d])
                        results_bfs.append([r, result])
                        times_bfs.append([r, time])
                
            print('DFBnB')
            print(results_dfbnb)
            print(times_dfbnb)
            print('BFS')
            print(results_bfs)
            print(times_bfs)

            f = 'ZK_results_'+ cities + 'r' + '20' + '.txt'

            m = open(f, 'w')
            m.write("Result of ATSP with matrices with the size of " + cities + '!\n')
            m.write("ZK \nDFBnB\n" + str(results_dfbnb) + "\n" + str(times_dfbnb) + "\n")
            m.write("BFS\n" + str(results_bfs) + "\n" + str(times_bfs) + "\n")
            
            m.close()
            prev = 25
            results_dfbnb = []
            times_dfbnb = []
            results_bfs = []
            times_bfs = []

        if prev == 25:
            for r in range(prev, 131, 5):
                
                filename = 'matr' + cities + '/matr' + str(r) + '.txt'
                print(r)
                result_d, time_d, without_d = start(filename, 3, 1) #here we should capture time and a result, then store them for the sake of the presentation
                
                if without_d == True:
                    results_dfbnb.append([r, result_d])
                    times_dfbnb.append([r, time_d])
                    print("Since it didn't reach BnB, we give the same time and result to BFS variation \n \n")
                    results_bfs.append([r, result_d])
                    times_bfs.append([r, time_d])
                else:
                    result, time, without = start(filename, 3, 2) #here we should capture time and a result, then store them for the sake of the presentation
                    if without == True:
                        print("Since it didn't reach BnB, we give the same time and result to DFBnB variation as well \n \n")
                        results_dfbnb.append([r, result])
                        times_dfbnb.append([r, time])
                        results_bfs.append([r, result])
                        times_bfs.append([r, time])
                    else:
                        results_dfbnb.append([r, result_d])
                        times_dfbnb.append([r, time_d])
                        results_bfs.append([r, result])
                        times_bfs.append([r, time])
                
            print('DFBnB')
            print(results_dfbnb)
            print(times_dfbnb)
            print('BFS')
            print(results_bfs)
            print(times_bfs)

            f = 'ZK_results_'+ cities + 'r' + '130' + '.txt'

            m = open(f, 'w')
            m.write("Result of ATSP with matrices with the size of " + cities + '!\n')
            m.write("ZK \nDFBnB\n" + str(results_dfbnb) + "\n" + str(times_dfbnb) + "\n")
            m.write("BFS\n" + str(results_bfs) + "\n" + str(times_bfs) + "\n")
            
            m.close()
            prev = 150
            results_dfbnb = []
            times_dfbnb = []
            results_bfs = []
            times_bfs = []
            # print(results_dfbnb)
            # print(results_bfs)
        if prev == 150:
            for r in range(prev, 999, 50): ####
                
                filename = 'matr' + cities + '/matr' + str(r) + '.txt'
                print(r)
                result_d, time_d, without_d = start(filename, 3, 1) #here we should capture time and a result, then store them for the sake of the presentation
                
                if without_d == True:
                    results_dfbnb.append([r, result_d])
                    times_dfbnb.append([r, time_d])
                    print("Since it didn't reach BnB, we give the same time and result to BFS variation \n \n")
                    results_bfs.append([r, result_d])
                    times_bfs.append([r, time_d])
                else:
                    result, time, without = start(filename, 3, 2) #here we should capture time and a result, then store them for the sake of the presentation
                    if without == True:
                        print("Since it didn't reach BnB, we give the same time and result to DFBnB variation as well \n \n")
                        results_dfbnb.append([r, result])
                        times_dfbnb.append([r, time])
                        results_bfs.append([r, result])
                        times_bfs.append([r, time])
                    else:
                        results_dfbnb.append([r, result_d])
                        times_dfbnb.append([r, time_d])
                        results_bfs.append([r, result])
                        times_bfs.append([r, time])
                
            print('DFBnB')
            print(results_dfbnb)
            print(times_dfbnb)
            print('BFS')
            print(results_bfs)
            print(times_bfs)

            f = 'ZK_results_'+ cities + 'r' + '1000' + '.txt'

            m = open(f, 'w')
            m.write("Result of ATSP with matrices with the size of " + cities + '!\n')
            m.write("ZK \nDFBnB\n" + str(results_dfbnb) + "\n" + str(times_dfbnb) + "\n")
            m.write("BFS\n" + str(results_bfs) + "\n" + str(times_bfs) + "\n")
            
            m.close()
            results_dfbnb = []
            times_dfbnb = []
            results_bfs = []
            times_bfs = []
            # print(results_dfbnb)
            # print(results_bfs)
            
        ####https://docs-python.ru/standart-library/modul-datetime-python/klass-timedelta-modulja-datetime/
 




# r= 5, 10, 20, 100, 130, 


main()
