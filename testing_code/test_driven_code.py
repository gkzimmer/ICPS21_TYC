#This is a file for demonstrating test-driven development in python.
#It is blank right now, for the first commit to git.
import numpy as np

def find_avg(a,b,c,d,e,f):
    sum = a + b + c + d + e + f

    #The int() function is added in response to the third commit.
    return int(sum / 6)

def find_range(a,b,c,d,e,f):
    range_array = np.array([a,b,c,d,e,f])
    return (np.amax(range_array) - np.amin(range_array))
