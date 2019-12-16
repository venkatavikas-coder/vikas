MATH482 FALL 2019  
NAME(S) _______________________________________________ max five people 
Programming Project-minimal obstacles in Instant Insanity
OUT: Tuesday, November 19, 2019.
RET: Due Tuesday, December 17, at the start of the final exam.

Design and implement a computer program to search for “obstacles,” if they exist, for Instant Insanity-style puzzles constructed from right triangular prisms as described in class.  I.e., these “pie slices” are constrained to move only by rotation-no flipping.  They have colors on their vertical sides.  There are only three positions that a given slice can have relative to the rest of the tower.  One can visualize the pie slice with a hole in the center through which a wire passes, preventing the flipping of any slice of the puzzle.  FYI is flipping is allowed, the problem no longer is NP-Complete, and there is a particularly simple criteria for determining if a solution exists.   If an obstacle exists find the smallest one.  As mentioned in class, by obstacle I refer to a subset of the pie slices, which cannot be part of any solution.  I.e., any stacking of these slices entails at least one of the three sides having some color showing up two or more times. You have free reign over what type of algorithm to use, but I would prefer for you to write the program in Python as it will be easier for me to understand.  Please turn in your source code along with your results. Particularly insightful and efficient algorithm design may qualify for extra credit.  Note that observing that a particular color only shows up only two times is not the same as identifying the smallest obstacle.  For this project we are looking for obstacles, not solving puzzles that have solutions.  Of course it is possible (although unlikely) that one of the “randomly” built puzzles below actually has a solution.   In that case, simply provide the solution.  These puzzles are assumed to have 100 slices and each slice has three faces.  Therefore the puzzle coloring scheme is determined by a list of 300 colors.  Assume that the colors generated refer to the colors of the slices in the following way.
The first three colors will color the bottom slice, slice #1.  They will color in order the faces as seen from the top of the puzzle, counterclockwise.  The next three colors in the list will color the second slice, etc.  
1 + ((floor nπ) mod 100), 		1 ≤ n ≤ 300, for puzzle one, 
1 + ((floor ne) mod 100), 		1 ≤ n ≤ 300, for puzzle two,
1 + ((floor n√2)  mod 100), 	1 ≤ n ≤ 300, for puzzle three,
1 + ((floor n√3)  mod 100), 	1 ≤ n ≤ 300, for puzzle four.
These formulas specify, exactly, which colors land on which faces, so everyone will have the exact same data set.  
Please provide an English description of your algorithm (pseudocode) for determining the smallest obstacle.  Please also provide your source code, and output.  The key is an obstacle of minimal size.  Be sure to include this in your report.  If you cannot solve the problem entirely, then you can give an upper bound on the size of the smallest obstacle, for partial credit.  For instance, if you determine that the puzzle does not have a solution, then you can surely say the obstacle size is ≤ 100.  But of course I want to see, for a puzzle without solution, what the smallest obstacle is.  Or at least, a better upper bound than 100!
As I said earlier, extra credit will be awarded for a particularly clever or insightful algorithm (something beyond brute-force).  Also you might compare your input with other groups, just to make sure you are dealing with the same puzzles.  If your input is wrong I cannot give credit!

Finally, I allow you to work in groups.  Maximum group size is FIVE. Each group will submit one report; each member of a given group will receive the same score on the program.  It is probably obvious with no need to say it, but when forming your group you should take into consideration the attendance of the candidate members.  If someone has skipped a lot of lectures then they will most likely skip group meetings, too.  













Algorithm 

	Start
	The plan is to use a stack to implement DFS brute force through the given puzzles. I always want to do a histogram of the colors each puzzle 
	Creating the sliceGenerator funtions
	Defining stack and testing stack
	Getting the input color puzzle for  0<n<300 and calling the function slicegenraton and printing the list of pies 
	Creating DFS calling for stack and searching for the minimu obstacle 
	Returning the minimum obstacle 
	End






