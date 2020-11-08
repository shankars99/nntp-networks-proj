import json
import os
import pickle
from types import SimpleNamespace

data = pickle.load(open('../data/auth.p', 'rb'))

#data["hi"] = "welcome"

#pickle.dump(data, open('../data/auth.p', 'wb'))
print(data["admin"])