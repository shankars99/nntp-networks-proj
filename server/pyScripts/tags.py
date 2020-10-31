import json
import os
import pickle
from types import SimpleNamespace


files = os.listdir("../articles/annotation")
id = []
tags = ['CHILDREN']

data = pickle.load(open('../data/tags.p', 'rb'))

for i in files:
    with open('../articles/annotation/' + i, 'r') as data:
        x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))
        for j in x.tags:
            if j in tags:
                id.append(x.number)

pickle.dump(id, open('../data/tags.p', 'wb'))
print(id)