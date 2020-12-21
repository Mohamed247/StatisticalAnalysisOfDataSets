import matplotlib.pyplot as plt
import dataSetImport
stateNames, deathsPerState, percentageSmokersPerState = dataSetImport.run()


x = dataSetImport.abbreviateStateNames(stateNames)
y = deathsPerState
z = percentageSmokersPerState

xValues = x
yValues = y
plt.plot(xValues, yValues, 'go', markersize=8)

# axis labeling
plt.xlabel('Numbers')
plt.ylabel('Values')

# figure name
plt.title('Dot plot graph')
plt.show()