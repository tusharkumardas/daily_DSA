def remove_duplicates(arr):
    #set() is used to list unique elements of the array
    t=sorted(list(set(arr)))
    return t
