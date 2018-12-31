import matplotlib.pyplot as plt
import time

#x = [0.4866817845556715, 0.4949201990965185, 0.5105319188986261, 0.5064612611149616, 0.4947576277187779,
#     0.30176169837516637, 0.5105319188986261, 0.5064612611149616, 0.4947576277187779, 0.30176169837516637,
#     0.6519161807184997, 0.6482276758340694, 0.6519161807184997, 0.65631281967961]
#y = [0.549168951410761, 0.5489748098167351, 0.53025541961193681, 0.5280635268000036, 0.5116498769543399,
#      0.7274890158477515, 0.5302541961193681, 0.5280635268000036, 0.5116498769543399, 0.7274890158477515,
#      0.3045585613845179, 0.30060709427954097, 0.3045585613845179, 0.3070986415902664]

x = []
y = []

p = []
q = []

i = []
j = []

plt.ion()
plt.figure()

def test(a, b, id):
    if(id == "X"):
        x.append(a)
        y.append(b)

    elif(id == "Y"):
        p.append(a)
        q.append(b)

    elif(id == "Z"):
        i.append(a)
        j.append(b)

    plt.clf()
    #print("test", x, y, p, q, i, j)

    if(len(x) == 1):
        plt.scatter(x, y, label = "tagX", color = "red")

    elif (len(x) > 1):
        plt.plot(x, y, label="tagX", color = "red")
        plt.scatter(x[len(x)-1], y[len(y)-1], color = "red")

    if (len(p) == 1):
        plt.scatter(p, q, label="tagY", color = "orange")

    elif(len(p) > 1):
        plt.plot(p, q, label="tagY", color = "orange")
        plt.scatter(p[len(p)-1], q[len(q)-1], color = "orange")

    if (len(i) == 1):
        plt.scatter(i, j, label="tagZ", color = "green")

    elif(len(i) > 1):
        plt.plot(i, j, label="tagZ", color = "green")
        plt.scatter(i[len(i)-1], j[len(j)-1], color = "green")

    string = 'TimeStamp $t$ = ' + str(time.time())
    plt.suptitle(string)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis((0, 0.5, 0, 0.5))
    plt.legend()
    plt.pause(0.5)
    plt.show()
