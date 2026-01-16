#calculate frequency of characters in a string
s=input("Enter String:")
dict={}
for ch in s:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
print(dict)
