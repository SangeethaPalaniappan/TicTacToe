import time
start = time.time()
print(start)
i = 0
while time.time() - start <= 10:
    if int(time.time() - start) == 5 and i == 0:
        print("5 seconds more")
        i = 1