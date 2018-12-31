import test1 as t1
import random
import time
import dictionarytest as dt

tags = ["X", "Y", "Z"]
while(1):
    x = random.uniform(0, 0.5)
    y = random.uniform(0, 0.5)
    z = random.choice(tags)
    print("Vis", x, y, z)
    t1.test(x, y, z)
    dt.filehand(x, y, z, time.time())
