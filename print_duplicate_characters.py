#print all the duplicaytes of the string
s=input("Enter String:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("the duplicates in the string are:")
for ch in freq:
    if freq[ch]>1:
        print(ch)
