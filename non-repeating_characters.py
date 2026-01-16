#find non repeating characters of a string
s=input("Enter String:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("the non repeating characters are:")
for ch in freq:
   if freq[ch]==1:
      print(ch)

