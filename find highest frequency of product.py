#using array-find the highest frequency product 

def highestProduct(n,arr):
    high=0
    pr=0
    count=0
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if high< count:
            high=count
            pr=arr[i]
        elif high==count:
            pr=min(pr,arr[i])   #if two  product have same frequency then smaller productid is selected
    return pr
n=int(input())
arr = list(map(int, input().split()))
print(highestProduct(n,arr))
            
                
