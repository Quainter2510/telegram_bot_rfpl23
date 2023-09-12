import json

q = False
with open("settings.json") as js:
    data = json.load(js)
    q = data["all_func_ready"]

print(q)
print(q)