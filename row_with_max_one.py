def row_with_max_one(Mat):
    max_row=0
    max=0
    count=0
    flag=0
    m=len(Mat)
    for i in range(m):
        count=0
        n=len(Mat[i])
        for j in range(n):
            if Mat[i][j]==1:
                count+=1
            if max<count:
                max=count
                max_row=i
                flag=1
    if flag==1:
        return max_row
    else:
        return -1
Mat=[[0,1,0,1,0,1,1,1],[1,1,1,1],[0,1,0]]
print(row_with_max_one(Mat))
    
