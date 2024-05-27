import string
def palindromeAsik(s,b):
    s=s.lower().translate(str.maketrans("","",string.punctuation))
    if b<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return palindromeAsik(s[1:-1],len(s[1:-1]))
    
print(palindromeAsik("k!@!a#s()u$$rr#%u^s&%a*k",24))
