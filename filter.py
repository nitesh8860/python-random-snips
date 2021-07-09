s='a man, a plan, a canal: panama'
s="".join(filter(str.isalnum, s.upper()))
print(s)
print( s == s[::-1] )