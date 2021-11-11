import os
import timeit

f = open("file.txt", "w")
while (os.path.getsize('file.txt')/(1000*1000)) < 50:
    f.write('4352556726456542\n')

t = """
opentest1 = open("file.txt", "r")
res = 0
for line in open1.readlines():
    if line.strip().isdigit():
        res+=1
opentest1.close()
"""
print(timeit.timeit(t, number=10))

t = """
opentest2 = open("file.txt", "r")
res = 0
for line in open2:
    if line.strip().isdigit():
        res+=1
opentest2.close()
"""
print(timeit.timeit(t, number=10))

t = """
opentest3 = open("file.txt", "r")
res = sum(int(line.strip().isdigit()) for line in open3)
opentest3.close()
"""
print(timeit.timeit(t, number=10))