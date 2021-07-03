import sys

def calc(l,v):
    vals = l.split(" ")
    if vals[0].startswith("!"):
        res = not v[vals[0][1]]
    else:
        res = v[vals[0]]
    for vi in vals[1:]:
        if vi.startswith("!"):
            res &= not v[vi[1]]
        else:
            res &= v[vi]
    return res

def main(f):
    nv = []
    code = open(f)
    dict_ = {}
    lines = code.readlines()
    values = lines[1][:-1].split(" ")
    booleans = lines[0][:-1].split(" ")
    tmp = 0
    for i,v in enumerate(values):
        if v.startswith("!"):
            dict_[v[1]] = int(booleans[i])
        else:
            dict_[v] = int(booleans[i])
    for line in lines[1:]:
        if ord(line[-1]) == 0xa:
            line = line[:-1]
        tmp |= calc(line,dict_)
    print(tmp)

main(sys.argv[1])