import json
import matplotlib.pyplot as plt
import numpy as np

f=open("EURUSD.json", "r")
a=json.load(f)
f.close()
eur=json.loads(a)

f=open("GBPUSD.json", "r")
a=json.load(f)
f.close()
gbp=json.loads(a)
print(eur["change"][0], eur["date"][0])
print(gbp["change"][0], gbp["date"][0])

#print(eur.keys()) #Headers of my data
#print(gbp.keys())
def cf(change):
    i1=change.find("(")
    i2=change.find("%")
    change=float(change[i1+1:i2].replace("−","-"))
    return change
print(cf(eur["change"][0]))
print(cf(gbp["change"][0]))

europen1=eur["open"][0]
eurcloselist=eur["close"]
gbpopen1=gbp["open"][0]
gbpcloselist=gbp["close"]
farklist=[]
for i in range(len(eurcloselist)):
    eurfark=(eurcloselist[i]-europen1)/europen1
    gbpfark=(gbpcloselist[i]-gbpopen1)/gbpopen1
    farklist.append(gbpfark-eurfark)

xpoints = np.array(eur["date"])
ypoints = np.array(farklist)

plt.plot(xpoints, ypoints)
plt.grid()
plt.show()