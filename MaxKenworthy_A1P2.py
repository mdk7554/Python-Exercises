'''This python program takes the location and dimensions of 2 squares and calculates the overlap. 
Location and dimensions of a square are represented as a list of 3 numbers = [x-coord,y-coord,side length].'''

#list3 function checks if input is a list with 3 elements
def list3(x):
    if type(x)==list and len(x)==3:
        return True
    else:
        return False

#square function evaluates if input represents a valid square with length of side >0
def square(x):
    if list3(x)==False:
        return False
    elif x[2]<0:
        return False
    else:
        return True


#function to calculate perimeter
def perimeter(x):
    if square(x)==False:
        return -1
    else:
        return x[2]*4


#function to calculate area
def area(x):
    if square(x)==False:
        return -1
    else:
        return x[2]**2

#calculate overlap
def overlap(sq1,sq2):
    #calculate area of intersection
    area = (min(sq1[0]+sq1[2],sq2[0]+sq2[2])-max(sq1[0],sq2[0])) * (min(sq1[1]+sq1[2],sq2[1]+sq2[2])-max(sq1[1],sq2[1]))
    #check if lists are valid squares
    if square(sq1)==False or square(sq2)==False:
        return -1
    elif area <= 0:
        return 0
    else:
        return area


#create random squares to test overlap function and print results

sq1 = [1,0,2]
sq2 = [2,1,5]
sq3 = [4,3,1]
sq4 = [1,5,3]
sq5 = [6,4,-3]
sq6 = [6,4,'three']

print("The overlap of " + str(sq1) + " and " + str(sq2) + " is " + str(overlap(sq1,sq2)))
print("The overlap of " + str(sq2) + " and " + str(sq3) + " is " + str(overlap(sq2,sq3)))
print("The overlap of " + str(sq2) + " and " + str(sq4) + " is " + str(overlap(sq2,sq4)))
print("The overlap of " + str(sq1) + " and " + str(sq4) + " is " + str(overlap(sq1,sq4)))
print("The overlap of " + str(sq1) + " and " + str(sq5) + " is " + str(overlap(sq1,sq5)))
print("The overlap of " + str(sq1) + " and " + str(sq6) + " is " + str(overlap(sq1,sq5)))

