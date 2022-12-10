import sys
import re
from dataclasses import dataclass
from typing import Callable


@dataclass
class EventStream:
    stream : Callable
    time_remaining : int = 0
    operation: Callable = None
    data: object = None
    
with open(sys.argv[1], "rt") as fd:
    clock = 0
    X = 1
    scan_line = []

    def get_pixel(x_pos):
        symbol = ' '
        if x_pos >= X - 1 and x_pos <= X+1:
            symbol = '#'
        return symbol        

    def increment(value):
        global X
        X += value
        #print(f"End of cycle {'%02d'%clock}: finish executing addx {value} (Register X is now {X})")
        #print("Sprite position:","".join([get_pixel(i) for i in range(40)]))

    def sample(value):
        global scan_line
        x_pos = (clock-1) % 40
        scan_line.append(get_pixel(x_pos))
        #print(f"During cycle {'%02d' % clock}: CRT draws pixel in position {x_pos}")
        #print("Current CRT row:","".join(scan_line))
        if clock == 10:
            breakpoint()
        if x_pos == 39:
            print("".join(scan_line))
            scan_line = []
#        global accum
#        strength = clock * X
#        print(f"clock={clock},X={X},strength={strength}")
#        accum += strength

    def parse(fd):
        for line in fd:
            line = line.strip()
            m = re.match("addx (\\S+)", line)
            if m is not None:
                yield (2, increment, int(m.group(1)))
                continue
            assert line == 'noop', f"line={repr(line)}"
            yield (1, None, None)

    def sample_stream():
        yield (1, sample, None)
        while True:
            yield (1, sample, None)
    
    streams = [EventStream(sample_stream()), EventStream(parse(fd)) ]
    running = True
    while running:
        time_step = min([x.time_remaining for x in streams])
        clock += time_step
        for stream in streams:
            stream.time_remaining -= time_step
            
        for stream in streams:
            if stream.time_remaining == 0:
                if stream.operation is not None:
                    stream.operation(stream.data)
                
                try:
                    delay, callback, data = next(stream.stream)
                except StopIteration:
                    running = False
                    break
                stream.operation = callback
                stream.data = data
                stream.time_remaining = delay
#    print(accum)
