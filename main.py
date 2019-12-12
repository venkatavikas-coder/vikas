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
            if((i+1)%5 == 0):
                pies.append(pie)
                pie =[]
    return pies            
colors_of_puzzle1 =[1+math.floor(i*math.pi%100)for i in range(1,301)]
print("the list length of the colors in puzzle one :",len(colors_of_puzzle1))
print("the colors of puzzle one : ",colors_of_puzzle1 )
pies1 = sliceGenerator(colors_of_puzzle1)
print(len(pies1))
for i in range(30):
    print(pies1)



