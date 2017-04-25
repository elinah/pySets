def union(A, B):
  return [i for i in A if i not in B] + inter(A, B) + [i for i in B if i not in A];
  
def inter(A, B):
  return [i for i in A if i in B];
  
def setDiff(A, B):
  return [i for i in A if i not in B];
  
def symmDiff(A, B):
  return [i for i in A if i not in B] + [i for i in B if i not in A];
  
def cartProd(A, B):
  return [(a, b) for a in A for b in B];
  
#tests
print union([1, 2, 3], [2, 3, 4]);
print inter([1, 2, 3], [2, 3, 4]);
print setDiff([1, 2, 3], [2, 3, 4]);
print setDiff([2, 3, 4], [1, 2, 3]);
print symmDiff([1, 2, 3], [2, 3, 4]);
print cartProd([1, 2, 3], [2, 3, 4]);