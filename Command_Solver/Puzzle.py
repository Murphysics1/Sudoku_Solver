# -*- coding: utf-8 -*-
def puzzle():

    mypuzzle = []
    mylist =[]
    
    row = input('Enter the values for row 1: ')
    
    for num in row:
        mylist.append(int(num))
    
    mypuzzle.append(mylist)
    mylist = []
    
    for i in range(2,len(row)+1):
    
        row = input(f'Enter the values for row {i}: ')
        
        for num in row:
            mylist.append(int(num))
            
        mypuzzle.append(mylist)
        mylist = []

    return mypuzzle

if __name__ == '__main__':
    print('NO')
    
    