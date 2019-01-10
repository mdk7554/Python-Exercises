'''
Exercise: Write functions that take a positive integer as input and returns true if input is prime
and/or a happy prime.  Additional functions create list of first 100 happy and non-happy primes.
'''

#evaluate input as prime or non-prime
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

#evalute input as happy or non-happy number
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


#evaluate input as happy or non-happy prime
def happy_prime(x):
    if prime(x)==True and happy(x)==True:
        return True
    else:
        return False

#create and print list of first 100 happy primes
def hp100():
    lst=[]
    x=0
    while len(lst) < 100:
        x+=1
        if happy_prime(x) == True:
            lst.append(x)
    print(lst)

#create and print list of first 100 non-happy primes
def sad100():
    lst=[]
    x=0
    while len(lst) < 100:
        x+=1
        if prime(x) == True and happy(x) == False:
            lst.append(x)
    print(lst)