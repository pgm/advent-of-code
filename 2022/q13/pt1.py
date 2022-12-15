#-*-coding:utf8;-*-
#qpy:console
import sys

def cmp(a, b):
 if type(a) == int and type(b) == int:
  if a<b:
   return -1
  if a>b:
   return 1
  return 0
 else:
  if type(a)==int:
      a=[a]
  if type(b)==int:
      b=[b]
  for ia, ib in zip(a, b):
      t = cmp(ia,ib)
      if t != 0:
          return t
  if len(a) < len(b):
      return -1
  if len(b) < len(a):
      return 1
  return 0

fd=open(sys.argv[1],"rt")
buf = fd.read().strip()
batches =buf.split("\n\n")
pairs =[ [eval(x) for x in batch.split("\n")]
  for batch in batches]



index =[]
#breakpoint()
for i, pair in enumerate(pairs):
  if cmp(pair[0],pair[1])<=0:
   index.append(i+1)
  else:
   print(i+1, "wrong")
  print("\n")
  
print(sum(index))
