import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
df=pd.read_csv("data1.txt")
df=df.iloc[:,0:2]

x=df.to_numpy()

plt.plot(x[:,0],x[:,1],'o')
plt.grid()


k=int(input("Enter k:\n"))
mu=np.random.rand(k,2)

for i in range(1,100):
    buck=[]
    for i in range(k):
        t=[]
        buck.append(t)
    for j in range(len(x)):
        dis=[]
        for p in range(k):
            dis.append(np.linalg.norm(x[j]-mu[p]))
        f=np.argmin(dis)
        buck[f].append(x[j])
    for y in range(k):
         buck[y]=np.array(buck[y])
         mu[y][0]=buck[y][:,0].mean()
         mu[y][1]=buck[y][:,1].mean()
print(mu)
plt.plot(mu[:,0],mu[:,1],'o')
plt.show()



