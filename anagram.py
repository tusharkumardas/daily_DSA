def anagram(s1,s2):
    if len(s1)==len(s2):
      if sorted(s1)==sorted(s2):
         print("anagram")
    else:
        print("false")
s1="listen"
s2="silent"
anagram(s1,s2)
    
