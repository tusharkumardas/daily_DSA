def longest_substring(s):
  last_seen={}
  start=0
  max_len=0
  max_sub=""

  for i in range(len(s)):
    if s[i] in last_seen and last_seen[s[i]]>=start:
      start=last_seen[s[i]]+1
    last_seen[s[i]]=i

    current_len=i-start+1
    if current_len>max_len:
      max_len=current_len
      max_sub=s[start:i+1]
  return max_len,max_sub
s=("Enter string:")
print(longest_substring(s))

