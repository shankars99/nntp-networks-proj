import json
import os
import pickle
from types import SimpleNamespace

data = pickle.load(open('server/data/auth.p', 'rb'))

#data["hi"] = "welcome"

#pickle.dump(data, open('server/data/auth.p', 'wb'))
print(data["admin"])