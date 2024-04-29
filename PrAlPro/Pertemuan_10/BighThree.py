def BigThree(data):
  for i in range(len(data) - 1, -1, -1):
    item = data[i]
    if isinstance(item, list):
      del data[i]             
      BigThree(item) 
      data[i:i] = item   
  data.sort(reverse=True)
  return data[:3]
print(BigThree([9,0,1,3,4,-1,10]))