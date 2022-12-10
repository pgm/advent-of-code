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
    accum = 0

    def increment(value):
        global X
        X += value

    def sample(value):
        global accum
        strength = clock * X
        print(f"clock={clock},X={X},strength={strength}")
        accum += strength

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
        yield (20, sample, None)
        while True:
            yield (40, sample, None)
    
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
    print(accum)
