
x = 300
y = 250
li = []

for i in range(x-1):
    for j in range(y-1):
        li.append((i+j*x, i+1+j*x))
for i in range(x):
    for j in range(y-1):
        li.append((j+i*x, j+x+i*x))
