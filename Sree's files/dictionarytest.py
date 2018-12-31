def filehand(x, y, z, ts):
    inp = open("test.txt", "a+")
    inp.write("tagID: " + str(z)+" Location: (" + str(x) + "," + str(y) + ") TimeStamp: " + str(ts) +"\n")
    inp.close()