#removing duplicates
s=input("Enter String:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1

    else:
        freq[ch]=1
print("After removing duplicates:")
for i in freq:
    print(i,end="")
