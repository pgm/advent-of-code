import sys

with open(sys.argv[1], "rt") as fd:
    matrix = [x.strip() for x in fd.readlines()]
    w = len(matrix[0])
    h = len(matrix)
    
    def scan(origin_x, origin_y, minor_x, minor_y):
        x, y = origin_x, origin_y
        _max = matrix[y][x]
        count = 0
        while True:
            x += minor_x
            y += minor_y
            
            if x < 0 or x >= w or y < 0 or y >= h:
#                print("off map, ret",count)
                return count
            
#            print(f"x={x},y={y},max={_max}, pos={matrix[y][x]}")
            if matrix[y][x] >= _max:
#                print("highter ret", count+1)
                return count + 1
            count += 1
    
    def visible(x, y):
        accum = 1
        for origin_x, origin_y, major_x, major_y, minor_x, minor_y, major_count, minor_count in [
            (0,0,0,1,1,0,h,w), # h, r -> l
            (w-1,0, 0,1, -1,0, h,w), # h, l -> r
            (0,0,1,0,0,1,w,h), # v, t -> b
            (0,h-1,1,0,0,-1,w,h) # v, b -> t
            ]:
            print("x", origin_x, origin_y, major_x, major_y, minor_x, minor_y, major_count, minor_count)
            accum *= scan(x, y, minor_x, minor_y)
#            for j in range(major_count):
        return accum            

    print(visible(2,1))
    print("---")
    print(visible(2,3))

    scores = []
    for y in range(h):
        for x in range(w):
            scores.append(visible(x,y))
    print("answer", max(scores))
