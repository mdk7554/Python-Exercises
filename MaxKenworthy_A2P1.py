"""
Created on Thu Oct  4 15:35:09 2018

Max Kenworthy

Honor statement: “I have not given or received any unauthorized assistance on this assignment.”
"""

import pandas as pd

def print_last_char():

    #open and read in text file to lists
    gfile = open("/Users/maxkenworthy/Desktop/Datasets/namesGirls.txt",'r')
    bfile = open("/Users/maxkenworthy/Desktop/Datasets/namesBoys.txt",'r')
    
        
    girls = gfile.read().split('\r\n')
    boys = bfile.read().split('\r\n')
    
    gfile.close()
    bfile.close()
    
    #create 2 new empty lists for last characters of names
    g_char,b_char = [],[]
    
    #iterate through each list collecting last characters of all names
    for i in girls:
        for j in i:
            g_char.append(i[-1])
            break
    
    for k in boys:
        for l in k:
            b_char.append(k[-1])
            break        
    
    #convert to Pandas Series and use value_counts to sum all unique values
    
    last_chars_b = pd.Series(b_char).value_counts(sort=False)
    last_chars_g = pd.Series(g_char).value_counts(sort=False)
    
    #make internal alphabet list
    alpbt = pd.Series(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    
    #check last character lists if missing any letters of alphabet, if so impute 0
    for k in alpbt:
        if k not in last_chars_b.index:
            last_chars_b=last_chars_b.append(pd.Series([0],[k]))
    
    for t in alpbt:
        if t not in last_chars_g.index:
            last_chars_g=last_chars_g.append(pd.Series([0],[t]))
            
    #sort Series by index alphabetically
    chars_sortb = pd.Series.sort_index(last_chars_b)
    chars_sortg = pd.Series.sort_index(last_chars_g)
    
    #concatenate boy & girl and apply column header
    df = pd.concat([chars_sortg,chars_sortb],axis=1)
    df.columns=['Girls','Boys']
        
    return df

print_last_char()
