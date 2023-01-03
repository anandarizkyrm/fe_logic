def anagram(array):
  sortedStr = []
  
  for i in range(0, len(array)):
    sortedStr.append(str(''.join(sorted(array[i]))))

  result = [[]]
  checkIfusedIdx = []
  for i in range(0, len(sortedStr) ):
    if(i not in checkIfusedIdx and len(result[len(result) - 1]) == 0):
      result[len(result) - 1].append(array[i])
      checkIfusedIdx.append(i)
  
      
    for j in range(i, len(sortedStr)):
      if (i != j):
        if (sortedStr[i] == sortedStr[j] and j not in checkIfusedIdx):
          result[len(result) - 1].append(array[j])
          checkIfusedIdx.append(j)
        elif (j == len(sortedStr) - 1 and len(result[len(result) - 1]) != 0 ):
          result.append([])
          if(i not in checkIfusedIdx):
            result[len(result) - 1].append(array[i])

            
  if(len(result[len(result) - 1]) == 0):
    result.pop(len(result) - 1)
      
  return result
  


print(anagram(['kita', 'atik', 'tika', 'aku', 'kia', 'makan', 'kua']))
