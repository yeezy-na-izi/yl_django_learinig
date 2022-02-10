import json
import sys

d = {
    "request": {},
    "response": {}
}

for line in sys.stdin:
    name, value = line.strip().split(' = ')
    if int(value) < 0:
        d["request"][name] = value
    elif int(value) > 0:
        d["response"][name] = str(value)

with open('contact.json', 'w') as outfile:
    outfile.write(json.dumps(d))
