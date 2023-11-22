import matplotlib.pyplot as plt
import numpy as np

def xF(V,L,R):
    return np.sqrt(np.pi*R*R/(V*(L+np.pi/4*2*R)))

def yF(F):
    return F*2*np.pi

frequency=[175,189,147,142,129]
volume=[335,530,520,775,1050]
#volume2=[330,500,500,750,1000]
volume2=[315,460,480,725,980]
length=[8.5,7,9,9,7]
radius=[1.8,2.2,1.8,2.2,2.2]


xValues=[]
yValues=[]

for i in range(5):
    radius[i] /= 200
    length[i] /= 100
    volume2[i] /= 1000000
    volume[i] /= 1000000
for i in range(5):
    xValues.append(xF(volume2[i],length[i],radius[i]))
    yValues.append(yF(frequency[i]))

m,b=np.polyfit(xValues,yValues,deg=1)
print(m,b)
line=np.linspace(1.5,3.5,num=100)

plt.plot(line,340*line,color="r",lw=1.5,label='Literaturwert')
plt.plot(line,390*line,color="k",lw=1.5,label='Durchschnittsmessung')
plt.legend()

plt.scatter(xValues,yValues)
for a,b in zip(xValues,yValues):
    plt.text(a,b+20,(round(a,2),round(b,1)),ha='center',va='bottom',fontsize=10)
plt.xlabel("(A/VL)^(1/2)")
plt.ylabel("f*2pi")
plt.show()

