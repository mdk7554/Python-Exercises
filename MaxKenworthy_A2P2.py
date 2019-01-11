
"""
Created on Thu Oct  4 18:17:00 2018

Max Kenworthy

Honor statement: “I have not given or received any unauthorized assistance on this assignment.”
"""

#read in files
file1 = open("/Users/maxkenworthy/Desktop/Datasets/StemAndLeaf1.txt",'r')
file2 = open("/Users/maxkenworthy/Desktop/Datasets/StemAndLeaf2.txt",'r')
file3 = open("/Users/maxkenworthy/Desktop/Datasets/StemAndLeaf3.txt",'r')
    
        
sal1 = file1.read().split('\n')
sal2 = file2.read().split('\n')
sal3 = file3.read().split('\n')

file1.close()
file2.close()
file3.close()

#call this function sl_start() to begin game 
def sl_start():
    
    print('Greetings user, would you like to see a stem and leaf plot?\n')
    
    #while loop asks for file number input and calls second function that prints stem and leaf plot
    while True:
        x = int(input('Enter a file number 1, 2, or 3 (Zero to exit) '))
        if x==1:
            sal_123(sal1)
        elif x==2:
            sal_123(sal2)
        elif x==3:
            sal_123(sal3)
        elif x==0:
            print('Thanks for playing')
            break
        else:
            print('Invalid input. Enter 1, 2, 3 or 0.')

    return None

#function that prints stem and leaf
def sal_123(file):
    
    sl_dict = {} 

    #separate stems and add to dict as keys
    for s in file:
        if s[:-1] not in sl_dict.keys():    
            sl_dict.update({int(s[:-1]):[]})
    
    #append leaves to appropriate stems as a list 
    for l in file:
        sl_dict[int(l[:-1])].append(int(l[-1]))
        
    print("Stem and Leaf Plot\n")
    
    #format stem and leaf plot
    for key,val in sorted(sl_dict.items()):
        print(str(key)+' | ',end='')
        for v in sorted(val):
            print(v, end=' ')
        print('\n')
    
    return None
