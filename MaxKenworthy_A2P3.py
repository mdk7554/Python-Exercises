'''
Exercise: Calculate descriptive statistics for attribute "Total Volume" of Avocado dataset WITHOUT storing data into memory.
Only read in one value at a time.
'''

import numpy as np
import pandas as pd
import statistics as st
import csv

#read and store data in memory then calculate mean, standard deviation, and median using statistics library
def read_in(var):
    col = pd.read_csv(".../avocado.csv",usecols=[var])
    return col[var]

def readcomp_mean_sm(var):
    col = read_in(var)
    return st.mean(col)


def readcomp_stdv_sm(var):
    col = read_in(var)
    return st.stdev(col)


def readcomp_med_sm(var):
    col = read_in(var)
    return st.median(col)

print(readcomp_mean_sm('Total Volume'),readcomp_stdv_sm('Total Volume'),readcomp_med_sm('Total Volume'))

#formulate descriptive statistics with homegrown/original algorithm (i.e. not using third-party library)
def mean_hg(var):
    col = read_in(var)
    return sum(col)/len(col)

def std_hg(var):
    col = read_in(var)
    mean=readcomp_mean_sm(var)
    mean2=0
    for i in col:
        mean2+=(i-mean)**2
    
    return (mean2/len(col))**0.5

def median_hg(var):
    col = read_in(var)
    mid = len(col)/2
    if len(col)%2 != 0:
        return sorted(col)[int(mid)]
    else:
        return (sorted(col)[int(mid)] + sorted(col)[int(mid)+1])/2

print(mean_hg('Total Volume'),std_hg('Total Volume'),median_hg('Total Volume'))

#calculate descriptive statistics by only storing one value in memory at a time

#function to read in single value given the variable and index
def read_1val(var,r_idx):
    c = pd.read_csv("/Users/maxkenworthy/Desktop/Datasets/avocado.csv",nrows=1,index_col=0)
    c_idx = c.columns.get_loc(var)
    val=pd.read_csv("/Users/maxkenworthy/Desktop/Datasets/avocado.csv",usecols=[c_idx+1],nrows=1,skiprows=r_idx)
    return val.iloc[0][0]

#find index of minimum and maximum values
def min_max_totaln(var):
    max_v,v,i = 0,0,0
    min_v = read_1val(var,i)
    try:
        while True:
            v=read_1val(var,i)
            i= i+1
            if v>max_v:
                max_v=v
            elif v<min_v:
                min_v=v
    except IndexError:
        return min_v,max_v,i

min_v, max_v, n_v = min_max_totaln('Total Volume')
print(min_v,max_v,n_v)

#calculate mean
def mean_mml(var,n):
    totsum=0
    for i in range(n):
        totsum = totsum + read_1val(var,i)
    return totsum/n

mean_v = mean_mml("Total Volume",n_v)
print(mean_v)

#standard deviation
def sd_mml(var,n):
    mean2=0
    for i in range(n):
        mean2+=(read_1val(var,i)-mean_mml(var,n))**2
    
    return (mean2/n)**0.5
