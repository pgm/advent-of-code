import sys
import re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CD:
    path:str
    
@dataclass
class File:
    size: int
    name: str

@dataclass
class LS:
    files: List[File]

def tokenize(fd):
    line = None
    
    while True:
        if line is None:
            line = fd.readline().strip()
        if line == "":
            break
        print(repr(line))
        
        if line == '$ ls':
            files = []
            while True:
                line = fd.readline().strip()
                if line.startswith("$") or line == "":
                    break
                    
                m = re.match("dir (\\S+)", line)
                if m:
#                    files.append(File(size=None, name=m.group(1)))
                    continue
                    
                m = re.match("(\\d+) (\\S+)", line)
                if m:
                    files.append(File(size=int(m.group(1)), name=m.group(2)))
                    continue
                    
            yield LS(files=files)
        else:
            m = re.match("\\$ cd (\\S+)", line)
            assert m, line
            line = None
            
            yield CD(m.group(1))
        
@dataclass
class Tree:
    name : Optional[str] = None
    files : Optional[list] = None
    children :Optional[dict] = None
    size : Optional[int] = None

with open(sys.argv[1], "rt") as fd:
    cwd = []
    root = Tree(children=dict(), files=[])
    
    def insert_into_tree(node, path, files):
#        print(node, path, files)
        def g(p):
            if p not in node.children:
                node.children[p] = Tree(children=dict(), files=[])
            return node.children[p]
    
        if len(path) > 0:
            insert_into_tree(g(path[0]), path[1:], files)
        else:
            node.files = files
    
    for tk in tokenize(fd):
        if isinstance(tk, CD):
            if tk.path == '..':
                cwd.pop()
            else:
                assert ".." not in tk.path
                cwd.append(tk.path)
        else: # LS
            insert_into_tree(root, cwd, tk.files)
    

    def set_size(node):
        this_size = sum([file.size for file in node.files])
    
        for child_name, child in node.children.items():
            this_size += set_size(child)

        node.size = this_size
        return this_size
            
    def pnode(name, node, indent=0):
        print(" "*indent, name, node.size)
        for child_name, child in node.children.items():
            pnode(child_name, child, indent+1)
    
    def walk(node):
        yield node.size
        for child in node.children.values():
            for size in walk(child):
                yield size
    
    set_size(root)
    pnode("/", root)

    free_space = 70000000 - root.size
    needed_space = 30000000 - free_space

    print("need", needed_space)
    sizes_lt = [x for x in walk(root) if x >= needed_space]
    print(min(sizes_lt))