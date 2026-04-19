def count_sorted_rows(Mat):
    count=0
    for row in Mat:
        inc=True
        dec=True
        n=len(row)
        for i in range(n-1):
            if row[i]>=row[i+1]:
                inc=False
            elif row[i]<=row[i+1]:
                dec=False
            if not inc and not dec:
                break
        if inc or dec:
            count+=1
    return count
Mat=[[1,2,3],[4,6,5],[7,8,9],[9,10,11,12,13]]
print(count_sorted_rows(Mat))
    
