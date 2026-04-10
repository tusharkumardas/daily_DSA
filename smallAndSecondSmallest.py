def MinAndMin2(arr):
   smallest=float ('inf')
   second_smallest=float ('inf')

   for num in arr:
      if num < smallest:
          second_smallest=smallest
          smallest=num
      elif num > smallest and num < second_smallest:
          second_smallest=num
   if second_smallest== ('inf'):
      return [-1]

   return [smallest,second_smallest]
arr=[5,8,6,4,7,9,3,4,8]
print(MinAndMin2(arr))
    
   
