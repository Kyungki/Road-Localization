import json
import test1 as t1

class Anchor:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

class Tag:
    def __init__(self, ip, user):
        self.ip = ip
        self.user = user

input_data = open("Config.json", "r")
json_data = json.load(input_data)
anchors = [json_data["anchors1"]]
print(anchors)
tags = [json_data["tags1"]]
id, x, y, z = [], [], [], []
ip, user = [], []
for i in anchors:
    for j in range(len(i)):
        id.append(i[j]["id"])
        x.append(i[j]["x"])
        y.append(i[j]["y"])
        z.append(i[j]["z"])
t1.callvis(id)

for i in tags:
    for j in range(len(i)):
        ip.append(i[j]["ip"])
        user.append(i[j]["user"])

a1 = Anchor(id[0], x[0], y[0], z[0])
t1 = Tag(ip[0], user[0])


