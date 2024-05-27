def pasanganHuruf(s):
  if len(s)<=2:
      return 0
  return (1 if s[0]==s[2] else 0)+ pasanganHuruf(s[1:]) 
    
print(pasanganHuruf("ababa")) #3
print(pasanganHuruf("acay")) #1
print(pasanganHuruf("bxbxx")) #2
print(pasanganHuruf("kukuruyuk")) #4