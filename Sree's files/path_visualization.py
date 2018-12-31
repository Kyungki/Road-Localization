import matplotlib.pyplot as plt
import json

input_data = open("Config.json", "r")
json_data = json.load(input_data)
anchors = [json_data["anchors1"]]
id, Ax, Ay, Az = [], [], [], []
for i in anchors:
    for j in range(len(i)):
        id.append(i[j]["id"])
        Ax.append(i[j]["x"])
        Ay.append(i[j]["y"])
        Az.append(i[j]["z"])

class Tag:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.id = []

a1 = Tag()
a2 = Tag()
a1.id = "vehicle1"
a2.id = "vehicle2"

file = open("exp1.txt", "r")
data = file.readlines()

id, x, y, z = [], [], [], []
x1, y1, x2, y2 = [], [], [], []
for lines in data:
    words = lines.replace("(", "")
    words = words.replace(")", "")
    words = words.replace(",", "")
    words = words.split()
    id.append(words[2])
    x.append(float(words[4]))
    y.append(float(words[5]))
    z.append(float(words[6]))

for i in range(len(id)):
    if(id[i] == a1.id):
        a1.x.append(x[i])
        a1.y.append(y[i])
        a1.z.append(z[i])

    elif(id[i] == a2.id):
        a2.x.append(x[i])
        a2.y.append(y[i])
        a2.z.append(z[i])

plt.plot(a1.x, a1.y, label="vehicle1")
plt.plot(a2.x, a2.y, label="vehicle2")
plt.scatter(Ax, Ay, label="Anchors", color="red")
plt.legend()
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.axis((-1, 4, -1, 9))
plt.show()
