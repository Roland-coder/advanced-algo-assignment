# Function to count the number of pairs of socks in an array
# Socks are stored as individual integer values

def sockMerchant(n, ar):

    #initializing dictionary that would be used to store pairs of socks
    my_dict = {}
    
    #Looping through array to get the count of individual element count
    for i in ar:
    
    # storing key pair values, keys as elements and values as the count
    
        my_dict[i] = ar.count(i)//2
        
    # since dictionaries do not support duplicates, we expect that only unique elements and their counts will be in the dictionary
    # We then get all the values and store in a variable
    
    values = my_dict.values()
    
    # returning the sum of the array to get the number of pairs
    return sum(values)
    
