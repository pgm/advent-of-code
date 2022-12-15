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


seqs=[ [[2]], [[6]],
 ]
for i, pair in enumerate(pairs):
  seqs.extend(pair)
  
import functools
seqs = sorted(seqs, key=functools.cmp_to_key(cmp))

print((seqs.index([[2]])+1) * (seqs.index([[6]])+1))

