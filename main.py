from algorithm import *

def main():
    hello = int(input('Would you like to run it a matrix or do an experiment? (0 - matrix, any - experiment) \n'))

    if hello == 0:
        filename = input('Which matrix? (Filename has to end with .txt) \n')
        al_input = int(input("Which algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n 2 - Best-First Search \n any - Zhang & Korf's Algorithm\n Type here: "))
        if al_input == 2 or al_input == 1:
            method = 0
        else:
            method = int(input('Which method of ZK algorithm would you like to test? \n 1 - Depth-First Branch and Bound \n any - Best-First Search\n Type here: '))
        start(filename, al_input, method)
    else:
        filename = 'matr2aaa.txt'
        al_input = 3
        method = 2
        start(filename, al_input, method)
        method = 1
        start(filename, al_input, method)

        # folder = 
        ...




main()
