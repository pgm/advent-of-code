import sys

with open(sys.argv[1], "rt") as fd:
    matrix = [x.strip() for x in fd.readlines()]
    w = len(matrix[0])
    h = len(matrix)
    
    def visible():
        for origin_x, origin_y, major_x, major_y, minor_x, minor_y, major_count, minor_count in [
            (0,0,0,1,1,0,h,w), # h, r -> l
            (w-1,0, 0,1, -1,0, h,w), # h, l -> r
            (0,0,1,0,0,1,w,h), # v, t -> b
            (0,h-1,1,0,0,-1,w,h) # v, b -> t
            ]:
            print("x", origin_x, origin_y, major_x, major_y, minor_x, minor_y, major_count, minor_count)
            for j in range(major_count):
                _max = "/"
                x, y = origin_x, origin_y
                for i in range(minor_count):
                    print(f"i={i},x={x},y={y}")
                    if _max < matrix[y][x]:
                        _max = matrix[y][x]
                        yield (x,y)
                    x += minor_x
                    y += minor_y
                origin_x += major_x
                origin_y += major_y

    trees = set(visible())

    print(len(trees))
    
    for j in range(h):
        for i in range(w):
            print("*" if (i, j) in trees else " ", end="")
        print("")