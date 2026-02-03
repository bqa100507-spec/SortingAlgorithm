import random

mx, mi = int(1e18), int(-1e18)

with open('1.txt', 'w') as f :
    n = random.randint(9*10**5, 10**6)
    f.writelines(str(n) + "\n")
    prev = mi + random.randint(0, 1000)
    for i in range(0, 10**6) :
        prev = random.randint(prev, prev + 100000)
        f.write(str(prev) + " ")

with open('2.txt', 'w') as f :
    n = random.randint(9*10**5, 10**6)
    f.writelines(str(n) + "\n")
    prev = mx - random.randint(0, 1000)
    for i in range(0, 10**6) :
        prev = random.randint(prev - 100000, prev)
        f.write(str(prev) + " ")

for i in range(3, 7) :
    name = f"{i}.txt"
    with open(name, 'w') as f :
        n = random.randint(9*10**5, 10**6)
        f.writelines(str(n) + "\n")
        for i in range(0, 10**6) :
            f.write(str("{:.7f}".format(random.uniform(mi, mx))) + " ")

for i in range(7, 11) :
    name = f"{i}.txt"
    with open(name, 'w') as f :
        n = random.randint(9*10**5, 10**6)
        f.writelines(str(n) + "\n")
        for i in range(0, 10**6) :
            f.write(str(random.randint(mi, mx)) + " ")