puzzle1(https://github.com/venkatavikas-coder/vikas/blob/master/puzzle1)
import math  # This will import math module
def sliceGenerator(colors):
    pies =[]
    pie =[]
    three_sides=[]
    for i in range(300):
        three_sides.append(colors[i])
        if((i+1)%3==0):
            pie.append(three_sides)
            three_sides=[]
            if((i+1)%3 == 0):
                pies.append(pie)
                pie =[]
    return pies 
    
    
    class Stack():
     def __init__(self):
        self.stack = []
    def push(self, a):
       self.stack.insert(0,a)
    def pop(self):
        return self.stack.pop(0)
    def top(self):
        print(self.stack[0])
    def size(self):
      return len(self.stack)
        
    stack = Stack()
    stack.push(3)
    print(stack.size())
    stack.top()
    print(stack.pop())    
    
colors_of_puzzle1 =[1+math.floor(i*math.pi%100)for i in range(1,301)]
print("the list length of the colors in puzzle one :",len(colors_of_puzzle1))
print("the colors of puzzle one : ",colors_of_puzzle1 )
pies1 = sliceGenerator(colors_of_puzzle1)
print(len(pies1))
for i in range(100):
    print(pies1[i])
    
def DFS(pies,index):
    visited = [[False, False,False] for i in range(len(pies))]
    thread1 = [[False, False,False] for i in range(len(pies))]
    thread2 = [[False, False,False] for i in range(len(pies))]
    multiplicity = [0 for i in range(100)]
    good = True
    halfSolutions = []
    halfSolution = []
    s = Stack()
    s.push([piess[0][index],index])
    halfSolution.append([pies[0][index], index])
    visited[0][index] = True
    while(s.size() != 0):
        print("This ran")
        pair = s.pop()
        if( (multiplicity[pair[0][0]] < 3) and (multiplicity[pair[0][1]] < 3) ):
            multiplicity[pair[0][0]] += 1
            multiplicity[pair[0][1]] += 1
        if(pair[1] == 29):
            halfSolutions.append(halfSolution)
            halfSolution = []
        print(pair[0][0])
        print(pair[0][1])
        print(pair[0][2])
        for i in range(3):
            if ( (visited[pair[1]+1][i] == False) and (multiplicity[pies[pair[1]+1][i][0]] < 3 and multiplicity[cubes[pair[1]+1][i][1]] < 3) ): 
                s.push([cubes[pair[1]+1][i],i])
                halfSolution.append(cubes[pair[1]+1][i])                
                print("This ran")     
    if(len(halfSolutions) == 0):
        print("No half solutions found starting from index ", index)
        
    return halfSolutions
    
    Solutions = DFS(pies1,0)
print(Solutions)

Puzzle 2 (https://github.com/venkatavikas-coder/vikas/blob/master/puzzle2)
import math  # This will import math module
def sliceGenerator(colors):
    pies =[]
    pie =[]
    three_sides=[]
    for i in range(300):
        three_sides.append(colors[i])
        if((i+1)%3==0):
            pie.append(three_sides)
            three_sides=[]
            if((i+1)%3 == 0):
                pies.append(pie)
                pie =[]
    return pies 
    
    
    class Stack():
     def __init__(self):
        self.stack = []
    def push(self, a):
       self.stack.insert(0,a)
    def pop(self):
        return self.stack.pop(0)
    def top(self):
        print(self.stack[0])
    def size(self):
      return len(self.stack)
        
    stack = Stack()
    stack.push(3)
    print(stack.size())
    stack.top()
    print(stack.pop())    
    
colors_of_puzzle1 =[1+math.floor(i*math.e%100)for i in range(1,301)]
print("the list length of the colors in puzzle one :",len(colors_of_puzzle1))
print("the colors of puzzle one : ",colors_of_puzzle1 )
pies1 = sliceGenerator(colors_of_puzzle1)
print(len(pies1))
for i in range(100):
    print(pies1[i])
    
def DFS(pies,index):
    visited = [[False, False,False] for i in range(len(pies))]
    thread1 = [[False, False,False] for i in range(len(pies))]
    thread2 = [[False, False,False] for i in range(len(pies))]
    multiplicity = [0 for i in range(100)]
    good = True
    halfSolutions = []
    halfSolution = []
    s = Stack()
    s.push([piess[0][index],index])
    halfSolution.append([pies[0][index], index])
    visited[0][index] = True
    while(s.size() != 0):
        print("This ran")
        pair = s.pop()
        if( (multiplicity[pair[0][0]] < 3) and (multiplicity[pair[0][1]] < 3) ):
            multiplicity[pair[0][0]] += 1
            multiplicity[pair[0][1]] += 1
        if(pair[1] == 29):
            halfSolutions.append(halfSolution)
            halfSolution = []
        print(pair[0][0])
        print(pair[0][1])
        print(pair[0][2])
        for i in range(3):
            if ( (visited[pair[1]+1][i] == False) and (multiplicity[pies[pair[1]+1][i][0]] < 3 and multiplicity[cubes[pair[1]+1][i][1]] < 3) ): 
                s.push([cubes[pair[1]+1][i],i])
                halfSolution.append(cubes[pair[1]+1][i])                
                print("This ran")     
    if(len(halfSolutions) == 0):
        print("No half solutions found starting from index ", index)
        
    return halfSolutions
    
    Solutions = DFS(pies1,0)
print(Solutions)

Output:
the list length of the colors in puzzle one : 300
	the colors of puzzle one :  [4, 7, 10, 13, 16, 19, 22, 26, 29, 32, 35, 38, 41, 44, 48, 51, 54, 57, 60, 63, 66, 70, 73, 76, 79, 82, 85, 88, 92, 95, 98, 1, 4, 7, 10, 14, 17, 20, 23, 26, 29, 32, 36, 39, 42, 45, 48, 51, 54, 58, 61, 64, 67, 70, 73, 76, 80, 83, 86, 89, 92, 95, 98, 2, 5, 8, 11, 14, 17, 20, 24, 27, 30, 33, 36, 39, 42, 46, 49, 52, 55, 58, 61, 64, 68, 71, 74, 77, 80, 83, 86, 90, 93, 96, 99, 2, 5, 8, 12, 15, 18, 21, 24, 27, 30, 34, 37, 40, 43, 46, 49, 52, 55, 59, 62, 65, 68, 71, 74, 77, 81, 84, 87, 90, 93, 96, 99, 3, 6, 9, 12, 15, 18, 21, 25, 28, 31, 34, 37, 40, 43, 47, 50, 53, 56, 59, 62, 65, 69, 72, 75, 78, 81, 84, 87, 91, 94, 97, 100, 3, 6, 9, 13, 16, 19, 22, 25, 28, 31, 35, 38, 41, 44, 47, 50, 53, 57, 60, 63, 66, 69, 72, 75, 79, 82, 85, 88, 91, 94, 97, 1, 4, 7, 10, 13, 16, 19, 23, 26, 29, 32, 35, 38, 41, 45, 48, 51, 54, 57, 60, 63, 67, 70, 73, 76, 79, 82, 85, 89, 92, 95, 98, 1, 4, 7, 10, 14, 17, 20, 23, 26, 29, 32, 36, 39, 42, 45, 48, 51, 54, 58, 61, 64, 67, 70, 73, 76, 80, 83, 86, 89, 92, 95, 98, 2, 5, 8, 11, 14, 17, 20, 24, 27, 30, 33, 36, 39, 42, 46, 49, 52, 55, 58, 61, 64, 68, 71, 74, 77, 80, 83, 86, 90, 93, 96, 99, 2, 5, 8, 12, 15, 18, 21, 24, 27, 30, 34, 37, 40, 43]
	100
	[[4, 7, 10]]
	[[13, 16, 19]]
	[[22, 26, 29]]
	[[32, 35, 38]]
	[[41, 44, 48]]
	[[51, 54, 57]]
	[[60, 63, 66]]
	[[70, 73, 76]]
	[[79, 82, 85]]
	[[88, 92, 95]]
	[[98, 1, 4]]
	[[7, 10, 14]]
	[[17, 20, 23]]
	[[26, 29, 32]]
	[[36, 39, 42]]
	[[45, 48, 51]]
	[[54, 58, 61]]
	[[64, 67, 70]]
	[[73, 76, 80]]
	[[83, 86, 89]]
	[[92, 95, 98]]
	[[2, 5, 8]]
	[[11, 14, 17]]
	[[20, 24, 27]]
	[[30, 33, 36]]
	[[39, 42, 46]]
	[[49, 52, 55]]
	[[58, 61, 64]]
	[[68, 71, 74]]
	[[77, 80, 83]]
	[[86, 90, 93]]
	[[96, 99, 2]]
	[[5, 8, 12]]
	[[15, 18, 21]]
	[[24, 27, 30]]
	[[34, 37, 40]]
	[[43, 46, 49]]
	[[52, 55, 59]]
	[[62, 65, 68]]
	[[71, 74, 77]]
	[[81, 84, 87]]
	[[90, 93, 96]]
	[[99, 3, 6]]
	[[9, 12, 15]]
	[[18, 21, 25]]
	[[28, 31, 34]]
	[[37, 40, 43]]
	[[47, 50, 53]]
	[[56, 59, 62]]
	[[65, 69, 72]]
	[[75, 78, 81]]
	[[84, 87, 91]]
	[[94, 97, 100]]
	[[3, 6, 9]]
	[[13, 16, 19]]
	[[22, 25, 28]]
	[[31, 35, 38]]
	[[41, 44, 47]]
	[[50, 53, 57]]
	[[60, 63, 66]]
	[[69, 72, 75]]
	[[79, 82, 85]]
	[[88, 91, 94]]
	[[97, 1, 4]]
	[[7, 10, 13]]
	[[16, 19, 23]]
	[[26, 29, 32]]
	[[35, 38, 41]]
	[[45, 48, 51]]
	[[54, 57, 60]]
	[[63, 67, 70]]
	[[73, 76, 79]]
	[[82, 85, 89]]
	[[92, 95, 98]]
	[[1, 4, 7]]
	[[10, 14, 17]]
	[[20, 23, 26]]
	[[29, 32, 36]]
	[[39, 42, 45]]
	[[48, 51, 54]]
	[[58, 61, 64]]
	[[67, 70, 73]]
	[[76, 80, 83]]
	[[86, 89, 92]]
	[[95, 98, 2]]
	[[5, 8, 11]]
	[[14, 17, 20]]
	[[24, 27, 30]]
	[[33, 36, 39]]
	[[42, 46, 49]]
	[[52, 55, 58]]
	[[61, 64, 68]]
	[[71, 74, 77]]
	[[80, 83, 86]]
	[[90, 93, 96]]
	[[99, 2, 5]]
	[[8, 12, 15]]
	[[18, 21, 24]]
	[[27, 30, 34]]
	[[37, 40, 43]]

