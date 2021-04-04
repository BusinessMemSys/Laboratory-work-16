import matplotlib.pyplot as plt
x = [i for i in range(-2,50)]
y = []
for i in x:
    k = (2-i)/(3+i)
    y.append(float(k))
plt.plot(x,y)
plt.show()