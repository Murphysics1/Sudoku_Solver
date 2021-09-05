# -*- coding: utf-8 -*-

def view_grid(grid_space):
    
    for row in range(len(grid_space)):
        for column in range(len(grid_space[0])):
            print (grid_space[row][column],end = ' '),
            if column == 2 or column == 5:
                print('|', end=' ')
        if row == 2 or row == 5:
            print('')
            print('-'*6+"+"+'-'*7+"+"+'-'*7,end ='')
        print ('')
        
#check to see if an input would be valid
#check row, column, and square



def valid_input(guess,loc,grid_space):
    
    #loc is a tuple returned from the zero_loc function
    #row id-> loc[0] ; column id -> loc[1]
    
    #check row
    for num in range(len(grid_space)):
        if guess == grid_space[loc[0]][num]:
            return False
    
    #check column
    for num in range(len(grid_space[0])):
        if guess == grid_space[num][loc[1]]:
            return False
   
    #check square
    #I dont like the square check, there should be a cleaner way, but it works
    
    
    #this will slow down the algorithm
    subsquare_elements =[]
    
    #creates the list for the items in each subsquare
    #map is above 
    for row in range(len(grid_space)):
        if loc[0]//3 == row//3:
            for column in range(len(grid_space[0])):
                if column//3 == loc[1]//3:
                    subsquare_elements.append(grid_space[row][column])
                    
    #if the item is in the list, then it is in the subsquare       
    if guess in subsquare_elements:
        return False
    
    #if its not in the row, column, or susquare, then it is a valid input
    return True



def zero_loc(grid_space):
    
    for row in range(len(grid_space)):
        for col in range(len(grid_space[0])):
            if grid_space[row][col] == 0:
                return (row,col)
    
    return False



def solve(grid_space):
    
    #if there are no zeros:
    if zero_loc(grid_space) == False:
        #then the puzzle is soved
        return True
    
    #otherwise, move into the solving algorithm
    else:
        #unpack the tuple
        row,col = zero_loc(grid_space)
        #start trying #1-9
        for guess in range(1,len(grid_space)+1):
            if valid_input(guess,(row,col),grid_space):
                #if a valid number is found, replace it in the grid
                grid_space[row][col] = guess
                
                #call this function again and see if it is True(solved)
                if solve(grid_space):
                    return True
                
                #if not then reset and move onto the next value in the guess for loop
                grid_space[row][col] = 0

if __name__ == "__main__":
    print('NO')
