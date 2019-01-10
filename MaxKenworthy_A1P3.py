## Max Kenworthy
## 9/24/18
## honor statement "I have not given or received unauthorized assistance on this assignment"

# P3 a)

def prime(x):
    # check if input is valid
    if type(x) != int or x < 0:
        return False
    #calculate if number is prime
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True

#P3 b)

def happy(x):
    lst = []
    #check for invalid input
    if type(x) != int or x < 0:
        return False
    while True:
        a=0
        #accumulate sum of digits from input number as 'a'
        for i in str(x):
            a += int(i)**2
        #return true if number is happy (if a=1)
        if a == 1:
                return True
        #check list for a repeated value and return false
        elif a in lst:
                return False
        #add 'a' to list so it can be checked for repeats and reset x value to start loop over
        else:
                lst.append(a)
                x=a

# P3 c)

def happy_prime(x):
    if prime(x)==True and happy(x)==True:
        return True
    else:
        return False

# P3 d)

def hp100():
    lst=[]
    x=0
    while len(lst) < 100:
        x+=1
        if happy_prime(x) == True:
            lst.append(x)
    print(lst)

# P3 e)

def sad100():
    lst=[]
    x=0
    while len(lst) < 100:
        x+=1
        if prime(x) == True and happy(x) == False:
            lst.append(x)
    print(lst)