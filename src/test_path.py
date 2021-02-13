import sys
import os
import json
path = os.path.join(sys.path[0], "../config/login.json")
print(path)
print(json.load(open(path)))

