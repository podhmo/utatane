import json
from pympler.asizeof import asizeof

ns = list(range(1, 11))
dataset = [
    list(zip(ns,
             [asizeof([i] * i) for i in ns])),
    list(zip(ns,
             [asizeof([i for i in range(i)]) for i in ns])),
    list(zip(ns,
             [asizeof({i
                       for i in range(i)}) for i in ns])),
    list(zip(ns,
             [asizeof({i: i
                       for i in range(i)}) for i in ns])),
]
print(json.dumps({"values": dataset, "labels": ["list0", "list1", "set", "dict"]}))
