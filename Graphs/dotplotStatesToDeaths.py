import matplotlib.pyplot as plt
import numpy as np
import dataSetImport
stateNames, percentageDeathsPerState, percentageSmokersPerState = dataSetImport.run()


x = stateNames
#y = dataSetImport.roundDeathsToTheNearestThousand(deathsPerState)
y = percentageDeathsPerState
z = percentageSmokersPerState

dictt={}


xvalues = y

zvalues=[]
for i in xvalues:
    if i in dictt:
        dictt[i]+=1
    else:
         dictt[i]=1
    zvalues.append(dictt[i])


plt.plot(xvalues, zvalues, 'go', markersize=8)

plt.xlabel('Percentage of Deaths')
plt.ylabel('Frequency')

plt.title('Dot plot graph')
plt.show()