def checkSort(arr):
    t=sorted(list(arr))
    if t==arr:
        return True
    else:
        return False

arr=[1,2,3,4,5,6]
print(checkSort(arr))
