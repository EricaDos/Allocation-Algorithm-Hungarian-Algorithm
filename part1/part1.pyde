import sys # Allows the sys module to be used to allow me to find the minimum number 
def setup():
    
    countr = 0 #Defult counts for the number of zeros in a row
    countv = 0#Defult counts for the number of zeros in a row
    smallest = 0 #Setting a default value for the variable
    matrix = [] #An array for the where the file will be imported to

    
    size (500,500) #Sets the size of the canvas
    fill(0)
    text("Minimisation Part 1",80,20,80) #Prints the title of the hungarian algorithm
    text("Minimisation Part 2", 280,20,280)
    originalfile = open("part1.txt","r") #Opens the file of the table being used 
    linelist = originalfile.readline() #Reads the next line in the file

    for aline in originalfile: # Creating a for loop that will reitweate over each line of the file
        originalmatrix = aline.split() #Splits the file to allow be split into a list - therefore making it easier to be able to locate a sinle element in the list
        linelist = originalfile.readline #Assigns each line to line list
        originalmatrix = [int(i) for i in originalmatrix] #Changes the string elements in the list to integers
                #Also a form of list comprehension of a for loop to change every element in the matrix will be changed into an integer

        matrix.append(originalmatrix) #Add the contents from the file into a variable array called row. 

    for i in matrix: 
        print(i) #Prints out the original table before deduction are made

    
    originalfile.close() #Closes the file as it doesnt need to be importedx anymore
    
        
    for i in range(0,len(matrix)): #Loop which iterates through the 
        smallest = min(matrix[i]) #Calculates the minimum number of each element in the lines
        for x in range(0,len(matrix[0])):#Checks every element in the row
            matrix[i][x] -= smallest #Assigns the smallest number to the variable name
    
    for i in range(0,len(matrix)): #Iterates over the range of the matrix which is a 4x4
        minimum = sys.maxsize #Defult value which is the largest supported value in python
        for z in range(0,len(matrix[0])):#For loop which will go through the rows of the file
            if matrix[z][i] < minimum: #Replaces the minimum variable with the smallest integer in the file
                minimum = matrix[z][i] #Assigning the new value of minimum
            
        for x in range(0,len(matrix[0])): #For loop which looks for the columns
            matrix[x][i] -= minimum #Assigns the new value of minimum
        

    delcol = 50 #Default colum location
    margin = 10  #The margin around the size of the display where the location of the matrix will be 
    delrow = 50 # distance between rows
    y = margin
    for i in range(14):
        line(margin, y,width-margin,y) #Draw horizontal lines
        y = y + delrow
    discol = 50 #The distance in between each element
    x = margin #Assigns x to the margin
    for i in range(14): #Iterates over 14
        line(x,margin,x,height-margin) #Draws the verticle lines
        x = x + discol
       
    for i in range(0,len(matrix)): #Iterates the whole row in the matrix
        for j in range(0,len(matrix)):  #Iterates the each element in the row
            fill(0) #Black text
            text(matrix[i][j],(j * delrow) + 20, (i * delcol) + 40 )
            if matrix[i][j] != 10: #Checks that its not 10 as 10 contains 0 and it would locate it
                if matrix[i][j] == 0: #Checks for the 0's in the matrix
                    countr = countr + 1 #Counts the number of zeros in the row
                    i_ = i * delcol + 50 #This is variable which will be able to display the location of the elements my magnifing it with the size of the canvas therefore the cooridnates will be accessible and in range
                    j_ = j * delrow + 45
                    stroke(255,50,50) #The RGB colour 
                
                    point(j_,i_-10) #The location of each zero in the array
                    if countr == 2: #The number of zeros displayed on that row and colum to know where to add the line
                        stroke(255,0,0)
                        line(margin+5,j_,200,j_) #The line
                        line(margin+5,i_,200,i_) #The line
                if matrix[j][i] == 0:
                    countv = countv + 1 #Counts the amount of verticle zeros
                    if countv == 3: #Checks to see if there's 3 zero's vertically
                        stroke(255,0,0)
                        line(j_-10,200,j_-10,margin+20)
    for a in range(0,len(matrix)):
        for b in range(0,len(matrix)):
            a_ = a * delcol + 280 
            b_ = b * delrow + 45
            
            #Adds at the intersections +1
            if matrix[0][3] == 4:
                matrix[0][3] += 1
            if matrix[2][3] == 0:
                matrix[2][3] += 1
                
            #Minimisation process
            if matrix[1][0] == 1:
                matrix[1][0]-=1
            if matrix[1][1] == 2:
                matrix[1][1] -= 1
            if matrix[1][2] == 8:
                matrix[1][2] -= 1
                
            if matrix[3][0] == 1:
                matrix[3][0]-=1
            if matrix[3][1] == 5:
                matrix[3][1] -= 1
            if matrix[3][2] == 10:
                matrix[3][2] -= 1
            if matrix[b][a] == 0:
                stroke(255,50,50) #The RGB colour 
                point(a_,b_) #The location of each zero in the array
                line(margin+450,a_-240,260,a_-240)
            text(matrix[a][b],( b *delrow) + margin + 260,(a *delcol)+margin + 30)
        
            
    noLoop()

    
    