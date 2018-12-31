import socket
import matplotlib.pyplot as plt
import time

class Tag:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.id = ''


ip_list = ['192.168.50.231', '192.168.50.145']
port = 12345
a1 = Tag()
a2 = Tag()
a1.id = ip_list[0]
a2.id = ip_list[1]

plt.ion()
plt.figure()

while 1:
    for i in ip_list:
        s = socket.socket()
        s.connect((i, port))
        data = s.recv(1024)
        if (i == a1.id):
            a1.x.append(data[0])
            a1.y.append(data[1])

        if (i == a2.id):
            a2.x.append(data[0])
            a2.y.append(data[1])

        plt.clf()

        if (len(a1.x) == 1):
          plt.scatter(a1.x, a1.y, label="Vehicle 1", color="red")

        elif (len(a1.x) > 1):
          plt.plot(a1.x, a1.y, label="Vehicle 1", color="red")
          plt.scatter(a1.x[len(a1.x) - 1], a1.y[len(a1.y) - 1], color="red")

        if (len(a2.x) == 1):
          plt.scatter(a2.x, a2.y, label="Vehicle 2", color="orange")

        elif (len(a2.x) > 1):
          plt.plot(a2.x, a2.y, label="Vehicle 2", color="orange")
          plt.scatter(a2.x[len(a2.x) - 1], a2.y[len(a2.y) - 1], color="orange")

        string = 'TimeStamp $t$ = ' + str(time.time())
        plt.suptitle(string)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        #plt.axis((0, 0.5, 0, 0.5))
        plt.legend()
        plt.pause(0.5)
        plt.show()

        s.close()
