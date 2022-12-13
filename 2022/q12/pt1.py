#-*-coding:utf8;-*-
import sys

with open(sys.argv[1], "rt") as fd:
    m = [x.strip() for x in fd.read().split("\n") if x.strip() != ""]
    h = len(m)
    w = len(m[0])
    for y in range(h):
        for x in range(w):
            height = m[y][x]
            if height == 'S':
                start_pos = (x,y)
            elif height == 'E':
                dest_pos = (x,y)

def heightat(pos):
    x,y=pos
    h = m[y][x]
    if h in ['S']:
        h = 'a'
    elif h == 'E':
        h = 'z'
    return ord(h)

def getexits(pos):
    exits = []
    x,y=pos
    height = heightat(pos)
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
     nx=dx+x
     ny=dy+y
     if nx >= 0 and ny >= 0 and nx < w and ny < h:
#         print(f"height={height} heightat((nx,ny))={heightat((nx,ny))}")
         if height +1 >= heightat((nx,ny)):
          exits.append((nx,ny))
    return exits

def bfs(pos, dst):
 queue = [pos]
 paths={pos:[]}
# breakpoint()
 while True:
  pos = queue[0]
  del queue[0]
  
  exits = getexits(pos)
#  print("exits", exits)
  for exit in exits:
   if exit in paths:
    if len(paths[exit])>len(paths[pos])+1:
     paths[exit] = paths[pos] +[exit]
   else:
    paths[exit] = paths[pos] +[exit]
    queue.append(exit)
  if len(queue) ==0:
   break
  
 return paths

paths = bfs(start_pos, dest_pos)
##print(paths)
print([ chr(heightat(x)) for x in paths[dest_pos] ])
print(getexits((4,0)))

print(len(paths[dest_pos]))
